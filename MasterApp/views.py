from django.shortcuts import render,redirect
from .models import CustUser
from . import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime, timedelta
from django.contrib.auth.models import Permission


# @user_passes_test(lambda u:u.is_superuser)




# ================ Admin =================================
def AdminLoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        aut = authenticate(username=username,password=password)
        if aut is None:         # check empty feild
            return redirect('admin_login')
        else:
            login(request,aut)  # check empty feild
            if aut.is_superuser:
                return redirect('admin_Home')
            else:
                return redirect('admin_login')

    html = 'Admin Login.html'
    context = {'title':'Admin Login',
               'page_heading': 'ADMIN LOGIN',
               'active':False
        }
    return render(request,html,context)


@user_passes_test(lambda u:u.is_superuser,redirect_field_name='admin_login')
@login_required(login_url='admin_login')
def AdminHomeView(request):
    obj1 = models.CustUser.objects.filter(is_employee=True)
    obj2 = models.Project.objects.filter(Flage=True)
    count1 = 0
    for i in obj1:
        count1 = count1 + 1

    count2 = 0
    for i in obj2:
        count2 = count2 + 1

    html = 'Admin Home.html'
    context = {
        'title':'Admin Home',
        'page_heading':'ADMIN DASHBOARD',
        'count1':count1,    # Employee count
        'count2':count2,     # Project count
        'active': True
    }
    return render(request,html,context)


def AddPermissionView(request):
    data = models.CustUser.objects.all()
    menus = models.Menu.objects.all()
    if request.method == 'POST':
        for idx,i in enumerate(menus):
            emp_id = request.POST.get('name')
            isView = request.POST.get('isView'+str(idx+1),False)
            isAdd = request.POST.get('isAdd'+str(idx+1),False)
            isEdit = request.POST.get('isEdit'+str(idx+1),False)
            isDelete = request.POST.get('isDelete'+str(idx+1),False)
            Employee = models.CustUser.objects.get(id=emp_id)
            if isView == 'on': isView = True
            if isAdd == 'on': isAdd = True
            if isEdit == 'on': isEdit = True
            if isDelete == 'on': isDelete = True
            models.Permissions.objects.update_or_create(Menu=i,
                                                     defaults={'isDelete':isDelete,'isEdit':isEdit,'isView':isView,'isAdd':isAdd},
                                                     Employee=Employee)


    html = 'Add Permission.html'
    context = {
        'title':'Permission',
        'page_heading':'PERMISSION',
        'data':data,
        'menus':menus
     }
    return render(request,html,context)


# @user_passes_test(lambda u:u.is_superuser)
# @login_required(login_url='admin_login')
def AddEmployeeView(request):
    data = models.CustUser.objects.filter(is_employee=True)
    EmpCateg = models.Category.objects.filter(E=True, P=False)

    if request.method =='POST':
        Name = request.POST.get('Name')
        Mobile = request.POST.get('mobile_no')
        Email = request.POST.get('email')
        Category_id = request.POST.get('Category_id')
        username = request.POST.get('username')
        password = request.POST.get('password')
        Confirm_Password = request.POST.get('confirm_password')
        Type = models.Category.objects.get(id=Category_id)

        if password == Confirm_Password:
            user = CustUser.objects.create_user(is_employee=True,is_staff=True,Name=Name,Mobile=Mobile,email=Email,Type=Type,username=username,password=password)

            return redirect('add_employee')
        else:
            return redirect('add_employee')
    html = 'Add Employee.html'
    context = {
        'title':'Add Employee',
        'page_heading': 'ADD EMPLOYEE',
        'data':data,
        'EmpCateg':EmpCateg,
        }
    return render(request,html,context)

# @login_required(login_url='admin_login')
def EmployeeView(request):
    data = models.CustUser.objects.filter(is_employee=True)
    html = 'Edit Employee.html'
    context = {
        'title':'Employee',
        'page_heading': 'EMPLOYEE',
        'data':data,
        }
    return render(request,html,context)
