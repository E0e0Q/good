from django.urls import path
from blog.views import post_list,post_detaili,glavnii_list,kruiz,fail

urlpatterns = [
    path('',glavnii_list, name='glavnii_list'),
    path('post/listr',post_list, name='post_list'),
    path('post/fail',fail, name='fail'),
    path('post/kruiz <int:i_pk>',kruiz, name='kruiz'),
    path('post/list',post_list, name='post_list'),
    path('post/detaili <int:i_pk>',post_detaili, name='post_detaili'),

]