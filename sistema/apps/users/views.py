from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import RedirectView
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.urls import reverse_lazy
# Forms
from .forms import LoginForm, UserRegisterForm, UpdatePasswordForm
# Models
from .models import User


class LoginView(FormView):
    template_name = 'home/login.html'
    form_class = LoginForm
    success_url = "/"
    
    def get_initial(self):
        # Funcion para iniciar valores
        initial = super().get_initial()
        initial['next'] = self.request.GET.get('next')
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Login"
        context["bg_body"] = "bg-gradient-primary"
        return context
        
    def dispatch(self, request, *args, **kwargs):
        # Validamos si el usuario ya esta logeado
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        # Añadimos una clase para las validaciones
        for field in form.errors:
            if field != "__all__":
                form[field].field.widget.attrs['class'] = 'is-invalid'
    
        return super().form_invalid(form, *args, **kwargs)

    def form_valid(self, form):
        # Autenticacion de credenciales de acceso
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        # messages.success(self.request, f"Bienvenido {user} ({user.email})")
        messages.success(self.request, f"Bienvenido {user.email}")

        # Redireccionamiento 
        next=form.cleaned_data['next']
        if (next!=''):
            return redirect(next)

        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    url = reverse_lazy('users:login')

    def get(self, request, *args, **kwargs):
        # Validacion de usuario logeado
        if request.user.id != None:
            messages.success(self.request, "Sesion cerrada exitosamente")
            logout(request)
                
        # Validacion de redireccionamiento
        if request.GET.get('next'):
            self.url = '{}?next={}'.format(self.url, request.GET.get('next'))

        return super(LogoutView, self).get(request, *args, **kwargs)


class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        # Udo de datos validados desde el formulario
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['name'],
            form.cleaned_data['last_name'],
            form.cleaned_data['password1']
        )
        # Message de confirmacion
        # messages.success(self.request, "Usuario creado exitosamente")
        return super(UserRegisterView, self).form_valid(form)


class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = 'users/update.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('users:login')

    def get_initial(self):
        # Iniciamos con un valor el email (hidden)
        initial = super().get_initial()

        initial['email'] = self.request.user.email

        return initial
    

    def form_valid(self, form):
        # Enviamos datos al formulario
        usuario = self.request.user
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password1']
        )

        # Validamos las credenciales
        if user:
            # Realizamos el cambio de la contraseña
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()
            # Message
        # Cerramos sesion
        logout(self.request)
        return super(UpdatePasswordView, self).form_valid(form)