#
# @login_required(login_url='admin_login')
def EditEmployeeView(request,id):
    categ = models.Category.objects.filter(E=True,P=False)
    data = models.CustUser.objects.all()
    emp = models.CustUser.objects.get(id=id)

    if request.method =='POST':
        obj = models.CustUser.objects.get(id=id)
        obj.Name = request.POST.get('name')
        obj.Mobile = request.POST.get('mobile_no')
        obj.Email = request.POST.get('email')
        Categoryid = request.POST.get('Category_id')
        obj.Type = models.Category.objects.get(id=Categoryid)
        obj.save()
        return redirect('edit_employee')

    html = 'Edit Employee Edit.html'
    context = {
        'title': 'Edit Employee',
        'page_heading': 'EDIT EMPLOYEE',
        'data': data,
        'emp':emp,
        'categ':categ,
    }
    return render(request,html,context)

@login_required(login_url='admin_login')
def DeleteEmployeeView(request,id):
    dele = models.CustUser.objects.get(id=id)
    dele.delete()
    return redirect('edit_employee')
    html = 'Edit Employee.html'
    context = {
        'title':'Employee',
        'page_heading': 'EMPLOYEE',
        }
    return render(request,html,context)



@login_required(login_url='admin_login')
def AddProjectsView(request):
    data = models.Project.objects.all()
    ProCateg = models.Category.objects.filter(P=True,E=False)

    if request.method =='POST':
        Name = request.POST.get('Name')
        Category_id = request.POST.get('Category_id')
        Start_Date = request.POST.get('Start_Date')
        End_Date = request.POST.get('End_Date')
        Category = models.Category.objects.get(id=Category_id)
        obj = models.Project.objects.create(Flage=True, Name=Name, Category=Category, Start_Date=Start_Date, End_Date=End_Date)
        obj.save()
        return redirect('add_projects')

    html = 'Add projects.html'
    context = {
        'title':'Projects',
        'page_heading': 'PROJECTS',
        'data':data,
        'ProCateg':ProCateg,
        }
    return render(request,html,context)

@login_required(login_url='admin_login')
def ProjectsView(request):
    data = models.Project.objects.all()
    html = 'Edit Projects.html'

    context = {
        'title':'Projects',
        'page_heading': 'PROJECTS',
        'data':data,
        }
    return render(request,html,context)

@login_required(login_url='admin_login')
def EditProjectsView(request,id):
    categ = models.Category.objects.filter(P=True, E=False)
    data = models.Project.objects.all()
    pro = models.Project.objects.get(id=id)

    if request.method == 'POST':
        Categoryid = request.POST.get('Category_id')
        obj = models.Project.objects.get(id=id)
        obj.Category = models.Category.objects.get(id=Categoryid)
        obj.Name = request.POST.get('Name')
        obj.Start_Date = request.POST.get('Start_Date')
        obj.End_Date = request.POST.get('End_Date')
        obj.save()
        return redirect('edit_projects')

    html = 'Edit Projects Edit.html'
    context = {
        'title':'Edit Projects',
        'page_heading': 'EDIT PROJECTS',
        'pro':pro,
        'data':data,
        'categ':categ,
        }
    return render(request,html,context)

@login_required(login_url='admin_login')
def DeleteProjectView(request,id):
    dele = models.Project.objects.get(id=id)
    dele.delete()
    return redirect('edit_projects')

    html = 'Edit Projects.html'
    context = {
        'title':'Projects',
        'page_heading': 'PROJECTS',
        }
    return render(request,html,context)


def LogoutView(request):
    logout(request)
    return redirect('Dashboard')

@login_required(login_url='admin_login')
def AddCategoryView(request):
    P1 = models.Category.objects.filter(P=True,E=False)
    E1 = models.Category.objects.filter(E=True,P=False)

    obj = models.Category()
    if request.method == 'POST' and 'project_submit' in request.POST:
        Project_Category = request.POST.get('Project_Category')
        obj.Project_Category = Project_Category
        obj.Employee_Category = 'null'
        obj.P = True
        if Project_Category == '':
            return redirect('add_category')
        else:
            obj.save()
            return redirect('add_category')

    if request.method == 'POST' and 'employee_submit' in request.POST:
        Employee_Category = request.POST.get('Employee_Category')
        obj.Employee_Category = Employee_Category
        obj.Project_Category = 'null'
        obj.E = True
        if Employee_Category == '':
            return redirect('add_category')
        else:
            obj.save()
            return redirect('add_category')

    html = 'Add Category.html'
    context = {
        'title':'Category',
        'page_heading': 'CATEGORY',
        'P1':P1,
        'E1':E1
        }
    return render(request,html,context)


