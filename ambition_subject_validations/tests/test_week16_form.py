from django import forms
from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_base.utils import get_utcnow
from edc_constants.constants import YES, NO

from ..form_validators import Week16FormValidator


class TestWeek16Form(TestCase):

    def test_patient_dead_death_datetime(self):
        cleaned_data = {'patient_alive': NO,
                        'death_datetime': None}
        week16 = Week16FormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, week16.clean)

        cleaned_data = {'patient_alive': NO,
                        'death_datetime': get_utcnow()}
        week16 = Week16FormValidator(cleaned_data=cleaned_data)

        try:
            week16.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_patient_alive_activities_help(self):
        cleaned_data = {'patient_alive': YES,
                        'illness_problems': NO,
                        'ranking_score': 1,
                        'activities_help': None}
        week16 = Week16FormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, week16.clean)

        cleaned_data = {'patient_alive': YES,
                        'illness_problems': NO,
                        'ranking_score': 1,
                        'activities_help': YES}
        week16 = Week16FormValidator(cleaned_data=cleaned_data)

        try:
            week16.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_patient_alive_illness_problems(self):
        cleaned_data = {'patient_alive': YES,
                        'ranking_score': 1,
                        'activities_help': YES,
                        'illness_problems': None}
        week16 = Week16FormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, week16.clean)

        cleaned_data = {'patient_alive': YES,
                        'ranking_score': 1,
                        'activities_help': YES,
                        'illness_problems': YES}
        week16 = Week16FormValidator(cleaned_data=cleaned_data)

        try:
            week16.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_patient_alive_ranking_score(self):
        cleaned_data = {'patient_alive': YES,
                        'activities_help': YES,
                        'illness_problems': YES,
                        'ranking_score': None}
        week16 = Week16FormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, week16.clean)

        cleaned_data = {'patient_alive': YES,
                        'activities_help': YES,
                        'illness_problems': YES,
                        'ranking_score': 2}
        week16 = Week16FormValidator(cleaned_data=cleaned_data)

        try:
            week16.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
