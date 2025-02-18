from rest_framework import serializers

class CreateBookingRequestDTO(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    show_id = serializers.IntegerField()
    show_seat_ids = serializers.ListField(child=serializers.IntegerField())