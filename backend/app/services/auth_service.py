"""
Authentication service
"""

from app.utils.helpers import (
    hash_password, generate_otp, get_db, is_valid_email, is_strong_password
)
from app.services.email_service import EmailService
from flask import current_app
from datetime import datetime, timedelta


class AuthService:
    """Service for authentication operations"""
    
    @staticmethod
    def register_user(username, email, password, first_name=None, last_name=None):
        """
        Register a new user
        
        Args:
            username: Username
            email: Email address
            password: Password
            first_name: First name (optional)
            last_name: Last name (optional)
        
        Returns:
            Dictionary with status and message
        """
        db = get_db()
        cursor = db.cursor()
        
        try:
            # Validate inputs
            if not is_valid_email(email):
                return {'status': False, 'message': 'Invalid email format'}
            
            if not is_strong_password(password):
                return {'status': False, 'message': 'Password must be at least 8 characters with uppercase, lowercase, digit, and special character'}
            
            # Check if username or email already exists
            cursor.execute("SELECT id FROM users WHERE username = %s OR email = %s", (username, email))
            if cursor.fetchone():
                return {'status': False, 'message': 'Username or email already exists'}
            
            # Hash password
            password_hash = hash_password(password)
            
            # Insert user
            cursor.execute(
                """
                INSERT INTO users (username, email, password_hash, first_name, last_name, is_active)
                VALUES (%s, %s, %s, %s, %s, TRUE)
                """,
                (username, email, password_hash, first_name, last_name)
            )
            user_id = cursor.lastrowid
            db.commit()
            
            # Generate and send OTP
            otp = generate_otp()
            otp_hash = hash_password(otp)
            expiry_time = datetime.now() + timedelta(minutes=current_app.config['OTP_EXPIRY'])
            
            cursor.execute(
                """
                INSERT INTO otp_verifications (user_id, otp, email, purpose, expires_at)
                VALUES (%s, %s, %s, 'registration', %s)
                """,
                (user_id, otp_hash, email, expiry_time)
            )
            db.commit()
            
            # Send email
            EmailService.send_verification_email(email, otp)
            
            return {'status': True, 'message': 'Registration successful. Check your email for verification code.', 'user_id': user_id}
        
        except Exception as e:
            db.rollback()
            current_app.logger.error(f"Registration error: {str(e)}")
            return {'status': False, 'message': 'An error occurred during registration'}
        finally:
            cursor.close()
    
    @staticmethod
    def verify_otp(user_id, otp):
        """
        Verify OTP for user
        
        Args:
            user_id: User ID
            otp: OTP to verify
        
        Returns:
            Dictionary with status and message
        """
        db = get_db()
        cursor = db.cursor()
        
        try:
            otp_hash = hash_password(otp)
            
            cursor.execute(
                """
                SELECT id, is_used, expires_at FROM otp_verifications
                WHERE user_id = %s AND otp = %s AND purpose = 'registration'
                ORDER BY created_at DESC LIMIT 1
                """,
                (user_id, otp_hash)
            )
            otp_record = cursor.fetchone()
            
            if not otp_record:
                return {'status': False, 'message': 'Invalid OTP'}
            
            if otp_record['is_used']:
                return {'status': False, 'message': 'OTP already used'}
            
            if datetime.now() > otp_record['expires_at']:
                return {'status': False, 'message': 'OTP expired'}
            
            # Mark user as verified
            cursor.execute("UPDATE users SET is_verified = TRUE WHERE id = %s", (user_id,))
            
            # Mark OTP as used
            cursor.execute("UPDATE otp_verifications SET is_used = TRUE WHERE id = %s", (otp_record['id'],))
            
            db.commit()
            
            # Send welcome email
            cursor.execute("SELECT email, first_name FROM users WHERE id = %s", (user_id,))
            user = cursor.fetchone()
            if user:
                EmailService.send_welcome_email(user['email'], user['first_name'] or 'User')
            
            return {'status': True, 'message': 'Email verified successfully'}
        
        except Exception as e:
            db.rollback()
            current_app.logger.error(f"OTP verification error: {str(e)}")
            return {'status': False, 'message': 'An error occurred during verification'}
        finally:
            cursor.close()
    
    @staticmethod
    def login_user(email, password):
        """
        Authenticate user login
        
        Args:
            email: Email or username
            password: Password
        
        Returns:
            Dictionary with status and user data
        """
        db = get_db()
        cursor = db.cursor()
        
        try:
            cursor.execute(
                """
                SELECT id, username, email, password_hash, role, is_verified, is_active, first_name
                FROM users 
                WHERE (email = %s OR username = %s) AND is_active = TRUE
                """,
                (email, email)
            )
            user = cursor.fetchone()
            
            if not user:
                return {'status': False, 'message': 'Invalid credentials'}
            
            if not user['is_verified']:
                return {'status': False, 'message': 'Please verify your email first'}
            
            if hash_password(password) != user['password_hash']:
                return {'status': False, 'message': 'Invalid credentials'}
            
            # Remove sensitive data
            del user['password_hash']
            
            return {'status': True, 'message': 'Login successful', 'user': user}
        
        except Exception as e:
            current_app.logger.error(f"Login error: {str(e)}")
            return {'status': False, 'message': 'An error occurred during login'}
        finally:
            cursor.close()
    
    @staticmethod
    def initiate_password_reset(email):
        """
        Initiate password reset process
        
        Args:
            email: User email
        
        Returns:
            Dictionary with status and message
        """
        db = get_db()
        cursor = db.cursor()
        
        try:
            cursor.execute("SELECT id, email FROM users WHERE email = %s", (email,))
            user = cursor.fetchone()
            
            if not user:
                # Don't reveal if email exists
                return {'status': True, 'message': 'If email exists, password reset link has been sent'}
            
            # Generate reset token
            from app.utils.helpers import generate_token
            reset_token = generate_token()
            token_hash = hash_password(reset_token)
            expiry_time = datetime.now() + timedelta(hours=current_app.config['PASSWORD_RESET_TOKEN_EXPIRY'])
            
            # Store token (could use a separate table or update user table)
            # For now, using user table
            cursor.execute(
                "UPDATE users SET reset_token = %s, reset_token_expiry = %s WHERE id = %s",
                (token_hash, expiry_time, user['id'])
            )
            db.commit()
            
            # Send email with reset link
            reset_link = f"{current_app.config['APP_URL']}/auth/reset-password/{reset_token}"
            EmailService.send_password_reset_email(email, reset_link)
            
            return {'status': True, 'message': 'If email exists, password reset link has been sent'}
        
        except Exception as e:
            db.rollback()
            current_app.logger.error(f"Password reset initiation error: {str(e)}")
            return {'status': False, 'message': 'An error occurred'}
        finally:
            cursor.close()
    
    @staticmethod
    def reset_password(reset_token, new_password):
        """
        Reset user password
        
        Args:
            reset_token: Password reset token
            new_password: New password
        
        Returns:
            Dictionary with status and message
        """
        db = get_db()
        cursor = db.cursor()
        
        try:
            token_hash = hash_password(reset_token)
            
            cursor.execute(
                """
                SELECT id FROM users 
                WHERE reset_token = %s AND reset_token_expiry > %s
                """,
                (token_hash, datetime.now())
            )
            user = cursor.fetchone()
            
            if not user:
                return {'status': False, 'message': 'Invalid or expired reset token'}
            
            if not is_strong_password(new_password):
                return {'status': False, 'message': 'Password must be at least 8 characters with uppercase, lowercase, digit, and special character'}
            
            # Update password
            password_hash = hash_password(new_password)
            cursor.execute(
                """
                UPDATE users 
                SET password_hash = %s, reset_token = NULL, reset_token_expiry = NULL
                WHERE id = %s
                """,
                (password_hash, user['id'])
            )
            db.commit()
            
            return {'status': True, 'message': 'Password reset successful'}
        
        except Exception as e:
            db.rollback()
            current_app.logger.error(f"Password reset error: {str(e)}")
            return {'status': False, 'message': 'An error occurred'}
        finally:
            cursor.close()
