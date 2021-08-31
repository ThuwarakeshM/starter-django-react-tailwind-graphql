import graphene


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi from Thuwarakesh!")


schema = graphene.Schema(query=Query)
