# JobPortal: Enterprise Recruitment Management System

> A comprehensive, full-stack recruitment platform designed to bridge the gap between talent and opportunity. Features specialized workflows for Job Seekers, Employers, and Administrators.

[![Django Version](https://img.shields.io/badge/Django-5.x-darkgreen.svg)](https://www.djangoproject.com/)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-336791.svg)](https://www.postgresql.org/)

## 📑 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Development](#development)
- [Deployment](#deployment)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Contact](#contact)

## 🎯 Overview

JobPortal is an enterprise-grade recruitment management system built with **Django 5.x** and **PostgreSQL**. It provides a complete solution for managing job postings, applications, and employer workflows with role-based access control.

### Key Capabilities

- **Multi-tenant job discovery** with advanced filtering
- **Employer verification system** with multi-step onboarding
- **Application workflow** with status tracking
- **Admin dashboard** for system governance
- **Resume management** with upload support
- **Saved jobs** feature for future reference

## ✨ Features

### 👤 Job Seeker

- **Account Management**: Secure registration, login, email verification, and profile customization
- **Discovery**: Advanced browsing and filtering of active job listings by category, location, and salary range
- **Engagement**: One-click application submission with application status tracking
- **Saved Jobs**: Bookmark and organize job listings for later review
- **Resume Management**: Upload and manage multiple resumes
- **Notifications**: Track application updates and employer messages

### 🏢 Employer

- **Verified Access**: Multi-step onboarding via secure Employer Request system with admin approval
- **Corporate Identity**: Dedicated company profiles with logo, description, and website
- **Recruitment Tools**: Full CRUD capabilities for job postings with images and requirements
- **Applicant Tracking**: View, manage, and track job applications
- **Company Dashboard**: Overview of posted jobs and application statistics
- **Application Filtering**: View applicants sorted by application date and status

### 🛡️ System Administrator

- **Governance**: Oversight of employer verification and approval workflow
- **Data Management**: Global administration of users, companies, and job listings
- **Django Admin Suite**: Comprehensive admin dashboard for system configuration
- **User Management**: Create, edit, and manage user accounts and roles
- **Report Generation**: Monitor system activity and user engagement

## 🛠️ Tech Stack

| Category           | Technology               | Purpose                   |
| ------------------ | ------------------------ | ------------------------- |
| **Backend**        | Django 5.x               | Web framework             |
| **Language**       | Python 3.10+             | Core language             |
| **Database**       | PostgreSQL               | Production database       |
| **Frontend**       | HTML5, CSS3, Bootstrap 5 | UI/UX                     |
| **JavaScript**     | Vanilla JS               | Client-side interactivity |
| **Authentication** | Django Contrib Auth      | User authentication       |
| **Deployment**     | Render, Gunicorn         | Hosting & WSGI server     |
| **Storage**        | Cloudinary / AWS S3      | Media file storage        |

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- PostgreSQL (production) or SQLite (development)
- pip and virtualenv
- Git

### Installation (5 minutes)

**1. Clone & Navigate**

```bash
git clone https://github.com/trongphuccute/JOBPORTAL.git
cd JOBPORTAL/jobportal
```

**2. Create Virtual Environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install Dependencies**

```bash
pip install -r requirements.txt
```

**4. Environment Configuration**

```bash
# Create .env file in the root directory
cp .env.example .env  # if available, or create manually
```

**5. Database Setup**

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # Create admin account
```

**6. Run Server**

```bash
python manage.py runserver
```

Visit: **http://localhost:8000/**

For detailed setup instructions, see [SETUP.md](../SETUP.md).

## 📂 Project Structure

```
jobportal/
├── accounts/               # Authentication, user profiles, employer requests
│   ├── models.py          # User, Profile, EmployerRequest, Notification
│   ├── views.py           # Registration, login, profile views
│   ├── forms.py           # User forms and validation
│   ├── decorators.py      # Role-based access control
│   └── signals.py         # User creation signals
├── jobs/                  # Job listings and company management
│   ├── models.py          # Company, Job, JobImage
│   ├── views.py           # Job listing, detail, creation views
│   ├── form.py            # Job creation/editing forms
│   └── utils.py           # Job filtering and utilities
├── applications/          # Application tracking and saved jobs
│   ├── models.py          # Application, Resume, SavedJob
│   ├── views.py           # Application and resume views
│   └── urls.py            # Application URL routing
├── blog/                  # Blog functionality
│   ├── models.py          # BlogPost, Comment
│   ├── views.py           # Blog views
│   └── forms.py           # Blog post forms
├── ai_assistant/          # AI-powered features (future expansion)
│   └── models.py          # AI assistant models
├── templates/             # HTML templates organized by app
│   ├── base/             # Base layout templates
│   ├── auth/             # Login/registration templates
│   ├── accounts/         # User account templates
│   ├── jobs/             # Job-related templates
│   ├── applications/     # Application templates
│   └── components/       # Reusable UI components
├── static/               # CSS, JavaScript, images
│   ├── css/
│   │   ├── style.css     # Main stylesheet
│   │   └── upgrade.css   # Additional styles
│   ├── js/
│   │   └── main.js       # Client-side logic
│   └── img/              # Static images
├── media/                # User-uploaded files (avatars, resumes, job images)
├── manage.py             # Django CLI
├── requirements.txt      # Python dependencies
└── .env                  # Environment variables (not versioned)
```

For architecture details, see [ARCHITECTURE.md](../ARCHITECTURE.md).

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root with the following:

```env
# Django Settings
SECRET_KEY=your-unique-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (Development)
DATABASE_URL=sqlite:///db.sqlite3

# Database (Production)
# DATABASE_URL=postgresql://user:password@localhost:5432/jobportal

# Email Configuration
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Cloudinary CDN (for media storage)
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret

# Admin Superuser
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=secure-password
```

## 🔧 Development

### Database Migrations

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# View migration status
python manage.py showmigrations
```

### Static Files

```bash
# Collect static files (production)
python manage.py collectstatic --noinput

# Development (auto-served by Django)
# Static files are automatically served in DEBUG=True mode
```

### Useful Commands

```bash
# Create superuser
python manage.py createsuperuser

# Access Django shell
python manage.py shell

# Check deployment readiness
python manage.py check --deploy

# Run tests
python manage.py test
```

## 🌐 Deployment

### Production Environment Variables

| Variable                | Description                | Example                               |
| ----------------------- | -------------------------- | ------------------------------------- |
| `SECRET_KEY`            | Django secret key          | `django-insecure-...`                 |
| `DEBUG`                 | Debug mode (must be False) | `False`                               |
| `ALLOWED_HOSTS`         | Permitted hostnames        | `yourdomain.com,www.yourdomain.com`   |
| `DATABASE_URL`          | PostgreSQL connection      | `postgresql://user:pass@host:5432/db` |
| `EMAIL_HOST_USER`       | SMTP email address         | `noreply@yourdomain.com`              |
| `EMAIL_HOST_PASSWORD`   | SMTP password              | `app-specific-password`               |
| `CLOUDINARY_CLOUD_NAME` | CDN cloud name             | `your-cloud`                          |

### Deploy to Render

1. Push code to GitHub repository
2. Connect repository to Render.com
3. Set environment variables in Render dashboard
4. Configure build command: `pip install -r requirements.txt && python manage.py migrate`
5. Set start command: `gunicorn jobportal.wsgi:application`
6. Deploy and monitor

For complete deployment guide, refer to [SETUP.md](../SETUP.md).

## 🗺️ Roadmap

- [x] Basic user authentication and registration
- [x] Job listing and filtering
- [x] Application workflow
- [x] Employer verification system
- [x] Resume uploads
- [ ] **Persistent Storage**: Migrate media assets to Cloudinary or AWS S3 (in progress)
- [ ] **Enhanced Search**: Full-text search with Elasticsearch
- [ ] **Real-time Notifications**: WebSocket notifications for application updates
- [ ] **Analytics Dashboard**: Employer dashboard with application metrics and trends
- [ ] **AI-Powered Matching**: Resume-to-job matching algorithm
- [ ] **Email Campaigns**: Bulk email to job seekers by category
- [ ] **Mobile App**: Native mobile applications for iOS/Android
- [ ] **Chat System**: Direct messaging between employers and job seekers

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** changes: `git commit -m 'Add amazing feature'`
4. **Push** to branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request

### Coding Standards

- Follow PEP 8 style guidelines
- Write descriptive commit messages
- Include docstrings for new functions
- Test your changes before submitting PR

## 🐛 Troubleshooting

### Common Issues

**Issue**: "No module named 'django'"

```bash
# Solution: Install requirements
pip install -r requirements.txt
```

**Issue**: "ModuleNotFoundError: No module named 'psycopg2'"

```bash
# Solution: Install PostgreSQL adapter
pip install psycopg2-binary
```

**Issue**: Database connection error

```bash
# Solution: Check DATABASE_URL in .env
# For SQLite: sqlite:///db.sqlite3
# For PostgreSQL: postgresql://user:password@localhost:5432/dbname
```

**Issue**: "ProgrammingError" after database changes

```bash
# Solution: Run migrations
python manage.py migrate
```

**Issue**: Static files not loading

```bash
# Solution: Ensure DEBUG=True in development
# Or run collectstatic in production
python manage.py collectstatic --noinput
```

### Getting Help

- 📖 Check [ARCHITECTURE.md](../ARCHITECTURE.md) for system design
- 🔄 Review [FLOWS.md](../FLOWS.md) for workflow documentation
- 📋 See [URL_ROUTES.md](../URL_ROUTES.md) for available endpoints

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

### MIT License Summary

You are free to:

- ✅ Use commercially
- ✅ Modify the code
- ✅ Distribute copies
- ✅ Use privately

You must:

- ⚠️ Include copyright notice
- ⚠️ Include license copy

## 📧 Contact & Support

- **Repository**: [github.com/trongphuccute/JOBPORTAL](https://github.com/trongphuccute/JOBPORTAL)
- **Issues**: [GitHub Issues](https://github.com/trongphuccute/JOBPORTAL/issues)
- **Email**: For inquiries, open an issue on GitHub
- **Author**: Huỳnh Trọng Phúc

---

**Made with ❤️ by the JobPortal Team**
