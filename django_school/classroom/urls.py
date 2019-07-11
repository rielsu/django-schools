from django.urls import include, path
from django.views.generic import TemplateView
from classroom.views import TimeTableView, classroom_view, subject_view

urlpatterns = [
	path('', classroom_view, name='classrooms'),
	path('subject/', subject_view, name='subjects'),
	path('timetable/', TimeTableView.as_view(), name='timetable'),
	# path('timetable', TemplateView.as_view(template_name="classroom/timetable.html"), name='timetable'),
]

