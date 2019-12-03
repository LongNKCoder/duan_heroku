from django.contrib import admin
from django.urls import path, include
from login_register import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from post import views as PostView

urlpatterns = [
    path('', PostView.IndexView.as_view(), name = 'index'),
    path('timraovat/', PostView.PostListView.as_view(), name = 'search'),
    path('admin/', admin.site.urls),
    path('users/', include('login_register.urls')),
    path('post/', include('post.urls')),
    path('logout/',auth_views.LogoutView.as_view(), name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
