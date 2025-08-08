from django.shortcuts import render, redirect
from django.views import View
from . import tasks
from django.contrib import messages
from utils import IsAdminUserMixin


class HomeView(View):
    template_name = "base.html"
    def get(self, request):
        return render(request, self.template_name)


class ViewIndex(View):
    template_name = "home/index.html"
    def get(self, request):
        title = {}
        return render(request, self.template_name, {'title': title})
    
    
    
class BucketHomeView(IsAdminUserMixin, View):
    template_name="home/bucket.html"
    def get(self, request):
        objects = tasks.all_bucket_objects_task()
        return render(request, self.template_name, {"objects": objects})
    
    
    
class DeleteBucketObject(IsAdminUserMixin, View):
    def get(self, request, key):
        tasks.delete_object_task.delay(key)
        messages.success(request, "Your Delete Object The Perfect ... ")
        return redirect("home:bucket")
    
    
class DownloadBucketObjectView(IsAdminUserMixin, View):
    def get(self, request, key):
        tasks.download_object_task.delay(key)
        messages.success(request, "Your Download Perfect File ...", "info")
        return redirect("home:bucket")

        