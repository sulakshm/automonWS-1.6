from django.db import models
from django.contrib.auth.models import User, Group
from django.utils import timezone
import datetime

# Create your models here.
class GpsNode(models.Model):
    """ A GpsNode identifies uniquely an entity belonging to an User, that 
        publishes gps metrics.
    """
    ident = models.CharField(max_length=200) # primary identifier, IMEI
    user = models.ForeignKey(User)
    last_active = models.DateTimeField('last active')

    def recently_active(self):
        """ returns True if the last active timestamp was within an hour """
        now = timezone.now()
        return (now - datetime.timedelta(hours=1)) <= self.last_active <= now 

    def __unicode__(self):
        return 'GpsNode#'+self.ident

class GpsNodeMetrics(models.Model):
    """ This class defines all metrics attributes possible from a GpsNode """
    node = models.ForeignKey(GpsNode)
    latitude = models.DecimalField(max_digits=14, decimal_places=12)
    longitude = models.DecimalField(max_digits=14, decimal_places=12)
    accuracy = models.FloatField()
    speed = models.FloatField() 
    altitude = models.FloatField()
    nsecTimestamp = models.BigIntegerField()
    bearing = models.FloatField()
    vin = models.CharField(max_length=24)
    vinLastCached = models.BooleanField(default=False)

    def __unicode__(self):
        return 'GpsMetrics@'+str(self.nsecTimestamp)

    def get_all_fields(self):
        fields = []
        for f in self._meta.fields:
            fname = f.name
            try:
                value = getattr(self, fname)
            except User.DoesNotExist:
                value = None
            fields.append({'label' : f.verbose_name,
                           'name' : f.name,
                           'value' : value })
        return fields
