from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views import View
from .forms import BookForm
from .models import Book
from django.views.generic import DetailView, DeleteView, ListView


class BookFormView(FormView):
    template_name = 'book_form.html'
    form_class = BookForm
    success_url = reverse_lazy('form_success')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class FormSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Book record saved successfully")


class BookCreateView(CreateView):
    model = Book
    fields = ['name', 'author']
    template_name = 'book_form.html'
    success_url = reverse_lazy('form_success')
    success_ur1 = '/form_success'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'


class BookListView(ListView):
    template_name = 'book_list.html'
    Model = Book
    queryset = Book.objects.order_by('name')
    context_object_name = 'book_list'


class BookUpdateView(UpdateView):
    model = Book
    fields = ['name', 'author']
    template_name = 'book_form.html'
    success_url = reverse_lazy('update_success')
    success_ur1 = '/update_success'


class BookDeleteView(DeleteView):
    template_name = 'book_delete_form.html'
    model = Book
    success_url = reverse_lazy('book_success')
    success_ur1 = '/book_success'


class DeleteSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Book record deleted successfully")


class UpdateSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Book record Update successfully")
