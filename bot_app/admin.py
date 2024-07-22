from django.contrib import admin
from .models import Client, Issue, Message

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'created_at')
    readonly_fields = ('created_at',)

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('client',  'title', 'description', 'created_at')
    readonly_fields = ('created_at', 'photos', 'videos', 'audios')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('issue', 'content', 'media_url', 'media_type', 'sent_at', 'response')
    readonly_fields = ('media_url', 'media_type', 'sent_at')
