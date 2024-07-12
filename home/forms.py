from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'placeholder' : 'add task ','class':'form-control m-auto'}))

    class Meta:
        model = Task
        fields = '__all__'

