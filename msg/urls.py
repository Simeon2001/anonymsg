from django.urls import path
from . import views 
from .views import SignUpView,PostCreateView,PostDeleteView,IndeView
urlpatterns = [
    path('', IndeView.as_view(), name='ome/'),
    path('homes', views.IndexView, name='Home/'),
    path('logout/', views.logout, name='logout/'),
    path('post/<str:pk>/', views.postr, name="post_detail/"),
    path('comment/<str:pi>/', views.comment_lock, name="comment_lock/"),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='pdelete/'),
    
]
