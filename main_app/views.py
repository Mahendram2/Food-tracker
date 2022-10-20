from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.db.models import Sum
from .models import Food

# Create your views here.
def home(request):
  return render(request,'home.html')

def about(request):
  return render(request, 'about.html')

def api(request):
  import json
  import requests
  if request.method == 'POST':
        query = request.POST['query']
        api_request = requests.get('https://api.api-ninjas.com/v1/nutrition?query=' + query, headers={'X-Api-Key': 'PNH8MnUSvxfXfIl2BJ9czQ==KxF5yVwD8rPHe16v'})
        api = json.loads(api_request.content)
        return render(request, 'api.html', {'api': api})
  else:
        return render(request, 'api.html', {'query': 'Enter a valid query'})

@login_required
def foods_index(request):
  foods=Food.objects.filter(user=request.user)
  data = Food.objects.filter(user=request.user).aggregate(
    Sum('calories'), 
    Sum('protein'), 
    Sum('carbohydrates'), 
    Sum('fat'), 
    Sum('fiber'))
  return render(request, 'foods/index.html', {'foods':foods, 'data':data})

@login_required
def foods_detail(request, food_id):
  food=Food.objects.get(id=food_id)
  return render(request, 'foods/detail.html', {'food':food})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('foods_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


class FoodsCreate(LoginRequiredMixin, CreateView):
  model = Food
  fields=('name', 'calories','carbohydrates', 'protein', 'fat' , 'fiber')
  success_url = '/foods/'

  def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class FoodsUpdate(LoginRequiredMixin, UpdateView):
  model = Food
  fields = ('name', 'calories','carbohydrates', 'protein', 'fat' , 'fiber')
  success_url = '/foods/'


class FoodsDelete(LoginRequiredMixin, DeleteView):
  model = Food
  success_url = '/foods/'