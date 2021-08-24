from django.urls import path, include
from Alteernlingual_topic import views


urlpatterns = [ 
												
		path('ar/<slug>/read/', views.ARReadView, name='AR_read_topic'),
		path('fr/<slug>/read/', views.FRReadView, name='FR_read_topic'),
		path('yo/<slug>/read/', views.YOReadView, name='YO_read_topic'),
		path('ha/<slug>/read/', views.HAReadView, name='HA_read_topic'),
		path('ig/<slug>/read/', views.IGReadView, name='IG_read_topic'),
		path('en/<slug>/read/', views.ENReadView, name='EN_read_topic'),

		path('AR-topics/', views.ArabicList.as_view(), name='AR_topic_list'),
		path('FR-topics/', views.FrenchList.as_view(), name='FR_topic_list'),
		path('YO-topics/', views.YorubaList.as_view(), name='YO_topic_list'),
		path('HA-topics/', views.HausaList.as_view(), name='HA_topic_list'),
		path('IG-topics/', views.IgboList.as_view(), name='IG_topic_list'),
		path('EN-topics/', views.EnglishList.as_view(), name='EN_topic_list'),

		path('category/<int:pk>/', views.CategoryDetail.as_view(), name='category_detail'),
		 path('lessons', views.Lessons, name='lessons'),

		path('en/<slug:slug>/', views.EnglishTopicDetailView.as_view(), name='ETdetail'),
		path('ig/<slug:slug>/', views.IgboTopicDetailView.as_view(), name='IGdetail'),
		path('ha/<slug:slug>/', views.HausaTopicDetailView.as_view(), name='HAdetail'),
		path('yo/<slug:slug>/', views.YorubaTopicDetailView.as_view(), name='YOdetail'),
		path('fr/<slug:slug>/', views.FrenchTopicDetailView.as_view(), name='FRdetail'),
		path('ar/<slug:slug>/', views.ArabicTopicDetailView.as_view(), name='ARdetail'),
		

]
