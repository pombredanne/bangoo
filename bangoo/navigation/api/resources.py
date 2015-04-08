import json

from restify import status
from restify.http.response import ApiResponse
from restify.resource import ModelResource

from bangoo.navigation.menu.forms import MenuCreateForm
from bangoo.navigation.models import Menu


class MenuResource(ModelResource):
    class Meta:
        resource_name = 'menu-api'

    def common(self, request, menu_id):
        post = request.body.decode()
        self.form = MenuCreateForm(json.loads(post) if post != '' else None)

    def get(self, request, menu_id):
        return ApiResponse(self.form)

    def post(self, request, menu_id):
        if self.form.is_valid():
            data = self.form.cleaned_data

            plugin = data['plugin']
            titles = {}

            for k, v in data.items():
                if k in self.form.language_fields:
                    code = self.form.language_fields[k]
                    titles[code] = v

            Menu.handler.add_menu(titles=titles, plugin=plugin)

            # TODO: Return new menu instances
            return ApiResponse({})
        return ApiResponse(self.form, status_code=status.HTTP_400_BAD_REQUEST)