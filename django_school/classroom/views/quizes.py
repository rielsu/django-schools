from rest_framework import viewsets

from ..serializers import QuizSerializer
from ..models import Quiz

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer