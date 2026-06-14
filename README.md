# AI Career Development Platform

A comprehensive Full Stack SaaS application that helps users advance their careers through AI-powered analysis, job matching, and personalized learning paths.

## 🚀 Features

### User Module
- ✅ Registration with email verification (OTP)
- ✅ Secure login/logout with session management
- ✅ Forgot password with email reset link
- ✅ Comprehensive profile management
- ✅ PDF resume upload with AI parsing

### AI Career Analysis
- 🤖 Resume parsing and analysis
- 🤖 Skill extraction and validation
- 🤖 Career recommendations based on resume & market data
- 🤖 Skill gap analysis
- 🤖 Personalized learning roadmap generation
- 🤖 Interview question generation
- 📊 Resume score calculation

### Job Board Module
- 💼 Advanced job search with filters
- 💼 AJAX-powered dynamic filtering
- 💼 Job recommendations based on skills
- 💼 Apply for jobs with cover letter
- 💼 Save favorite jobs
- 💼 Track application status

### Learning Module
- 📚 Curated course catalog
- 📚 Course enrollment
- 📚 Progress tracking
- 📚 Certificate issuance
- 📚 Skill-based course recommendations

### Analytics Dashboard
- 📈 Skills distribution visualization (Chart.js)
- 📈 Resume score metrics
- 📈 Job application tracking
- 📈 Learning progress analytics
- 📈 Career growth metrics

### Admin Panel
- 👨‍💼 User management
- 💼 Job posting and management
- 📚 Course management
- 📊 Analytics and reports
- 📥 Content approval system
- 📤 Report export functionality

### Advanced Features
- 🌙 Dark mode support
- 📱 Fully responsive design (Mobile, Tablet, Desktop)
- 🔐 Role-based access control (User/Admin)
- 🔔 Real-time notifications
- 📧 Email alerts for job matches
- 🔍 AJAX search and filters
- ⚡ Secure password hashing
- 🛡️ CSRF protection
- 🧹 SQL injection prevention
- 🚫 XSS protection

## 🛠️ Tech Stack

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with flexbox & grid
- **Bootstrap 5** - Responsive design framework
- **JavaScript (Vanilla)** - Interactive features
- **AJAX** - Dynamic content loading
- **Chart.js** - Data visualization

### Backend
- **Python 3.10+** - Backend language
- **Flask** - Web framework
- **Flask-MySQLdb** - MySQL database connector

### Database
- **MySQL 8.0+** - Relational database
- **JSON columns** - For flexible data storage

### Security
- **Werkzeug** - Password hashing (bcrypt)
- **PyJWT** - Token generation
- **PyOTP** - OTP generation
- **dotenv** - Environment variable management

### Additional Libraries
- **PyPDF2** - PDF processing
- **pdfplumber** - PDF text extraction
- **OpenAI API** - AI-powered features
- **Gunicorn** - Production WSGI server

## 📁 Project Structure

```
ai-career-platform/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   ├── user.py
│   │   │   ├── resume.py
│   │   │   ├── ai_career.py
│   │   │   ├── jobs.py
│   │   │   ├── courses.py
│   │   │   ├── admin.py
│   │   │   └── api.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── resume.py
│   │   │   ├── job.py
│   │   │   ├── course.py
│   │   │   └── notification.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── auth_service.py
│   │   │   ├── email_service.py
│   │   │   ├── resume_service.py
│   │   │   ├── ai_service.py
│   │   │   ├── job_service.py
│   │   │   └── analytics_service.py
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   ├── decorators.py
│   │   │   ├── validators.py
│   │   │   ├── constants.py
│   │   │   └── helpers.py
│   │   ├── static/
│   │   │   ├── css/
│   │   │   │   ├── style.css
│   │   │   │   ├── dark-mode.css
│   │   │   │   └── responsive.css
│   │   │   ├── js/
│   │   │   │   ├── main.js
│   │   │   │   ├── ajax-handlers.js
│   │   │   │   ├── charts.js
│   │   │   │   └── dark-mode.js
│   │   │   └── uploads/
│   │   └── templates/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── auth/
│   │       │   ├── register.html
│   │       │   ├── login.html
│   │       │   ├── verify_otp.html
│   │       │   └── reset_password.html
│   │       ├── user/
│   │       │   ├── dashboard.html
│   │       │   ├── profile.html
│   │       │   └── resume.html
│   │       ├── career/
│   │       │   ├── analysis.html
│   │       │   ├── recommendations.html
│   │       │   └── roadmap.html
│   │       ├── jobs/
│   │       │   ├── list.html
│   │       │   ├── details.html
│   │       │   ├── applications.html
│   │       │   └── saved.html
│   │       ├── courses/
│   │       │   ├── list.html
│   │       │   ├── details.html
│   │       │   └── my_courses.html
│   │       ├── analytics/
│   │       │   ├── dashboard.html
│   │       │   └── reports.html
│   │       └── admin/
│   │           ├── dashboard.html
│   │           ├── users.html
│   │           ├── jobs.html
│   │           ├── courses.html
│   │           └── analytics.html
│   ├── run.py
│   ├── config.py
│   └── requirements.txt
├── database/
│   └── schema.sql
├── docs/
│   ├── ER_DIAGRAM.md
│   ├── WIREFRAMES.md
│   ├── API_DOCUMENTATION.md
│   └── DEPLOYMENT.md
├── .env.example
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- MySQL 8.0 or higher
- pip package manager
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-career-platform.git
   cd ai-career-platform
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup database**
   ```bash
   mysql -u root -p < database/schema.sql
   ```

5. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

6. **Run the application**
   ```bash
   cd backend
   python run.py
   ```

   The application will be available at `http://localhost:5000`

