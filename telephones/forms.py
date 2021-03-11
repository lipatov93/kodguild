from .models import Telephones
from django.forms import ModelForm, TextInput

class TelephonesForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = False


    class Meta:
        model = Telephones
        fields = ['name','tel_namber','who_insures_name','who_insures_tel_namber' ]
        required = ('who_insures_name','who_insures_tel_namber')

        widgets = {
            "name":TextInput(attrs={
                'class' : 'form-control input-default',
                'placeholder' : "Ник"

            }),
            "tel_namber":TextInput(attrs={
                'class' : 'form-control input-default',
                'placeholder' : "Телефон"

            }),
            "who_insures_name":TextInput(attrs={
                'class' : 'form-control input-default',
                'placeholder' : "Ник"

            }),
            "who_insures_tel_namber":TextInput(attrs={
                'class' : 'form-control input-default',
                'placeholder' : "Телефон"

            }),

        }
