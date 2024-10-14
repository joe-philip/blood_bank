from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .utils import success


class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response: Response = renderer_context.get('response')
        if response.status_code in range(200, 400):
            data = success(data)
        return super().render(data, accepted_media_type, renderer_context)
