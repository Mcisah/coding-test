import json
from graphene_django.utils.testing import GraphQLTestCase
from codingtest.schema import schema


class CalculateTestCase(GraphQLTestCase):
    # inject the test case's schema and mount url
    GRAPHQL_URL = "/graphiql/"
    GRAPHQL_SCHEMA = schema

    def test_query(self):
        response = self.query(
            '''
            query Calculate($input:RequiredInput!){
                calculatePrice(arg:$input)  
            }
            ''',
            op_name='calculatePrice',
            input_data={'type': 'sell', 'margin': 0.2, 'exchangeRate': 0.0028}
        )
        content = json.loads(response.content)
        print(content)

        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)
