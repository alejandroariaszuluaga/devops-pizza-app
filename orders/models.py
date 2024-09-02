from django.db import models

class Order(models.Model):
    PIZZA_CHOICES = [
        ('Margherita', 'Margherita'),
        ('Pepperoni', 'Pepperoni'),
        ('Vegetarian', 'Vegetarian'),
    ]

    pizza_type = models.CharField(max_length=20, choices=PIZZA_CHOICES)
    comments = models.TextField(blank=True)

    def __str__(self):
        return f"{self.pizza_type} - {self.comments[:20]}"
