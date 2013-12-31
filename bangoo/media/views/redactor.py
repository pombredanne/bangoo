"""
    Handling media content in redactor.js
"""
import json
import os
from PIL import Image
from django.conf import settings
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required


@csrf_exempt
@require_POST
@login_required
def upload_images(request):
    retval = []
    for f in request.FILES.getlist("file"):
        if f.content_type.find('image') == -1:
            raise Http404() ## very ugly type check, TODO
        out = open(settings.MEDIA_ROOT + f.name, 'w')
        out.write(f.read())
        retval.append({"filelink": settings.MEDIA_URL + f.name})
    return HttpResponse(json.dumps(retval), mimetype="application/json")


@login_required
def list_images(request):
    images = [
        {"thumb": settings.MEDIA_URL + fname, 
         "image": settings.MEDIA_URL + fname}
        for fname in os.listdir(settings.MEDIA_ROOT)
    ]
    return HttpResponse(json.dumps(images), mimetype="application/json")