"""
    Decides:
        1. What logic runs
        2. Who can access
        3. What happens on GET/ POST/ PUT/ DELETE
"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from assessment.choices import QuestionTypeChoices, DifficultyChoices

from rest_framework.response import Response

from .models import Question
from .serializers import QuestionSerializer

class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]

        return [IsAuthenticated()]

    # returns easy, medium and hard question each of 5 numbers
    def list(self, request, *args, **kwargs):

        allowed_types = [QuestionTypeChoices.GRAMMAR, QuestionTypeChoices.VOCABULARY]

        easy_questions = Question.objects.filter(
            difficulty=DifficultyChoices.EASY,
            question_type__in=allowed_types,
        ).order_by('?')[:5]

        medium_questions = Question.objects.filter(
            difficulty=DifficultyChoices.MEDIUM,
            question_type__in=allowed_types,
        ).order_by('?')[:5]

        hard_questions = Question.objects.filter(
            difficulty=DifficultyChoices.HARD,
            question_type__in=allowed_types,
        ).order_by('?')[:5]

        return Response({
            "easy": QuestionSerializer(easy_questions, many=True).data,
            "medium": QuestionSerializer(medium_questions, many=True).data,
            "hard": QuestionSerializer(hard_questions, many=True).data,
        })

    