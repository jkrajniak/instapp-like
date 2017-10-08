from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='main_index'),
    url(r'upload/', views.upload_image, name="upload_image")
]