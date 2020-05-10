
from django.views.decorators.csrf import csrf_exempt

import json

from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

from .models import TheCat

@csrf_exempt
def api_view(request):
    if request.method == 'GET':
        cat_name = request.GET['name']
        existing_cats = TheCat.objects.filter(name=cat_name).values()
        resp = json.dumps(list(existing_cats), cls=DjangoJSONEncoder)
        return JsonResponse(resp, safe=False)
    elif request.method == 'POST':
        params = request.read()
        params = json.loads(params)
        new_cat = TheCat(**params)
        new_cat.save()
        return JsonResponse({'mess': 'New cat was created!'})
    elif request.method == 'PUT':
        params = request.read()
        params = json.loads(params)
        existing_cat = TheCat.objects.get(id=params['cat_id'])
        existing_cat.name = params['name']
        existing_cat.save()
        return JsonResponse({'mess': 'The cat was changed!'})
    elif request.method == 'DELETE':
        params = request.read()
        params = json.loads(params)
        existing_cats = TheCat.objects.get(id=params['cat_id'])
        existing_cats.delete()
        return JsonResponse({'mess': 'The cat was deleted!'})

    return JsonResponse({})

from django.views import View
from django.http import HttpResponse

class OtherTestView(View):
    def get(self, request):
        return HttpResponse('Hello world!')


class MyView(View):
    def get(self, request):
        cat_name = request.GET['name']
        existing_cats = TheCat.objects.filter(name=cat_name).values()
        resp = json.dumps(list(existing_cats), cls=DjangoJSONEncoder)
        return JsonResponse(resp, safe=False)

    def post(self, request):
        params = request.read()
        params = json.loads(params)
        new_cat = TheCat(**params)
        new_cat.save()
        return JsonResponse({'mess': 'New cat was created!'})

    def put(self, request):
        params = request.read()
        params = json.loads(params)
        existing_cat = TheCat.objects.get(id=params['cat_id'])
        existing_cat.name = params['name']
        existing_cat.save()
        return JsonResponse({'mess': 'The cat was changed!'})

    def delete(self, request):
        params = request.read()
        params = json.loads(params)
        existing_cats = TheCat.objects.get(id=params['cat_id'])
        existing_cats.delete()
        return JsonResponse({'mess': 'The cat was deleted!'})


from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

class TCatView(TemplateView):
    template_name = "cat.html"

    def get_context_data(self, **kwargs):
        context = super(TCatView, self).get_context_data(**kwargs)
        context['some_cats'] = TheCat.objects.all()
        return context

from django.shortcuts import render

@csrf_exempt
def template_cat(request):
    context = {}
    context['object_list'] = TheCat.objects.all()
    return render(request, 'list_cat.html', context=context)

from django.shortcuts import get_object_or_404
from distutils.util import strtobool
class LCatView(ListView):
    model = TheCat

    def get_queryset(self):
        #if self.args[0] == 'fluffy':
        #    fluffy = True
        #else:
        #    fluffy = False
        #fluffy = bool(strtobool(self.args[0]))
        #self.fluffy = get_object_or_404(TheCat, fluffy=fluffy)
        return TheCat.objects.filter(fluffy=True)

class DetailCatView(DetailView):
    model = TheCat

    queryset = TheCat.objects.all()
