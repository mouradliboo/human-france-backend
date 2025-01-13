from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status as drf_status
from rest_framework.pagination import LimitOffsetPagination
from .models import AgentProfile
from .serializers import AgentListInscriptionSerializer,AgentDetailSerializer
from .docstrings.list_agents_doc import agent_list_schema
from .docstrings.agent_by_id_doc import agent_detail_schema,patch_agent_schema,delete_agent_schema

class MyLimitOffsetPagination(LimitOffsetPagination):
    
  default_limit=9
@agent_list_schema()
@api_view(['GET'])
def list_agents(request):
    try:
        # Get the `status` query parameter
        status_param = request.query_params.get('status', 'approved')

 
            # Filter users based on the provided status
        agents = AgentProfile.objects.filter(status=status_param)
        
        print(len(agents))
        
        
        
        paginator = MyLimitOffsetPagination()
    
    # Paginate the queryset
        paginated_queryset = paginator.paginate_queryset(agents, request)
        print(paginated_queryset)
    
    # Serialize the paginated data

    
        serializer=AgentListInscriptionSerializer(paginated_queryset,many=True)
   

        # Serialize the filtered users
       
        return Response(serializer.data, status=drf_status.HTTP_200_OK)

    except Exception as e:
        # Handle unexpected errors
        return Response({"error": str(e)}, status=drf_status.HTTP_400_BAD_REQUEST)
    


@delete_agent_schema()
@patch_agent_schema()
@agent_detail_schema()
@api_view(['GET','PATCH','DELETE'])
def agentDetail(request,pk):
 if request.method =='GET':
    try:
        agent = AgentProfile.objects.get(id=pk)
        print(agent)
        serializer = AgentDetailSerializer(agent)
        return Response(serializer.data)
    except AgentProfile.DoesNotExist:
        return Response({},status=drf_status.HTTP_404_NOT_FOUND)
 if request.method =='PATCH':

    try:
        agent = AgentProfile.objects.get(id=pk)
        serializer = AgentDetailSerializer(agent, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=drf_status.HTTP_400_BAD_REQUEST)
    except AgentProfile.DoesNotExist:
        return Response({"error":"agents does exist"},status=drf_status.HTTP_404_NOT_FOUND)
 if request.method =='DELETE':
        try:
            agent = AgentProfile.objects.get(id=pk)
            agent.delete()
            return Response({"message":"inscription deleted succussfully"},status=drf_status.HTTP_204_NO_CONTENT)
        except AgentProfile.DoesNotExist:
            return Response({"error":"agents does exist"},status=drf_status.HTTP_404_NOT_FOUND)