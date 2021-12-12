from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, View
# Models
from apps.products.models import Mark, Category, UMedida, Product, SubCategory
# Forms
from apps.products.forms import MarkForm, CategoryForm, UMedidaForm, ProductForm, SubCategoryForm
# Mixins
from apps.core.views import FormInvalid, BaseListView


class CategoryListView(BaseListView):
    model = Category
    template_name = "products/category-list.html"   
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Categorias"
        context["add_new_url"] = reverse_lazy("products:category-add")
        context["add_new"] = "Nueva Categoria"
        return context


class CategoryCreateView(FormInvalid, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "bases/form-base.html"
    success_url = reverse_lazy("products:categorys")
    success_message = "Categoria creada exitosamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Nueva Categoria"
        context["list_url"] = self.success_url
        return context


class CategoryUpdateView(FormInvalid, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "bases/form-base.html"
    success_url = reverse_lazy("products:categorys")
    success_message = "Categoria actualizada"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Actualizacion de Categoria"
        context["list_url"] = self.success_url
        return context


class SubCategoryListView(BaseListView):
    model = SubCategory
    template_name = "products/subcategory-list.html"
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "SubCategorias"
        context["add_new_url"] = reverse_lazy("products:subcategory-add")
        context["add_new"] = "Nueva SubCategoria"
        return context


class SubCategoryCreateView(FormInvalid, CreateView):
    model = SubCategory
    form_class = SubCategoryForm
    template_name = "bases/form-base.html"
    success_url = reverse_lazy("products:subcategorys")
    success_message = "SubCategoria creada exitosamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Nueva SubCategoria"
        context["list_url"] = self.success_url
        return context


class SubCategoryUpdateView(FormInvalid, UpdateView):
    model = SubCategory
    form_class = SubCategoryForm
    template_name = "bases/form-base.html"
    success_url = reverse_lazy("products:subcategorys")
    success_message = "SubCategoria actualizada"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Actualizacion de SubCategoria"
        context["list_url"] = self.success_url
        return context


class MarkListView(BaseListView):
    model = Mark
    template_name = "products/mark-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Marcas"
        context["add_new_url"] = reverse_lazy('products:mark-add')
        context["add_new"] = "Nueva Marca"
        return context  


class MarkCreateView(FormInvalid, CreateView):
    model = Mark
    form_class = MarkForm
    template_name = "bases/form-base.html"
    success_url = reverse_lazy("products:marks")
    success_message = "Marca creada exitosamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Nueva Marca"
        context["list_url"] = self.success_url
        return context


class MarkUpdateView(FormInvalid, UpdateView):
    model = Mark
    form_class = MarkForm
    template_name = "bases/form-base.html"
    success_url = reverse_lazy("products:marks")
    success_message = "Marca actualizada"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Actualizacion de Marca"
        context["list_url"] = self.success_url
        return context


class UMedidaListView(BaseListView):
    model = UMedida
    template_name = "products/umedida-list.html"
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Unid. de Medida"
        context["add_new_url"] = reverse_lazy('products:umedida-add')
        context["add_new"] = "Nueva Unidad de Medida"
        return context


class UMedidaCreateView(FormInvalid, CreateView):
    model = UMedida
    form_class = UMedidaForm
    template_name = "bases/form-base.html"
    success_url = reverse_lazy("products:umedidas")
    success_message = "Unidad de Medida creada exitosamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Nueva Unidad de Medida"
        context["list_url"] = self.success_url
        return context


class UMedidaUpdateView(FormInvalid, UpdateView):
    model = UMedida
    form_class = UMedidaForm
    template_name = "bases/form-base.html"
    success_url = reverse_lazy("products:umedidas")
    success_message = "Unidad de Medida actualizada"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Actualizacion de Unidad de Medida"
        context["list_url"] = self.success_url
        return context


class ProductListView(BaseListView):
    model = Product
    template_name = "products/product-list.html"
    
    def get_queryset(self):
        res = Product.objects.select_related("mark","subcategory","umedida").all()
        return res
    
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Productos"
        context["add_new_url"] = reverse_lazy('products:product-add')
        context["add_new"] = "Nuevo Producto"
        return context


class ProductCreateView(FormInvalid, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "bases/form-base.html"
    success_url = reverse_lazy("products:products")
    success_message = "Producto creado exitosamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Nuevo Producto"
        context["list_url"] = self.success_url
        return context


class ProductUpdateView(FormInvalid, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "bases/form-base.html"
    success_url = reverse_lazy("products:products")
    success_message = "Producto actualizado"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Actualizacion de Producto"
        context["list_url"] = self.success_url
        return context

   
class ActiveView(View):

    def get(self, request, *args, **kwargs):
        slug =self.kwargs['slug']
        model = self.kwargs['model']
        if model == 'category':
            obj = get_object_or_404(Category, slug=slug)
            msg = "Categoria"
        if model == 'subcategory':
            obj = get_object_or_404(SubCategory, slug=slug)
            msg = "SubCategoria"
        if model == 'mark':
            obj = get_object_or_404(Mark, slug=slug)
            msg = "Marca"
        if model == 'umedida':
            obj = get_object_or_404(UMedida, slug=slug)
            msg = "Unidad de Medida"
        if model == 'product':
            obj = get_object_or_404(Product, slug=slug)
            msg = "Producto"
        # Inactivacion
        if obj.active:
            obj.active = False
            messages.info(request, f"{msg} inactivada(o)")
        else:
            obj.active = True
            messages.success(request, f"{msg} activada(o)")
        obj.save()
        # Pagina anterior
        # request.META.get('HTTP_REFERER')

        return redirect(request.META.get('HTTP_REFERER'))
