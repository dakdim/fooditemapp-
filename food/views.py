from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
# Create your views here.
def index(request):
    item_list=Item.objects.all()
    # template=loader.get_template('food/index.html')
    # no need of it we are using render
    context={
        'item_list':item_list

    }
    # return HttpResponse(template.render(context,request))
    # we are using render instead of http[response in this]
    return render(request,'food/index.html',context)
class IndexClassView(ListView):
    model=Item;
    template_name='food/index.html' 
    comtext_object_name='item_list'



def item(request):
    return HttpResponse('<h1>these are the item</h1>')

def detail(request,item_id):
    item=Item.objects.get(pk=item_id)
    context={
        'item':item,

    }
    return render(request,'food/detail.html',context)
  
class FoodDetail(DetailView) :
    model=Item
    template_name='food/detail.html'

# def detail(request, item_id):
#     item = get_object_or_404(Item, pk=item_id)  # Ensure you fetch the correct object or return a 404
#     context = {
#         'item': item,
#     }
#     return render(request, 'food/detail.html', context)

def create_item(request):
    form=ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food')
    return render(request,'food/item-form.html',{'form':form})

# this is a class based view for create item
class CreateItem(CreateView):
    model=Item;
    fields=['item_name','item_desc','item_price','item_image'] 
    template_name='food/item-form.html'

    def form_valid(self, form):
        form.instance.user_name=self.request.user
        return super().form_valid(form)
    



def update_item(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        return HttpResponseNotFound("Item not found")

    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food')
    
    return render(request, 'food/item-form.html', {'form': form, 'item': item})
# view deleting an item
def delete_item(request,id):
    
    item = Item.objects.get(id=id)
    

    if request.method=='POST':
        item.delete()
        return redirect('food')
    
    return render(request,'food/item-delete.html',{'item':item})
    

