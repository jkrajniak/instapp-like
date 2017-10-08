#  Copyright (C) 2017
#      Jakub Krajniak (jkrajniak at gmail.com)
#
#  This file is part of instapp.
#
#  instapp is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  instapp is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from . import tools
from .forms import UploadFileForm
from .models import Image


def index(request):
    image_list = Image.objects.all()
    image_paginator = Paginator(image_list, 8)

    page = request.GET.get('page')
    try:
        images = image_paginator.page(page)
    except PageNotAnInteger:
        images = image_paginator.page(1)
    except EmptyPage:
        images = image_paginator.page(image_paginator.num_pages)

    return render(request, 'main/index.html', {'images': images})


def upload_image(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = form.save(commit=True)
            visual_attrs = tools.handle_image(new_image)
            new_image.visual_attrs = visual_attrs
            new_image.save()
            return HttpResponseRedirect(reverse('main_index'))
    else:
        form = UploadFileForm()

    return render(request, 'main/upload.html', {'upload_form': form})


def view_image(request, image_id):
    try:
        image = Image.objects.get(pk=image_id)
    except Image.DoesNotExist:
        raise Http404('Image does not exist')

    return render(request, 'main/image_detail.html', {'image': image})
