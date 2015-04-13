import json

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

        post = request.body.decode()
        if post == '':
            post = None
        else:
            post = json.loads(post)
        self.form = EditContentForm(post, instance=self.content, initial={'authors': [str(_.pk) for _ in self.content.authors.all()]})

    def get(self, request, content_id):
        return ApiResponse(self.form)

    def post(self, request, content_id):
        if self.form.is_valid():
            self.form.save()
            return ApiResponse(data=self.form.instance)
        return ApiResponse(self.form, status_code=status.HTTP_400_BAD_REQUEST)