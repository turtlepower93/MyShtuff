from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ShtuffList, Shtuff
from django.urls import reverse, reverse_lazy


# Create your views here.


def home(request):
    return render(request, 'home.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class ShtuffListList(LoginRequiredMixin, ListView):
    model = ShtuffList
    
    def get_queryset(self):
        queryset1 = super(ShtuffListList, self).get_queryset()
        queryset2 = queryset1.filter(user=self.request.user)
        return queryset2

class ShtuffListCreate(LoginRequiredMixin, CreateView):
    model = ShtuffList
    fields = ['name','description','image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ShtuffListDelete(LoginRequiredMixin, DeleteView):
    model = ShtuffList
    success_url = '/shtuff_lists/'

class ShtuffListUpdate(LoginRequiredMixin, UpdateView):
    model = ShtuffList
    fields = ['description','image']

@login_required
def shtuff_list_detail(request, shtuff_list_id):
    shtuff_list = ShtuffList.objects.get(id = shtuff_list_id)
    shtuffs = Shtuff.objects.filter(shtuff_list=shtuff_list_id)
    return render(request, 'shtuff_lists/shtuff_lists_detail.html', {
        'shtuff_list' : shtuff_list,
        'shtuffs' : shtuffs
    })

class ShtuffCreate(LoginRequiredMixin,CreateView):
    model = Shtuff
    fields = ['name','description', 'price', 'image', 'url']

    def form_valid(self, form):
        new_shtuff = form.save(commit = False)
        new_shtuff.shtuff_list = ShtuffList.objects.get(id=self.kwargs['pk'])
        new_shtuff.save()
        return super().form_valid(form)

class ShtuffDelete(LoginRequiredMixin,DeleteView):
    model = Shtuff

    def get_success_url(self):
        return reverse('shtuff_list_detail', kwargs={'shtuff_list_id': self.object.shtuff_list.id})

class ShtuffUpdate(LoginRequiredMixin,UpdateView):
    model = Shtuff
    fields = ['description', 'price', 'image', 'url']

@login_required
def shtuff_detail(request, shtuff_id):
    shtuff = Shtuff.objects.get(id = shtuff_id)
    return render(request, 'shtuff/shtuff_detail.html', {
        'shtuff' : shtuff,
    })

@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})
