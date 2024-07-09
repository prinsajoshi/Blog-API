from django.urls import path
from .views import BlogDetail,BlogListCreate

#Urlpatterns for performing http actions
urlpatterns=[
    path("blogs/",BlogListCreate.as_view(),name='blog-list-create'),
    path("blogs/<int:pk>/",BlogDetail.as_view(),name='blog-detail'),
]