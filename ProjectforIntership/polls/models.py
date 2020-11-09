from django.db import models

from user.models import User


class Ad(models.Model):

    CONDITION_CHOICES = [
        ('used', 'Used'),
        ('new', 'New'),
    ]

    COLOR_CHOICES = [
        ('white', 'White'),
        ('yellow', 'Yellow'),
        ('green', 'Green'),
        ('gold', 'Gold'),
        ('red', 'Red'),
        ('silver', 'Silver'),
        ('pink', 'Pink'),
        ('gray', 'Gray'),
        ('blue', 'Blue'),
        ('purple', 'Purple'),
        ('black', 'Black'),
        ('other', 'Other'),

    ]

    PRODUCT_CHOICES = [
        ('phone', 'Phone'),
        ('laptop', 'Laptop'),
        ('tablet', 'Tablet'),
        ('headphones', 'Headphones'),
        ('monitor', 'Monitor'),
        ('component', 'Component'),
        ('ga', 'Gaming Accessories'),
    ]

    product_type = models.CharField(max_length=100, verbose_name='Type', choices=PRODUCT_CHOICES)
    model = models.CharField(max_length=200, verbose_name='Model')
    name = models.CharField(max_length=250, verbose_name='Name')
    color = models.CharField(max_length=100, verbose_name='Color', choices=COLOR_CHOICES)
    condition = models.CharField(max_length=100, verbose_name='Condition', choices=CONDITION_CHOICES)
    description = models.TextField(max_length=10000, verbose_name='Description')
    price = models.IntegerField(default=0, verbose_name='Price')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    place = models.CharField(max_length=155, verbose_name='Place')

    def __str__(self):
        return '%s, %s, %s' % (self.name, self.model, self.color)


class AdPhoto(models.Model):
    url = models.ImageField(max_length=255, verbose_name='URL')
    product_id = models.ForeignKey(Ad, on_delete=models.CASCADE)

    def __str__(self):
        return 'Its photo for %s' % (self.product_id)