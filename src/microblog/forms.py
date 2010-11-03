from django.forms.models import ModelForm
from microblog.models import Microblog

class MicroblogForm(ModelForm):
    class Meta:
        model = Microblog
