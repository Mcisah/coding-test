import graphene


class GenderEnum(graphene.Enum):
    sell = "sell"
    buy = "buy"

    class Meta:
        description = 'This can either be buy or sell, nothing else.'


class RequiredInput(graphene.InputObjectType):
    type = GenderEnum()
    margin = graphene.Float(description='This is a percentage that will be used in a calculation.')
    exchangeRate = graphene.Float(description='A custom USD/NGN exchange rate.')
