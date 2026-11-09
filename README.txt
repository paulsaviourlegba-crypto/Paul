TRANSPORTATION RECORD MANAGEMENT SYSTEM
Nasiru Abubakar and Sons Nig. Ltd.

REQUIREMENTS
- Python 3.10 or newer
- Internet connection for Bootstrap CDN (optional after downloading Bootstrap locally)

INSTALLATION (Windows)
1. Extract the ZIP file.
2. Open the extracted folder in VS Code.
3. Open Terminal.
4. Create virtual environment:
   python -m venv venv
5. Activate it:
   venv\Scripts\activate
6. Install Django:
   pip install -r requirements.txt
7. Create database tables:
   python manage.py makemigrations
   python manage.py migrate
8. Create admin login:
   python manage.py createsuperuser
   Enter username, email (optional), and password.
9. Start the website:
   python manage.py runserver
10. Open browser:
    http://127.0.0.1:8000/

LOGIN
Use the username and password created with createsuperuser.
Admin backend: http://127.0.0.1:8000/django-admin/

IMPORTANT NOTES
- This is a simple academic/development version. DEBUG=True and the sample SECRET_KEY are for local development only.
- Before real deployment, set DEBUG=False, use a private SECRET_KEY, configure ALLOWED_HOSTS, HTTPS, backups and proper user permissions.
- Payment records are stored separately and the trip's amount_paid is recalculated when a payment is added. If an existing payment is edited/deleted through Django admin, update the related trip amount_paid accordingly.
- Deleting a truck or driver that is used by a trip is prevented to protect records.
