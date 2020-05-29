from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Reset, Field
from crispy_forms.bootstrap import PrependedText, AppendedText, FormActions


class PostcardForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_method = 'post'

        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-4'

        self.helper.layout = Layout(
            Fieldset(
                'ADDRESSES'
                'N2',
                AppendedText('address', '&#9993;', placeholder="почтовый адрес"),
                PrependedText('email', '@', placeholder="email"),
                AppendedText('date_of_delivery', '', placeholder='дата доставки'),
            ),
            Fieldset(
                'AUTHOR',
                'author',
                'compli'
                'ment',
            ),
            FormActions(
                Submit('submit', 'Submit'),
                Reset('reset', 'Reset'),
            )
        )


    address = forms.CharField(label='Destination Address')
    author = forms.CharField(min_length=3)
    compliment = forms.CharField(max_length=1024)
    date_of_delivery = forms.DateField(input_formats=['%Y/%m/%d'])
    email = forms.EmailField()