## 🔐 Authentication & Security

### Features Implemented
- ✅ Password hashing with bcrypt (Werkzeug)
- ✅ Session-based authentication
- ✅ Email OTP verification
- ✅ JWT tokens for API endpoints
- ✅ CSRF protection on all forms
- ✅ SQL injection prevention (parameterized queries)
- ✅ XSS prevention (template auto-escaping)
- ✅ Secure password reset tokens
- ✅ Rate limiting on sensitive endpoints
- ✅ CORS configuration for API

### Default Admin Account
```
Email: admin@example.com
Password: Admin@123456
```
⚠️ Change this immediately after first login!

## 📊 Database Schema

### Core Tables
- **users** - User accounts and profiles
- **otp_verifications** - Email verification records
- **resumes** - Resume files and parsed data
- **skills** - User skills with proficiency levels
- **career_recommendations** - AI-generated recommendations
- **jobs** - Job listings
- **job_applications** - Application tracking
- **saved_jobs** - Bookmarked jobs
- **courses** - Course catalog
- **enrollments** - Course participation
- **notifications** - User notifications
- **admin_logs** - Audit trail

See [ER_DIAGRAM.md](docs/ER_DIAGRAM.md) for complete schema details.

## 📚 API Endpoints

### Authentication
- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `POST /auth/verify-otp` - OTP verification
- `POST /auth/forgot-password` - Password reset request
- `POST /auth/reset-password/<token>` - Reset password
- `GET /auth/logout` - User logout

### User
- `GET /api/user/profile` - Get user profile
- `PUT /api/user/profile` - Update profile
- `POST /api/user/upload-resume` - Upload resume
- `GET /api/user/skills` - List user skills
- `POST /api/user/skills` - Add skill

### AI Career
- `POST /api/career/analyze-resume` - Analyze resume
- `GET /api/career/recommendations` - Get recommendations
- `GET /api/career/skill-gap` - Skill gap analysis
- `GET /api/career/roadmap` - Learning roadmap
- `GET /api/career/interview-questions` - Interview prep

### Jobs
- `GET /api/jobs` - List jobs (with filters)
- `GET /api/jobs/<id>` - Job details
- `POST /api/jobs/<id>/apply` - Apply for job
- `POST /api/jobs/<id>/save` - Save job
- `GET /api/applications` - User applications

### Courses
- `GET /api/courses` - List courses
- `GET /api/courses/<id>` - Course details
- `POST /api/courses/<id>/enroll` - Enroll in course
- `GET /api/enrollments` - User enrollments

### Analytics
- `GET /api/analytics/dashboard` - Dashboard data
- `GET /api/analytics/skills` - Skills distribution
- `GET /api/analytics/applications` - Application stats
- `GET /api/analytics/learning` - Learning progress

### Admin
- `GET /api/admin/users` - List users
- `POST /api/admin/jobs` - Create job
- `POST /api/admin/courses` - Create course
- `GET /api/admin/reports` - Generate reports

See [API_DOCUMENTATION.md](docs/API_DOCUMENTATION.md) for detailed endpoint specifications.

## 🎨 Features in Detail

### Resume Analysis
The platform uses OpenAI's GPT API to:
- Extract personal information
- Identify technical skills
- Parse work experience
- Extract education details
- Calculate resume score
- Identify skill gaps

### AI Career Recommendations
Based on resume analysis:
- Recommends job titles matching skills
- Calculates match percentage
- Identifies missing skills
- Creates learning roadmap
- Suggests interview preparation

### Job Matching Algorithm
- Skills-based matching
- Experience level consideration
- Location preferences
- Salary expectations
- Career progression analysis

### Analytics Dashboard
- Resume score tracking
- Job application metrics
- Skills distribution
- Learning progress
- Career growth timeline

## 🌙 Dark Mode

Toggle available in:
- Navbar (top-right)
- Settings (user menu)
- Automatically saved to localStorage

CSS variables used:
```css
--bg-primary
--bg-secondary
--text-primary
--text-secondary
--border-color
--accent-color
```

## 📱 Responsive Design

Breakpoints:
- **Mobile**: < 576px
- **Tablet**: 576px - 1024px
- **Desktop**: > 1024px

All components tested on:
- iPhone 12/13/14
- iPad
- Samsung Galaxy
- Desktop (1920px)

## 🚀 Deployment

### Production Setup
1. Update `.env` with production values
2. Set `FLASK_ENV=production`
3. Use Gunicorn for WSGI:
   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 run:app
   ```
4. Use Nginx as reverse proxy
5. Enable HTTPS with SSL certificates

See [DEPLOYMENT.md](docs/DEPLOYMENT.md) for detailed deployment instructions.

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support, email support@aicareerplatform.com or open an issue on GitHub.

## 🙏 Acknowledgments

- Bootstrap team for amazing CSS framework
- Chart.js for visualization
- OpenAI for powerful AI API
- Flask community for great documentation

---

**Made with ❤️ for career development**
