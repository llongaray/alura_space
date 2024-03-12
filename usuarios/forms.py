from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(label="Nome de Login", required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ex.: Jaojaja.700"}))
    senha_login = forms.CharField(label="Senha", required=True, max_length=70, widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder": "Digite sua senha"}))

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(label="Nome de cadastro", required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ex.: Jaojaja.700"}))
    email_cadastro = forms.EmailField(label="E-mail", required=True, max_length=100, widget=forms.EmailInput(attrs={"class":"form-control", "placeholder": "Ex.: Jaojaja.700@gmail.com"}))
    senha_cadastro = forms.CharField(label="Senha", required=True, max_length=70, widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder": "Digite sua senha"}))
    resenha_cadastro = forms.CharField(label="Confirme sua Senha", required=True, max_length=70, widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder": "Digite sua senha novamente"}))
