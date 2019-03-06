from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('incidences/', IncidenceData, name='incidences'),
    path('county/', CountyData, name='counties'),
    
]
