from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.index, name='read'),
    path('create/', v.create,name='create'),
    path('update/<int:id>', v.update,name='update'),
    path('delete/<int:id>', v.delete,name='delete'),
   
]