@login_required(login_url='admin_login')
def ProjectTaskView(request):
    data = models.ProjectTask.objects.all().order_by('ProjectName_id')

    html = 'Project Task.html'
    context = {
        'title':'Project Task',
        'page_heading': 'PROJECT TASK',
        'data':data,
        }
    return render(request,html,context)


@login_required(login_url='admin_login')
def AddProjectTaskView(request):
    Proj = models.Project.objects.all()
    Emp = models.CustUser.objects.filter(is_employee=True)
    list = [1,2,3,4,5]
    stat_list = {'Not_Started': 'Not Started', 'In_Progress': 'In Progress', 'Pending': 'Pending','Completed': 'Completed'}

    if request.method == 'POST':
        Projectid = request.POST.get('ProjectName')
        Priority = request.POST.get('Priority')
        Employeeid = request.POST.get('ProjectEmployee')
        Task = request.POST.get('Task')
        Task_Due_date = request.POST.get('Due_date')
        Task_Status = request.POST.get('Status')
        Task_Discription = request.POST.get('Discription')
        ProjectName = models.Project.objects.get(id=Projectid)
        ProjectEmployee = models.CustUser.objects.get(id=Employeeid)
        obj = models.ProjectTask.objects.create(PT=True, ProjectName=ProjectName, Priority=Priority,
                                                ProjectEmployee=ProjectEmployee,Task=Task,Task_Due_date=Task_Due_date,Task_Discription=Task_Discription,Task_Status=Task_Status)

        return redirect('Project_Task')

    html = 'Add Project Task.html'
    context = {
        'title':'Assign Task',
        'page_heading': 'PROJECT TASK',
        'Proj':Proj,
        'Emp':Emp,
        'list':list,
        'list_val': stat_list
        }
    return render(request,html,context)


@login_required(login_url='admin_login')
def EditProjectTaskView(request, id):
    data = models.ProjectTask.objects.get(id=id)
    Proj = models.Project.objects.all()
    Emp = models.CustUser.objects.all()

    if request.method =='POST':
        obj = models.ProjectTask.objects.get(id=id)

        Projectid = request.POST.get('ProjectName')
        obj.Priority = request.POST.get('Priority')
        Employeeid = request.POST.get('ProjectEmployee')
        obj.Task = request.POST.get('Task')
        obj.Task_Due_date = request.POST.get('Due_date')
        obj.Task_Status = request.POST.get('Status')
        obj.Task_Discription = request.POST.get('Discription')
        obj.ProjectName = models.Project.objects.get(id=Projectid)
        obj.ProjectEmployee = models.CustUser.objects.get(id=Employeeid)
        obj.save()

        return redirect('Project_Task')

    stat_list = {'Not_Started': 'Not Started', 'In_Progress': 'In Progress', 'Pending': 'Pending','Completed': 'Completed'}
    html = 'Edit Project Task.html'
    context = {
        'title': 'Edit Project Task',
        'page_heading': 'EDIT PROJECT TASK',
        'data': data,
        'Proj': Proj,
        'Emp': Emp,
        'list': [1, 2, 3, 4, 5],
        'list_val':stat_list
    }
    return render(request, html, context)

@login_required(login_url='admin_login')
def DeleteProjectTaskView(request, id):
    dele = models.ProjectTask.objects.get(id=id)
    dele.delete()
    return redirect('Project_Task')

    html = 'Project Task.html'
    context = {
        'title':'Project Task',
        'page_heading': 'PROJECT TASK',
        'data':data
        }
    return render(request,html,context)

