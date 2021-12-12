from django import forms
# Models
from apps.products.models import Mark, Category, SubCategory, UMedida, Product


class CategoryForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
            }
        )
    )
    
    class Meta:
        model = Category
        fields = "__all__"


class SubCategoryForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
            }
        )
    )
    category = forms.ModelChoiceField(
        queryset = Category.other_objects.show_actives(),
        label = "Categoria"
    )
    
    class Meta:
        model = SubCategory
        fields = "__all__"


class MarkForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
            }
        )
    )
    class Meta:
        model = Mark
        fields = "__all__"


class UMedidaForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
            }
        )
    )
    class Meta:
        model = UMedida
        fields = "__all__"


class ProductForm(forms.ModelForm):
    mark = forms.ModelChoiceField(
        queryset = Mark.other_objects.show_actives(),
        label = "Marca"
    )
    subcategory = forms.ModelChoiceField(
        queryset = SubCategory.other_objects.show_actives(),
        label = "SubCategoria"
    )
    umedida = forms.ModelChoiceField(
        queryset = UMedida.other_objects.show_actives(),
        label = "Unidad de Medida"
    )
    description = forms.CharField(
        label="Descripcion",
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
            }
        )
    )
    
    class Meta:
        model = Product
        fields = "__all__"

    