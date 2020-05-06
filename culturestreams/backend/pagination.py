from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


DEFAULT_PAGE = 1

# class CustomJSONRenderer(JSONRenderer):
#     def render(self, data, accepted_media_type=None, renderer_context=None):
#         response_data = {}

        #determine the resource name for this request - default to objects if not defined
        # resource = getattr(renderer_context.get('view').get_serializer().Meta, 'resource_name', 'objects')
        # response_data['meta'] = CustomPagination.get_paginated_response(resource)
        # check if the results have been paginated
        # if data.get('paginated_results'):
            #add the resource key and copy the results
            # response_data['meta'] = data.get('meta')
        #     response_data[resource] = data.get('paginated_results')
        # else:
        #     response_data[resource] = data
        # response_data[resource] = data

        #call super to render the response
        # response = super(CustomJSONRenderer, self).render(response_data, accepted_media_type, renderer_context)
        # return response

class CustomPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = 10
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        # resource = getattr(data.get('view').get_serializer().Meta, 'resource_name', 'objects')
        paginated_response = {
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'limit': self.page_size,
            'objects': data
            }
        # paginated_response[resource] = data
        return Response(paginated_response)
