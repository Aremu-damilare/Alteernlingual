from django.urls import path
from . import views

app_name = 'subject'

urlpatterns = [ 
	path('', views.subjectView.as_view(), name='subject_view'),
	path('<int:pk>', views.languageDetail.as_view(), name='subjects'),
	path('topics/<int:pk>', views.subjectDetail.as_view(), name='subjects_topics'),
	path('topic/<int:pk>', views.topicDetail.as_view(), name='subjects_topics_detail'),
]
