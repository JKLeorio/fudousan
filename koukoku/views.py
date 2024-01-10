from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from .forms import EstateCreationForm, ImagesFormSet
from .models import Estate, Image


# class ImageUploadView(LoginRequiredMixin, CreateView):
#     template_name = 'image_upload.html'
#     form_class = ImageUploadForm
#     success_url = reverse_lazy('estate_update')

class EstateInline:
    model = Estate
    form_class = EstateCreationForm
    success_url = "/"
    template_name = "estate_create.html"

    def form_valid(self, form: ModelForm):
        image_formset = self.get_images_formset()
        if not image_formset.is_valid():
            form.add_error(None, "image formset error")
            return super().form_invalid(form)

        data = form.cleaned_data

        estate = self.object

        if not self.object:
            new_form = EstateCreationForm(data=data, files=form.files)
            estate = new_form.save()
        else:
            estate.save()

        for form in image_formset:
            self.form_images_valid(form, estate)

        return redirect("estate_list")

    def form_images_valid(self, form, estate):
        image = form.save(commit=False)
        image.estate = estate
        image.save()


class EstateCreateView(EstateInline, CreateView, LoginRequiredMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = ImagesFormSet(prefix="images")
        return context

    def get_images_formset(self):
        if self.request.method == "GET":
            return ImagesFormSet(prefix='images')
        else:
            return ImagesFormSet(self.request.POST or None, self.request.FILES or None, prefix='images',
                                 form_kwargs={'empty_permitted': False})


class EstateListView(ListView):
    template_name = 'estate_list.html'
    model = Estate
    context_object_name = 'estates'


class EstateDetailView(DetailView):
    model = Estate
    template_name = 'estate_detail.html'


class EstateUpdateView(EstateInline, UpdateView, LoginRequiredMixin):

    def get_context_data(self, **kwargs):
        context = super(EstateUpdateView, self).get_context_data(**kwargs)

        context['formset'] = self.get_images_formset()
        return context

    def get_images_formset(self):
        return ImagesFormSet(
            self.request.POST or None,
            self.request.FILES or None,
            instance=self.object,
            prefix='images',
        )


class EstateDeleteView(LoginRequiredMixin, DeleteView):
    model = Estate
    success_url = reverse_lazy('estate_list')


def delete_image(request, pk):
    try:
        image = Image.objects.get(id=pk)
    except Image.DoesNotExist:
        messages.success(
            request, 'Object Does not exit'
        )
        return redirect('estate_create')

    image.delete()
    messages.success(
        request, 'Image deleted successfully'
    )
    return redirect('estate_update', pk=image.estate.id)

# class FavoritesAddView(LoginRequiredMixin, CreateView):
#     pass
