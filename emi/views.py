# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http.response import JsonResponse
from django.views.generic.list import ListView

from .forms import EMIRateForm
from .models import EMIRate


class EMIRateListView(ListView):
    model = EMIRate
    response_class = JsonResponse

    def get(self, request, *args, **kwargs):
        form = EMIRateForm(data=request.GET)
        if form.is_valid():
            self.form = form
            return super(EMIRateListView, self).get(request, *args, **kwargs)
        else:
            return self.render_to_response({
                'errors': form.errors,
            })

    def get_queryset(self):
        return EMIRate.objects.filter(amount=self.form.cleaned_data['amount'])

    def get_context_data(self, **kwargs):
        context_data = super(EMIRateListView, self).get_context_data(**kwargs)
        object_list = context_data['object_list']
        bank = None
        bank_list = []
        for row in object_list.order_by('bank').values('bank', 'tenure', 'rate', 'amount'):
            if row['bank'] != bank:
                bank = row['bank']
                bank_details = {}
                bank_details['bank'] = row['bank']
                bank_details['tenures'] = []
                bank_list.append(bank_details)
            bank_details['tenures'].append({
                'months': row['tenure'],
                'rate': row['rate'],
                'minimum_amount': row['amount']
            })
        return {
            'data': bank_list,
        }

    def render_to_response(self, context, **response_kwargs):
        if context.get('errors'):
            status = 400
        else:
            status = 200
        return self.response_class(
            data=context,
            status=status
        )
