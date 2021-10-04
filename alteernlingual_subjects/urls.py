from django.urls import path
from . import views

app_name = 'subject'

urlpatterns = [ 
	path('', views.subjectView.as_view(), name='subject_view'),
	 path('follow/<int:pk>', views.followSubjectView.as_view(), name='follow_subject'),
	# path('<int:pk>', views.languageDetail.as_view(), name='subjects'),
	path('topics/<int:pk>', views.subjectDetail.as_view(), name='subjects_topics'),
	path('topic-detail/<int:pk>', views.topicContentDetail.as_view(), name='topics_detail'),
]
