from django.urls import path
from . import views


urlpattern = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('bloggers/', views.BloogerListView.as_view(), name='bloggers'),
    path('blogger/<int:pk>', views.BlogsByAuthorListView.as_view(), name='blog-by-author'),
]