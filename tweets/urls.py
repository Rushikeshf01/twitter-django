from django.urls import path, include
from .views import TweetCreateView, TweetDisplayView, TopTweetDisplayView
from rest_framework.routers import DefaultRouter

# created : yashvi ghetiya
app_name = "tweets"
router = DefaultRouter()
router.register(r"tweet", TweetCreateView, basename="tweet")
router.register(r"gettweets", TweetDisplayView, basename="tweet_get")
router.register(r"gettoptweets", TopTweetDisplayView, basename="top_tweet_get")
urlpatterns = [path("", include(router.urls))]