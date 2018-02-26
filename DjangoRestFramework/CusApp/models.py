from django.db import models
from collections import namedtuple

from django.db import connection

# Create your Table here.
class customers(models.Model):
    CustomerID = models.TextField()
    CompanyName = models.TextField()
    ContactName = models.TextField()
    ContactTitle = models.TextField()
    Address = models.TextField()
    City = models.TextField()
    Region = models.TextField()
    PostalCode = models.TextField()
    Country = models.TextField()
    Phone = models.TextField()
    Fax = models.TextField()
    Email = models.EmailField()
    PaymentTerm = models.TextField()

    class Meta:
        db_table = "customers"
        app_label = "customers" # If "CusApp" doesn't write in "settings/INSTALLED_APPS", "app_label" should add here.


# query by CompanyName with RawSQL(Only allow GET, HEAD, OPTIONS)
def fun_raw_sql_query(**kwargs):
    CompanyQuery = kwargs.get('Company')
    if CompanyQuery:
        result = customers.objects.raw('SELECT * FROM customers WHERE CompanyName = %s', [CompanyQuery])
    else:
        result = customers.objects.raw('SELECT * FROM customers')
    return result


def namedtuplefetchall(cursor):
    # Return all rows from a cursor as a namedtuple
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


# update CompanyName with RawSQL
def fun_sql_cursor_update(**kwargs):
    CompanyName = kwargs.get('Company')
    pk = kwargs.get('pk')

    '''
    Note that if you want to include literal percent signs in the query, 
    you have to double them in the case you are passing parameters:
    '''
    with connection.cursor() as cursor:
        cursor.execute("UPDATE customers SET CompanyName = %s WHERE id = %s", [CompanyName, pk])
        cursor.execute("SELECT * FROM customers WHERE id = %s", [pk])
        # result = cursor.fetchone()
        result = namedtuplefetchall(cursor)
    result = [
        {
            'id': r.id,
            'CustomerID': r.CustomerID,
            'CompanyName': r.CompanyName,
            'ContactName': r.ContactName,
            'ContactTitle': r.ContactTitle,
            'Address': r.Address,
            'City': r.City,
            'Region': r.Region,
            'PostalCode': r.PostalCode,
            'Country': r.Country,
            'Phone': r.Phone,
            'Fax': r.Fax,
            'Email': r.Email,
            'PaymentTerm': r.PaymentTerm,
        }
        for r in result
    ]
    return result        