from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'inventario/producto_list.html', {'object_list': productos})

def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_list')        # <-- aquí rediriges
    else:
        form = ProductoForm()
    return render(request, 'inventario/producto_form.html', {'form': form})

def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list')        # <-- y aquí también
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'inventario/producto_form.html', {
        'form': form,
        'object': producto
    })

def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('producto_list')
    return render(request, 'inventario/producto_confirm_delete.html', {'object': producto})
