from django.db import models


class Advertisement(models.Model):
    """
    Represents a real estate advertisement
    """

    bienici_id = models.CharField(null=True, max_length=255)
    condominium_fees = models.FloatField(null=False)
    department = models.CharField(default=None)
    city = models.CharField(null=False)
    zipcode = models.CharField(null=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.department:
            self.department = self.zipcode[0:2]
