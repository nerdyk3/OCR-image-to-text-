from django.urls import path
from . import views 
from  django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('index',views.index,name='index'),
    # path('analyze', views.analyze, name='analyze'),
    
    # path('ex1', views.ex1, name='ex1'),
    # path('index', views.index, name='index'),
]


## for media setting()
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)