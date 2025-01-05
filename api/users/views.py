from .models import AgentProfile
from rest_framework.response import Response
from .serializers import AgentListInscriptionSerializer
from rest_framework.decorators import api_view
@api_view(['GET'])

def listInscription(request):
    agents_panding = AgentProfile.objects.filter(status="pending")
    serializer = AgentListInscriptionSerializer(agents_panding, many=True)
    return Response(serializer.data, status=200)
@api_view(['GET'])
def listDesAgents(request):
    agents_panding = AgentProfile.objects.filter(status="approved")
    serializer = AgentListInscriptionSerializer(agents_panding, many=True)
    return Response(serializer.data, status=200)
    # if request.method == 'GET':
    #     agents = Agent.objects.all()
    #     serializer = AgentSerializer(agents, many=True)
    #     return JsonResponse(serializer.data, safe=False)
    # return JsonResponse(serializer.errors, status=400)
    return Response({"message":"Hello world"}, status=200)