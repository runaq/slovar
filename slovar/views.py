from django.shortcuts import render
from .models import Words
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def index(request):
     return render(request, 'slovar/rus_slov.html', {})
def rus_slov(request):
    
    words = Words.objects.all().order_by('?')
    paginator = Paginator(words, 1)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
    return render(request,'slovar/rus_slov.html',
                  
                  {'page_obj': page_obj})
    


def slov_rus(request):
    return render(request, 'slovar/slov_rus.html', {})
