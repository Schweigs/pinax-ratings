from django.conf.urls import patterns, url


urlpatterns = patterns(
    "agon_ratings.views",
    url(r"^(?P<content_type_id>\d+)/(?P<object_id>\d+)/rate/$", "rate", name="agon_ratings_rate"),
)
