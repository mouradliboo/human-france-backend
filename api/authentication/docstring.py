from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

def login_schema():
    """
    Returns the OpenAPI schema for user login.
    """
    # Request body schema
    request_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['email', 'password'],
        properties={
            'email': openapi.Schema(type=openapi.TYPE_STRING, example='email@gmail.com'),
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


def signup_schema():
    """
    Returns the OpenAPI schema for user signup with modified fields for diplomas, experience, and tenues.
    """
    # Request body schema
    request_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['first_name', 'last_name', 'email', 'phone', 'address', 'agent_fonction'],
        properties={
            'first_name': openapi.Schema(type=openapi.TYPE_STRING, example='Alex'),
            'last_name': openapi.Schema(type=openapi.TYPE_STRING, example='Johnson'),
            'email': openapi.Schema(type=openapi.TYPE_STRING, example='ma_misskkzdzm@esi.dz'),
            'phone': openapi.Schema(type=openapi.TYPE_STRING, example='+1234567890'),
            'address': openapi.Schema(type=openapi.TYPE_STRING, example='789 Elm St, Springfield'),
            'photo_identity': openapi.Schema(type=openapi.TYPE_STRING, example='https://example.com/photo_identity.jpg'),
            'nss': openapi.Schema(type=openapi.TYPE_STRING, example='9876f5432109876'),
            'card_number_pro': openapi.Schema(type=openapi.TYPE_STRING, example='PRO987654'),
            'security_card_photo': openapi.Schema(type=openapi.TYPE_STRING, example='https://example.com/security_card_photo.jpg'),
            'nub': openapi.Schema(type=openapi.TYPE_STRING, example='NUB456'),
            'agent_fonction': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING), example=["securite", "tricking"]),
            'driver_licence_type': openapi.Schema(type=openapi.TYPE_STRING, example='B'),
            'emergency_contact_name': openapi.Schema(type=openapi.TYPE_STRING, example='Sarah Johnson'),
            'emergency_contact_phone': openapi.Schema(type=openapi.TYPE_STRING, example='+0987654321'),
            'diplomes': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_OBJECT), example=[
                {"title": "BSc in Security Management", "year": 2015},
                {"title": "Certified Fire Safety Specialist", "year": 2018}
            ]),
            'experience': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_OBJECT), example=[
                {"company": "Fire Safety Inc.", "position": "Senior Agent", "years": 3},
                {"company": "Secure Solutions", "position": "Team Lead", "years": 2}
            ]),
            'tenues': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING), example=["lux", "lanc"]),
            'languages': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING), example=["arabic", "french"])
        }
    )

  

# Response schema for 201 Created
    response_schema_201 = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'agent': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=6),
                'photo_identity': openapi.Schema(type=openapi.TYPE_STRING, example='https://example.com/photo_identity.jpg'),
                'nss': openapi.Schema(type=openapi.TYPE_STRING, example='9876f5432109876'),
                'card_number_pro': openapi.Schema(type=openapi.TYPE_STRING, example='PRO987654'),
                'security_card_photo': openapi.Schema(type=openapi.TYPE_STRING, example='https://example.com/security_card_photo.jpg'),
                'nub': openapi.Schema(type=openapi.TYPE_STRING, example='NUB456'),
                'agent_fonction': openapi.Schema(type=openapi.TYPE_STRING, example='securite,tricking'),
                'driver_licence_type': openapi.Schema(type=openapi.TYPE_STRING, example='B'),
                'emergency_contact_name': openapi.Schema(type=openapi.TYPE_STRING, example='Sarah Johnson'),
                'emergency_contact_phone': openapi.Schema(type=openapi.TYPE_STRING, example='+0987654321'),
                'diplomes': openapi.Schema(
                    type=openapi.TYPE_ARRAY, 
                    items=openapi.Schema(type=openapi.TYPE_OBJECT), 
                    example=[
                        {"title": "BSc in Security Management", "year": 2015},
                        {"title": "Certified Fire Safety Specialist", "year": 2018}
                    ]
                ),
                'experience': openapi.Schema(
                    type=openapi.TYPE_ARRAY, 
                    items=openapi.Schema(type=openapi.TYPE_OBJECT), 
                    example=[
                        {"company": "Fire Safety Inc.", "position": "Senior Agent", "years": 3},
                        {"company": "Secure Solutions", "position": "Team Lead", "years": 2}
                    ]
                ),
                'tenues': openapi.Schema(type=openapi.TYPE_STRING, example='lux,lanc'),
                'languages': openapi.Schema(type=openapi.TYPE_STRING, example='arabic,french'),
                'status': openapi.Schema(type=openapi.TYPE_STRING, example='pending'),
                'created_at': openapi.Schema(type=openapi.TYPE_STRING, example='2025-01-11T15:35:55.638601Z'),
                'updated_at': openapi.Schema(type=openapi.TYPE_STRING, example='2025-01-11T15:35:55.639130Z'),
                'user': openapi.Schema(type=openapi.TYPE_INTEGER, example=9),
            }
        ),
        'user': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=9),
                'first_name': openapi.Schema(type=openapi.TYPE_STRING, example='Alexx'),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING, example='Johnson'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, example='jy_attou@esi.dz'),
                'phone': openapi.Schema(type=openapi.TYPE_STRING, example='+1234567890'),
                'address': openapi.Schema(type=openapi.TYPE_STRING, example='789 Elm St, Springfield')
            }
        )
    }
)

    # Response schema for 400 Bad Request
    response_schema_400 = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(type=openapi.TYPE_STRING, example='user with this username already exists.')
            ),
            'email': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(type=openapi.TYPE_STRING, example='user with this email already exists.')
            ),
            'phone': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(type=openapi.TYPE_STRING, example='This field is required.')
            ),
        }
    )

    return swagger_auto_schema(
        method='POST',
        operation_description="User signup - Register a new user and associate agent details",
        request_body=request_body,
        responses={
            201: openapi.Response(
                description="Signup successful. Returns agent and user details.",
                schema=response_schema_201,
            ),
            400: openapi.Response(
                description="Bad Request. A required field (e.g., username, email, phone) is missing.",
                schema=response_schema_400,
            ),
        }
    )
