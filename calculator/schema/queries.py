import graphene
import requests
from calculator.schema.typeDefs import RequiredInput


class Query(graphene.ObjectType):
    calculatePrice = graphene.Field(graphene.String, arg=RequiredInput(required=True))

    @staticmethod
    def resolve_calculatePrice(self, info, arg):
        # get input data
        type = arg.get('type')
        margin = arg.get('margin')
        exchangeRate = arg.get('exchangeRate')

        # make api call
        url = 'https://api.coindesk.com/v1/bpi/currentprice/USD.json'
        request = requests.get(url)

        if request.status_code != 200:
            return "An Error Occurred: Request Failed"

        result = request.json()
        currentPrice = result['data']['bpi']['USD']['rate_float']

        if type is 'sell':
            val = (currentPrice - margin)
        else:
            val = (currentPrice + margin)

        finalVal = (exchangeRate * val)

        # return output data
        return "NGN"+str(finalVal)