from django.db import models


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.country_name or "Unnamed Country"

    class Meta:
        managed = False
        db_table = 'countries'


class Vacation(models.Model):
    vacation_id = models.AutoField(primary_key=True)
    vacation_name = models.CharField(max_length=100, blank=True, null=True)
    vacation_description = models.CharField(
        max_length=2000, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    vacation_img = models.ImageField(
        upload_to='vacation_images/', blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    likes = models.IntegerField(blank=True, null=True)
    vacation_days = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vacations'


class Like(models.Model):
    like_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    vacation = models.ForeignKey(Vacation, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'likes'
