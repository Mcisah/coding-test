import graphene


class GenderEnum(graphene.Enum):
    sell = "sell"
    buy = "buy"


class RequiredInput(graphene.InputObjectType):
    type = GenderEnum()
    margin = graphene.String()
    exchangeRate = graphene.String()
