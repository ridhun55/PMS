
from django.urls import path
from . import views

urlpatterns = [

    # ================  Admin ===================

    path('admin_login/',views.AdminLoginView,name='admin_login'),                               # admin_login ok
    path('admin_Home/',views.AdminHomeView,name='admin_Home'),                                  # admin_Home ok

    path('add_permission/',views.AddPermissionView,name='add_permission'),                      # Permission

    path('add_employee/', views.AddEmployeeView, name='add_employee'),                              # Add Employee ok
    path('edit_employee/', views.EmployeeView, name='edit_employee'),                               # View All Employee ok
    path('edit_employee/<int:id>', views.EditEmployeeView, name='edit_employee edit'),              # Edit Employee ok
    path('delete_edit_employee/<int:id>', views.DeleteEmployeeView, name='edit_employee delete'),   # Delete Employee ok

    path('add_projects/',views.AddProjectsView,name='add_projects'),                            # Add Project ok
    path('edit_projects/',views.ProjectsView,name='edit_projects'),                             # View All Project ok
    path('edit_projects/<int:id>',views.EditProjectsView,name='edit_projects edit'),            # Edit Project ok
    path('delete_projects/<int:id>',views.DeleteProjectView,name='edit_projects delete'),       # Delete Project ok

    path('add_category/', views.AddCategoryView, name='add_category'),                          # Add Category ok

    path('Project_Task/', views.ProjectTaskView, name='Project_Task'),                              # View All Project Task
    path('Add_Project_Task/', views.AddProjectTaskView, name='Add_Project_Task'),                   # Add Project Task
    path('Edit_Project_Task/<int:id>/', views.EditProjectTaskView, name='Project_Task edit'),       # Edit Project Task
    path('delete_Project_Task/<int:id>/', views.DeleteProjectTaskView, name='Project_Task delete'), # Edit Project Task

    path('EditIssue/',views.IssueView, name='Issue'),                                    # View All Issues
    path('AddIssue/',views.AddIssueView, name='AddIssue'),                                      # Add Issue
    path('EditIssue/<int:id>',views.EditIssueView, name='AddIssue edit'),                                      # Add Issue




    # ================  Employee  ===================

    path('signup/',views.SignupView,name='signup'),                                             # Registration ok
    path('login/',views.LoginView,name='login'),                                                 # User Login ok
    path('logout/',views.LogoutView,name='logout'),                                             # Logout ok
    path('',views.DashboardView,name='Dashboard'),                                              # Main Dashboard ok

    path('Employee_Dashboard/',views.EmployeeDashboardView,name='Employee_Dashboard'),      # My Home Dashboard

    path('MyTask/',views.MyTaskView,name='MyTask'),                                         # My Task
    path('MyTask/<int:id>', views.EditMyTaskView, name='My_Task edit'),                     # Edit MyTask
    path('TodayMyTask/',views.TodayMyTaskView,name='TodayMyTask'),                          # Today My Task
    path('TodayMyTask/',views.TodayMyTaskView,name='TodayMyTask'),                          # Today My Task
    path('OverdueMyTask/',views.OverdueMyTaskView,name='OverdueMyTask'),                          # Today My Task


    path('MyIssues/',views.MyIssuesView,name='MyIssues'),                                   # My Issue
    path('MyIssues/<int:id>', views.EditMyIssuesView, name='MyIssues edit'),                # Edit My Issue
    path('TodayMyIssues/',views.TodayMyIssuesView,name='TodayMyIssues'),                    # Today My Issue
    path('OverdueMyIssues/',views.OverdueMyIssuesView,name='OverdueMyIssues'),                    # Today My Issue

# ============================ Lead management ===================

    path('industry/',views.IndustryView,name='industry'),
    path('industry/<int:id>',views.DeleteIndustryView,name='industry delete'),

    path('product/',views.ProductView,name='product'),
    path('product/<int:id>',views.DeleteProductView,name='product delete'),

    path('service/',views.ServiceView,name='service'),
    path('service/<int:id>',views.DeleteServiceView,name='service delete'),

    path('organisation/',views.OrganisationView,name='organisation'),
    path('add_organisation/',views.AddOrganisationView,name='add_organisation'),
    path('edit_organisation/<int:id>',views.EditOrganisationView,name='edit_organisation'),
    path('delete_organisation/<int:id>',views.DeleteOrganisationView,name='delete_organisation'),

    path('lead/',views.LeadView,name='lead'),
    path('add_lead/',views.AddLeadView,name='add_lead'),





]
