from rest_framework import serializers
from CusApp.models import customers

class ToUpperCaseCharField(serializers.CharField):
    def to_representation(self, value):
        return value.upper()


class CusSerializer(serializers.ModelSerializer):
    CompanyName = ToUpperCaseCharField()    # Make CompanyName Capital
    
    class Meta:
        model = customers
        # fields = '__all__'    # alternative for below line
        fields = ('id', 'CustomerID', 'CompanyName', 'ContactName', 'ContactTitle', 'Address', 'City', 'Region', 'PostalCode', 'Country', 'Phone', 'Fax', 'Email', 'PaymentTerm')
 
# if Version exists, using CusSerializerV1 to serialize
class CusSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = customers
        fields = ('id', 'CustomerID', 'CompanyName', 'ContactName', 'ContactTitle', 'Phone', 'Fax', 'Email', 'PaymentTerm')
               