from rest_framework import serializers

from .models import FichaVehiculo, Marca, TipoVehiculo, Vehiculo


class FichaVehiculoListCreateSerializer(serializers.ModelSerializer):
    """Serializador para creacion y visualizacion completa de ficha"""

    class Meta:
        model = FichaVehiculo
        fields = "__all__"


class FichaVehiculoSerializer(serializers.ModelSerializer):
    """Serializador para mostrar info de ficha en vehiculo"""

    class Meta:
        model = FichaVehiculo
        fields = [
            "titulo_principal",
            "descrip_principal",
            "img_principal",
            "titulo2",
            "descrip2",
            "img_2",
            "titulo3",
            "descrip3",
            "img_3",
        ]


class TipoVehiculoSerializer(serializers.ModelSerializer):
    """Serializador para manipular info de tipo de vehiculo"""

    class Meta:
        model = TipoVehiculo
        fields = "__all__"


class MarcaSerializer(serializers.ModelSerializer):
    """Serializador para manipular info de marca de vehiculo"""

    class Meta:
        model = Marca
        fields = "__all__"


class VehiculoDetailSerializer(serializers.ModelSerializer):
    """Serializador para mostrar info completa de un vehiculo"""

    ficha = FichaVehiculoSerializer(source="fichavehiculo", read_only=True)
    tipo = TipoVehiculoSerializer()
    marca = MarcaSerializer()

    class Meta:
        model = Vehiculo
        fields = fields = [
            "id",
            "nombre",
            "tipo",
            "marca",
            "anio",
            "precio",
            "imagen",
            "ficha",
        ]


class VehiculoCreateSerializer(serializers.ModelSerializer):
    """Serializador para crear un vehiculo"""

    class Meta:
        model = Vehiculo
        fields = "__all__"


class VehiculoDeleteUpdateSerializer(serializers.ModelSerializer):
    """Serializador para actualizar un vehiculo"""

    class Meta:
        model = Vehiculo
        fields = "__all__"
