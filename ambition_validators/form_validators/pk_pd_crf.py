from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES, OTHER

from ..constants import DEVIATION
from edc_base.modelform_validators.base_form_validator import NOT_REQUIRED_ERROR
from django.forms import forms


class PkPdCrfFormValidator(FormValidator):

    def clean(self):

        self.required_if(
            YES,
            field='flucytosine_doses_missed',
            field_required='flucytosine_dose_missed')
