from django.db import models
from users.models import User
from assessment.choices import QuestionTypeChoices, DifficultyChoices
from users.choices import LevelChoices
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

    options = models.JSONField(
        null=True,
        blank=True,
        help_text="List of options for MCQs."
    )

    correct_answer=models.TextField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.type} - {self.question_text}"

class AssessmentSession(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='assessment_sessions'
    )

    attempt_number=models.PositiveIntegerField()

    started_at=models.DateTimeField(auto_now_add=True)
    completed_at=models.DateTimeField(null=True, blank=True)

    is_completed=models.BooleanField(default=False)

    level_assigned = models.CharField(
        max_length=20, 
        choices=LevelChoices.choices,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.user.email} - {self.started_at}"

class UserResponse(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    assessment_session=models.ForeignKey(
        AssessmentSession,
        on_delete=models.CASCADE,
        related_name='responses'
    )

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    question=models.ForeignKey(Question, on_delete=models.CASCADE)

    text_answer=models.TextField(null=True, blank=True)

    audio_answer=models.FileField(
        upload_to='assessment/response',
        null=True,
        blank=True
    )

    score=models.FloatField(default=0)

    remarks=models.TextField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.question.type}"

class AssessmentResult(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    assessment_session=models.OneToOneField(
        AssessmentSession,
        on_delete=models.CASCADE,
        related_name='result'
    )

    user=models.ForeignKey(User, on_delete=models.CASCADE)

    grammar_score=models.FloatField(default=0)
    vocabulary_score=models.FloatField(default=0)
    listening_score=models.FloatField(default=0)
    speaking_score=models.FloatField(default=0)

    overall_score=models.FloatField(default=0)

    feedback = models.TextField(
        null=True,
        blank=True
    )

    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.overall_score}"


    