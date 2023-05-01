from django import forms


class CreateDocForm(forms.Form):
    user_name = forms.CharField(label='Имя пользователя', widget=forms.TextInput())
    user_password = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    space_name = forms.CharField(label='Пространство', widget=forms.TextInput())
    doc_title = forms.CharField(label='Название', widget=forms.TextInput())
    doc_text = forms.CharField(
        label='Текст',
        max_length=2000,
        widget=forms.Textarea()
    )
    
    def clean(self):
        cleaned_data = super(CreateDocForm, self).clean()
        user_name = cleaned_data.get('user_name')
        user_password = cleaned_data.get('user_password')
        space_name = cleaned_data.get('space_name')
        doc_title = cleaned_data.get('doc_title')
        doc_text = cleaned_data.get('doc_text')
        if not user_name and not user_password and not space_name and not doc_title and not doc_text:
            raise forms.ValidationError('Некоторые поля не заполнены!')
