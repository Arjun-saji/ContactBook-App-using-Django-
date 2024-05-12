from django.db import models


class Contact(models.Model):
	contact_name=models.CharField(max_length=200)
	email=models.EmailField(max_length=100)
	phone=models.CharField(max_length=200,default="")


	def __str__(self):
		return self.contact_name

