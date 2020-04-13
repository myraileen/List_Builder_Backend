from .models import User, List
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, ListSerializer

# User Viewset
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer

class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ListSerializer

