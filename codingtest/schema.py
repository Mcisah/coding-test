# main schema
import graphene
from calculator.schema import queries


class Query(queries.Query):
    pass


# noinspection PyTypeChecker
schema = graphene.Schema(query=Query)
