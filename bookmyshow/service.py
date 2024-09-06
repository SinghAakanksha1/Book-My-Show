from bookmyshow.models import User, ShowSeat, showSeatStatus


class BookShowService:
    def create_booking(self, user_id , show_seat_ids , show_id):
        if len(show_seat_ids)>10:
            raise ValueError("Show seat id should be less than 10")
        try :
            user = User.objects.get(id=user_id)
            if user is None:
                raise User.DoesNotExist
            show = Show.objects.get(id=show_id)
            if show is None:
                raise Show.DoesNotExist

            show_seats = ShowSeat.objects.filter(id=show_seat_ids)
            for show_seat in show_seats:
                if show_seat.show_seat_status != showSeatStatus.AVAILABLE :
                    raise ValueError("Show seat not available")

            for show_seat in show_seats:
                show_seat.show_seat_status = showSeatStatus.LOCKED
                show_seat.save()


            #create booking
            booking = Ticket(
                user=user,
                show=show,
                amount =100,
                booking_status= "PENDING" ,
                ticket_number = timezone.now(),
                # show_seats = show_seats,
            )
            booking.save()
            #CREATE PAYMENT
            for show_seat in show_seats:
                show_seat.show_seat_status = showSeatStatus.RESERVED
                show_seat.save()

            booking.show_seats=show_seats
            booking.save()
            return booking
        except Exception as e:
            print(e)





