from .forms import ItemForm
from django.views.generic import ListView


def index(request):
    items = Item.objects.all()
    item_form = ItemForm()
    return render(request, 'index.html', {'items': items, 'item_form': item_form})

def add_item(request):
    item_form = ItemForm(request.POST)
    item_form.save()    
    return redirect('/')

def delete_item(request, id):
    Item.objects.get(id=id).delete()
    return redirect('/')