from restify.api import Api

from bangoo.content.api import resources as content_resources
from bangoo.navigation.api import resources as navigation_resources
from bangoo.blog.api import resources as blog_resources

api = Api(api_name='v1')
api.register(regex='content/(?P<menu_id>(\d+|new))/$', resource=content_resources.ContentResource)
api.register(regex='navigation/(?P<menu_id>(\d+|new))/$', resource=navigation_resources.MenuResource)
api.register(regex='blog/(?P<post_id>(\d+|publish|list|new))/$', resource=blog_resources.PostResource)
