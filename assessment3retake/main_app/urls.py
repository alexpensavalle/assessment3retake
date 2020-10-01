from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_item', views.add_item, name='add_item'),
    path('delete_item/<int:id>', views.delete_item, name='delete_item')
]