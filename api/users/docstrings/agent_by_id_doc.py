from drf_yasg.utils import swagger_auto_schema


from drf_yasg import openapi

def agent_detail_schema():
    """
    Returns the OpenAPI schema for retrieving a single agent object by ID.
    """
    agent_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=5),
            'user': openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=8),
                    'first_name': openapi.Schema(type=openapi.TYPE_STRING, example='Alice'),
                    'last_name': openapi.Schema(type=openapi.TYPE_STRING, example='Smith'),
                    'email': openapi.Schema(type=openapi.TYPE_STRING, example='alice.smith@example.com'),
                    'phone': openapi.Schema(type=openapi.TYPE_STRING, example='+987654321'),
                    'address': openapi.Schema(type=openapi.TYPE_STRING, example='456 Elm Street, Metropolis'),
                }
            ),
            'photo_identity': openapi.Schema(type=openapi.TYPE_STRING, example='path/to/alice_photo_identity.jpg'),
            'nss': openapi.Schema(type=openapi.TYPE_STRING, example='98765432109876'),
            'card_number_pro': openapi.Schema(type=openapi.TYPE_STRING, example='PRO-567890'),
            'security_card_photo': openapi.Schema(type=openapi.TYPE_STRING, example='path/to/security_card_photo_alice.jpg'),
            'nub': openapi.Schema(type=openapi.TYPE_STRING, example='67890'),
            'agent_fonction': openapi.Schema(type=openapi.TYPE_STRING, example='securite'),
            'driver_licence_type': openapi.Schema(type=openapi.TYPE_STRING, example='A'),
            'emergency_contact_name': openapi.Schema(type=openapi.TYPE_STRING, example='Bob Smith'),
            'emergency_contact_phone': openapi.Schema(type=openapi.TYPE_STRING, example='+123456789'),
            'diplomes': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'diploma_name': openapi.Schema(type=openapi.TYPE_STRING, example='Bachelor of Security'),
                        'year': openapi.Schema(type=openapi.TYPE_STRING, example='2020'),
                    }
                ),
            ),
            'experience': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'job_title': openapi.Schema(type=openapi.TYPE_STRING, example='Security Specialist'),
                        'company': openapi.Schema(type=openapi.TYPE_STRING, example='SecureCorp Ltd.'),
                        'duration': openapi.Schema(type=openapi.TYPE_STRING, example='3 years'),
                    }
                ),
            ),
            'tenues': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'type': openapi.Schema(type=openapi.TYPE_STRING, example='Tactical Vest'),
                        'size': openapi.Schema(type=openapi.TYPE_STRING, example='L'),
                        'quantity': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
                    }
                ),
            ),
            'status': openapi.Schema(type=openapi.TYPE_STRING, example='approved'),
            'created_at': openapi.Schema(type=openapi.TYPE_STRING, example='2025-01-05T19:50:28.834823Z'),
            'updated_at': openapi.Schema(type=openapi.TYPE_STRING, example='2025-01-05T20:42:11.734471Z'),
        }
    )

    return swagger_auto_schema(
        method='GET',
        operation_description="Retrieve details of a single agent by ID.",
        responses={
            200: openapi.Response(
                description="Successfully retrieved the agent's details",
                schema=agent_schema,
            ),
            404: openapi.Response(
                description="Agent not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING, example='agents does not exist'),
                    }
                ),
            ),
        }
    )


