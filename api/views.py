from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer,DetailBookSerializer
from .models import calculate


# Create your views here.





@api_view(['GET'])
def taskList(request):
    tasks = calculate.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = DetailBookSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
