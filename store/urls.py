from django.urls import path


from . import views

urlpatterns = [
    # path("", ) # Временно закомментировали маршрут на главную страницу. С ней будем работать позже.
    path("products/", views.get_product_list, name='product_list'),
    path("products/<int:product_id>/", views.get_post_detail, name='product_detail'),
]
