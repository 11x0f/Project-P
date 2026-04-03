from django.db import models
from users.models import User
from assessment.choices import QuestionTypeChoices, DifficultyChoices
import uuid

class Question(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)

    question_type=models.CharField(
        max_length=20,
        choices=QuestionTypeChoices
    ) 

    difficulty =  models.CharField(
        max_length=10,
        choices=DifficultyChoices.choices,
        default=DifficultyChoices.MEDIUM
    )

    question_text=models.TextField()

    audio_file=models.FileField(
        upload_to='assessment/audio/',
        null=True,
        blank=True
    )

    correct_answer=models.TextField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.type} - {self.question_text}"

class UserResponse(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    question=models.ForeignKey(Question, on_delete=models.CASCADE)

    text_answer=models.TextField(null=True, blank=True)

    audio_answer=models.FileField(
        upload_to='assessment/response',
        null=True,
        blank=True
    )

    score=models.FloatField(default=0)

    def __str__(self):
        return f"{self.user.email} - {self.question.type}"

class AssessmentResult(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    grammar_score=models.FloatField(default=0)
    listening_score=models.FloatField(default=0)
    speaking_score=models.FloatField(default=0)

    overall_score=models.FloatField(default=0)

    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.overall_score}"


    