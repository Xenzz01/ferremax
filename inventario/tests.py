from django.test import TestCase
from django.urls import reverse
from .models import Producto

class ProductoModelTest(TestCase):
    def setUp(self):
        self.producto = Producto.objects.create(
            nombre="Martillo",
            categoria="Herramientas",
            descripcion="Martillo de madera",
            precio=1200.0,
            stock=15
        )

    def test_str_representation(self):
        self.assertEqual(str(self.producto), "Martillo")


class ProductoViewsTest(TestCase):
    def setUp(self):
        self.producto = Producto.objects.create(
            nombre="Destornillador",
            categoria="Herramientas",
            descripcion="Destornillador Phillips",
            precio=300.0,
            stock=30
        )

    def test_list_view(self):
        response = self.client.get(reverse('producto_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventario/producto_list.html')
        self.assertContains(response, self.producto.nombre)

    def test_create_view(self):
        data = {
            'nombre': 'Llave inglesa',
            'categoria': 'Herramientas',
            'descripcion': 'Llave ajustable',
            'precio': '450.0',
            'stock': '10'
        }
        response = self.client.post(reverse('producto_create'), data)
        # Tras crear, debe redirigir al listado
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Producto.objects.filter(nombre='Llave inglesa').exists())

    def test_update_view(self):
        url = reverse('producto_update', args=[self.producto.pk])
        data = {
            'nombre': 'Destornillador Actualizado',
            'categoria': 'Herramientas',
            'descripcion': 'Destornillador plano',
            'precio': '350.0',
            'stock': '25'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.producto.refresh_from_db()
        self.assertEqual(self.producto.nombre, 'Destornillador Actualizado')

    def test_delete_view(self):
        url = reverse('producto_delete', args=[self.producto.pk])
        response = self.client.post(url)
        # Tras eliminar, debe redirigir al listado
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Producto.objects.filter(pk=self.producto.pk).exists())