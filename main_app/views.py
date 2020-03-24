from django.shortcuts import render, redirect 
from django.views.generic import CreateView
from .models import Item
# Create your views here.

def index(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})

class CreateItem(CreateView):
    model = Item
    fields = '__all__'
    template_name = 'add.html'
    success_url = '/'

def delete(request, id):
    Item.objects.get(id=id).delete()
    return redirect('/')