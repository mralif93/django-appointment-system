from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin
from .models import User, UserProfile, Doctor, DoctorAvailability, Patient, Appointment, Payment

# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
  list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active')
  list_filter = ('is_staff', 'is_active')
  fieldsets = (
    (None, {'fields': ('username', 'first_name', 'last_name', 'email', 'password')}),
    ('Permissions', {'fields': ('is_staff', 'is_active')}),
  )
  add_fieldsets = (
    (None, {
      'classes': ('wide',),
      'fields': ('username', 'email', 'password1', 'password2'),
    }),
  )
  search_fields = ('username', 'email')
  ordering = ('username',)
  filter_horizontal = ()


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
  pass

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
  list_display = ('name', 'specialization', 'email', 'phone')

@admin.register(DoctorAvailability)
class DoctorAvailabilityAdmin(admin.ModelAdmin):
  list_display = ('doctor', 'date', 'start_time', 'end_time')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
  list_display = ('name', 'phone', 'address')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
  list_display = ('doctor', 'patient', 'date', 'time', 'status')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
  list_display = ('appointment', 'amount', 'status', 'payment_date', 'proof_of_payment_link')

  def proof_of_payment_link(self, obj):
    if obj.proof_of_payment:
      return format_html('<a href="{}" target="_blank">View Proof</a>', obj.proof_of_payment.url)
    return "No Proof Uploaded"
  proof_of_payment_link.short_description = "Proof of Payment"
