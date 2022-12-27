from django.http import HttpResponse


class StripeWH_Handler:
    """
    Handle Stripe webhooks
    Credits to Boutique Ado Walkthrough
    """
    def __init__(self, event):
        self.request = request

    def handle_event(self, event):
        """
        Handle a unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeded webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.succeded webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)
