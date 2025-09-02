import graphene
from graphene_django import DjangoObjectType
from .models import Subscription
from django.contrib.auth.models import User

class SubscriptionType(DjangoObjectType):
    class Meta:
        model = Subscription

class Query(graphene.ObjectType):
    subscriptions = graphene.List(SubscriptionType)

    def resolve_subscriptions(self, info):
        return Subscription.objects.all()

class CreateSubscription(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        cost = graphene.Decimal(required=True)
        renewal_date = graphene.Date(required=True)
        notification_days_before = graphene.Int()
        user_id = graphene.ID(required=True)

    subscription = graphene.Field(SubscriptionType)

    def mutate(self, info, name, cost, renewal_date, notification_days_before=7, user_id=None):
        user = User.objects.get(pk=user_id)
        subscription = Subscription(
            user=user,
            name=name,
            cost=cost,
            renewal_date=renewal_date,
            notification_days_before=notification_days_before
        )
        subscription.save()
        return CreateSubscription(subscription=subscription)

class Mutation(graphene.ObjectType):
    create_subscription = CreateSubscription.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
