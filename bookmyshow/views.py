from django.shortcuts import render
from rest_framework import viewsets
from bookmyshow import *
from bookmyshow.serializer import CreateBookingRequestDTO


# Create your views here.
class BookingViewSet(viewsets.viewSet):
    def create_booking(self, request):
        req = CreateBookingRequestDTO(request.data)
        req.is_valid(raise_exception=True)
        try:
        except exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)



