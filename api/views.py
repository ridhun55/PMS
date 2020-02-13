
from MasterApp import  models
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from django.shortcuts import get_object_or_404
from  rest_framework import status

# Create your views here.

class ProjectView(APIView):

    def get(self, request,id=None):
        if id != None:
            data = get_object_or_404(models.Project, pk=id)
            Var = serializers.ProjectSerializer(data)
        else:
            data = models.Project.objects.all()
            Var = serializers.ProjectSerializer(data,many=True)
        data = Var.data
        return Response({'success': True, 'data': data, 'error': None}, status=status.HTTP_200_OK)

    def post(self,request):
        Var = serializers.ProjectSerializer(data = request.data)
        if Var.is_valid():
            Var.save()
            data = Var.data
            return Response({'success':True,'data':data,'error':None},status=status.HTTP_201_CREATED)
        else:
            error = Var.errors
            return Response({'success':False,'data':None,'error':error},status=status.HTTP_400_BAD_REQUEST)


# class EmployeeView(APIView):
#
#     def get(self, request):
#         data = models.Employee.objects.all()
#         serial = serializers.EmployeeSerializer(data,many=True)
#         return Response(serial.data)