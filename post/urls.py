from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('create/', views.CreatePostView.as_view(), name = 'dangtin'),
    path('<int:pk>', views.PostDetailView.as_view(), name = 'baitinchitiet'),
    path('update/<int:pk>', views.UpdatePostView.as_view(), name = 'capnhat'),
]