from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status as drf_status
from rest_framework.pagination import LimitOffsetPagination
from .models import AgentProfile
from .serializers import AgentListInscriptionSerializer,AgentDetailSerializer
from .docstrings.list_agents_doc import agent_list_schema
from .docstrings.agent_by_id_doc import agent_detail_schema,patch_agent_schema,delete_agent_schema
from .pagination import CustomPageNumberPagination
from rest_framework.views import APIView
from rest_framework import mixins ,generics
from drf_spectacular.utils import extend_schema,OpenApiParameter,OpenApiTypes
import  django_filters
from rest_framework import filters
class AgentListFilter(django_filters.FilterSet):
    agent_function = django_filters.CharFilter(field_name="agent_function",lookup_expr='iexact')
    ville = django_filters.CharFilter(field_name="ville",lookup_expr='iregex')
    status = django_filters.CharFilter(field_name="status",lookup_expr='exact')

    class Meta:
        model = AgentProfile
        fields = ['agent_function',"ville","status"]
class AgentList(generics.ListAPIView): 
    model = AgentProfile
    serializer_class = AgentDetailSerializer
   
    pagination_class= CustomPageNumberPagination
    queryset=AgentProfile.objects.all()
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.SearchFilter)
    filterset_class = AgentListFilter
   
    search_fields = ['^user__first_name','^user__last_name','^user__email']
   

    @extend_schema(
    summary="List Agents",
       
    description="Retrieve a paginated list of agents with filtering and search capabilities.",
    responses={200: AgentDetailSerializer(many=True)}
)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)




  


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