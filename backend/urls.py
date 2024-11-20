from django.urls import path
from . import views

urlpatterns = [
  # authentication session
  path('login/', views.LoginView, name='login_view'),
  path('logout/', views.LogoutView, name='logout_view'),

  # dashboard
  path('', views.DashboardView, name='dashboard_view'),
  
  # bookings
  path('bookings/', views.ListAppointmentsView, name='list_appointment_view'),
  path('bookings/create/', views.CreateAppointmentsView, name='create_appointment_view'),
  path('bookings/read/<int:id>/', views.ReadAppointmentsView, name='read_appointment_view'),
  path('bookings/update/<int:id>/', views.UpdateAppointmentsView, name='update_appointment_view'),
  path('bookings/delete/<int:id>/', views.DeleteAppointmentsView, name='delete_appointment_view'),

  # doctors
  path('doctors/', views.ListDoctorsView, name='list_doctor_view'),
  path('doctors/create/', views.CreateDoctorsView, name='create_doctor_view'),
  path('doctors/read/<int:id>/', views.ReadDoctorsView, name='read_doctor_view'),
  path('doctors/update/<int:id>/', views.UpdateDoctorsView, name='update_doctor_view'),
  path('doctors/delete/<int:id>/', views.DeleteDoctorsView, name='delete_doctor_view'),

  # patients
  path('patients/', views.ListPatientsView, name='list_patient_view'),
  path('patients/create/', views.CreatePatientsView, name='create_patient_view'),
  path('patients/read/<int:id>/', views.ReadPatientsView, name='read_patient_view'),
  path('patients/update/<int:id>/', views.UpdatePatientsView, name='update_patient_view'),
  path('patients/delete/<int:id>/', views.DeletePatientsView, name='delete_patient_view'),

  # payments
  path('payments/', views.ListPaymentsView, name='list_payment_view'),
  path('payments/create/', views.CreatePaymentsView, name='create_payment_view'),
  path('payments/read/<int:id>/', views.ReadPaymentsView, name='read_payment_view'),
  path('payments/update/<int:id>/', views.UpdatePaymentsView, name='update_payment_view'),
  path('payments/delete/<int:id>/', views.DeletePaymentsView, name='delete_payment_view'),
  path('payments/update/proof/<int:id>/', views.UpdatePaymentProofView, name='update_proof_payment_view'),
]