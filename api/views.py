from rest_framework import viewsets
from .serializer import ProgrammerSerializer
from .models import Programmer


class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
