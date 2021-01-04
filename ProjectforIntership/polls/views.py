from django.shortcuts import render, redirect
from .models import Ad
from .forms import AdForm
from django.views.generic import DetailView, UpdateView, DeleteView


def klo(request):
    return render(request, 'polls/home.html')


class AdDetailView(DetailView):
    model = Ad
    template_name = 'polls/details_ad.html'
    context_object_name = 'detail_ad'


class AdUpdateView(UpdateView):
    model = Ad
    template_name = 'polls/create.html'

    form_class = AdForm


class AdDeleteView(DeleteView):
    model = Ad
    success_url = '/offers'
    template_name = 'polls/ad-delete.html'


def offers(request):
    ad = Ad.objects.order_by('-date')
    return render(request, 'polls/offersklo.html', {'ad': ad})


def about(request):
    return render(request, 'polls/aboutklo.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('offers')
        else:
            error = 'Error: The form has been filled out incorrectly'

    form = AdForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'polls/create.html', data)











