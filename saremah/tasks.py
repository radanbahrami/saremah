from celery import shared_task
from .models import Subscription
from datetime import date, timedelta

@shared_task
def notify_upcoming_renewals():
    today = date.today()
    for sub in Subscription.objects.all():
        notify_date = sub.renewal_date - timedelta(days=sub.notification_days_before)
        if today == notify_date:
            # Use actual email sending logic here in production
            print(f"NOTIFICATION: Your {sub.name} subscription renews on {sub.renewal_date}. User: {sub.user.email}")
