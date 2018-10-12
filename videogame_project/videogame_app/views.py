from django.http import HttpResponse



def name(request):
    return HttpResponse("The game name is ")


def genre(request):
    return HttpResponse("The genre of the game is ")