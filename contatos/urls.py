from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('busca/>',views.busca,name='busca'),
    path('<int:contato_id>',views.ver_contato,name='ver_contato'),
    path('sobre/<int:contato_string>',views.ver_categoria,name='ver_categoria'),
    path('sobre',views.ver_sobre,name='sobre'),




]