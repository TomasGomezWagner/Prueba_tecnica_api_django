from django.db import models


class TipoVehiculo(models.Model):
    """Modelo para entidad tipo de vehiculo"""

    descripcion = models.CharField(max_length=50)

    objects = models.Manager()

    def __str__(self) -> str:
        return str(self.descripcion)


class Marca(models.Model):
    """Modelo para entidad Marca"""

    descripcion = models.CharField(max_length=50)

    objects = models.Manager()

    def __str__(self) -> str:
        return str(self.descripcion)


class Vehiculo(models.Model):
    """Modelo para entidad Vehiculo"""

    nombre = models.CharField(max_length=50, null=True)
    tipo = models.ForeignKey(TipoVehiculo, null=True, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, null=True, on_delete=models.CASCADE)
    anio = models.IntegerField(null=True)
    precio = models.IntegerField(null=True)
    imagen = models.CharField(max_length=50, null=True)

    objects = models.Manager()

    def __str__(self) -> str:
        return str(self.nombre)


class FichaVehiculo(models.Model):
    """Modelo para entidad FichaVehiculo (vista particular de vehiculo)"""

    nombre = models.OneToOneField(
        Vehiculo, on_delete=models.CASCADE, null=False, blank=False
    )
    titulo_principal = models.CharField(max_length=50)
    descrip_principal = models.TextField(max_length=120)
    titulo2 = models.CharField(max_length=50)
    descrip2 = models.TextField(max_length=120)
    titulo3 = models.CharField(max_length=50)
    descrip3 = models.TextField(max_length=120)
    img_principal = models.CharField(max_length=50)
    img_2 = models.CharField(max_length=50)
    img_3 = models.CharField(max_length=50)

    objects = models.Manager()

    def __str__(self) -> str:
        return f"Ficha {self.nombre}"
