from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view

from rest_framework import status as drf_status


def agent_list_schema():
    """
    Returns the OpenAPI schema for retrieving a list of agent objects filtered by status.
    """
    agent_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=7),
            'user': openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=5),
                    'first_name': openapi.Schema(type=openapi.TYPE_STRING, example='John'),
                    'last_name': openapi.Schema(type=openapi.TYPE_STRING, example='Doe'),
                    'email': openapi.Schema(type=openapi.TYPE_STRING, example='johndoe@example.com'),
                    'phone': openapi.Schema(type=openapi.TYPE_STRING, example='+1234567890'),
                    'address': openapi.Schema(type=openapi.TYPE_STRING, example='123 Main St, Cityville'),
                }
            ),
            'updated_at': openapi.Schema(type=openapi.TYPE_STRING, example='2025-01-05T18:41:40.079465Z'),
        }
    )

    return swagger_auto_schema(
        method='GET',
        operation_description="Retrieve a list of agents filtered by status.",
        responses={
            200: openapi.Response(
                description="Successfully retrieved the list of agents",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=agent_schema,
                ),
            ),
            400: openapi.Response(
                description="Bad request - error in filtering agents",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='Invalid status parameter'),
                    }
                ),
            ),
        },
        query_parameters=[
            openapi.Parameter(
                'status', openapi.IN_QUERY, description="Filter agents by status (approved or pending)", type=openapi.TYPE_STRING
            ),
        ]
    )
