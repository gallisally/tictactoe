from django.shortcuts import render,HttpResponse,redirect
from tictactoe.models import Room
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method =='GET':
        return render(request,"index.html")
    if request.method=='POST':
        print(request.POST)
        roomID=request.POST.get("room-id",None)
        playerName=request.POST.get("player-name","unknown player")
        if (roomID):
            try:
                room=Room.objects.get(id=roomID)
                return redirect(f'/tictactoe/{room.id}/{playerName}/')
            except Room.DoesNotExist:
                messages.error(request,'La habitacion no existe')
                return redirect(f'/')         
        else:
            room=Room.objects.create()
            return redirect(f'/tictactoe/{room.id}/{playerName}')

        #return HttpResponse('manejando solicitud POST')

def game(request,id=None, name=None):
    try:
        room=Room.objects.get(id=id)
        return render(request,'game.html',{'room':room,'name':name})
    except Room.DoesNotExist:
        messages.error(request,'La habitacion no existe')
        return redirect(f'/')    


    return render(request,'game.html')
