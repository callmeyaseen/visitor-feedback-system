from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone
from .forms import SignUpForm, LoginForm, FeedbackForm
from .models import Feedback, UserProfile


def index(request):
    if request.user.is_authenticated:
        return redirect('feedback')
    return redirect('login')


def signup(request):
    if request.user.is_authenticated:
        return redirect('feedback')
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('feedback')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = SignUpForm()
    
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('feedback')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            try:
                user = User.objects.get(email=email)
                user = authenticate(request, username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f'Welcome back, {user.first_name or user.username}!')
                    return redirect('feedback')
                else:
                    messages.error(request, 'Invalid password.')
            except User.DoesNotExist:
                messages.error(request, 'Email not found.')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')


@login_required(login_url='login')
def feedback_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    today = timezone.localdate()
    existing_today = Feedback.objects.filter(user=request.user, created_at__date=today).exists()

    if existing_today:
        messages.warning(request, 'Aapne aaj pehle hi feedback diya hai. Kal phir submit karein.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.score = Feedback.EMOTION_SCORES[feedback.emotion]
            feedback.save()
            messages.success(request, 'Thank you for your feedback!')
            return redirect('thank_you')
    else:
        form = FeedbackForm()
    
    return render(request, 'feedback.html', {
        'form': form,
        'user_profile': user_profile,
        'question': 'How was your visit today?'
    })


@login_required(login_url='login')
def thank_you(request):
    recent_feedback = Feedback.objects.filter(user=request.user).first()
    return render(request, 'thank_you.html', {'feedback': recent_feedback})


@login_required(login_url='login')
def dashboard(request):
    user_feedbacks = Feedback.objects.filter(user=request.user)
    total_feedback = user_feedbacks.count()
    avg_score = sum([f.score for f in user_feedbacks]) / total_feedback if total_feedback > 0 else 0
    
    happy_count = user_feedbacks.filter(emotion='happy').count()
    unhappy_count = user_feedbacks.filter(emotion='unhappy').count()
    sad_count = user_feedbacks.filter(emotion='sad').count()
    
    emotion_counts = {
        'happy': happy_count,
        'unhappy': unhappy_count,
        'sad': sad_count,
    }
    
    # Calculate percentages for progress bars
    emotion_percentages = {}
    if total_feedback > 0:
        emotion_percentages['happy'] = (happy_count / total_feedback) * 100
        emotion_percentages['unhappy'] = (unhappy_count / total_feedback) * 100
        emotion_percentages['sad'] = (sad_count / total_feedback) * 100
    else:
        emotion_percentages['happy'] = 0
        emotion_percentages['unhappy'] = 0
        emotion_percentages['sad'] = 0
    
    return render(request, 'dashboard.html', {
        'user_feedbacks': user_feedbacks,
        'total_feedback': total_feedback,
        'avg_score': round(avg_score, 2),
        'emotion_counts': emotion_counts,
        'emotion_percentages': emotion_percentages
    })


@login_required(login_url='login')
def user_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'profile.html', {'user_profile': user_profile})
