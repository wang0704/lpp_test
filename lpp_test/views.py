from django.shortcuts import render

# Create your views here.
from common.mymako import render_mako_context


def hello(request):
    context = {'hello': 'Hello World!'}
    return render_mako_context(request, '/lpp_test/hello.html', context)