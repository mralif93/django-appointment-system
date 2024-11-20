from django import forms
from django.forms import DateTimeInput
from .models import Doctor, Patient, Appointment, Payment

# Create custom here
class DateTimeInputCustom(DateTimeInput):
    input_type = 'date'

# Create form here
class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialization', 'email', 'phone']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'phone', 'address']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'patient', 'remarks', 'date', 'time']
        widgets = {
            'date': DateTimeInputCustom(attrs={'type': 'date'}),
            'time': DateTimeInputCustom(attrs={'type': 'time'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['remarks'].required = False  # Make it optional

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['appointment', 'amount', 'status', 'proof_of_payment']  # Include the new field

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['proof_of_payment'].required = False  # Make it optional

class PaymentProofForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['proof_of_payment', 'status']  # Include the new field

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['proof_of_payment'].required = False  # Make it optional
    