def IssueView(request):
    data = models.Issue.objects.all()

    html = 'Project Issue.html'
    context = {
        'title': 'Project Issues',
        'page_heading': 'PROJECT ISSUES',
        'data': data,
    }
    return render(request, html, context)

def AddIssueView(request):
    stat_list = {'Not_Started': 'Not Started', 'In_Progress': 'In Progress', 'Pending': 'Pending',
                 'Completed': 'Completed'}
    Proj = models.Project.objects.all()
    Emp = models.CustUser.objects.all()
    data = models.Issue.objects.all()

    if request.method =='POST':
        ProjectNameid = request.POST.get('project')
        ProjectEmployeeid = request.POST.get('employee')
        Issue = request.POST.get('Issue')
        Issue_Due_date = request.POST.get('Due_date')

        obj = models.Issue()
        obj.ProjectName = models.Project.objects.get(id=ProjectNameid)
        obj.ProjectEmployee = models.CustUser.objects.get(id=ProjectEmployeeid)
        obj.Issue_Status = 'Pending'
        obj.Issues = Issue
        obj.Issue_Due_date = Issue_Due_date
        obj.save()
        return redirect('Issue')

    html = 'Add Issue.html'
    context = {
        'title': 'Add Issues',
        'page_heading': 'ADD ISSUES',
        'Proj': Proj,
        'Emp': Emp,
        'data':data,
        'stat_list':stat_list,
    }
    return render(request, html, context)

def EditIssueView(request,id):
    stat_list = {'Not_Started': 'Not Started', 'In_Progress': 'In Progress', 'Pending': 'Pending',
                 'Completed': 'Completed'}
    x = models.Project.objects.all()
    Emp = models.CustUser.objects.all()
    data = models.Issue.objects.get(id=id)

    if request.method == 'POST':
        ProjectEmployeeid = request.POST.get('employee')
        Issue = request.POST.get('Issue')
        Status = request.POST.get('Status')
        Issue_Due_date = request.POST.get('Due_date')

        obj = models.Issue.objects.get(id=id)
        obj.ProjectEmployee = models.CustUser.objects.get(id=ProjectEmployeeid)
        obj.Issue_Status = Status
        obj.Issues = Issue
        obj.Issue_Due_date = Issue_Due_date
        obj.save()
        return redirect('Issue')


    html = 'Edit Issue.html'
    context = {
        'title': 'Edit Issues',
        'page_heading': 'EDIT ISSUES',
        'x':x,
        'Emp':Emp,
        'data':data,
        'list_val': stat_list,
    }
    return render(request, html, context)


# ================ User =================================

