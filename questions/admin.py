from django.contrib import admin
from .models import Question , Answers

# Register your models here.
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["title" , "created_by"]

@admin.register(Answers)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["title" , "created_by"]
