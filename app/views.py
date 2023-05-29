from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status

from .models import *
from .serializers import *

class TaskAPI(APIView):

    def get(self, request):
        obj = Task.objects.all()
        serializer = TaskSerializer(obj, many=True)
        return Response({
            'status':True,
            'data':serializer.data
        })
    
    def post(self, request):
        data = request.data
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status':True,
                'data':serializer.data
            }, status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def put(self, request):
        data = request.data
        obj = Task.objects.get(id = data['id'])
        serializer = TaskSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status':True,
                'data':serializer.data
            }, status.HTTP_202_ACCEPTED)
        return Response(serializer.errors)
        
    def patch(self, request):
        data = request.data
        obj = Task.objects.get(id = data['id'])
        serializer = TaskSerializer(obj, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status':True,
                'data':serializer.data
            }, status.HTTP_202_ACCEPTED)
        return Response(serializer.errors)
    
    def delete(self, request):
        data = request.data
        obj = Task.objects.get(id = data['id'])
        obj.delete()
        return Response({
            'status':True,
            'message': 'Deleated.'
        }, status.HTTP_200_OK)
    