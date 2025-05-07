from django.urls import path
from . import views
from .views import CatCreate, CatUpdate, CatDelete, ToyCreate, ToyUpdate, ToyDelete, ToyList, ToyDetail

urlpatterns = [
    # Authentication
    path('about/', views.about, name='about'),
    path('', views.Home.as_view(), name='home'),
    path('accounts/signup/', views.signup, name='signup'),


    # Cat views
    path('cats/', views.cat_index, name='cat-index'),
    path('cats/<int:cat_id>/', views.cat_detail, name='cat-detail'),
    path('cats/create/', CatCreate.as_view(), name='cat-create'),
    path('cats/<int:pk>/update/', CatUpdate.as_view(), name='cat-update'),
    path('cats/<int:pk>/delete/', CatDelete.as_view(), name='cat-delete'),
    path('cats/<int:cat_id>/add-feeding/', views.add_feeding, name='add-feeding'),
    path('cats/<int:cat_id>/assoc-toy/<int:toy_id>/', views.associate_toy, name='associate-toy'),
    path('cats/<int:cat_id>/remove-toy/<int:toy_id>/', views.remove_toy, name='remove-toy'),

    # Toy views
    path('toys/', ToyList.as_view(), name='toy-index'),
    path('toys/create/', ToyCreate.as_view(), name='toy-create'),
    path('toys/<int:pk>/', ToyDetail.as_view(), name='toy-detail'),
    path('toys/<int:pk>/update/', ToyUpdate.as_view(), name='toy-update'),
    path('toys/<int:pk>/delete/', ToyDelete.as_view(), name='toy-delete'),
]