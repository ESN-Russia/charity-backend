from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CharityLot(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True)
    seller = models.TextField(blank=True)
    image_url = models.TextField(blank=True)

    minimum_bid = models.IntegerField(default=0)
    start_time = models.DateTimeField(blank=True)
    end_time = models.DateTimeField(blank=True)

    def __str__(self):
        return str(self.name)


class CharityBid(models.Model):
    user = models.ForeignKey(User, related_name="bids", on_delete=None)
    charity_lot = models.ForeignKey(CharityLot, related_name="bids", on_delete=None)

    bid = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} bid {} RUB on {}".format(self.user, self.bid, self.charity_lot)
