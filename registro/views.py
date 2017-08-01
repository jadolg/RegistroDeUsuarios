from django.http.response import HttpResponseRedirect

# Create your views here.

def redirect_to_list(request):
    return HttpResponseRedirect('/admin/registro/usuario/')