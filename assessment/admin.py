from django.contrib import admin
from .models import Question, AssessmentSession, UserResponse, AssessmentResult

# Register your models here.

@admin.register(Question)
class QuestionModel(admin.ModelAdmin):
    list_display = [field.name for field in Question._meta.fields]

    list_filter = ('question_type', 'difficulty')
    search_filter = ('question_text')

@admin.register(AssessmentSession)
class AssessmentSessionModel(admin.ModelAdmin):
    list_display = [field.name for field in AssessmentSession._meta.fields]

    search_filter = ('user')

@admin.register(UserResponse)
class UserResponseModel(admin.ModelAdmin):
    list_display = [field.name for field in UserResponse._meta.fields]

    search_filter = ('user')

@admin.register(AssessmentResult)
class AssessmentResultModel(admin.ModelAdmin):
    list_display = [field.name for field in AssessmentResult._meta.fields]

    search_filter = ('user')
     


