from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator
# Create your models here.
class StaffMember(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    employeeID = models.CharField(max_length=10)
    department = models.CharField(max_length=20)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.employeeID

class Shift(models.Model):
    staff = models.ForeignKey(StaffMember, on_delete=models.CASCADE)
    startDate = models.DateField(unique=True)
    startTime = models.TimeField()
    lengthHours = models.IntegerField()
    lengthMinutes = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (str(self.startDate) +" staff ID: "+ str(self.staff))

class Pattern(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Day(models.Model):
    name = models.CharField(max_length=30)
    pattern = models.ForeignKey(StaffMember, on_delete=models.CASCADE)
    mondayStartTime = models.TimeField()
    mondayShiftLengthHours = models.IntegerField(validators=[MaxValueValidator(23)])
    mondayShiftLengthMinutes = models.IntegerField(validators=[MaxValueValidator(59)])
    tuesdayStartTime = models.TimeField()
    tuesdayShiftLengthHours = models.IntegerField(validators=[MaxValueValidator(23)])
    tuesdayShiftLengthMinutes = models.IntegerField(validators=[MaxValueValidator(59)])
    wednesdayStartTime = models.TimeField()
    wednesdayShiftLengthHours = models.IntegerField(validators=[MaxValueValidator(23)])
    wednesdayShiftLengthMinutes = models.IntegerField(validators=[MaxValueValidator(59)])
    thursdayStartTime = models.TimeField()
    thursdayShiftLengthHours = models.IntegerField(validators=[MaxValueValidator(23)])
    thursdayShiftLengthMinutes = models.IntegerField(validators=[MaxValueValidator(59)])
    fridayStartTime = models.TimeField()
    fridayShiftLengthHours = models.IntegerField(validators=[MaxValueValidator(23)])
    fridayShiftLengthMinutes = models.IntegerField(validators=[MaxValueValidator(59)])
    saturdayStartTime = models.TimeField()
    saturdayShiftLengthHours = models.IntegerField(validators=[MaxValueValidator(23)])
    saturdayShiftLengthMinutes = models.IntegerField(validators=[MaxValueValidator(59)])
    sundayStartTime = models.TimeField()
    sundayShiftLengthHours = models.IntegerField(validators=[MaxValueValidator(23)])
    sundayShiftLengthMinutes = models.IntegerField(validators=[MaxValueValidator(59)])

    def __str__(self):
        return self.name
