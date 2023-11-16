from django.urls import path
from .views import UploadFeed, Check_duplicate, Date_feed_send

urlpatterns = [
    path('upload', UploadFeed.as_view()),
    path('check_duplicate', Check_duplicate.as_view()),
    path('date_feed_send', Date_feed_send.as_view()),
]
