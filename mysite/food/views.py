from django.shortcuts import render, redirect
from django.http import HttpResponse
from food.models import Items
from django.template import loader
from food.forms import ItemForm

# Create your views here.
def index(request):
    item_list = Items.objects.all()
    #item_list = Items.objects.all().values()
    #template = loader.get_template('food/index.html')
    context = {
        'item_list': item_list
    }
    # return HttpResponse(item_list)
    #return HttpResponse(template.render(context,request))
    return render(request,'food/index.html', context)
def hello(request):
    return HttpResponse('<h1 style="color:red;">Hello world</h1>')

def item(request):
    return HttpResponse('This is an item view')

# def detail(request,item_id):
#     item_1 = Items.objects.get(pk=1)       #pk - primary key
#     item_2 = Items.objects.get(pk=3)
#     context = {
#         'item_1':item_1,
#         'item_2':item_2,
#         'int': item_id,
#     }
#     #return HttpResponse('This is detail view. %s' % item_id)
#     return render(request, 'food/detail.html',context)

def detail(request,item_id):
    item = Items.objects.get(pk=item_id)       #pk - primary key
    context = {
        'item':item,
    }
    #return HttpResponse('This is detail view. %s' % item_id)
    return render(request, 'food/detail.html',context)

def create_item(request):
    form = ItemForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.html', {'form':form})

def update_item(request,id):
    item = Items.objects.get(pk = id)
    form = ItemForm(request.POST or None,instance=item)
    
    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html', {'form':form,'item':item})

def delete_item(request,id):
    item = Items.objects.get(pk=id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request, 'food/item-delete.html',{'item':item})
