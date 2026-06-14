-- AI Career Development Platform - Database Schema
-- MySQL Database Schema with all normalized tables

-- Drop existing tables (if any)
DROP TABLE IF EXISTS admin_logs;
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS notifications;
DROP TABLE IF EXISTS saved_jobs;
DROP TABLE IF EXISTS job_applications;
DROP TABLE IF EXISTS jobs;
DROP TABLE IF EXISTS career_recommendations;
DROP TABLE IF EXISTS skills;
DROP TABLE IF EXISTS resumes;
DROP TABLE IF EXISTS otp_verifications;
DROP TABLE IF EXISTS users;

-- Users Table
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone VARCHAR(15),
    location VARCHAR(100),
    headline VARCHAR(200),
    bio TEXT,
    profile_image VARCHAR(255),
    role ENUM('user', 'admin') DEFAULT 'user',
    is_verified BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_email (email),
    INDEX idx_username (username),
    INDEX idx_role (role)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- OTP Verifications Table
CREATE TABLE otp_verifications (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    otp VARCHAR(10) NOT NULL,
    email VARCHAR(100) NOT NULL,
    purpose ENUM('registration', 'password_reset') DEFAULT 'registration',
    is_used BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_user_id (user_id),
    INDEX idx_email (email),
    INDEX idx_expires_at (expires_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Resumes Table
CREATE TABLE resumes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL UNIQUE,
    file_path VARCHAR(255) NOT NULL,
    file_name VARCHAR(100) NOT NULL,
    file_size INT,
    original_text LONGTEXT,
    parsed_data JSON,
    resume_score DECIMAL(5, 2),
    extracted_skills JSON,
    extracted_education JSON,
    extracted_experience JSON,
    is_analyzed BOOLEAN DEFAULT FALSE,
    analyzed_at TIMESTAMP NULL,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_user_id (user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Skills Table
CREATE TABLE skills (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    skill_name VARCHAR(100) NOT NULL,
    proficiency_level ENUM('beginner', 'intermediate', 'advanced', 'expert') DEFAULT 'intermediate',
    years_of_experience DECIMAL(4, 1),
    endorsements INT DEFAULT 0,
    is_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_user_id (user_id),
    INDEX idx_skill_name (skill_name),
    UNIQUE KEY unique_user_skill (user_id, skill_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Career Recommendations Table
CREATE TABLE career_recommendations (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    recommended_job_title VARCHAR(100) NOT NULL,
    match_percentage DECIMAL(5, 2),
    skill_gap_analysis JSON,
    learning_roadmap JSON,
    estimated_timeline VARCHAR(50),
    salary_range JSON,
    market_demand VARCHAR(50),
    interview_questions JSON,
    recommendation_reason TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_user_id (user_id),
    INDEX idx_created_at (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Jobs Table
CREATE TABLE jobs (
    id INT PRIMARY KEY AUTO_INCREMENT,
    job_title VARCHAR(100) NOT NULL,
    company_name VARCHAR(100) NOT NULL,
    description LONGTEXT NOT NULL,
    requirements TEXT,
    salary_min DECIMAL(10, 2),
    salary_max DECIMAL(10, 2),
    currency VARCHAR(10) DEFAULT 'USD',
    location VARCHAR(100),
    job_type ENUM('full-time', 'part-time', 'contract', 'internship', 'freelance') DEFAULT 'full-time',
    experience_level ENUM('entry', 'mid', 'senior', 'lead') DEFAULT 'mid',
    skills_required JSON,
    company_logo VARCHAR(255),
    apply_link VARCHAR(255),
    posted_by_admin INT,
    is_active BOOLEAN DEFAULT TRUE,
    posted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (posted_by_admin) REFERENCES users(id),
    INDEX idx_company (company_name),
    INDEX idx_location (location),
    INDEX idx_job_type (job_type),
    INDEX idx_experience_level (experience_level),
    INDEX idx_posted_at (posted_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Job Applications Table
CREATE TABLE job_applications (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    job_id INT NOT NULL,
    application_status ENUM('applied', 'reviewed', 'shortlisted', 'rejected', 'accepted') DEFAULT 'applied',
    cover_letter TEXT,
    applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    reviewed_at TIMESTAMP NULL,
    status_updated_at TIMESTAMP NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (job_id) REFERENCES jobs(id) ON DELETE CASCADE,
    INDEX idx_user_id (user_id),
    INDEX idx_job_id (job_id),
    INDEX idx_status (application_status),
    UNIQUE KEY unique_user_job (user_id, job_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Saved Jobs Table
CREATE TABLE saved_jobs (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    job_id INT NOT NULL,
    saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (job_id) REFERENCES jobs(id) ON DELETE CASCADE,
    INDEX idx_user_id (user_id),
    INDEX idx_job_id (job_id),
    UNIQUE KEY unique_user_saved_job (user_id, job_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Courses Table
CREATE TABLE courses (
    id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100) NOT NULL,
    description LONGTEXT,
    course_level ENUM('beginner', 'intermediate', 'advanced') DEFAULT 'intermediate',
    instructor_name VARCHAR(100),
    duration_hours INT,
    course_image VARCHAR(255),
    course_link VARCHAR(255),
    category VARCHAR(50),
    skills_taught JSON,
    certification_available BOOLEAN DEFAULT TRUE,
    created_by_admin INT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by_admin) REFERENCES users(id),
    INDEX idx_category (category),
    INDEX idx_course_level (course_level)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Enrollments Table
CREATE TABLE enrollments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    course_id INT NOT NULL,
    enrollment_status ENUM('enrolled', 'in_progress', 'completed', 'dropped') DEFAULT 'enrolled',
    progress_percentage DECIMAL(5, 2) DEFAULT 0,
    completion_date TIMESTAMP NULL,
    certificate_issued BOOLEAN DEFAULT FALSE,
    certificate_number VARCHAR(100),
    enrolled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE,
    INDEX idx_user_id (user_id),
    INDEX idx_course_id (course_id),
    INDEX idx_status (enrollment_status),
    UNIQUE KEY unique_user_course (user_id, course_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Notifications Table
CREATE TABLE notifications (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    notification_type ENUM('job_match', 'course_recommendation', 'application_update', 'alert', 'system') DEFAULT 'alert',
    title VARCHAR(100) NOT NULL,
    message TEXT NOT NULL,
    related_id INT,
    is_read BOOLEAN DEFAULT FALSE,
    is_sent_email BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_user_id (user_id),
    INDEX idx_is_read (is_read),
    INDEX idx_created_at (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Admin Logs Table
CREATE TABLE admin_logs (
    id INT PRIMARY KEY AUTO_INCREMENT,
    admin_id INT NOT NULL,
    action VARCHAR(100) NOT NULL,
    entity_type VARCHAR(50),
    entity_id INT,
    details JSON,
    ip_address VARCHAR(45),
    user_agent VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (admin_id) REFERENCES users(id),
    INDEX idx_admin_id (admin_id),
    INDEX idx_action (action),
    INDEX idx_created_at (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Create indexes for better query performance
CREATE INDEX idx_users_created_at ON users(created_at);
CREATE INDEX idx_jobs_is_active ON jobs(is_active);
CREATE INDEX idx_enrollments_completion ON enrollments(completion_date);
CREATE INDEX idx_applications_applied_at ON job_applications(applied_at);
