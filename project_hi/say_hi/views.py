from django.shortcuts import render, redirect
from .models import Name
from .forms import NameForm
from django_tables2 import Table
from django_filters import rest_framework as filters
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django.views.generic import TemplateView
from django.contrib import messages


class NamesFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Name
        fields = []


class NameTable(Table):
    class Meta:
        model = Name
        template_name = "django_tables2/bootstrap.html"
        fields = ('name', 'created_at')


class FilteredListView(SingleTableMixin, FilterView):
    table_class = NameTable
    model = Name
    filterset_class = NamesFilter
    template_name = "all_names.html"


class Say_Hi(TemplateView):
    def get(self, request):
        form = NameForm()
        return render(request, 'index.html', {'form': form})

    def post(self, request):
        form = NameForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            messages.add_message(request, messages.INFO, f'Привіт {form.data.get("name")}')
            post.save()
        else:
            messages.add_message(request, messages.INFO, f'Вже бачилися, {form.data.get("name")}')
        return redirect('index')
