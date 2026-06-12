# Feedback System - Django Project

A simple and elegant feedback collection system with user authentication and emotional response tracking (Happy, Unhappy, Sad).

## Features

- **User Authentication**: Simple registration and login system
- **Feedback Submission**: Users can submit feedback with three emotion options
  - 😊 Happy (100% score)
  - 😐 Unhappy (50% score)
  - 😢 Sad (0% score)
- **Dashboard**: View feedback statistics and history
- **User Profile**: Manage user information
- **Beautiful UI**: Modern Bootstrap-based responsive design

## Project Structure

```
feedback_project/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── feedback_project/          # Project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __init__.py
├── feedback_app/              # Main Django app
│   ├── models.py              # Database models
│   ├── views.py               # View logic
│   ├── forms.py               # Form definitions
│   ├── urls.py                # App URL routing
│   ├── admin.py               # Admin configuration
│   └── __init__.py
├── templates/                 # HTML templates
│   ├── base.html
│   ├── login.html
│   ├── signup.html
│   ├── feedback.html
│   ├── thank_you.html
│   ├── dashboard.html
│   └── profile.html
└── static/                    # Static files (CSS, JS)
    ├── css/
    └── js/
```

## Installation

### 1. Create a Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

## Running the Application

```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/`

## Usage

1. **Sign Up**: Create a new account by providing:
   - Email
   - First Name (optional)
   - Last Name (optional)
   - Phone (optional)
   - City (optional)
   - Password

2. **Login**: Log in with your email and password

3. **Submit Feedback**: 
   - Answer "How was your visit today?" by selecting one of three emotions
   - Your response gets a score (Happy: 100%, Unhappy: 50%, Sad: 0%)

4. **View Dashboard**: 
   - See statistics about your feedbacks
   - View your feedback history
   - See emotional response breakdown

5. **View Profile**: 
   - View your user information
   - See your feedback statistics

## Admin Panel

Access the admin panel at `http://127.0.0.1:8000/admin/` with your superuser credentials.

From the admin panel, you can:
- Manage users
- View all feedback submissions
- Manage user profiles
- Filter and search feedback by emotion or date

## Database Models

### UserProfile
- Linked to Django's User model (one-to-one)
- Fields: phone, city, created_at

### Feedback
- user: ForeignKey to User
- emotion: Choice field (happy, unhappy, sad)
- score: Integer (100, 50, 0)
- created_at: Timestamp

## Scoring System

| Emotion  | Score | Representation |
|----------|-------|-----------------|
| Happy    | 100%  | 😊             |
| Unhappy  | 50%   | 😐             |
| Sad      | 0%    | 😢             |

## Technologies Used

- **Django**: Web framework
- **SQLite**: Database (default)
- **Bootstrap 5**: UI Framework
- **Chart.js**: Data visualization
- **Font Awesome**: Icons

## Future Enhancements

- Add analytics dashboard with advanced charts
- Export feedback reports to PDF/CSV
- Multi-language support
- Email notifications
- SMS feedback reminders
- Social media integration
- Pagination for feedback history
- Advanced search and filtering

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please create an issue in the project repository.

## Production Deployment

### 1. Configure environment variables
Create a `.env` file at the project root by copying `.env.example`:

```bash
copy .env.example .env
```

Then update the values:

- `DJANGO_SECRET_KEY` — use a strong random secret key
- `DJANGO_DEBUG=False`
- `DJANGO_ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com`
- `DJANGO_SESSION_COOKIE_SECURE=True`
- `DJANGO_CSRF_COOKIE_SECURE=True`
- `DJANGO_SECURE_SSL_REDIRECT=True`

### 2. Install production dependencies

```bash
pip install -r requirements.txt
```

### 3. Collect static files

```bash
python manage.py collectstatic --noinput
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Serve with Gunicorn

```bash
gunicorn feedback_project.wsgi --bind 0.0.0.0:8000
```

### 6. GitHub deployment notes

- Add `.env` and `db.sqlite3` to `.gitignore`
- Commit code and push to GitHub
- Use a deployment platform such as Heroku, PythonAnywhere, Render, or Railway
- On Heroku, use the included `Procfile`
- Set environment variables in the hosting service settings

### 7. Recommended production improvements

- Use PostgreSQL or another production database instead of SQLite
- Enable HTTPS and secure cookies
- Set `ALLOWED_HOSTS` to your real domain only
- Rotate the `DJANGO_SECRET_KEY` for each deployment
