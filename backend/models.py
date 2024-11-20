from django.db import models
from django.utils import formats
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

# Create your models here.
class User(AbstractUser):
	pass

	def __str__(self):
		return f"{self.first_name} {self.last_name}"

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	mykad = models.CharField(max_length=100, null=True, blank=True)
	mobile = models.CharField(max_length=15, null=True, blank=True)
	address_one = models.CharField(max_length=100, null=True, blank=True)
	address_two = models.CharField(max_length=100, null=True, blank=True)
	address_three = models.CharField(max_length=100, null=True, blank=True)
	postcode = models.CharField(max_length=10, null=True, blank=True)
	city = models.CharField(max_length=100, null=True, blank=True)
	state = models.CharField(max_length=100, null=True, blank=True)
	country = models.CharField(max_length=100, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.user.first_name} {self.user.last_name}"

# Create a user Profile by default when user signs up
def create_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)
		instance.userprofile.save()    

# Automate the profile thing
post_save.connect(create_profile, sender=User)

# Doctor
class Doctor(models.Model):
	name = models.CharField(max_length=100)
	specialization = models.CharField(max_length=100)
	email = models.EmailField()
	phone = models.CharField(max_length=15)

	def __str__(self):
		return self.name

# Doctor Availability
class DoctorAvailability(models.Model):
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	date = models.DateField()
	start_time = models.TimeField()
	end_time = models.TimeField()

	def __str__(self):
		return f"Dr. {self.doctor.name} available on {self.date}"

# Patient
class Patient(models.Model):
	name = models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address = models.TextField()

	def __str__(self):
		return self.name

class Appointment(models.Model):
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	remarks = models.TextField(default='')
	date = models.DateField()
	time = models.TimeField()
	status = models.CharField(max_length=20, choices=(
		('Pending', 'Pending'),
		('Confirmed', 'Confirmed'),
		('Cancelled', 'Cancelled'),
	), default='Pending')

	def __str__(self):
		return f"Appointment with Dr. {self.doctor.name} on {formats.date_format(self.date, 'd/M/Y')} at {formats.time_format(self.time, 'H:i A')}"

class Payment(models.Model):
	appointment = models.OneToOneField('Appointment', on_delete=models.CASCADE)
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	status = models.CharField(max_length=20, choices=(
		('Pending', 'Pending'),
		('Completed', 'Completed'),
		('Failed', 'Failed'),
	), default='Pending')
	payment_date = models.DateTimeField(auto_now_add=True)
	proof_of_payment = models.FileField(upload_to='payment_proofs/', blank=True, null=True)  # New field

	def __str__(self):
		return f"Payment for {self.appointment}"
