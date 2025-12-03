from django import forms


class ProductForm(forms.Form):
  title = forms.CharField(
    max_length=200,
    label="Наименование товара:",
    required=False,
    widget=forms.TextInput(attrs={
      'placeholder': "Наименование товара (максимальная длина 200 символов)"
    }) # Можно передавать другие атрибуты, например, "class": 'title-input'
  )

  text = forms.CharField(
    label="Описание товара:",
    widget=forms.Textarea(attrs={
      'row': 3
    })
  )

  def clean_title(self):
    title = self.cleaned_data['title'].strip()

    if not title:
      raise forms.ValidationError("Наименование товара обязательно.")
    
    if len(title) < 5:
      raise forms.ValidationError("Наименование товара не должно быть короче 5 символов.")
    
    return title
