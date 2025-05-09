from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'user_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.user_register_view, name='register'),
    path('login/', views.user_sign_in_view, name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html', next_page='login'), name='logout'),
    path('', include('article_app.urls'))

]
