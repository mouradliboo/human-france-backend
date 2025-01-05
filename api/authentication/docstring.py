from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

def login_schema():
    """
    Returns the OpenAPI schema for user login.
    """
    # Request body schema
    request_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['username', 'password'],
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, example='username'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, example='password'),
        }
    )

    # Response schema for 200 OK
    response_schema_200 = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'refresh': openapi.Schema(type=openapi.TYPE_STRING, example='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'),
            'access': openapi.Schema(type=openapi.TYPE_STRING, example='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'),
            'email': openapi.Schema(type=openapi.TYPE_STRING, example='ma_missoum@esi.dz'),
            'role': openapi.Schema(type=openapi.TYPE_STRING, example='agent'),
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
        }
    )

    # Response schema for 400 Bad Request
    response_schema_400 = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'password': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(type=openapi.TYPE_STRING, example='This field is required.')
            ),
        }
    )

    # Response schema for 401 Unauthorized
    response_schema_401 = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'detail': openapi.Schema(type=openapi.TYPE_STRING, example='No active account found with the given credentials'),
        }
    )

    return swagger_auto_schema(
        operation_description="User login - Authenticate a user and retrieve access and refresh tokens",
        request_body=request_body,
        responses={
            200: openapi.Response(
                description="Login successful. Returns access and refresh tokens along with user details.",
                schema=response_schema_200,
            ),
            400: openapi.Response(
                description="Bad Request. A required field (e.g., username or password) is missing.",
                schema=response_schema_400,
            ),
            401: openapi.Response(
                description="Unauthorized. Invalid credentials provided.",
                schema=response_schema_401,
            ),
        }
    )
