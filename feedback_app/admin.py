from django.contrib import admin
from .models import UserProfile, Feedback


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'city', 'created_at']
    search_fields = ['user__username', 'phone', 'city']


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['user', 'emotion', 'score', 'created_at']
    list_filter = ['emotion', 'created_at']
    search_fields = ['user__username']
    readonly_fields = ['score', 'created_at']
    fields = ['user', 'emotion', 'remarks', 'score', 'created_at']
