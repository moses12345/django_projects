from django.forms import ModelForm
from .models import Poll

class Createforms(ModelForm):
    class Meta:
        model=Poll
        fields=['question','option1','option2','option3']

        