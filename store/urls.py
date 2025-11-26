from django.urls import path


from . import views

urlpatterns = [
  # path("", ) # Временно закомментировали маршрут на главную страницу. С ней будем работать позже.
  path("products/", views.get_product_list) # Вместо "products" можно указать, что угодно. 
  #"/" после него ставить обязательно. + "views.get_product_list" пишем без круглых скобок, 
  # потому что если написать так: "views.get_product_list()", то это будет вызов функции. Здесь это не нужно.
]
