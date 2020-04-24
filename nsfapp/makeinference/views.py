from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
import pandas, numpy, gensim


from .forms import TextForm

def home(request):
    
    return render(request, 'home.html', {'boards': 'text'})

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        form = TextForm
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = TextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text_input']

        args = {'form':form, 'text':text}

        return render(request, self.template_name, args)




