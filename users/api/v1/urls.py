from django.urls import path, include
from .viewsets import HolidayCoincides

urlpatterns = [
    
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('hoilday_coincide/', HolidayCoincides.as_view(), name='hoilday_coincide')
]