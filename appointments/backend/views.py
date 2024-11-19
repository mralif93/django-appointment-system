from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from .models import Doctor, Patient, Appointment, Payment
from .forms import DoctorForm, PatientForm, AppointmentForm, PaymentForm, PaymentProofForm

# Create your views here.
def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # login user
            login(request, user)

            #  if user want to remember session
            if not request.POST.get('remember'):
                request.session.set_expiry(0)  # Session expires when the browser is closed

            # send message
            messages.success(request, 'You have been sign in successfully')

            # Redirect to dashboard
            return redirect('dashboard_view')  # Default home page
        else:
            messages.error(request, 'Invalid username or password!')
            return redirect('login_view')
        
    context = {}
    return render(request, 'backend/login.html', context)

def LogoutView(request):
    # logout user
    logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect('login_view')

# Dashboard
@login_required
def DashboardView(request):
    #  current date
    now = timezone.now()

    # fetch all appointments
    appointments = Appointment.objects.all()
    p_appointments = Appointment.objects.filter(date__gte=now)

    # fetch all doctors
    doctors = Doctor.objects.all()

    # fetch all patients
    patients = Patient.objects.all()

    # fetch all payments
    payments = Payment.objects.all()
    p_payments = Payment.objects.filter(status='Pending')

    context = {
        'appointments': appointments,
        'doctors': doctors,
        'patients': patients,
        'payments': payments,
        'p_appointments': p_appointments,
        'p_payments': p_payments,
        'now': now,
    }
    return render(request, 'backend/index.html', context)


# Appointments
@login_required
def ListAppointmentsView(request):
    # fetch all appointments
    appointments = Appointment.objects.all()

    context = {
        'view': 'list',
        'appointments': appointments,
    }
    return render(request, 'backend/crud_appointment.html', context)

@login_required
def CreateAppointmentsView(request):
    # submit
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully created appointment!')
            return redirect('list_appointment_view')
    else:
        form = AppointmentForm()

    context = {
        'view': 'create',
        'form': form,
    }
    return render(request, 'backend/crud_appointment.html', context)

@login_required
def ReadAppointmentsView(request, id):
    # fetch appointment
    appointment = Appointment.objects.get(id=id)
    
    context = {
        'view': 'read',
        'appointment': appointment,
    }
    return render(request, 'backend/crud_appointment.html', context)

@login_required
def UpdateAppointmentsView(request, id):
    # fetch appointment
    appointment = Appointment.objects.get(id=id)

    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated appointment!')
            return redirect('list_appointment_view')
    else:
        form = AppointmentForm(instance=appointment)

    context = {
        'view': 'update',
        'form': form,
    }
    return render(request, 'backend/crud_appointment.html', context)

@login_required
def DeleteAppointmentsView(request, id):
    # fetch appointment
    appointment = Appointment.objects.get(id=id)

    if request.method == "POST":
        appointment.delete()
        messages.success(request, 'Successfully deleted appointment!')
        return redirect('list_appointment_view')

    context = {
        'view': 'delete',
        'appointment': appointment,
    }
    return render(request, 'backend/crud_appointment.html', context)


# Doctors
@login_required
def ListDoctorsView(request):
    # get list of doctor
    doctors = Doctor.objects.all()

    context = {
        'view': 'list',
        'doctors': doctors,
    }
    return render(request, 'backend/crud_doctor.html', context)

@login_required
def CreateDoctorsView(request):
    # post
    if request.method == "POST":
        form = DoctorForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully created doctor!')
            return redirect('list_doctor_view')
    else:
        form = DoctorForm()

    context = {
        'view': 'create',
        'form': form,
    }
    return render(request, 'backend/crud_doctor.html', context)

@login_required
def ReadDoctorsView(request, id):
    #  search by id
    doctor = Doctor.objects.get(id=id)

    context = {
        'view': 'read',
        'doctor': doctor,
    }
    return render(request, 'backend/crud_doctor.html', context)

@login_required
def UpdateDoctorsView(request, id):
    #  search by id
    doctor = Doctor.objects.get(id=id)

    if request.method == "POST":
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated details doctor!')
            return redirect('list_doctor_view')
    else:
        form = DoctorForm(instance=doctor)

    context = {
        'view': 'update',
        'form': form,
    }
    return render(request, 'backend/crud_doctor.html', context)

