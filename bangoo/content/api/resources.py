from django.conf import settings

from restify import status
from restify.http.response import ApiResponse
from restify.resource import ModelResource

from bangoo.content.admin.forms import EditContentForm
from bangoo.content.models import Content


class ContentResource(ModelResource):
    class Meta:
        resource_name = 'content-api'

    def common(self, request, content_id):
        lang = settings.LANGUAGES[0][0]
        try:
            self.content = Content.objects.language(lang).get(id=content_id)
        except Content.DoesNotExist:
            self.content = Content(is_page=True)
        self.form = EditContentForm(request.POST or None, instance=self.content, initial={'authors': [str(request.user)]})

    def get(self, request, content_id):
        return ApiResponse(self.form)

    def post(self, request, content_id):
        if self.form.is_valid():
            self.form.save()
            return ApiResponse(data=self.form.instance)
        return ApiResponse(self.form, status_code=status.HTTP_400_BAD_REQUEST)