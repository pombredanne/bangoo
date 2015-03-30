from restify.api import Api

from bangoo.content.api import resources as content_resources

api = Api(api_name='v1')
api.register(regex='content/(?P<content_id>(\d+|new))/$', resource=content_resources.ContentResource)