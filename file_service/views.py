from rest_framework import mixins, status, permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import File
from .serializers import FileSerializer


class FileView(mixins.CreateModelMixin,
               mixins.RetrieveModelMixin,
               GenericViewSet):
    serializer_class = FileSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        size = request.data.get('size')
        file = request.data.get('file')
        file_m = File.objects.create(
            name=name,
            size=size,
            file=file
        )
        return Response({
            'message': 'File uploaded!',
            'id': file_m.id,
        })

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
