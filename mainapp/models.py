from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=255)
    given_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    profile_description = models.TextField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.given_name} {self.surname}"


class Caregiver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="caregiver_photos/")
    gender = models.CharField(max_length=50)
    caregiving_type = models.CharField(max_length=255)
    hourly_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.user.given_name} ({self.caregiving_type})"


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    house_rules = models.TextField()

    def __str__(self):
        return f"{self.user.given_name}"


class Address(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    house_number = models.CharField(max_length=50)
    street = models.CharField(max_length=255)
    town = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.house_number} {self.street}, {self.town}"


class Job(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    required_caregiving_type = models.CharField(max_length=255)
    other_requirements = models.TextField()
    date_posted = models.DateField()

    def __str__(self):
        return f"Job {self.pk} ({self.required_caregiving_type})"


class JobApplication(models.Model):
    caregiver = models.ForeignKey(Caregiver, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    date_applied = models.DateField()

    def __str__(self):
        return f"Application for Job {self.job.pk} by {self.caregiver.user.given_name}"


class Appointment(models.Model):
    caregiver = models.ForeignKey(Caregiver, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    work_hours = models.IntegerField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Appointment ({self.appointment_date} at {self.appointment_time})"
