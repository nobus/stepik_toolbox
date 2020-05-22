from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import FormActions, PrependedText, Field


class PostcardForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Fieldset(
                'Postcard',
                #'address',
                Field('address', css_class="extra"),
                'author',
                'compliment',
                'date_of_delivery',
                #'email',
                PrependedText('email', '@', placeholder="email@doma.in")
            ),
            FormActions(
                Submit('submit', 'Submit', css_class='button white')
            )
        )

        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = '/thanks/'

        #self.helper.add_input(Submit('submit', 'Submit'))


    address = forms.CharField(label='Destination Address')
    author = forms.CharField(min_length=3)
    compliment = forms.CharField(max_length=1024)
    date_of_delivery = forms.DateField(input_formats=['%Y/%m/%d'])
    email = forms.EmailField()
