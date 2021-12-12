from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView


# class FormInvalid(LoginRequiredMixin):
class FormInvalid(SuccessMessageMixin, LoginRequiredMixin):
    # Mixin que añade una clase CSS y Login
    def form_invalid(self, form, *args, **kwargs):
        # Añadimos una clase para las validaciones
        for field in form.errors:
            if field != "__all__":                
                form[field].field.widget.attrs['class'] = 'is-invalid'

        return super().form_invalid(form, *args, **kwargs)


class BaseListView(LoginRequiredMixin, ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["full"] = "toggled"
        return context
