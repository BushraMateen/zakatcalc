from http.client import LineTooLong
from tkinter.tix import Tree
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ZakatTable
from .serializers import ZakatTableSerializer
from rest_framework import status
from rest_framework.parsers import JSONParser 
from .models import  ZakatDetails
from .serializers import  ZakatDetailsSerializer

@api_view(['GET'])
def getRoutes(request):
    
    routes = [
        {
            'Endpoint':'/host/',
            'method': 'GET',
            'body': None,
            'description': 'Return data'
        },
        {
            'Endpoint': '/entries/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getTable(request):
    tables =  ZakatDetails.objects.all()
    serializer = ZakatDetailsSerializer(tables, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def insertEntries(request):
    # zakatTable = ZakatTable(
    #         AmtVal = request.data['formState']['A1'])
    # zakatTable.save()


    tables = ZakatDetails.objects.all()
    serializer = ZakatDetailsSerializer(tables,many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    # entry = request.data['formState']
    # for i in entry.items():
    #     entry_data = ZakatDetails(
           
    #         AmtVal = i['intA']
    #     )
    #     entry_data.save()
            