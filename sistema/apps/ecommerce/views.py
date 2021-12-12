from django.views.generic import TemplateView
# MOdels
from apps.products.models import Mark, Product
# Utils Carts
from apps.carts.utils import get_or_create_cart


class EcommerceView(TemplateView):
    template_name = "ecommerce/base.html"

    def get_cart(self, request):
        cart = get_or_create_cart(request)
        return cart    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart"] = self.get_cart(self.request)
        context["marks"] = Mark.objects.all()
        context['best'] = Product.objects.select_related("mark","subcategory","umedida").first()
        # context["products"] = Product.objects.filter(active=True).order_by('-id')
        context["products"] = Product.other_objects.show_actives()[:8]
        context["products_featured"] = Product.other_objects.show_actives()[:6]
        context["products_onsale"] = Product.objects.select_related("mark","subcategory","umedida").order_by("-id")[:6]
        context["products_toprated"] = Product.objects.select_related("mark","subcategory","umedida").order_by("-updated")[:6]
        context['range'] = range(3)

        return context
    