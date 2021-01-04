from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ShtuffList, Shtuff


# Create your views here.


def home(request):
    return render(request, 'home.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class ShtuffListList(LoginRequiredMixin, ListView):
    model = ShtuffList

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

def shtuff_list_detail(request, shtuff_list_id):
    shtuff_list = ShtuffList.objects.get(id = shtuff_list_id)
    return render(request, 'shtuff_lists/shtuff_lists_detail.html', {
        'shtuff_list' : shtuff_list,
    })

class ShtuffCreate(CreateView):
    model = Shtuff
    fields = ['name','description', 'price', 'image', 'url']

    def form_valid(self, form):
        print('YOLOSWAG')
        print(self.kwargs['pk'])
        new_shtuff = form.save(commit = False)
        new_shtuff.shtuff_list = ShtuffList.objects.get(id=self.kwargs['pk'])
        new_shtuff.save()
        return super().form_valid(form)

class ShtuffDelete(LoginRequiredMixin,DeleteView):
    model = Shtuff
    success_url = '/shtuff_lists_detail/'

class ShtuffUpdate(LoginRequiredMixin,UpdateView):
    model = Shtuff
    fields = ['description', 'price', 'image', 'url']