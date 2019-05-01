from django import forms
from .models import StaffMember, Shift


class StaffMemberForm(forms.ModelForm):
    class Meta:
        model = StaffMember
        fields = [
            'firstName',
            'lastName',
            'employeeID',
            'email',
            'department'
        ]

class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = [
            'staff',
            'startDate',
            'startTime',
            'lengthHours',
            'lengthMinutes'
        ]
        widgets = {
            'startDate': forms.DateInput(attrs={'type':'date'}),
            'startTime': forms.TimeInput(attrs={'type':'time'}),
        }

class StaffSettingsForm(forms.Form):
    shiftsToAdd = forms.IntegerField(max_value=365)
