from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import FileSerializer
from .models import file

from django.http import FileResponse
import io

class FileViewSet(viewsets.ModelViewSet):
    queryset = file.objects.all()
    serializer_class = FileSerializer

    def post(self, request, *args, **kwargs):
        cover = request.data['cover']
        title = request.data['title']
        file.objects.create(title=title, cover=cover)
        return HttpResponse({'message': 'file Created'}, status=200)
    
  