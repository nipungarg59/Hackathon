from __future__ import unicode_literals

from django.db import models
from datetime import datetime


class UserHistory(models.Model):
	userid = models.CharField(max_length=200)
	radius_mean = models.FloatField(default=0.0)
	area_mean = models.FloatField(default=0.0)
	concave_points_mean = models.FloatField(default=0.0)
	concavity_mean = models.FloatField(default=0.0)
	perimeter_mean = models.FloatField(default=0.0)
	response = models.FloatField(default=0.0)

	def __unicode__(self):
		return self.userid
		