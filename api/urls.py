from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name = 'routes'),
    path('table/', views.getTable, name = 'tables'),
    path('entries/', views.insertEntries, name = 'tables')
]
