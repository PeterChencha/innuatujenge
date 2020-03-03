from django.shortcuts import render
from .forms import MaterialDeliveryForm
from django.utils import timezone
from django.views.generic.list import ListView
from .models import Materials

def material_delivery_create_view(request):
    form = MaterialDeliveryForm(request.POST or None)

    if form.is_valid():
        form.save()

    context = {
        'form':form
    }

    return render (request, "materials/delivery_create.html", context)


class MaterialDeliveredListView(ListView):

    model = Materials
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def get_queryset(self):
        return Materials.objects.all().order_by('-created_at')
