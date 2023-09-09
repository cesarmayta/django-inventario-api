from rest_framework.routers import DefaultRouter
from django.urls import path

from . import views

router = DefaultRouter()

router.register(r'almacen',views.AlmacenViewset,basename='almacen')
router.register(r'producto',views.ProductoViewset,basename='producto')
router.register(r'movimiento',views.MovimientoViewset,basename='movimiento')

urlpatterns = router.urls
