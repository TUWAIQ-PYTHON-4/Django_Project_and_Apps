
from django.shortcuts import render



def index(request):
    search = request.GET.get('search')

    return render(request, 'base.html',{'search':search})