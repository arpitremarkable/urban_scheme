# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class AbstractBaseModel(object):

    def __unicode__(self):
        try:
            return self.name
        except Exception:
            try:
                return self.title
            except Exception:
                return ''


class BaseModel(AbstractBaseModel, models.Model):
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class EMIRate(BaseModel):
    bank = models.CharField(max_length=50)
    tenure = models.IntegerField(help_text='In months')
    rate = models.IntegerField(help_text='Interest rate in percentage')
    amount = models.IntegerField(help_text='Minimum loan amount')

    def __unicode__(self):
        return "%s - %d months" % (self.bank, self.tenure, )

    class Meta(BaseModel.Meta):
        unique_together = ('bank', 'tenure', )
