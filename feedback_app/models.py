from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Feedback(models.Model):
    EMOTION_CHOICES = [
        ('happy', 'Happy - 100%'),
        ('unhappy', 'Unhappy - 50%'),
        ('sad', 'Sad - 0%'),
    ]

    EMOTION_SCORES = {
        'happy': 100,
        'unhappy': 50,
        'sad': 0,
    }

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks')
    emotion = models.CharField(max_length=20, choices=EMOTION_CHOICES)
    score = models.IntegerField()
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.emotion} ({self.score}%)"

    class Meta:
        ordering = ['-created_at']
