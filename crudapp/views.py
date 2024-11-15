from django.shortcuts import render, get_object_or_404, redirect
from .models import Item

# Create your views here.
#CRUD
def create_item(request):
    if request.method == 'P0ST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        Item.objects.create(name=name,description=description)
        return redirect('item_list')
    return render(request,'items_forms.html')
# read
def item_list(request):
    items=Item.objects.all()
    return render(request,'items_list.html',{'items':items})

def update_item(request,pk):
    item=get_object_or_404(Item,pk=pk)
    if request.method=='POST':
        item.name=request.POST.get('name')
        item.description=request.POST.get('description')
        item.save()
        return redirect('item_list')
    return render(request,'items_list.html',{'item':item})

# delete

def delete_item(request,pk):
    item=get_object_or_404(Item,pk=pk)
    if request.method=='POST':
        item.delete()
        return redirect('item_list')
    return render(request,'item_confirm_delete.html',{'item':item})