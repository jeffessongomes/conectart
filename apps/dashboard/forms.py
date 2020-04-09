from django import forms
from .models import Events, Subscribe_User, Admin, Photos, Our

class EventForm(forms.ModelForm):
    class Meta:
        model = Events 
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class']='form-control'


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe_User 
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SubscribeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class']='form-control'


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PhotoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class']='form-control'

class OurForm(forms.ModelForm):
    class Meta:
        model = Our 
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OurForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class']='form-control'