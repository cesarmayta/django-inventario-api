from django.db import models

# Create your models here.
class Almacen(models.Model):
    descripcion = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'tbl_almacen'
        
    def __str__(self):
        return self.descripcion
    
class Producto(models.Model):
    CATEGORIA_CHOICES = (
        (1,'FERRETERIA'),
        (2,'CONSTRUCCION')
    )
    codigo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    categoria = models.IntegerField(default=1,
                                 choices=CATEGORIA_CHOICES)
    
    class Meta:
        db_table = 'tbl_producto'
        
    def __str__(self):
        return self.descripcion
    
class Movimiento(models.Model):
    TIPOS_CHOICES = (
        (1,'INGRESO'),
        (2,'EGRESO')
    )
    
    almacen = models.ForeignKey(Almacen,on_delete=models.RESTRICT)
    producto = models.ForeignKey(Producto,on_delete=models.RESTRICT)
    tipo_movimiento = models.IntegerField(default=1,choices=TIPOS_CHOICES)
    cantidad = models.IntegerField(default=1)
    fecha = models.DateField(auto_now=True)
    saldo = models.IntegerField(null=True)
    
    class Meta:
        db_table = 'tbl_movimiento'
        
    def __str__(self):
        return almacen.descripcion + ' - ' + producto.descripcion
    
    