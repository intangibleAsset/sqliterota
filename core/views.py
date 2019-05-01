from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from django.contrib import messages
from datetime import datetime, date, timedelta, time

from .forms import ShiftForm, StaffMemberForm, StaffSettingsForm
from .models import Shift, StaffMember
# Create your views here.
class Index(View):
    template_name = 'core/index.html'
    def get(self,request):
        return render(request,self.template_name)

#class NoteListView(ListView):
#    template_name = 'core/index.html'
#    queryset = Note.objects.all()

class Seven_day_view(View):
    template_name = 'core/seven_day.html'
    def get(self, request):
        return render(request,self.template_name)

class Add_staff_member(View):
    def get(self, request):
        form = StaffMemberForm()
        context = {
        "form":form
        }
        return render(request, "core/add_staff_member.html", context)

#    for i in range(0,365):
#        s = Shift(emp=Employee,date=shiftDate,startTime=shiftDate,endTime=shiftDate,notes=getShiftOnDate(shiftDate,datetime(2019,1,11),shiftPattern))
#        shiftDate = shiftDate + timedelta(days=1)
#        s.save()

    def post(self, request):
        form = StaffMemberForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'staff member added')
            form = StaffMemberForm()

        context = {
            "form":form
        }
        return render(request,"core/add_staff_member.html",context)

class Add_shift_view(View):
    def get(self, request):
        form = ShiftForm()
        context = {
            "form":form
        }
        return render(request,"core/add_shift.html",context)

    def post(self, request):
        form = ShiftForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = ShiftForm()

        context = {
            "form":form
        }
        return render(request,"core/add_shift.html",context)

class Staff_list_view(ListView):
	template_name = 'core/staff_list.html'
	queryset = StaffMember.objects.all()
	context_object_name = 'staffMembers'

class Staff_lookup_view(View):

    def get(self, request, pk):
        obj = get_object_or_404(StaffMember,id=pk)
        sh = Shift.objects.filter(staff=obj).last()
        form = StaffSettingsForm()
        context = {"staff":obj, "form":form}
        return render(request,"core/add_multiple_shifts.html",context)

    def post(self, request):
        my_pk = request.POST.get('pk')
        number = request.POST.get('shiftsToAdd')
        print(str(number))
        obj = get_object_or_404(StaffMember,id=my_pk)

        shiftDate = datetime.now().date()
        for i in range(0,int(number)):
            s = Shift(staff=obj,startDate=shiftDate,startTime=time(0,0),lengthHours=9,lengthMinutes=0)
            shiftDate = shiftDate + timedelta(days=1)
            s.save()

        context = {
            "staff":obj,
            "number":number
        }
        return render(request,"core/add_multiple_shifts.html",context)
