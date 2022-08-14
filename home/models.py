from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class InvestorUpdate(models.Model):

    """Investor Update database fields"""

    title = models.CharField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now = True)
    image = models.ImageField(upload_to='static/images/investor_images', null=True, blank=True)
    image_alt = models.CharField(max_length=30, blank='True')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title