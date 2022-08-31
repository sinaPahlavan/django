from django.shortcuts import render
from .forms import SubmissionForm, ContactForm
from django.views.decorators.csrf import ensure_csrf_cookie

def index(request):
    return render(request, 'index.html')

@ensure_csrf_cookie
def upload(request):
    if request.POST:
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['videoSub']
            #print(file.name)
            form.save()
            return render(request, "submitted-successfully.html", {'form': form})

        else:
            print("form not valid")

    else:
        form = SubmissionForm()

    return render(request, 'upload-display-video.html', {'form': form})

# def submitted(request):
#     return render(request,'submitted-successfully.html')

def contact(request):
    if request.POST:
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            return render(request, "submitted-successfully.html", {'form': form})

        else:
            print("form not valid")

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
