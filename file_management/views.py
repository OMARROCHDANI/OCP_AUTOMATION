from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from ocp_scrape.models import GeneratedFiles
from django.shortcuts import get_object_or_404
# Create your views here.
def file_list(request):
    if request.user.is_authenticated:
        user_files = GeneratedFiles.objects.filter(user=request.user)

        if request.method == 'POST':
            file_id = request.POST.get('file_id')
            file_to_delete = GeneratedFiles.objects.get(id=file_id)
            file_to_delete.file_field.delete()  # Delete the actual file from storage
            file_to_delete.delete()  # Delete the database record

            return redirect('file_list')  # Redirect back to the file list page after deletion

        return render(request, 'file_management2.html', {'files': user_files})
    else:
        return redirect('/login/')

def latest_file_view(request):
    latest_file = GeneratedFiles.objects.latest('id')
    return render(request, 'latest-file2.html', {'file': latest_file})

