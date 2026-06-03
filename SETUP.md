# Job Portal - Setup & Installation Guide

## Quick Start

### Prerequisites

- Python 3.10+
- PostgreSQL (for production) or SQLite (for development)
- pip (Python package manager)
- Git

---

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/trongphuccute/JOBPORTAL.git
cd JOBPORTAL
```

### 2. Create Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the root directory with the following variables:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (Development - SQLite)
DATABASE_URL=sqlite:///db.sqlite3

# Database (Production - PostgreSQL)
# DATABASE_URL=postgresql://username:password@localhost:5432/jobportal_db

# Email Configuration (for verification emails)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Cloudinary (for image storage)
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret

# Admin Superuser (for automated deployment)
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=your-secure-password
```

### 5. Database Setup

Run migrations to create database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account:

- Username: admin
- Email: admin@example.com
- Password: (enter your secure password)

### 7. Collect Static Files (Optional for Development)

```bash
python manage.py collectstatic --noinput
```

### 8. Run Development Server

```bash
python manage.py runserver
```

The application will be available at: **http://127.0.0.1:8000/**

---

## Project Structure Overview

```
jobportal/
├── accounts/           # User authentication, profiles, employer requests
├── jobs/               # Job listings and company management
├── applications/       # Job applications and saved jobs
├── blog/               # Blog functionality
├── ai_assistant/       # AI assistant features
├── templates/          # HTML templates
│   ├── accounts/
│   ├── auth/
│   ├── jobs/
│   ├── applications/
│   ├── blog/
│   ├── components/
│   └── includes/
├── static/             # CSS, JavaScript, images
│   ├── css/
│   ├── js/
│   └── img/
├── media/              # User-uploaded files
│   ├── avatars/
│   ├── job_images/
│   ├── resumes/
│   └── company/
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
└── .env                # Environment variables
```

---

## Key Django Apps

### 1. **accounts** - Authentication & User Management

- User registration and login
- Email verification
- User profiles
- Avatar management
- Employer request workflow
- Notifications
- User role management (Job Seeker, Employer)

### 2. **jobs** - Job Listings

- Company profiles and management
- Job posting CRUD operations
- Job images and company logos
- Job filtering by type (Full-time, Part-time, Remote)
- Job search functionality

### 3. **applications** - Job Applications

- Job application submission
- Resume management
- Application status tracking (Pending, Accepted, Rejected)
- Saved jobs feature
- Application history

### 4. **blog** - Blog Module

- Blog post creation and management
- Comments on blog posts
- Blog post categories/slugs

### 5. **ai_assistant** - AI Features

- AI-powered job recommendations
- Chat assistance for job seekers

---

## Database Models Summary

### User Model (Custom)

- **Fields:** username, email, password, role, avatar, is_verified
- **Roles:** job_seeker, employer

### Company Model

- **Fields:** name, location, website, logo, description, user (OneToOne)

### Job Model

- **Fields:** title, description, requirements, location, job_type, salary, image, company (ForeignKey)
- **Job Types:** fulltime, parttime, remote

### Application Model

- **Fields:** user, job, resume, status, applied_at
- **Status:** pending, accepted, rejected

### SavedJob Model

- **Fields:** user, job
- **Purpose:** Bookmarking jobs for later

### Resume Model

- **Fields:** user, title, file, created_at

### EmployerRequest Model

- **Fields:** user, company_name, company_location, website, description, status
- **Status:** pending, approved, rejected

---

## Common Django Commands

```bash
# Create new migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Run development server
python manage.py runserver

# Run tests
python manage.py test

# Create superuser
python manage.py createsuperuser

# Access Django shell
python manage.py shell

# Collect static files
python manage.py collectstatic

# Dump database data
python manage.py dumpdata > backup.json

# Load database data
python manage.py loaddata backup.json

# Create new app
python manage.py startapp app_name
```

---

## Troubleshooting

### Port 8000 Already in Use

```bash
# Use a different port
python manage.py runserver 8001
```

### Database Errors

```bash
# Reset database (development only!)
python manage.py flush
python manage.py migrate
```

### Static Files Not Loading

```bash
python manage.py collectstatic --clear --noinput
```

### Module Import Errors

```bash
# Ensure virtual environment is activated
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

---

## Production Deployment

### Using Render.com

1. Push code to GitHub
2. Connect repository to Render
3. Set environment variables in Render dashboard
4. Deploy with the following build command:
   ```bash
   python manage.py collectstatic --noinput && python manage.py migrate
   ```
5. Set start command:
   ```bash
   gunicorn jobportal.wsgi:application
   ```

### Environment Variables for Production

- `DEBUG=False`
- `SECRET_KEY=` (strong random key)
- `ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com`
- `DATABASE_URL=postgresql://...` (PostgreSQL connection string)

---

## Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Render Deployment Guide](https://render.com/docs)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)

---

## Support

For issues or questions, please refer to the README.md or contact the development team.
