from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=150, label="Nom et prénom ", widget=forms.TextInput(attrs={'Placeholder': 'Votre nom et prénom'}))
    email = forms.EmailField(label="Votre email ", widget=forms.TextInput(attrs={'Placeholder': 'Votre email'}))
    subject = forms.CharField(max_length=500, label="Sujet de votre mail ", widget=forms.TextInput(attrs={'Placeholder': 'Votre sujet'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'Placeholder': 'Votre message...'}), label="Votre message ")