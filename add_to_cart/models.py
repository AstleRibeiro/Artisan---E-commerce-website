from django.db import models


# class Orders(models.Model):
#     order_id = models.AutoField(primary_key=True)
#     items_json = models.CharField(max_length=5000)
#     amount = models.IntegerField(default=0)
#     first_name = models.CharField(max_length=90)
#     last_name = models.CharField(max_length=111)
#     email = models.CharField(max_length=111)
#     address = models.CharField(max_length=111)
#     city = models.CharField(max_length=111)
#     state = models.CharField(max_length=111)
#     phone = models.IntegerField(default=0)
#     zip_code = models.CharField(max_length=111)
#
#     def __str__(self):
#         return str(self.email)


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.CharField(max_length=1000, default='')
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.order_id)


class Order(models.Model):
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=111)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    phone = models.IntegerField(default=0)
    zip_code = models.CharField(max_length=111)
    order_id = models.CharField(max_length=1000, primary_key=True)
    razorpay_payment_id = models.CharField(max_length=1000, blank=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return str(self.email)
