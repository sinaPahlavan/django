from django.shortcuts import render
from .forms import SubmissionForm
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def upload_display_video(request):
    if request.POST:
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            #print(file.name)
            form.save()
            return render(request, "submitted-successfully.html", {'form': form})

        else:
            print(form.errors)

    else:
        form = SubmissionForm()

    return render(request, 'upload-display-video.html', {'form': form})

# def submitted(request):
#     return render(request,'submitted-successfully.html')

def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
