from django.conf.urls import url

from .views import EMIRateListView

urlpatterns = [
    url(r'^emi-schemes/$', EMIRateListView.as_view(), name='emi_schemes'),
]
