from django.db import models


class Customer(models.Model):
    customer_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    social_media = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        return f"The customer {self.name} has been created successfully. Customer_id: {self.customer_id}"


class Interaction(models.Model):
    CHANNEL_CHOICES = [
        ("phone", "Phone"),
        ("sms", "SMS"),
        ("email", "Email"),
        ("letter", "Letter"),
        ("social_media", "Social Media"),
    ]

    DIRECTION_CHOICES = [
        ("inbound", "Inbound"),
        ("outbound", "Outbound"),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    channel = models.CharField(max_length=15, choices=CHANNEL_CHOICES)
    direction = models.CharField(max_length=10, choices=DIRECTION_CHOICES)
    interaction_date = models.DateField(auto_now_add=True)
    summary = models.TextField()
