# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from .models import EMIRate


class EMIRateForm(forms.ModelForm):
    class Meta:
        model = EMIRate
        fields = ('amount', )
