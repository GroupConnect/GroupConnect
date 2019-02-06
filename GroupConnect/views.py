from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Signboard
from . import forms

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'GroupConnect/index.html'

class SignboardView(generic.DetailView):
    model = Signboard
    template_name = 'GroupConnect/signboard_detail.html'

def SignboardPage(request, pk):
    signboard = get_object_or_404(Signboard, pk=pk)
    
    for query in Signboard.objects.filter(pk=pk).prefetch_related('post_set'):
        post_list = query.post_set.all()

    form = forms.PostCreateForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return render(request, 'GroupConnect/boad.html', context= {
            'signboard': signboard,
            'post_list' : post_list,
            'form': form
        })
    
    else:
        return render(request, 'GroupConnect/bord.html', context= {
            'signboard': signboard,
            'post_list' : post_list,
            'form': form
        })
class MypageView(generic.TemplateView):
    template_name = 'GroupConnect/mypage.html'

class GrouptopView(generic.TemplateView):
    template_name = 'GroupConnect/grouptop.html'

class BordView(generic.TemplateView):
    template_name = 'GroupConnect/bord.html'
