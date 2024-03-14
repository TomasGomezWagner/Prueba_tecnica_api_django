from django.urls import path

from . import views

urlpatterns = [
    path("", views.vehiculo_list_view),
    path("<int:pk>/", views.vehiculo_detail_view),
    path("<int:pk>/update/", views.vehiculo_update_view),
    path("<int:pk>/delete/", views.vehiculo_delete_view),
    path("create/", views.vehiculo_create_view),
]
