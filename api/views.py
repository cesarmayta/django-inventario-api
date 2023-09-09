from rest_framework import viewsets

from .models import (
    Almacen,
    Producto,
    Movimiento
)

from .serializers import (
    AlmacenSerializer,
    ProductoSerializer,
    MovimientoSerializer
)

class AlmacenViewset(viewsets.ModelViewSet):
    queryset = Almacen.objects.all()
    serializer_class = AlmacenSerializer
    
class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
class MovimientoViewset(viewsets.ModelViewSet):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer