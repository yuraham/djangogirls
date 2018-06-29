from django.http import HttpResponse
from django.http import Http404




def home(request):
    return HttpResponse("방문을 환영합니다.")


def url_error(request):
    raise Http404("요청이 잘 못 되었습니다.")