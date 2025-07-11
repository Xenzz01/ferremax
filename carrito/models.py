from django.db import models
from inventario.models import Producto

class Boleta(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    usuario_id_unico = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f"Boleta {self.codigo} - {self.usuario_id_unico}"

class DetalleBoleta(models.Model):
    boleta = models.ForeignKey(
        Boleta,
        related_name='detalles',
        on_delete=models.CASCADE
    )
    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT
    )
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=0)

    def subtotal(self):
        return self.precio * self.cantidad

    def __str__(self):
        return f"{self.producto.nombre} x{self.cantidad}"

class Carrito(models.Model):
    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE
    )
    cantidad = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.producto.precio * self.cantidad

    def __str__(self):
        return f"{self.producto.nombre} (x{self.cantidad})"
