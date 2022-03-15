from django.urls import path, include
from Alteernlingual_topic import views


urlpatterns = [ 
	
	path('lessons', views.lessonsView.as_view(), name='lessons'),
    path('<int:pk>', views.TopicDetail.as_view(), name='detail'),
    # path('course/<int:pk>', views.subTopicDetail.as_view(), name='topic_detail'),
    path('follow/<int:pk>', views.followLanguageView.as_view(), name='follow_cat'),
    path('follow-level/<int:pk>', views.FollowlevelView.as_view(), name='follow_ski'),
    path('follow-loi/<int:pk>', views.FollowLoiView.as_view(), name='follow_loi'),

    path('<slug>/read/', views.readView, name='read_topic'),
    path('search/', views.search, name='search'),

    # path('<int:pk>/add_comment/', views.CommentCreateView, name = 'add_comment'),
]
