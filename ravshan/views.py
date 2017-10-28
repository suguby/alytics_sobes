# -*- coding: utf-8 -*-
from django.urls import reverse
from django.views.generic import ListView, CreateView, DeleteView

from ravshan.models import DataSet


class DataSetsList(ListView):
    model = DataSet


class DataSetUpload(CreateView):
    model = DataSet
    fields = ('data_in', )

    def get_success_url(self):
        return reverse('datasets_list')


class DataSetDelete(DeleteView):
    model = DataSet

    def get_success_url(self):
        return reverse('datasets_list')
