from django.forms import*

from core.models import CateQuimico, Grano, Parcelas, Quimico

class CateQuimicoForm(ModelForm):
    class Meta:
        model = CateQuimico
        fields = '__all__'
        labels = {
                
            }
        widgets = {
            'nombre': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Nombre de Categoria',
                        
                }
            )
        }

class QuimicoForm (ModelForm):
    class Meta:
        model = Quimico
        fields = '__all__'
        labels = {
                
            }
        widgets = {
            'nombre': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Nombre',
                        
                }
            ),
            'categoria': Select(
                attrs= {'class':'form-control',
                        'placeholder':'Categoria',
                        
                }
            ),
            'ingrediente': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Ingrediente',
                        
                }
            ),
            'cantidad': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Cantidad',
                        
                }
            ),
            'unidades': Select(
                attrs= {'class':'form-control',
                        'placeholder':'Unidades de medida',
                        
                }
            )
            
        }

class GranoForm (ModelForm):
    class Meta:
        model = Grano
        fields = '__all__'
        labels = {
                
                
            }
        widgets = {
            'nombre': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Nombre',
                        
                }
            ),
            'variedad': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Variedad',
                        
                }
            ),
            'kilogramos': NumberInput(
                attrs= {'class':'form-control',
                        'placeholder':'Cantidad de Kilogramos',
                        
                }
            ),
            'precio': NumberInput(
                attrs= {'class':'form-control',
                        'placeholder':'Precio de compra',
                        
                }
            ),
            'procedencia': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Procedencia',
                        
                }
            ),
            
        }

class ParcelaForm (ModelForm):
    class Meta:
        model = Parcelas
        fields = '__all__'
        labels = {
                
            }
        widgets = {
            'nombre': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Nombre',
                        
                }
            ),
            'ubicacion': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Ubicacion',
                        
                }
            ),
            'hectareas': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Ingrediente',
                        
                }
            ),
            'trabajos': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Cantidad',
                        
                }
            ),
            'gasto': NumberInput(
                attrs= {'class':'form-control',
                        'placeholder':'Unidades de medida',
                        
                }
            )
            
        }









