from django.db import models

TYPE_CHOICE=(
    ('TWO WHEELER','TWO WHEELER'),
    ('FOUR WHEELER','FOUR WHEELER'),
)

STATUS_CHOICE=(
    ('F','FULL'),
    ('A','AVAILABLE'),
)
# Create your models here.
class locationclass(models.Model):
    location_id=models.IntegerField(primary_key=True)
    location_name=models.CharField(max_length=150)
    slot_type=models.CharField(max_length=150,choices=TYPE_CHOICE)
    image=models.ImageField(upload_to="media/parking")
    slot_status=models.CharField(max_length=150,choices=STATUS_CHOICE)
    
    
    def __str__(self):
        return self.location_name
    
    class Meta:
      verbose_name_plural = "Locations"