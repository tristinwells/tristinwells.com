from django import forms
from django.db.models.fields import CharField
from django.forms.models import ModelForm
from django_core.forms.fields import CharFieldStripped
from django_core.forms.mixins.users import UserFormMixin

from blog.models import Entry


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass

    class CharFieldStripped(CharField):
        """Wrapper around CharField that strips whitespace from the CharField
        when validating so .strip() doesn't have to be called every time you
        validate the field's data.
        """

    def clean(self, value):
        if value:
            value = value.strip()

        return super(CharFieldStripped, self).clean(value)


class EntryAddForm(UserFormMixin, ModelForm):

    class Meta:
        model = Entry
        fields = ['title', 'body', 'tags']

    def save(self, *args, **kwargs):
        self.instance.created_user = self.user
        return super(EntryAddForm, self).save(*args, **kwargs)


class EntryUpdateForm(ModelForm):
    # edit = forms.CharField(required=False)

    class Meta:
        model = Entry
        fields = ['title', 'body', 'tags']
