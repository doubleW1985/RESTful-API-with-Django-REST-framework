from django.shortcuts import get_object_or_404

from CusApp.models import customers
from CusApp.models import fun_raw_sql_query, fun_sql_cursor_update
from CusApp.serializers import CusSerializer, CusSerializerV1

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import detail_route, list_route 

# Create your views here.
class CusViewSet(viewsets.ModelViewSet):
    queryset = customers.objects.all()
    serializer_class = CusSerializer
    permission_classes = (IsAuthenticated,) # Add Authentication
    parser_classes = (JSONParser,)  # Content-Type only can be application/json for this ViewSet
    
    # /api/CusApp/raw_sql_query/
    # query by CompanyName with RawSQL(Only allow GET, HEAD, OPTIONS)
    @list_route(methods=['get'])
    def raw_sql_query(self, request):
        CompanyQuery = request.query_params.get('CompanyQuery', None)
        ResultQuery = fun_raw_sql_query(Company=CompanyQuery)
        serializer = CusSerializer(ResultQuery, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
     
    # /api/CusApp/{pk}/detail_part/
    # query part of customer data by PK(Only allow GET, HEAD, OPTIONS)
    @detail_route(methods=['get'], url_path='detail_part')
    def detail(self, request, pk=None):
        customer = get_object_or_404(customers, pk=pk)
        result = {
            'id': customer.id,
            'CustomerID': customer.CustomerID,
            'CompanyName': customer.CompanyName,
            'ContactName': customer.ContactName,
            'Phone': customer.Phone,
            'Fax': customer.Fax,
            'Email': customer.Email,
            'PaymentTerm': customer.PaymentTerm,
        }
        return Response(result, status=status.HTTP_200_OK)  
    
    # /api/CusApp/all_company/
    # query all company(Only allow GET, HEAD, OPTIONS)
    @list_route(methods=['get'])
    def all_company(self, request):
        all_customer = customers.objects.values_list('CompanyName', flat=True).distinct()
        return Response(all_customer, status=status.HTTP_200_OK)  
    
    # /api/CusApp/{pk}/sql_cursor_update/
    # update CompanyName with RawSQL
    @detail_route(methods=['put'])
    def sql_cursor_update(self, request, pk=None):
        CompanyUpdate = request.data.get('CompanyUpdate', None)
        if CompanyUpdate:
            ResultUpdate = fun_sql_cursor_update(Company=CompanyUpdate, pk=pk)
            return Response(ResultUpdate, status=status.HTTP_200_OK)

    # /api/CusApp/version_api/
    # if Version exists, using CusSerializerV1 to serialize
    @list_route(methods=['get'])
    def version_api(self, request):
        querysetV1 = customers.objects.all()
        if self.request.version == '1.0':
            serializer = CusSerializerV1(querysetV1, many=True)
        else:
            serializer = CusSerializer(querysetV1, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)