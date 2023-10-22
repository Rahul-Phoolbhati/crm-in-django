from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from website.models import Record
from .serializers import RecordSerializer
from rest_framework import viewsets # set of views, no need get,post.....it automatically call
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import  IsAuthenticatedOrReadOnly



# get all the data
# serialize them 
# return jsom


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication]





 

# @api_view(['GET']) # decorater
# def getData(request):
#     recordd=Record.objects.all()
#     serializer=RecordSerializer(recordd, many=True) #many=True, will serialize each instance in the list and return a list of JSON objects.
#         # person={'name':'harsh','age':24}
#     return Response({"Data's":serializer.data}) #this will be output as json # The Response class automatically serializes the data to JSON. 

# @api_view(['POST'])
# def addData(request):
#         serializer=RecordSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data) #request.data handles arbitary data, whule request .POST handles form data 

# @api_view(['DELETE'])
# def deleteData(request,pk):
#     delete_=Record.objects.get(id=pk)
#     delete_.delete()
#     return Response("Record deleted successfully") 

# @api_view(['PUT'])
# def updateData(request,pk):
#         update_=Record.objects.get(id=pk)
#         serializer = RecordSerializer(instance=update_, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data) 



# # Create your views here.