def SignupView(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('email')

        if password == confirm_password:
            user = CustUser.objects.create_user(is_employee=True,is_staff=True,Name=Name,username=username,password=password,email=email)
            user.save()
            return redirect('login')

    html = 'registration.html'
    context = {'title':'Registration',
               'page_heading': 'SIGNUP',
        }
    return render(request,html,context)


def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        aut = authenticate(username=username,password=password)
        if aut is None:         # check empty feild
            return redirect('login')
        else:
            login(request,aut)  # check empty feild
            if aut.is_employee:
                return redirect('Employee_Dashboard')
            else:
                return redirect('login')

    html = 'Login.html'
    context = {'title':'Employee Login',
               'page_heading': 'EMPLOYEE LOGIN',
        }
    return render(request,html,context)

def DashboardView(request):

    html = 'Dashboard.html'
    context = {
        'title':'Dashboard',
        'page_heading':'DASHBOARD',
    }
    return render(request,html,context)




# =========================================================== ok ==================

def EmployeeDashboardView(request):
    current_user = request.user.id

    MyTask = models.ProjectTask.objects.filter(ProjectEmployee_id=current_user)
    A = models.ProjectTask.objects.filter(ProjectEmployee_id=current_user)
    F = models.ProjectTask.objects.filter(ProjectEmployee_id=current_user,Task_Due_date=datetime.today().date())
    G = models.ProjectTask.objects.filter(ProjectEmployee_id=current_user,Task_Due_date__lt=datetime.today().date())

    B= models.Issue.objects.filter(ProjectEmployee_id=current_user)
    C= models.Issue.objects.filter(ProjectEmployee_id=current_user,Issue_Due_date=datetime.today().date())
    D= models.Issue.objects.filter(ProjectEmployee_id=current_user,Issue_Due_date__lt=datetime.today().date())

    c = 0
    for i in A:
        c +=1

    d = 0
    for i in B:
        d +=1

    e = 0
    for i in C:
        e +=1

    f = 0
    for i in D:
        f +=1

    g = 0
    for i in F:
        g +=1

    h = 0
    for i in G:
        h +=1

    html = 'Employee Home.html'
    context = {'title':'My Home',
               'page_heading': 'My Home',
               'MyTask':MyTask,
               'logo': models.CustUser.objects.get(id=request.user.id),
               'c':c,
               'd':d,
               'e':e,
               'f':f,
               'g':g,
               'h':h,
        }
    return render(request,html,context)


def EditEmployeeDashboardView(request,id):
    data = models.ProjectTask.objects.get(id=id)
    stat_list = {'Not_Started': 'Not Started', 'In_Progress': 'In Progress', 'Pending': 'Pending',
                 'Completed': 'Completed'}

    if request.method == 'POST':
        obj = models.ProjectTask.objects.get(id=id)
        obj.Status = request.POST.get('Status')
        obj.Issues = request.POST.get('Issues')
        obj.Discription = request.POST.get('Discription')
        obj.save()
        return redirect('Employee_Dashboard')

    html = 'Edit Employee Dashboard.html'
    context = {'title':'Edit Task',
               'page_heading': 'EDIT TASK',
               'data':data,
               'list_val': stat_list,
        }
    return render(request,html,context)


def MyTaskView(request):
    current_user = request.user.id


    MyTask = models.ProjectTask.objects.filter(ProjectEmployee_id=current_user)

    html = 'My Task.html'
    context = {
        'title':'My Task',
        'page_heading':'MY TASK',
        'data':MyTask,
    }
    return render(request,html,context)


def EditMyTaskView(request,id):
    data = models.ProjectTask.objects.get(id=id)
    stat_list = {'Not_Started': 'Not Started', 'In_Progress': 'In Progress', 'Pending': 'Pending',
                 'Completed': 'Completed'}

    if request.method == 'POST':
        obj = models.ProjectTask.objects.get(id=id)
        obj.Task_Status = request.POST.get('Status')
        obj.Issues = request.POST.get('Issues')
        obj.Task_Discription = request.POST.get('Discription')
        obj.save()
        return redirect('MyTask')


    html = 'Edit My Task.html'
    context = {
        'title':'Edit My Task',
        'page_heading':'Edit MY TASK',
        'data':data,
        'list': list,
        'list_val': stat_list
    }
    return render(request,html,context)



def TodayMyTaskView(request):
    current_user = request.user.id

    MyTask = models.ProjectTask.objects.filter(ProjectEmployee_id=current_user,Task_Due_date=datetime.today().date())
    html = 'Today MyTask.html'
    context = {
        'title': 'My Task',
        'page_heading': 'MY TASK',
        'data': MyTask
    }
    return render(request, html, context)


def OverdueMyTaskView(request):
    current_user = request.user.id

    MyTask = models.ProjectTask.objects.filter(ProjectEmployee_id=current_user,Task_Due_date__lt=datetime.today().date())
    html = 'Overdue MyTask.html'
    context = {
        'title': 'Overdue Task',
        'page_heading': 'Overdue TASK',
        'data': MyTask
    }
    return render(request, html, context)

# ===============================================

def MyIssuesView(request):
    current_user = request.user.id

    MyIssue = models.Issue.objects.filter(ProjectEmployee_id=current_user)
    html = 'My Issues.html'
    context = {
        'title': 'My Issues',
        'page_heading': 'MY ISSUES',
        'data': MyIssue
    }
    return render(request, html, context)


def EditMyIssuesView(request,id):
    data = models.Issue.objects.get(id=id)

    stat_list = {'Not_Started': 'Not Started', 'In_Progress': 'In Progress', 'Pending': 'Pending',
                 'Completed': 'Completed'}

    if request.method == 'POST':
        obj = models.Issue.objects.get(id=id)
        obj.Issue_Status = request.POST.get('Status')
        obj.Issues = request.POST.get('Issue')
        obj.save()
        return redirect('MyIssues')

    html = 'Edit My Issues.html'
    context = {
        'title': 'Edit My Issues',
        'page_heading': 'EDIT MY ISSUES',
        'data':data,
        'list': list,
        'list_val': stat_list
    }
    return render(request, html, context)

def TodayMyIssuesView(request):
    current_user = request.user.id

    MyIssue = models.Issue.objects.filter(ProjectEmployee_id=current_user,Issue_Due_date=datetime.today().date())
    html = 'Today My Issues.html'
    context = {
        'title': 'Today My Issues',
        'page_heading': 'TODAY MY ISSUES',
        'data': MyIssue
    }
    return render(request, html, context)


def OverdueMyIssuesView(request):
    current_user = request.user.id

    MyIssue = models.Issue.objects.filter(ProjectEmployee_id=current_user,Issue_Due_date__lt=datetime.today().date())
    html = 'Overdue MyIssues.html'
    context = {
        'title': 'Overdue Issues',
        'page_heading': 'OVERDUE ISSUES',
        'data': MyIssue
    }
    return render(request, html, context)


def IndustryView(request):
    data = models.Industry.objects.all()

    if request.method =='POST':
        industry = request.POST.get('industry')
        if industry == '':
            pass
        else:
            obj = models.Industry()
            obj.industry = industry
            obj.save()
            return redirect('industry')

    html = 'Industry.html'
    context = {
        'title': 'Industry',
        'page_heading': 'Industry',
        'data':data,
    }
    return render(request, html, context)

def DeleteIndustryView(request,id):
    obj = models.Industry.objects.get(id=id)
    obj.delete()
    return redirect('industry')

    html = 'Industry.html'
    context = {
        'title': 'Industry',
        'page_heading': 'Industry',
    }
    return render(request, html, context)

def OrganisationView(request):
    data = models.Organisation.objects.all()

    html = 'Organisation.html'
    context = {
        'title': 'Industry',
        'page_heading': 'Industry',
        'data':data,
    }
    return render(request, html, context)

def AddOrganisationView(request):
    Ind = models.Industry.objects.all()

    if request.method == 'POST':
        Owner = request.POST.get('Owner')
        Contacted_Person = request.POST.get('Contacted_Person')
        Mobile = request.POST.get('Mobile')
        Email = request.POST.get('Email')
        Website = request.POST.get('Website')
        Street = request.POST.get('Street')
        Country = request.POST.get('Country')
        State = request.POST.get('State')
        Description = request.POST.get('Description')
        Fax = request.POST.get('Fax')
        Industryid = request.POST.get('Industry')
        City = request.POST.get('City')
        Zipcode = request.POST.get('Zipcode')

        if Owner =='' or Contacted_Person =='' or Mobile =='' or Email =='' or Website =='' or Street =='' or Country =='' or State =='' or Description =='' or Fax =='' or City =='' or Zipcode =='':
            return redirect('add_organisation')
        else:
            obj = models.Organisation()
            obj.Owner = Owner
            obj.Contacted_Person = Contacted_Person
            obj.Mobile = Mobile
            obj.Email = Email
            obj.Website = Website
            obj.Street = Street
            obj.Country = Country
            obj.State = State
            obj.Description = Description
            obj.Fax = Fax
            obj.Industry = models.Industry.objects.get(id=Industryid)
            obj.City = City
            obj.Zipcode = Zipcode
            obj.save()
            return redirect('organisation')


    html = 'Add Organisation.html'
    context = {
        'title': 'Add Organisation',
        'page_heading': 'Add Organisation',
        'Ind':Ind,
    }
    return render(request, html, context)

def EditOrganisationView(request,id):
    Ind = models.Industry.objects.all()
    data = models.Organisation.objects.get(id=id)

    if request.method == 'POST':
        Owner = request.POST.get('Owner')
        Contacted_Person = request.POST.get('Contacted_Person')
        Mobile = request.POST.get('Mobile')
        Email = request.POST.get('Email')
        Website = request.POST.get('Website')
        Street = request.POST.get('Street')
        Country = request.POST.get('Country')
        State = request.POST.get('State')
        Description = request.POST.get('Description')
        Fax = request.POST.get('Fax')
        Industryid = request.POST.get('Industry')
        City = request.POST.get('City')
        Zipcode = request.POST.get('Zipcode')

        if Owner == '' or Contacted_Person == '' or Mobile == '' or Email == '' or Website == '' or Street == '' or Country == '' or State == '' or Description == '' or Fax == '' or City == '' or Zipcode == '':
            return redirect('edit_organisation')
        else:
            obj = models.Organisation.objects.get(id=id)
            obj.Owner = Owner
            obj.Contacted_Person = Contacted_Person
            obj.Mobile = Mobile
            obj.Email = Email
            obj.Website = Website
            obj.Street = Street
            obj.Country = Country
            obj.State = State
            obj.Description = Description
            obj.Fax = Fax
            obj.Industry = models.Industry.objects.get(id=Industryid)
            obj.City = City
            obj.Zipcode = Zipcode
            obj.save()
            return redirect('organisation')

    html = 'Edit Organisation.html'
    context = {
        'title': 'Edit Organisation',
        'page_heading': 'Edit Organisation',
        'data': data,
        'Ind':Ind,
    }
    return render(request, html, context)


def DeleteOrganisationView(request,id):
    data = models.Organisation.objects.get(id=id)
    data.delete()
    return redirect('organisation')

    html = 'Edit Organisation.html'
    return render(request, html, )


def ProductView(request):
    data = models.Products.objects.all()
    if request.method =='POST':
        product1 = request.POST.get('product')
        if product1 =='':
            return redirect('product')
        else:
            obj = models.Products()
            obj.product = product1
            obj.save()
            return redirect('product')


    html = 'Product.html'
    context = {
        'title': 'Product',
        'page_heading': 'Product',
        'data': data,
    }
    return render(request, html, context)



def DeleteProductView(request,id):
    data = models.Products.objects.get(id=id)
    data.delete()
    return redirect('product')

    html = 'Product.html'
    context = {
        'title': 'Product',
        'page_heading': 'Product',
        'data': data,
    }
    return render(request, html, context)


def ServiceView(request):
    data = models.Service.objects.all()
    if request.method == 'POST':
        service1 = request.POST.get('service')
        if service1 == '':
            return redirect('service')
        else:
            obj = models.Service()
            obj.service = service1
            obj.save()
            return redirect('service')

    html = 'Service.html'
    context = {
        'title': 'Service',
        'page_heading': 'Service',
        'data': data,
    }
    return render(request, html, context)


def DeleteServiceView(request,id):
    data = models.Service.objects.get(id=id)
    data.delete()
    return redirect('service')

    html = 'Service.html'
    context = {
        'title': 'service',
        'page_heading': 'service',
        'data': data,
    }
    return render(request, html, context)


def LeadView(request):
    html = 'Lead.html'
    context = {
        'title': 'Lead Details',
        'page_heading': 'Lead Details',
    }
    return render(request, html, context)

def AddLeadView(request):
    current_user = request.user.id
    user =  models.CustUser.objects.get(id=current_user)
    Own = models.Organisation.objects.all()
    Ind = models.Industry.objects.all()
    Lead_Title = ''
    Oid =''
    data = ''


    if request.method =='POST':
        if 'Click' in request.POST:
            Lead_Title = request.POST.get('Lead_Title')
            Oid = int(request.POST.get('Owner'))
            data = models.Organisation.objects.get(id=Oid)


    if request.method =='POST':
        if 'Submit' in request.POST:
            pass





    html = 'Add Lead.html'
    context = {
        'title': 'Add Lead Details',
        'page_heading': 'Add Lead Details',
        'Own':Own,
        'Ind':Ind,
        'Lead_Title':Lead_Title,
        'Oid':Oid,
        'data':data,
    }
    return render(request, html, context)


