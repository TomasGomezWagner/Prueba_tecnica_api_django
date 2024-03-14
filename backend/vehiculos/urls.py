from django.urls import path

from . import views

urlpatterns = [
    path("", views.vehiculo_list_view),
    path("<int:pk>/", views.vehiculo_detail_view),
    path("<int:pk>/update/", views.vehiculo_update_view),
    path("<int:pk>/delete/", views.vehiculo_delete_view),
    path("create/", views.vehiculo_create_view),
    path("tipos/", views.tipo_vehiculo_lis_create_view),
    path("marcas/", views.marca_list_create_view),
    path("fichas/", views.ficha_vehiculo_list_create_view),
]
