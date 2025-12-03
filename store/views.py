from django.shortcuts import render, get_object_or_404, redirect

from store.models import Products
from store.forms import ProductForm

# "request" в скобках указывать обязательно, можно поставить другое слово, 
# но лучше "request".
def get_product_list(request): 
  products = Products.objects.all()

  # Здесь уже нужно создать 
  # первый шаблон. Путь 'store/index.html' здесь не нужно указывать полный. 
  # Джанго шаблоны ищет в папке "templates".
  return render(request, 'store/product_list.html', context={'products': products}) 


def get_product_detail(request, product_id):
  # return render(request, 'store/product_detail.html', {"product": Products.objects.get(id=product_id)})
  return render(request, 'store/product_detail.html', {"product": get_object_or_404(Products, id=product_id)})


def create_product(request):
  form = ProductForm(request.POST or None)
  if request.method == "POST":

    if form.is_valid():
      product = Products.objects.create(
      product_name=form.cleaned_data['title'],
      about_item=form.cleaned_data['text']
      )


      return redirect('product_detail', product_id=product.id)
    # Если форма невалидна, продолжим к render ниже.
  
  return render(request, 'store/product_add.html', {"form": form})


