# Feedback System - Installation & Usage Guide

## 📋 Summary

A complete Django-based feedback collection system with:
- ✅ User Authentication (Email-based login/signup)
- ✅ Three Emotion Feedback (Happy 😊, Unhappy 😐, Sad 😢)
- ✅ Automatic Scoring (100%, 50%, 0%)
- ✅ Dashboard with Statistics
- ✅ Admin Panel
- ✅ Responsive Bootstrap UI

---

## 🚀 QUICK START (Choose One)

### Option 1: Automatic Setup (EASIEST)

**For Windows:**
```bash
setup_and_run.bat
```

**For Linux/macOS:**
```bash
bash setup_and_run.sh
```

This script will:
1. Create virtual environment ✅
2. Install Django ✅
3. Run migrations ✅
4. Create admin user ✅
5. Start the server ✅

### Option 2: Manual Setup

```bash
# Step 1: Create Python virtual environment
python -m venv venv

# Step 2: Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Step 3: Install Django
pip install -r requirements.txt

# Step 4: Setup database
python manage.py migrate

# Step 5: Create admin account (optional but recommended)
python manage.py createsuperuser
# You'll be asked for:
# - Email
# - Password
# - Password confirmation

# Step 6: Start development server
python manage.py runserver
```

---

## 🌐 After Starting Server

Your application will be available at:

```
http://127.0.0.1:8000/
```

### Key URLs:

| Page | URL | Description |
|------|-----|-------------|
| **Home** | `/` | Redirects to login or feedback |
| **Sign Up** | `/signup/` | Create new account |
| **Login** | `/login/` | Login with email & password |
| **Feedback** | `/feedback/` | Submit feedback with emoji |
| **Dashboard** | `/dashboard/` | View your statistics |
| **Profile** | `/profile/` | View your profile |
| **Admin** | `/admin/` | Manage system (superuser only) |

---

## 👤 User Registration Flow

1. Go to: `http://127.0.0.1:8000/signup/`
2. Enter details:
   - **Email** (required) - Used for login
   - **First Name** (optional)
   - **Last Name** (optional)
   - **Phone** (optional)
   - **City** (optional)
   - **Password** (required)
   - **Confirm Password** (required)
3. Click "Sign Up"
4. You'll automatically be logged in
5. Go to feedback page to submit your first feedback

---

## 📝 Feedback Submission

1. After login, go to `/feedback/`
2. Read: **"How was your visit today?"**
3. Click one emoji:
   - 😊 **Happy** = 100% score
   - 😐 **Unhappy** = 50% score
   - 😢 **Sad** = 0% score
4. Click "Submit Feedback"
5. See thank you page with your score
6. Feedback is saved to database

---

## 📊 Dashboard Features

View at: `http://127.0.0.1:8000/dashboard/`

**Shows:**
- 📈 Total feedback count
- 📊 Average score percentage
- 😊 Happy/Unhappy/Sad breakdown
- 📉 Pie chart visualization
- 📋 Complete feedback history with timestamps

---

## 🛠️ Useful Commands

```bash
# View admin panel
# URL: http://127.0.0.1:8000/admin/
# Login with superuser credentials

# Stop server (in terminal)
Ctrl + C

# Run on different port
python manage.py runserver 8080

# Open Django Python shell (for testing)
python manage.py shell

# Create another superuser
python manage.py createsuperuser

# Reset database (WARNING: Deletes all data!)
python manage.py flush

# Make new migrations (after model changes)
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

---

## 📧 Admin Panel Access

**URL:** `http://127.0.0.1:8000/admin/`

**From admin, you can:**
- ✅ View all user feedbacks
- ✅ Filter by emotion (Happy/Unhappy/Sad)
- ✅ Filter by date
- ✅ Search by username
- ✅ View user profiles
- ✅ Manage users

---

## 🎨 Customization

### Change Feedback Question

Edit file: `feedback_app/views.py` (Line ~74)

Change:
```python
'question': 'How was your visit today?'
```

To:
```python
'question': 'Your new question here?'
```

### Change Emotion Scores

Edit file: `feedback_app/models.py` (Lines 16-20)

```python
EMOTION_SCORES = {
    'happy': 100,      # 😊 Score
    'unhappy': 50,     # 😐 Score
    'sad': 0,          # 😢 Score
}
```

### Change UI Colors

Edit file: `templates/base.html` (Lines 7-13)

```css
:root {
    --primary-color: #6366f1;      /* Main blue color */
    --success-color: #10b981;      /* Green color */
    --warning-color: #f59e0b;      /* Yellow color */
    --danger-color: #ef4444;       /* Red color */
}
```

---

## 📁 Project Files Explained

```
feedback_project/
│
├── manage.py                    ← Main Django command file
├── requirements.txt             ← Python packages (Django)
├── setup_and_run.bat/sh        ← Quick setup scripts
│
├── feedback_project/            ← Project settings folder
│   ├── settings.py             ← Django configuration
│   ├── urls.py                 ← Main URL routing
│   └── wsgi.py                 ← Server configuration
│
├── feedback_app/                ← Application code
│   ├── models.py               ← Database structure
│   ├── views.py                ← Business logic
│   ├── forms.py                ← Form handling
│   ├── urls.py                 ← App URLs
│   └── admin.py                ← Admin panel setup
│
├── templates/                   ← HTML pages
│   ├── base.html               ← Main template
│   ├── login.html              ← Login page
│   ├── signup.html             ← Registration page
│   ├── feedback.html           ← Feedback form
│   ├── thank_you.html          ← Thank you page
│   ├── dashboard.html          ← Statistics page
│   └── profile.html            ← Profile page
│
└── static/                      ← CSS/JS files
    ├── css/
    └── js/
```

---

## ✅ Database Models

### User (Built-in Django)
- Email
- Username
- Password
- First Name
- Last Name

### UserProfile (Custom)
- Phone number
- City
- Created date

### Feedback (Custom)
- User (linked to User)
- Emotion (happy/unhappy/sad)
- Score (100/50/0)
- Date & time

---

## 🔒 Default Security

- ✅ Password hashing
- ✅ CSRF protection
- ✅ SQL injection prevention
- ✅ User session management
- ✅ Admin authentication

---

## 📱 Features Included

- ✅ Beautiful responsive design (works on mobile)
- ✅ Interactive emoji selector
- ✅ Real-time form validation
- ✅ Progress bars on dashboard
- ✅ Chart.js data visualization
- ✅ Feedback history
- ✅ User profile management

---

## 🐛 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| **Port 8000 in use** | Run: `python manage.py runserver 8080` |
| **Module not found** | Run: `pip install -r requirements.txt` |
| **Templates not found** | Check `templates/` folder exists |
| **Database error** | Run: `python manage.py migrate` |
| **Can't create superuser** | Run: `python manage.py createsuperuser` again |

---

## 📚 Documentation Files

Read these for more details:
- **README.md** - Full documentation with features
- **QUICKSTART.md** - Quick reference with useful commands
- **SETUP_COMPLETE.md** - Complete setup summary

---

## 🎓 Learning Resources

- Django: https://docs.djangoproject.com/
- Bootstrap: https://getbootstrap.com/
- SQLite: https://www.sqlite.org/

---

## 🎉 Ready to Go!

Your feedback system is complete and ready to use!

### START HERE:
1. Run setup script (Windows or Linux/macOS)
2. Create superuser when prompted
3. Visit `http://127.0.0.1:8000/`
4. Sign up and submit feedback!

**Happy Feedback Collecting!** 📊😊