@login_required
def DeleteDoctorsView(request, id):
    #  search by id
    doctor = Doctor.objects.get(id=id)

    if request.method == "POST":
        doctor.delete()
        messages.success(request, 'Successfully delete details doctor!')
        return redirect('list_doctor_view')

    context = {
        'view': 'delete',
        'doctor': doctor,
    }
    return render(request, 'backend/crud_doctor.html', context)


# Patients
@login_required
def ListPatientsView(request):
    # fetch all patients
    patients = Patient.objects.all()

    context = {
        'view': 'list',
        'patients': patients,
    }
    return render(request, 'backend/crud_patient.html', context)

@login_required
def CreatePatientsView(request):
    # submit form
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully created patient!')
            return redirect('list_patient_view')
    else:
        form = PatientForm()
        
    context = {
        'view': 'create',
        'form': form,
    }
    return render(request, 'backend/crud_patient.html', context)

@login_required
def ReadPatientsView(request, id):
    # search patient by id
    patient = Patient.objects.get(id=id)

    context = {
        'view': 'read',
        'patient': patient,
    }
    return render(request, 'backend/crud_patient.html', context)

@login_required
def UpdatePatientsView(request, id):
    # search patient by id
    patient = Patient.objects.get(id=id)

    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated patient!')
            return redirect('list_patient_view')
    else:
        form = PatientForm(instance=patient)

    context = {
        'view': 'update',
        'form': form,
    }
    return render(request, 'backend/crud_patient.html', context)

@login_required
def DeletePatientsView(request, id):
    # search patient by id
    patient = Patient.objects.get(id=id)

    # submit form
    if request.method == "POST":
        patient.delete()
        messages.success(request, 'Successfully deleted patient!')
        return redirect('list_patient_view')

    context = {
        'view': 'delete',
        'patient': patient,
    }
    return render(request, 'backend/crud_patient.html', context)


# Payments
@login_required
def ListPaymentsView(request):
    # search payment by id
    payments = Payment.objects.all()

    context = {
        'view': 'list',
        'payments': payments,
    }
    return render(request, 'backend/crud_payment.html', context)

@login_required
def CreatePaymentsView(request):
    # submit
    if request.method == "POST":
        form = PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully created payment!')
            return redirect('list_payment_view')
    else:
        form = PaymentForm()

    context = {
        'view': 'create',
        'form': form,
    }
    return render(request, 'backend/crud_payment.html', context)

@login_required
def ReadPaymentsView(request, id):
    # search payment by id
    payment = Payment.objects.get(id=id)

    context = {
        'view': 'read',
        'payment': payment,
    }
    return render(request, 'backend/crud_payment.html', context)

@login_required
def UpdatePaymentsView(request, id):
    # search payment by id
    payment = Payment.objects.get(id=id)

    # submit
    if request.method == "POST":
        form = PaymentForm(request.POST, request.FILES, instance=payment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated payment!')
            return redirect('list_payment_view')
    else:
        form = PaymentForm(instance=payment)

    context = {
        'view': 'update',
        'form': form,
    }
    return render(request, 'backend/crud_payment.html', context)

@login_required
def UpdatePaymentProofView(request, id):
    # search payment
    payment = Payment.objects.get(id=id)

    if request.method == "POST":
        form = PaymentProofForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            # message
            messages.success(request, 'Successfully updated payment!')
            # rediect
            return redirect('list_payment_view')
    else:
        form = PaymentProofForm(instance=payment)
    
    context = {
        'view': 'update',
        'form': form,
    }
    return render(request, 'backend/crud_payment.html', context)

@login_required
def DeletePaymentsView(request, id):
    # search payment by id
    payment = Payment.objects.get(id=id)

    # submit
    if request.method == "POST":
        payment.delete()
        messages.success(request, 'Successfully delete payment!')
        return redirect('list_payment_view')

    context = {
        'view': 'delete',
        'payment': payment,
    }
    return render(request, 'backend/crud_payment.html', context)