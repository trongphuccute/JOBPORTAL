JobPortal: Enterprise Recruitment Management System
JobPortal is a comprehensive, full-stack recruitment platform designed to bridge the gap between talent and opportunity. It features specialized workflows for Job Seekers, Employers, and Administrators.

🔗 Live Application: View on Render

🛠 Technical Specifications
Category	Technology
Backend	Django 5.x (Python)
Database	PostgreSQL
Frontend	HTML5, CSS3, JavaScript, Bootstrap
Auth	Django Contrib Auth
Deployment	Render (PaaS)
✨ Key Features
👤 Job Seeker
Account Management: Secure registration, login, and profile customization.

Discovery: Advanced browsing and filtering of active job listings.

Engagement: One-click application submission and a "Saved Jobs" tracking system.

🏢 Employer
Verified Access: Multi-step onboarding via an Employer Request system.

Corporate Identity: Management of dedicated Company Profiles.

Recruitment Tools: Full CRUD capabilities for job postings and applicant management.

🛡 System Administrator
Governance: Oversight of the Employer approval workflow.

Data Integrity: Global management of users, companies, and job listings via the Django Admin Suite.

📂 Project Structure
Plaintext
jobportal/
├── accounts/      # Auth, Profiles, and EmployerRequest logic
├── jobs/          # Job listing and filtering management
├── applications/  # Application processing & "Save Job" logic
├── templates/     # Centralized UI components and layouts
├── static/        # Assets (CSS, JS, Images)
├── media/         # User-uploaded content
└── manage.py      # Django CLI
⚙️ Installation & Local Development
1. Clone the Repository
Bash
git clone https://github.com/trongphuccute/JOBPORTAL.git
cd JOBPORTAL
2. Environment Setup
Windows:

Bash
python -m venv venv
venv\Scripts\activate
macOS/Linux:

Bash
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Bash
pip install -r requirements.txt
4. Database & Admin Setup
Bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
5. Run Server
Bash
python manage.py runserver
🌐 Deployment Configuration
For production environments, ensure these variables are set:

Variable	Description
SECRET_KEY	Unique Django secret key.
DEBUG	Set to False in production.
DATABASE_URL	PostgreSQL connection string.
DJANGO_SUPERUSER_PASSWORD	Admin password for automated deployment.
🗺 Development Roadmap
[ ] Persistent Storage: Migrate media assets to Cloudinary or AWS S3.

[ ] Enhanced Search: Implement full-text search and advanced filtering.

[ ] Notifications: Real-time application status updates.

[ ] Analytics: Employer dashboard for tracking application metrics.

✍️ Author
Huỳnh Trọng Phúc Lead Developer

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.
