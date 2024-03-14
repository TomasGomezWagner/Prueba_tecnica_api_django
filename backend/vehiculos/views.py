from rest_framework import filters, generics  # authentication

from .models import Vehiculo
from .serializers import (
    VehiculoCreateSerializer,
    VehiculoDeleteUpdateSerializer,
    VehiculoDetailSerializer,
)


class VehiculoDetailView(generics.RetrieveAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoDetailSerializer
    lookup_field = "pk"


vehiculo_detail_view = VehiculoDetailView.as_view()


class VehiculoCreateView(generics.CreateAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoCreateSerializer

    def perform_create(self, serializer):
        print(serializer)
        return serializer.save()


vehiculo_create_view = VehiculoCreateView.as_view()


class VehiculoUpdateView(generics.UpdateAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoDeleteUpdateSerializer
    lookup_field = "pk"


vehiculo_update_view = VehiculoUpdateView.as_view()


class VehiculoDeleteView(generics.DestroyAPIView):
    """Elimina el modelo y la ficha ya que tienen relacion uno a uno"""

    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoDetailSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


vehiculo_delete_view = VehiculoDeleteView.as_view()


class VehiculoListView(generics.ListAPIView):
    """
    Por defecto los ordena por año de menor a mayor
    forma de usar\n
    data = {"search": "auto", "ordering": "year"}\n
    response = requests.get(endpoint, params=data)
    """

    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoDetailSerializer
    # authentication_classes = [
    #     authentication.SessionAuthentication,
    #     TokenAuthentication,
    # ]
    # permission_classes = [permissions.DjangoModelPermissions]

    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ["tipo__descripcion"]
    ordering_fields = ["anio", "precio"]
    ordering = ["anio"]

    def get_queryset(self):
        queryset = Vehiculo.objects.all()
        tipo_param = self.request.query_params.get("tipo", None)

        if tipo_param is not None:
            queryset = queryset.filter(tipo_modelo__descripcion=tipo_param)

        return queryset


vehiculo_list_view = VehiculoListView.as_view()
