from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models as gis_models
from django.db.models import Manager as GeoManager


# Create your models here.
class Incidence(models.Model):
	title = models.CharField(max_length=20)
	description = models.TextField(max_length=250, null=True)
	date_reported = models.DateField(auto_now_add=True)
	location = gis_models.PointField(srid=4326)
	objects = GeoManager()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural =" Incidences"

class County(models.Model):
	counties = models.CharField(max_length=25)
	codes = models.IntegerField()
	cty_code = models.CharField(max_length=24)
	dis = models.IntegerField()
	geom = gis_models.MultiPolygonField(srid=4326)
	objects = GeoManager()

	def __str__(self):
		return self.counties

	class Meta:
		verbose_name_plural = 'Counties'