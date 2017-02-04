from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


from photos.models import Photo


class HomeView(View):

    def get(self, request):
        """

        :param request:
        :return:
        """
        photos = Photo.objects.all()
        context = {'photo_list': photos}
        return render(request, 'photos/home.html', context)


class ServiceView(View):
    def get(self, request):
        return render(request, 'photos/services.html')
