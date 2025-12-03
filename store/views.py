from django.shortcuts import render, get_object_or_404, redirect

from store.models import Products

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
  if request.method == "GET":
    return render(request, 'store/product_add.html')
  
  if request.method == "POST":
    title = request.POST.get('title').strip()
    text = request.POST.get('text').strip()

    errors = {}

    if not title:
      errors['title'] = 'Наименование товара необходимо заполнить.'
    if not text:
      errors['text'] = 'Описание товара обязателено нужно указать.'

    if not errors:
      product = Products.objects.create(product_name=title, about_item=text)

      return redirect('product_detail', product_id=product.id)
    else:
      context = {
        'errors': errors,
        'title': title,
        'text': text
      }

      return render(request, 'store/product_add.html', context)

