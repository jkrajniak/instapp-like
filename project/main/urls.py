from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='main_index'),
    url(r'upload/', views.upload_image, name="upload_image"),
    url(r'image/(?P<image_id>[0-9]+)/', views.view_image, name='view_image'),
    url(r'fetch_data/(?P<image_id>[0-9]+)/',
        views.fetch_data, name='fetch_data_image')
]
