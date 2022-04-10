from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('markets/index.html')
    return HttpResponse(template.render({}, request))


def market(request, name):
    template = loader.get_template('markets/market.html')
    context = {'name': name}
    return HttpResponse(template.render(context, request))
