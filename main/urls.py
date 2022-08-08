from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('datadawnload', views.datadownload,  name='datadawnload'),
    path('<str:filepath>/', views.cvb)
    # path('about', views.about),
    # path('mun', views.mun),
    # path('ruf', views.ruf)
    # path('upload/', views.upload),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
