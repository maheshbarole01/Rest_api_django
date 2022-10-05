from django.shortcuts import render
from rest_framework .decorators import api_view
from .serializers import AdmissionSerializer
from .models import AdmissionModel
from rest_framework.response import Response

# Create your views here.

@api_view(['GET','POST','PATCH','PUT','DELETE'])

def Admission_api(request,pk = None):
    if request.method =='GET':
        id = pk 
        if id is not None:
            add = AdmissionModel.objects.get(id=id)
            serializers  = AdmissionSerializer(add)
            return Response(serializers.data)

        # then condition is false 
        add = AdmissionModel.objects.all()
        serializers = AdmissionSerializer(add,many = True)
        return Response(serializers.data)
       

    if request.method == 'POST':
        serializers = AdmissionSerializer(data=request.data)
        if serializers .is_valid():
            serializers.save()
            return Response({'msg':'data created'})
        return Response(serializers.errors)

    if request.method == 'PATCH':
        id = pk 
        add = AdmissionModel.objects.get(id = id)
        serializers = AdmissionSerializer(add,data= request.data,partial = True)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'data patched'})
        return Response(serializers.errors)

    if request.method == 'PUT':
        id = pk 
        add = AdmissionModel.objects.get(id=id)
        serializers = AdmissionSerializer(add,data =request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"msg":'data completed updated '})
        return Response(serializers.errors)

    
    if request.method == 'DELETE':
        id = pk 
        add = AdmissionModel.objects.get(pk = id)
        add.delete()
        return Response({'msg':'Data deleted'})
