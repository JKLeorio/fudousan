from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from .forms import EstateCreationForm
from .models import Estate


# class ImageUploadView(LoginRequiredMixin, CreateView):
#     template_name = 'image_upload.html'
#     form_class = ImageUploadForm
#     success_url = reverse_lazy('estate_update')


class EstateCreateView(LoginRequiredMixin, CreateView):
    template_name = 'estate_create.html'
    form_class = EstateCreationForm
    success_url = reverse_lazy('estate_list')

    # def post(self, request, *args, **kwargs):
    #     if request.method == 'POST':
    #         form = EstateCreationForm(request.POST)
    #         if form.is_valid():
    #             estate = form.save(commit=False)
    #             estate.save()
    #             images = request.FILES.getlist('images')
    #             for img in images:
    #                 Image.objects.create(image=img, estate=estate)
    #             return redirect('estate_detail', pk=estate.pk)
    #     else:
    #         form = EstateCreationForm()
    #     return render(request, 'estate_create.html', {'form': form})


class EstateListView(ListView):
    template_name = 'estate_list.html'
    model = Estate
    context_object_name = 'estates'


class EstateDetailView(DetailView):
    model = Estate
    template_name = 'estate_detail.html'


class EstateUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'estate_update.html'
    form_class = EstateCreationForm
    model = Estate
    success_url = reverse_lazy('estate_list')

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #
    #     # сохраняем Estate
    #     response = super().form_valid(form)
    #
    #     # сохраняем изображения и связываем их с объектом Estate
    #     images = self.request.FILES.getlist('images')
    #     print(images)
    #     for image in images:
    #         print(image)
    #         img = Image(image=image, estate=self.object)
    #         img.save()
    #
    #     return response


class EstateDeleteView(LoginRequiredMixin, DeleteView):
    model = Estate
    success_url = reverse_lazy('estate_list')
