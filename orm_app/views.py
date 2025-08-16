from django.shortcuts import render
from .models import Countries, Employees, Locations, Jobs, Dependents
from django.http import HttpResponse
from django.db.models import Q, Count


# MVT - Model, Views, Templates


def index_page(request):

    return render(request, "index.html")


def get_max_salary_employees(request, top):
    queryset = Employees.objects.all().order_by('-salary')[:top]
    return render(request, "max_salary.html", {"max_salary": queryset})


def get_dependents(request, employee_id):
    queryset = Dependents.objects.all().filter(employee=employee_id)
    employee = Employees.objects.get(employee_id=employee_id)
    context = {"deps": queryset, "employee": employee}
    return render(request, "dependents.html", context)


# def orm_list(request):
#     queryset = Employees.objects.values("job_id").annotate(xodim_soni=Count("*"))
#
#     for i in queryset:
#         print(i)
#
#     return HttpResponse("ok")
#
#     # emp_list = ""
#     # for c in queryset:
#     #     emp_list += f"<li>{c.first_name} {c.last_name}</li>"
#     # return HttpResponse(f"<ol>{emp_list}</ol>")
