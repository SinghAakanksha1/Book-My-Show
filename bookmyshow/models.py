import uuid
from msilib import Feature

from django.utils import timezone

from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True, default=timezone.now)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

class User(BaseModel):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

class Region(BaseModel):
    name = models.CharField(max_length=50)

class Theatre(BaseModel):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

class Screen(BaseModel):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    features = models.ManyToManyRel(Feature, through='Feature')

class ScreenFeature(BaseModel):
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('screen', 'feature'),)

class ShowFeature(BaseModel):
    screen = models.ForeignKey(Show, on_delete=models.CASCADE)
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)

class SeatType(models.TextChoices):
    Gold = ('Gold', 'Gold')
    Silver = ('Silver', 'Silver')
    Platinum = ('Platinum', 'Platinum')



class Seat(BaseModel):
    row_number = models.IntegerField()
    col_number = models.IntegerField()
    number = models.CharField(max_length=50)
    seat_Type = models.CharField( choices=SeatType.choices)

class showSeatStatus(models.TextChoices):
    AVAILABLE = ('Available', 'Available')
    MAINTENANCE = ('Maintenance', 'Maintenance')
    RESERVED = ('Reserved', 'Reserved')
    
class ShowSeat(BaseModel):
    show = models.ForeignKey(Show , on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat , on_delete=models.CASCADE)


class Ticket(BaseModel):
    ticket_number = models.IntegerField()
    show = models.ForeignKey(Show , on_delete=models.CASCADE)
    show_seat_type = models.ForeignKey(SeatType, on_delete=models.CASCADE)
    amount = models.IntegerField()
    booking_status = models.CharField( choices=showSeatStatus.choices, max_length=50)
    show_seats = models.ManyToManyField(ShowSeat)

class Payment(BaseModel):
    ref_number = models.IntegerField()
    amount = models.IntegerField()
    mode = models.CharField( max_length=50)
    status = models.CharField( max_length=50)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)









