from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Advertisement
from .forms import AdvertisementForm
def index(request):
    title = request.GET.get('query')
    if title:
        advertisements = Advertisement.objects.filter(title__icontains=title)
    else:
        advertisements = Advertisement.objects.all()
    context = {
        'advertisements': advertisements,
        'title': title
    }
    return render(request, 'app_advertisements/index.html',context)


def top_sellers(request):
    return render(request, 'app_advertisements/top-sellers.html')


def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'app_advertisements/advertisement-post.html', context)


def get_absolute_url(self):
    return reverse('advertisement-detail', kwargs={'pk': self.pk})


def advertisement_detail(request, pk):
    advertisement = Advertisement.objects.get(pk=pk)
    context = {'advertisement': advertisement}
    return render(request, 'app_advertisements/advertisement-detail.html', context)