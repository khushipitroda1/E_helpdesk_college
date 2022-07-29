from django import forms
from django.db.models import fields
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column

class Signupform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password','joindate','enddate']



class ComplainForm(forms.ModelForm):
    class Meta:
        model = Complain
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        # self.fields['std_id'].widget.attrs['hidden'] = True
        self.fields['std_id'].required = False
        
        self.helper.layout = Layout(
            Row(Column('type', css_class='form-group col-md-12')),
            Row(Column('date', css_class='form-group col-md-12')),
            Row(Column('message', css_class='form-group col-md-12')),
            Row(Column('img', css_class='form-group col-md-12')),
        )

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.fields['std_id'].widget.attrs['disabled'] = True
        self.fields['std_id'].required = False
        self.helper.layout = Layout(
        )

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
        )
