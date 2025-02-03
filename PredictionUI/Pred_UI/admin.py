from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import SalaryPrediction

@admin.register(SalaryPrediction)
class SalaryPredictionAdmin(admin.ModelAdmin):
    list_display = ('years_experience', 'predicted_salary', 'created_at')
