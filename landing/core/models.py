from django.db import models


class UsersInfo(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "users_info"

    def __str__(self):
        return f"{self.name} <{self.email}>"


class UsersCounter(models.Model):
    count = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "users_counter"

    def __str__(self):
        return f"Users counter: {self.count}"
