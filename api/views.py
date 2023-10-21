from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from website.models import Record
from .serializers import RecordSerializer

@api_view(['GET'])
def getData(request):
    recordd=Record.objects.all()
    serializer=RecordSerializer(recordd, many=True)


    # person={'name':'harsh','age':24}
    return Response(serializer.data) #this will be output as json # The Response class automatically serializes the data to JSON. 

@api_view(['POST'])
def addData(request):
        serializer=RecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)





# Create your views here.
