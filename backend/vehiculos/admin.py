from django.contrib import admin
from .models import Vehiculo, TipoVehiculo, FichaVehiculo, Marca

admin.site.register(TipoVehiculo)
admin.site.register(FichaVehiculo)
admin.site.register(Marca)

class FichaInLine(admin.StackedInline):
    model = FichaVehiculo
    can_delete = False
    verbose_name = 'Fichas'

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    inlines = [FichaInLine]