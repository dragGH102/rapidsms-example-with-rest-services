# from django.shortcuts import render

from .models import Choice
from rest_framework import viewsets
from .serializers import ChoiceSerializer



# Views for API management

class ChoiceViewSet(viewsets.ModelViewSet): #>> ModelViewSet (type of Class-based view) to group views with common behavior
    """
    API endpoint that allows choices to be viewed or edited.
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
