import graphene
import requests
import graphql

from calculator.schema.typeDefs import RequiredInput


class Query(graphene.ObjectType):
    calculatePrice = graphene.Field(graphene.Float, arg=RequiredInput(required=True))

    @staticmethod
    def resolve_calculatePrice(self, info, arg):
        # get input data
        type = arg.get('type')
        margin = arg.get('margin')
        exchangeRate = arg.get('exchangeRate')

        # make api call
        url = 'https://api.coindesk.com/v1/bpi/currentprice/USD.json'
        try:
            request = requests.get(url)
        except:
            raise graphql.GraphQLError('request failed')

        if request.status_code is not 200:
            raise graphql.GraphQLError('request failed')

        result = request.json()
        currentPrice = result['bpi']['USD']['rate_float']

        if type is 'sell':
            val = currentPrice - (margin / 100)
        else:
            val = currentPrice + (margin / 100)

        return exchangeRate * val