def patch_agent_schema():
    """
    Returns the OpenAPI schema for updating an agent's information.
    """
    # Request body schema (optional fields)
    request_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'photo_identity': openapi.Schema(type=openapi.TYPE_STRING, example='path/to/alice_photo_identity.jpg'),
            'nss': openapi.Schema(type=openapi.TYPE_STRING, example='98765432109876'),
            'card_number_pro': openapi.Schema(type=openapi.TYPE_STRING, example='PRO-567890'),
            'security_card_photo': openapi.Schema(type=openapi.TYPE_STRING, example='path/to/security_card_photo_alice.jpg'),
            'nub': openapi.Schema(type=openapi.TYPE_STRING, example='67890'),
            'agent_fonction': openapi.Schema(type=openapi.TYPE_STRING, example='securite'),
            'driver_licence_type': openapi.Schema(type=openapi.TYPE_STRING, example='A'),
            'emergency_contact_name': openapi.Schema(type=openapi.TYPE_STRING, example='Bob Smith'),
            'emergency_contact_phone': openapi.Schema(type=openapi.TYPE_STRING, example='+123456789'),
            'diplomes': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                'diploma_name': openapi.Schema(type=openapi.TYPE_STRING, example='Bachelor of Security'),
                'year': openapi.Schema(type=openapi.TYPE_STRING, example='2020')
            })),
            'experience': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                'job_title': openapi.Schema(type=openapi.TYPE_STRING, example='Security Specialist'),
                'company': openapi.Schema(type=openapi.TYPE_STRING, example='SecureCorp Ltd.'),
                'duration': openapi.Schema(type=openapi.TYPE_STRING, example='3 years')
            })),
            'tenues': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                'type': openapi.Schema(type=openapi.TYPE_STRING, example='Tactical Vest'),
                'size': openapi.Schema(type=openapi.TYPE_STRING, example='L'),
                'quantity': openapi.Schema(type=openapi.TYPE_INTEGER, example=1)
            })),
        }
    )

    # Response schema for 201 Created
    response_schema_201 = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=5),
            'user': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=8),
                'first_name': openapi.Schema(type=openapi.TYPE_STRING, example='Alice'),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING, example='Smith'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, example='alice.smith@example.com'),
                'phone': openapi.Schema(type=openapi.TYPE_STRING, example='+987654321'),
                'address': openapi.Schema(type=openapi.TYPE_STRING, example='456 Elm Street, Metropolis')
            }),
            'photo_identity': openapi.Schema(type=openapi.TYPE_STRING, example='path/to/alice_photo_identity.jpg'),
            'nss': openapi.Schema(type=openapi.TYPE_STRING, example='98765432109876'),
            'card_number_pro': openapi.Schema(type=openapi.TYPE_STRING, example='PRO-567890'),
            'security_card_photo': openapi.Schema(type=openapi.TYPE_STRING, example='path/to/security_card_photo_alice.jpg'),
            'nub': openapi.Schema(type=openapi.TYPE_STRING, example='67890'),
            'agent_fonction': openapi.Schema(type=openapi.TYPE_STRING, example='securite'),
            'driver_licence_type': openapi.Schema(type=openapi.TYPE_STRING, example='A'),
            'emergency_contact_name': openapi.Schema(type=openapi.TYPE_STRING, example='Bob Smith'),
            'emergency_contact_phone': openapi.Schema(type=openapi.TYPE_STRING, example='+123456789'),
            'diplomes': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                'diploma_name': openapi.Schema(type=openapi.TYPE_STRING, example='Bachelor of Security'),
                'year': openapi.Schema(type=openapi.TYPE_STRING, example='2020')
            })),
            'experience': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                'job_title': openapi.Schema(type=openapi.TYPE_STRING, example='Security Specialist'),
                'company': openapi.Schema(type=openapi.TYPE_STRING, example='SecureCorp Ltd.'),
                'duration': openapi.Schema(type=openapi.TYPE_STRING, example='3 years')
            })),
            'tenues': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                'type': openapi.Schema(type=openapi.TYPE_STRING, example='Tactical Vest'),
                'size': openapi.Schema(type=openapi.TYPE_STRING, example='L'),
                'quantity': openapi.Schema(type=openapi.TYPE_INTEGER, example=1)
            })),
            'status': openapi.Schema(type=openapi.TYPE_STRING, example='approved'),
            'created_at': openapi.Schema(type=openapi.TYPE_STRING, example='2025-01-05T19:50:28.834823Z'),
            'updated_at': openapi.Schema(type=openapi.TYPE_STRING, example='2025-01-05T20:42:11.734471Z')
        }
    )

    # Response schema for 404 Not Found
    response_schema_404 = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={}
    )

    return swagger_auto_schema(
        method='PATCH',
        operation_description="Update agent details by ID. Fields are optional.",
        request_body=request_body,
        responses={
            201: openapi.Response(
                description="Agent updated successfully.",
                schema=response_schema_201,
            ),
            404: openapi.Response(
                description="Agent not found.",
                schema=response_schema_404,
            ),
        }
    )




def delete_agent_schema():
    """
    Returns the OpenAPI schema for deleting an agent.
    """
    # Request body is not needed for DELETE requests, but it's still good to document that this endpoint
    # doesn't require any body content.

    # Response schema for 204 No Content (Success)
    response_schema_204 = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'message': openapi.Schema(type=openapi.TYPE_STRING, example='inscription deleted successfully')
        }
    )

    # Response schema for 404 Not Found (Agent not found)
    response_schema_404 = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'error': openapi.Schema(type=openapi.TYPE_STRING, example='agents does exist')
        }
    )

    return swagger_auto_schema(
        method='DELETE',
        operation_description="Delete an agent by ID.",
        responses={
            204: openapi.Response(
                description="Agent deleted successfully.",
                schema=response_schema_204,
            ),
            404: openapi.Response(
                description="Agent not found. The agent does not exist.",
                schema=response_schema_404,
            ),
        }
    )
