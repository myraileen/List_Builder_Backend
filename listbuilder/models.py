from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=100)
    status = models.CharField(max_length=200)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, default='', null=True, blank=True)
    email_address = models.CharField(max_length=100, default='', null=True, blank=True)
    photo_url = models.TextField(default='', null=True, blank=True)
    create_ts = models.DateTimeField(auto_now_add=True)
    update_ts = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_id

class List(models.Model):
    title = models.CharField(max_length=200)
    list_type = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    image_url = models.TextField(default='', null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lists')
    create_ts = models.DateTimeField(auto_now_add=True)
    update_ts = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title