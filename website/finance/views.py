from django.shortcuts import render
from django.views import generic
from .models import BankScrewsIndexValuation


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'finance/index.html'
    context_object_name = 'info_list'

    def get_queryset(self):
        """get info"""
        return


# ------------- BankScrews View -------------
class BankScrewsView(generic.ListView):
    template_name = 'finance/bank_screws/index.html'
    context_object_name = 'none'

    def get_queryset(self):
        return


class BankScrewsIndexValuationView(generic.ListView):
    template_name = 'finance/bank_screws/index_valuation.html'
    context_object_name = 'index_valuation_list'

    def get_queryset(self):
        return BankScrewsIndexValuation.objects.order_by('title')
