from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ZakatTable
from .serializers import ZakatTableSerializer
from rest_framework import status
from rest_framework.parsers import JSONParser 

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
    tables = ZakatTable.objects.all()
    serializer = ZakatTableSerializer(tables, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def insertEntries(request):
    tables = ZakatTable.objects.all()
    serializer = ZakatTableSerializer(tables, many = True)
    return Response(serializer.data)
    # new_entry = 'formState'
    # response = request.post( new_entry)
    # data = response.json()
    # serializer = ZakatTableSerializer(data=data)
    # entry = data['formState']
    # for i in entry:
    #         entry_data = ZakatTable(
    #             Line = i['intLine'],
    #             name = i['strname'],
    #             category = i['strcategory'],
    #             AmtVal = i['intAmtVal'],
    #             ZakatRate = i['decimalZakatRate'],
    #             ZakatDue = i['decimalZakatDue']
    #         )
    #         entry_data.save()
    #         return Response(serializer) 