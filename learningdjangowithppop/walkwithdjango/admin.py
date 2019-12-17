from django.contrib import admin
from .models import Sentiment

# Register your models here.

@admin.register(Sentiment)
class SentimentAdmin(admin.ModelAdmin):
    list_display = ('text', 'value')


