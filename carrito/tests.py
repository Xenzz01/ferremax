# carrito/tests.py
from django.test import TestCase
from django.urls import reverse
from inventario.models import Producto
from .models import Carrito            # <-- modelo correcto

class CarritoTestCase(TestCase):
    def setUp(self):
        # Crear un producto de prueba
        self.producto = Producto.objects.create(
            nombre="Clavo",
            categoria="Ferretería",
            descripcion="Clavo de 2 pulgadas",
            precio=50.0,
            stock=20
        )

    def test_agregar_al_carrito(self):
        response = self.client.get(
            reverse('agregar_al_carrito', args=[self.producto.id]),
            follow=True
        )
        self.assertRedirects(response, reverse('lista_productos'))
        items = Carrito.objects.filter(producto=self.producto)
        self.assertEqual(items.count(), 1)

    def test_ver_carrito_vacio(self):
        response = self.client.get(reverse('ver_carrito'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Tu carrito está vacío')

    def test_eliminar_del_carrito(self):
        # Añade un ítem primero
        self.client.get(reverse('agregar_al_carrito', args=[self.producto.id]))
        item = Carrito.objects.get(producto=self.producto)
        # Ahora elimínalo
        response = self.client.post(
            reverse('eliminar_del_carrito', args=[item.id]),
            {'cantidad': 1},
            follow=True
        )
        self.assertRedirects(response, reverse('ver_carrito'))
        self.assertFalse(Carrito.objects.filter(id=item.id).exists())
