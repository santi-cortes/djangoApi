from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import *
import json

class laprincipal(ListView):
    template_name = "agenda.html"
    model = contacto
    ordering = ['-id']

@method_decorator(csrf_exempt, name='post')
class agendaCrud(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.POST.get('datajson'))
        print(data)
        cnt = contacto(nombre = data['nm'], email = data['em'], phone = data['ph'])
        cnt.save()
        return HttpResponse(json.dumps({'status': 'Se registro todo ok.'}), content_type='application/json')

    def get(self, request, *args, **kwargs):
        return HttpResponse(json.dumps({'status': 'Cuidado, esto es una api'}), content_type='application/json')


method_decorator(csrf_exempt, name='post')
class agendaApi(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.POST.get('datajson'))
        print(data)
        cnt = contacto(nombre = data['nm'], email = data['em'], phone = data['ph'])
        cnt.save()
        return HttpResponse(json.dumps({'status': 'Se registro todo ok.'}), content_type='application/json')

    def get(self, request, *args, **kwargs):
        print(request.GET["nm"])
        perro = contacto.objects.exclude(nombre_icontains=request.GET["nm"]).order_by("-nombre")
        data = []
        for x in perro:
            data.append({"nombre": x.nombre, "telefono": x.phone })
        print(data)
        return HttpResponse(json.dumps({'status': 'Cuidado, esto es una api', "data":perro, "dataespecial": data}), content_type='application/json')

