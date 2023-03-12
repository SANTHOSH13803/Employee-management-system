from django import forms
from . models import Employee
# from django.core.exceptions import ValidationError
# from django.utils.translation import gettext_lazy as _

import datetime

todaysdate = datetime.date.today()

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields= '__all__'
    
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['designation'].empty_label='Select'
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    
    name = forms.CharField(max_length=50,widget=forms.TextInput(
        attrs={'placeholder':'Enter your name'}
    ))
    address = forms.CharField(max_length=200,widget=forms.TextInput(
        attrs={'placeholder':'Enter your address'}
    ))
    city = forms.CharField(max_length=50,widget=forms.TextInput(
        attrs={'placeholder':'Enter your city'}
    ))
    country = forms.CharField(max_length=50,widget=forms.TextInput(
        attrs={'placeholder':'Enter your country'}
    ))
    zipcode = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder':'Enter your zipcode','type':'number','min':'100000','max':'999999'}))
    designation = forms.Select()
    state = forms.CharField(max_length=50,widget=forms.TextInput(
        attrs={'placeholder':'Enter your State'}
    ))

    #date validation 
    date_of_joining = forms.DateField(required=True,widget=forms.DateInput(
        attrs={'type':'date','max':todaysdate}
    ))
    date_of_birth = forms.DateField( required=True,widget=forms.DateInput(
        attrs={'type':'date','max':todaysdate}
    ))
    active_field = forms.BooleanField(required=False)
    on_leave = forms.BooleanField(required=False,initial=False)
    leave_count = forms.IntegerField(required=False, widget=forms.TextInput(
        attrs={'readonly':"True",'value':0}))
