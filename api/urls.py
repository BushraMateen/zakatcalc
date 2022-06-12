from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name = 'routes'),
    path('table/', views.getTable, name = 'tables'),
    path('entries/', views.insertEntries, name = 'tables'),
    path('userid/<int:id>/', views.getuserid,name= 'userids')
    #path('notes/create/', views.addnote, name='addnote'),

]
