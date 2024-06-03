import statistics
from django.conf import settings
from django.contrib import admin
from django.urls import path, include  
from django.conf.urls.static import static
# from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views  



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("ITapp.urls"),),
    path('index/', include("ITapp.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
     
    # path('logout/', LogoutView.as_view(next_page='/index'), name='logout'),
    #  path('login/', auth_views.LogoutView.as_view(), name='logout'), 
    # path('logout', auth_views.LogoutView.as_view(template_name = 'templates/registration/logout.html'), name = 'logout'), 
    # path('accounts/login/', auth_views.LogoutView.as_view(template_name = '/index.html'), name = 'logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
