def index(request):
    if request.method == 'POST':
        form = ChoiceForm(request.POST)

        if form.is_valid():
            room_type = form.cleaned_data['room_type']
            no_of_rooms = form.cleaned_data['no_of_rooms']
            # all_rooms = Rooms.objects.filter(room_type = room_type).update(available_count=no_of_rooms)
            q = Rooms.objects.get(pk=room_type)
            available_rooms = q.available_count
            if available_rooms >= no_of_rooms:
                q.available_count = available_rooms -no_of_rooms
                q.save()
                room_val =''
                if room_type=='1':
                    room_val ='Standard'
                elif room_type=='2':
                    room_val ='Classic'
                elif  room_type=='3' :
                    room_val ='Deluxe'
                return HttpResponse(f'{no_of_rooms} rooms of type {room_val} are booked')
            else:
                return HttpResponse('Booking failed')
    else:
        form = ChoiceForm()

    return render(request,
                  'Hotel/bookroom.html',
                  {'form': form})