from datetime import date, timedelta

from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse

from .models import Customer, Interaction
from .forms.customer_form import CustomerForm


class HomeView(View):
    def get(self, request: HttpRequest):
        customers = Customer.objects.all()
        context = {"customers": customers}
        return render(request, "index.html", context)


class CreateCustomerView(View):
    def get(self, request: HttpRequest):
        form = CustomerForm()
        return render(request, "add.html", {"form": form})

    def post(self, request: HttpRequest):
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            context = {"msg": "Customer created successfully"}
            return render(request, "add.html", context)


class ClearCookiesView(View):
    def get(self, request: HttpRequest):
        response = HttpResponse("All cookies cleared successfully")
        for key in request.COOKIES:
            response.delete_cookie(key)
        return response


class SummaryView(View):
    def get(self, request: HttpRequest):
        thirdy_days_ago = date.today() - timedelta(days=30)
        interactions = Interaction.objects.filter(interaction_date__gte=thirdy_days_ago)

        count = len(interactions)
        interactions = interactions.values("values", "direction").annotate(
            count=count("channel")
        )
        context = {"interactions": interactions, "count": count}
        return render(request, "summary.html", context)


class InteractView(View):
    def post(self, request: HttpRequest, customer_id: int):
        channels = Interaction.CHANNEL_CHOICES
        directions = Interaction.DIRECTION_CHOICES
        context = {"channels": channels, "directions": directions}

        customer = Customer.objects.get(id=customer_id)
        channel = request.post["channel"]
        direction = request.post["direction"]
        summary = request.post["summary"]
        interaction = Interaction.objects.create(
            customer=customer, channel=channel, direction=direction, summary=summary
        )
        interaction.save()
        context["msg"] = "User created successfully"

        return render(request, "interact.html", context)
