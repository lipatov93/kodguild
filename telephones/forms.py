from .models import Telephones
from django.forms import ModelForm

class TelephonesForm(ModelForm):
    class Meta:
        model = Telephones
        fields = ['name','tel_namber','who_insures_name','who_insures_tel_namber' ]
