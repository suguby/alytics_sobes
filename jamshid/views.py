# -*- coding: utf-8 -*-

# Create your views here.
from django.views.generic import TemplateView


class RunChecks(TemplateView):
    template_name = 'run_checks.html'

    def get_context_data(self, **kwargs):
        context = super(RunChecks, self).get_context_data(**kwargs)
        return context

    def post(self):
        pass
