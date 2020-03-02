from django.shortcuts import render
from .forms import MaterialDeliveryForm
# Create your views here.

def material_delivery_create_view(request):
    form = MaterialDeliveryForm(request.POST or None)

    if form.is_valid():
        form.save()

    context = {
        'form':form
    }

    return render (request, "materials/delivery_create.html", context)
