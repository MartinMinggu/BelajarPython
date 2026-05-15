from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer
from django.contrib.auth.models import User

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    # Siapa saja boleh mengakses halaman register tanpa perlu login dulu
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer