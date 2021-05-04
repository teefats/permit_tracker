from django.db import models

# Create your models here.
class Permit(models.Model):
    name = models.CharField(max_length=50, default=None)
    permit_type = models.CharField(max_length=100)
    permit_conditions = models.TextField()
    permit_authority = models.CharField(max_length=200)
    list_sites = (
        ('Gay', 'Gaydon'),
        ('W1', 'Wellesbourne Unit 1'),
        ('W2', 'Wellesbourne Unit 2'),
        ('SA', 'St. Athan'),
        ('WO', 'Wolverton Mill'),
        ('NP', 'Newport Pagnell'),


    )
    site = models.CharField(max_length=3, choices=list_sites)
    area = models.CharField(max_length=200)
    comments = models.TextField()
    issue_date = models.DateField()
    expiration_date = models.DateField()

    def __str__(self):
        return self.name
