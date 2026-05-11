JobPortal: Enterprise Recruitment Management System
JobPortal is a comprehensive, full-stack recruitment platform developed to streamline the connection between talent and opportunity. Built with a robust Django backend and powered by PostgreSQL, the system offers distinct workflows for Job Seekers, Employers, and Administrators.

Live Application
The production environment is hosted on Render and can be accessed at:
https://jobportal-4z3o.onrender.com/

Technical Specifications
Category	Technology
Framework	Django 5.x (Python)
Database	PostgreSQL
Frontend	HTML5, CSS3, JavaScript, Bootstrap
Authentication	Django Contrib Auth
Deployment	Render PaaS
Environment	Decoupled configuration via Environment Variables
System Architecture & User Roles
The platform operates on a hierarchical permission model to ensure secure data management and clear user boundaries.

Job Seeker

Account Management: Secure registration, login, and profile customization.

Discovery: Advanced browsing of active job listings.

Engagement: Application submission and a "Saved Jobs" tracking system.

Employer

Verified Access: Multi-step onboarding via an Employer Request system.

Corporate Identity: Management of dedicated Company Profiles.

Recruitment Tools: Full CRUD capabilities for job postings and applicant management.

System Administrator

Governance: Oversight of the Employer approval workflow.

Data Integrity: Global management of users, companies, and job listings via the Django Admin Suite.

Project Structure
The codebase is modularized to ensure scalability and ease of maintenance:

Plaintext
jobportal/
├── accounts/          # User authentication, Profiles, and EmployerRequest logic
├── jobs/              # Job listing, filtering, and detail management
├── applications/      # Application processing and "Save Job" functionality
├── templates/         # Centralized UI components and layouts
├── static/            # Asset management (CSS, JavaScript, Images)
├── media/             # User-uploaded content (Project-specific)
└── manage.py          # CLI for administrative tasks
Installation and Local Development
Follow these steps to initialize the development environment.

1. Clone the Repository

Bash
git clone https://github.com/trongphuccute/JOBPORTAL.git
cd JOBPORTAL
2. Environment Configuration

Initialize a virtual environment to isolate project dependencies:

Bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Dependency Installation

Bash
pip install -r requirements.txt
4. Database Initialization

Ensure PostgreSQL is running, then execute the following:

Bash
python manage.py makemigrations
python manage.py migrate
5. Create Administrative Access

Bash
python manage.py createsuperuser
6. Execute Development Server

Bash
python manage.py runserver
Deployment Configuration
For production environments (e.g., Render), the following environment variables are required:

Variable	Description
SECRET_KEY	Unique Django secret key for cryptographic signing.
DEBUG	Set to False in production environments.
DATABASE_URL	PostgreSQL connection string.
DJANGO_SUPERUSER_PASSWORD	Default admin password for automated deployment.
Core Workflow: Employer Onboarding
To maintain platform quality, JobPortal utilizes a moderated employer registration flow:

Application: A registered user submits an EmployerRequest.

Review: Administrators evaluate the request within the management dashboard.

Provisioning: Upon approval, the user’s account type is elevated, and a linked Company Profile is automatically generated, enabling job posting capabilities.

Development Roadmap
Persistent Storage: Migration of media assets to Cloudinary or AWS S3 for production persistence.

Enhanced Search: Implementation of full-text search and advanced filtering for job listings.

Communication: Real-time notification system for application status updates.

Analytics: Dashboard for employers to track application metrics.

Author
Phuc Phuc
Lead Developer

License
This project is released under the MIT License - see the LICENSE file for details.
