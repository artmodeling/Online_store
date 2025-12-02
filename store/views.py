from django.shortcuts import render, get_object_or_404

from store.models import Products

# "request" в скобках указывать обязательно, можно поставить другое слово, 
# но лучше "request".
def get_product_list(request): 
  products = Products.objects.all()

  # Здесь уже нужно создать 
  # первый шаблон. Путь 'store/index.html' здесь не нужно указывать полный. 
  # Джанго шаблоны ищет в папке "templates".
  return render(request, 'store/product_list.html', context={'products': products}) 


def get_post_detail(request, product_id):
  return render(request, 'store/product_detail.html', {"product": Products.objects.get(id=product_id)})
  # return render(request, 'store/product_detail.html', {"product": get_object_or_404(Products, id=product_id)})
