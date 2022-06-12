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
from .serializers import  UsermappingSerializer
from .models import Usermapping

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

    result_data = request.data['formState']
    # call getuserid method to fetch the user id from database for given user key (result_data.formData.userid)
    userid = getuserid(result_data['UserId'])

    result_data.UserId = userid

    serializer = ZakatDetailsSerializer(data=result_data)
    if serializer.is_valid():
        serializer.save()
        #return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


def getuserid(userkey):
    userid = Usermapping.objects.filter(key=userkey)
    if userid is not None:
        return userid
    else:
        return (Usermapping.objects.all().order_by("-userid")[0] + 1)


            