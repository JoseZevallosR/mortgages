from django import forms


class tablesForm(forms.Form):
	file_upload = forms.FileField(required=True)
