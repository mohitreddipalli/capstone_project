"""
Email service for sending emails
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import current_app, render_template_string


class EmailService:
    """Service for sending emails"""
    
    @staticmethod
    def send_email(to_email, subject, html_content, text_content=None):
        """
        Send email
        
        Args:
            to_email: Recipient email
            subject: Email subject
            html_content: Email body (HTML)
            text_content: Email body (Text fallback)
        
        Returns:
            True if sent successfully, False otherwise
        """
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = current_app.config['MAIL_USERNAME']
            msg['To'] = to_email
            
            if text_content:
                msg.attach(MIMEText(text_content, 'plain'))
            msg.attach(MIMEText(html_content, 'html'))
            
            # Send email
            with smtplib.SMTP(current_app.config['MAIL_SERVER'], current_app.config['MAIL_PORT']) as server:
                server.starttls()
                server.login(current_app.config['MAIL_USERNAME'], current_app.config['MAIL_PASSWORD'])
                server.send_message(msg)
            
            return True
        except Exception as e:
            current_app.logger.error(f"Failed to send email to {to_email}: {str(e)}")
            return False
    
    @staticmethod
    def send_verification_email(email, otp):
        """Send OTP verification email"""
        subject = "Email Verification - AI Career Platform"
        html_content = f"""
        <html>
            <head></head>
            <body style="font-family: Arial, sans-serif;">
                <h2>Email Verification</h2>
                <p>Your verification code is: <strong>{otp}</strong></p>
                <p>This code will expire in 10 minutes.</p>
                <p>If you didn't request this code, please ignore this email.</p>
                <hr>
                <p>AI Career Development Platform</p>
            </body>
        </html>
        """
        return EmailService.send_email(email, subject, html_content)
    
    @staticmethod
    def send_password_reset_email(email, reset_link):
        """Send password reset email"""
        subject = "Password Reset - AI Career Platform"
        html_content = f"""
        <html>
            <head></head>
            <body style="font-family: Arial, sans-serif;">
                <h2>Password Reset Request</h2>
                <p>Click the link below to reset your password:</p>
                <p><a href="{reset_link}" style="background-color: #007AFF; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Reset Password</a></p>
                <p>This link will expire in 24 hours.</p>
                <p>If you didn't request this reset, please ignore this email.</p>
                <hr>
                <p>AI Career Development Platform</p>
            </body>
        </html>
        """
        return EmailService.send_email(email, subject, html_content)
    
    @staticmethod
    def send_job_recommendation_email(email, user_name, jobs):
        """Send job recommendation email"""
        subject = "New Job Recommendations - AI Career Platform"
        
        jobs_html = ""
        for job in jobs[:5]:  # Send top 5 recommendations
            jobs_html += f"""
            <tr>
                <td style="padding: 10px; border-bottom: 1px solid #ddd;">
                    <strong>{job['job_title']}</strong><br>
                    {job['company_name']} - {job['location']}<br>
                    Match: {job['match_percentage']}%
                </td>
            </tr>
            """
        
        html_content = f"""
        <html>
            <head></head>
            <body style="font-family: Arial, sans-serif;">
                <h2>New Job Recommendations for You</h2>
                <p>Hi {user_name},</p>
                <p>We found some great job opportunities that match your profile:</p>
                <table style="width: 100%; border-collapse: collapse;">
                    {jobs_html}
                </table>
                <p><a href="https://yourapp.com/jobs" style="background-color: #007AFF; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">View All Recommendations</a></p>
                <hr>
                <p>AI Career Development Platform</p>
            </body>
        </html>
        """
        return EmailService.send_email(email, subject, html_content)
    
    @staticmethod
    def send_welcome_email(email, user_name):
        """Send welcome email"""
        subject = "Welcome to AI Career Development Platform"
        html_content = f"""
        <html>
            <head></head>
            <body style="font-family: Arial, sans-serif;">
                <h2>Welcome, {user_name}!</h2>
                <p>Thank you for joining AI Career Development Platform.</p>
                <h3>Get started:</h3>
                <ul>
                    <li>Complete your profile</li>
                    <li>Upload your resume</li>
                    <li>Get AI-powered career recommendations</li>
                    <li>Explore job opportunities</li>
                    <li>Enroll in learning courses</li>
                </ul>
                <p><a href="https://yourapp.com/dashboard" style="background-color: #007AFF; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Go to Dashboard</a></p>
                <hr>
                <p>AI Career Development Platform</p>
            </body>
        </html>
        """
        return EmailService.send_email(email, subject, html_content)
