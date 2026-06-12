# Feedback System - Quick Start Guide

## 🚀 Getting Started

### Step 1: Setup the Project

**Windows:**
```bash
setup_and_run.bat
```

**Linux/macOS:**
```bash
bash setup_and_run.sh
```

Or do it manually:

### Manual Setup

1. **Create Virtual Environment**
   ```bash
   python -m venv venv
   ```

2. **Activate Virtual Environment**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **Linux/macOS:**
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create Admin User (Superuser)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start Development Server**
   ```bash
   python manage.py runserver
   ```

## 📍 Application URLs

| URL | Purpose |
|-----|---------|
| `http://127.0.0.1:8000/` | Home page (redirects to login/feedback) |
| `http://127.0.0.1:8000/login/` | User login |
| `http://127.0.0.1:8000/signup/` | User registration |
| `http://127.0.0.1:8000/feedback/` | Submit feedback |
| `http://127.0.0.1:8000/thank-you/` | Thank you page after submission |
| `http://127.0.0.1:8000/dashboard/` | View feedback statistics |
| `http://127.0.0.1:8000/profile/` | View user profile |
| `http://127.0.0.1:8000/logout/` | Logout |
| `http://127.0.0.1:8000/admin/` | Admin panel |

## 🎯 Usage Flow

1. **Register** → Go to `/signup/` and create an account
2. **Login** → Go to `/login/` with your email and password
3. **Submit Feedback** → Answer "How was your visit today?" by selecting an emotion
4. **View Dashboard** → Check your feedback statistics and history
5. **View Profile** → See your user information and feedback count

## 📊 Emotion Scoring

| Emotion | Emoji | Score |
|---------|-------|-------|
| Happy | 😊 | 100% |
| Unhappy | 😐 | 50% |
| Sad | 😢 | 0% |

## 🛠️ Useful Commands

### Database Management
```bash
# Create migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Reset database (deletes all data)
python manage.py flush

# Create a new migration
python manage.py makemigrations feedback_app
```

### User Management
```bash
# Create superuser
python manage.py createsuperuser

# Change password for a user
python manage.py changepassword username
```

### Server Management
```bash
# Run development server on default port (8000)
python manage.py runserver

# Run on specific port
python manage.py runserver 8080

# Run on specific IP and port
python manage.py runserver 0.0.0.0:8000
```

### Django Shell (for testing)
```bash
# Open Django shell
python manage.py shell

# Example queries in shell:
from feedback_app.models import UserProfile, Feedback
from django.contrib.auth.models import User

# Get all users
users = User.objects.all()

# Get all feedback
feedbacks = Feedback.objects.all()

# Get feedback for a specific user
user_feedback = Feedback.objects.filter(user__username='john')

# Get happy feedbacks
happy_feedbacks = Feedback.objects.filter(emotion='happy')

# Get average score
from django.db.models import Avg
avg_score = Feedback.objects.aggregate(Avg('score'))
```

## 📁 Project Structure

```
feedback_project/
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── README.md                    # Full documentation
├── QUICKSTART.md               # This file
├── setup_and_run.bat           # Setup script for Windows
├── setup_and_run.sh            # Setup script for Linux/macOS
├── db.sqlite3                  # SQLite database
│
├── feedback_project/            # Project settings
│   ├── __init__.py
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main URL routing
│   └── wsgi.py                 # WSGI configuration
│
├── feedback_app/                # Main app
│   ├── __init__.py
│   ├── models.py               # Database models
│   ├── views.py                # View logic
│   ├── forms.py                # Form definitions
│   ├── urls.py                 # App URL routing
│   ├── admin.py                # Admin configuration
│   └── apps.py                 # App configuration
│
├── templates/                   # HTML templates
│   ├── base.html               # Base template
│   ├── login.html
│   ├── signup.html
│   ├── feedback.html
│   ├── thank_you.html
│   ├── dashboard.html
│   └── profile.html
│
└── static/                      # Static files
    ├── css/
    └── js/
```

## 🔐 Default Admin Access

After creating a superuser:
- **URL:** `http://127.0.0.1:8000/admin/`
- **Username:** (as you set during `createsuperuser`)
- **Password:** (as you set during `createsuperuser`)

## 📝 Feedback Flow

### Step-by-step what happens:

1. User registers with email, name, phone, and city
2. User logs in with email and password
3. User sees the feedback question: "How was your visit today?"
4. User selects one of three emotions (😊, 😐, 😢)
5. Feedback is saved with automatic score assignment
6. User sees thank you page
7. User can view dashboard to see all their feedbacks and statistics
8. Admin can view all feedbacks in admin panel

## 🎨 Customization

### Change Question Text
Edit `feedback_view` in `feedback_app/views.py`:
```python
'question': 'Your custom question here?'
```

### Change Emotion Scores
Edit `EMOTION_SCORES` in `feedback_app/models.py`:
```python
EMOTION_SCORES = {
    'happy': 100,      # Change this
    'unhappy': 50,     # Or this
    'sad': 0,          # Or this
}
```

### Modify UI Colors
Edit CSS in `templates/base.html`:
```css
:root {
    --primary-color: #6366f1;
    --success-color: #10b981;
    --warning-color: #f59e0b;
    --danger-color: #ef4444;
}
```

## ⚠️ Troubleshooting

### Port Already in Use
```bash
# Use a different port
python manage.py runserver 8080
```

### Database Locked Error
```bash
# Delete and recreate database
rm db.sqlite3
python manage.py migrate
```

### Module Not Found Error
```bash
# Ensure virtual environment is activated and dependencies are installed
pip install -r requirements.txt
```

### Template Not Found Error
```bash
# Ensure settings.py has correct TEMPLATES configuration
# Check that template files are in the correct directory
```

## 🚢 Deployment Checklist

Before deploying to production:

- [ ] Set `DEBUG = False` in settings.py
- [ ] Change `SECRET_KEY` to a secure random value
- [ ] Update `ALLOWED_HOSTS` with your domain
- [ ] Use PostgreSQL or MySQL instead of SQLite
- [ ] Set up proper email backend for notifications
- [ ] Run `python manage.py collectstatic`
- [ ] Use environment variables for sensitive data
- [ ] Enable HTTPS
- [ ] Set proper CORS headers if needed
- [ ] Create regular database backups

## 📞 Support

For issues or questions:
1. Check the README.md file
2. Review Django documentation: https://docs.djangoproject.com/
3. Check your console for error messages

Happy Feedback Collecting! 🎉
