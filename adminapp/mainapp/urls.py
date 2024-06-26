from django.urls import path, include, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("career-categories", views.CareerCategoryViewSet, "career-category")
router.register("questions", views.QuestionViewSet, "question")
router.register("answers", views.AnswerViewSet, "answer")
router.register("users", views.UserViewSet, 'user')
router.register("surveys", views.SurveyViewSet, 'survey')
router.register("universities", views.UniversityViewSet, 'university')
router.register("feedbacks", views.FeedBackViewSet, 'feedBack')

urlpatterns = [
    path('', include(router.urls)),
    path('oauth2-info/', views.AuthInfo.as_view()),
    path('answers/vietnamese_classification', views.AnswerViewSet.as_view({'get': 'predict'}), name='vietnamese_classification'),
    path('answers/music_suggest', views.AnswerViewSet.as_view({'get': 'music_suggest'}), name='music_suggest'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
