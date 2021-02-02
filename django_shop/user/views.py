from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import RegisterForm, LoginForm
from .models import User
from django.contrib.auth.hashers import make_password
# Create your views here.


def index(request):
    user = request.session.get('user')
    if user:
        return redirect('/product')
    else:
        return render(request, 'index.html', {'email': request.session.get('user')})


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/login/'

    def form_valid(self, form):
        user = User(
            email=form.data.get('email'),
            password=make_password(form.data.get('password')),
            level='user'
        )
        user.save()

        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/product'

    def form_valid(self, form):
        self.request.session['user'] = form.data.get('email')

        return super().form_valid(form)


def logout(request):
    if 'user' in request.session:
        del(request.session['user'])
    return redirect('/')
