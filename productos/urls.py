from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static        

urlpatterns = [
    url(r'^$', views.hello_world, name='hello'),
    url(r'^producto/agregar', views.agregar_producto, name = "agregar")

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
