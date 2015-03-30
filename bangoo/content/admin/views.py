from .forms import EditContentForm
from bangoo.content.models import Content
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.conf import settings


@permission_required('content.add_content')
def edit_content(request, template_name='content/admin/edit_content.html'):
    lang = settings.LANGUAGES[0][0]
    try:
        content = Content.objects.language(lang).get(url=request.act_menu.path)
        print content
    except Content.DoesNotExist:
        content = Content(is_page=True)
    form = EditContentForm(request.POST or None, instance=content, initial={'authors': [request.user]})
    if form.is_valid():
        form.save()
        #return HttpResponseRedirect(reverse('admin-content-list'))
    return render(request, template_name, {'form': form, 'menu': request.act_menu})