from django.db import models


class Advertisement(models.Model):
    """
    Represents a real estate advertisement
    """

    bienici_id = models.CharField(null=True, max_length=255, unique=True)
    condominium_fees = models.FloatField(null=True, default=None)
    department = models.CharField(null=False)
    city = models.CharField(null=False)
    zipcode = models.CharField(null=False)
