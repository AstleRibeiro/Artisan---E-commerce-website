from django.forms import Form, ChoiceField, CharField


class FilterForm(Form):
    FILTER_CHOICES = (
        ('all', 'All'),
        ('people', 'People'),
        ('certification', 'Certification'),
        ('skillset', 'Skillset'),
    )
    search = CharField(required=False)
    filter_field = ChoiceField(choices=FILTER_CHOICES)