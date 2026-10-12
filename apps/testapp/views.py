from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from apps.testapp.permissions import IsModeratorOrAdmin
from rest_framework.views import APIView
from rest_framework.response import Response


class PublicDataView(APIView):
   permission_classes = [IsAuthenticated]

   def get(self, request):
      return Response({"message": f"Привет, {request.user.email}! Это обычные данные."})


# Эндпоинт 2: Доступен ТОЛЬКО Модераторам и Админам
class SecretModeratorView(APIView):
   permission_classes = [IsModeratorOrAdmin]

   def get(self, request):
      return Response({"message": f"Секретная панель! Твоя роль: {request.user.role}."})