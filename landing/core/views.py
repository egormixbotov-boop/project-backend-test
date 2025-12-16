from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import UsersInfoSerializer
from .models import UsersCounter


def index(request):
    # Увеличиваем счетчик посещений сайта
    counter, _ = UsersCounter.objects.get_or_create(id=1, defaults={"count": 0})
    counter.count += 1
    counter.save()

    return render(request, "index.html")


@api_view(["POST"])
def contact_create(request):
    serializer = UsersInfoSerializer(data=request.data)
    if serializer.is_valid():
        user_info = serializer.save()

        return Response(
            {
                "message": "Контакт успешно сохранён",
                "id": user_info.id,
            },
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
