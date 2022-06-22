
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
from django.db import connection
from decimal import *

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
    """displaying table from db to ui"""

    tables =  ZakatDetails.objects.all()
    serializer = ZakatDetailsSerializer(tables, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def insertEntries(request):

    result_data = request.data['formState']

    """if user id is not present in db then create it in mapping table and create records in zakat details table """
    if getuserid(result_data['UserId']) == 0:
        if Usermapping.objects.all().count() > 0:
            userid = Usermapping.objects.all().order_by("-userid")[0].id + 1
        else:
            userid = 1
        mapdata = {}
        mapdata['key'] = result_data['UserId']
        mapdata['userid'] = userid

        result_data['UserId'] = userid

        serializer = ZakatDetailsSerializer(data=result_data)

        mapserializer = UsermappingSerializer(data = mapdata)

        if mapserializer.is_valid():
            mapserializer.save()

        if serializer.is_valid():
            serializer.save()

        calculateZakat(userid , 90)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        """ if user id is present in db mapping table then update the corresponding zakat details table for given userid """
    else:
        userid = getuserid(result_data['UserId'])
        result_data['UserId'] = userid

        zakat_details = ZakatDetails.objects.filter(UserId=userid)
        # returns 1 or 0
        zakat_details.update(**result_data)
        calculateZakat(userid, 90)
    return Response("successfully calculated")

def getuserid(userkey):
    """userid = Usermapping.objects.get(key=userkey).userid """
    try:
        usermapid = Usermapping.objects.get(key=userkey).userid
        return usermapid
    except Usermapping.DoesNotExist:
        return 0

def calculateZakat(userid, nisab):
    """
    stored procedure is called written in db

    """
    SQL = 'call calculatezakat('+ str(userid) + ',' + str(nisab) +')'
    with connection.cursor() as curs:
        curs.execute(SQL)

        


            