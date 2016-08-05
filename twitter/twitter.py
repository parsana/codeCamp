from twython import Twython

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

message = "put message here"
twitter.update_status(status=message)
print("Tweeted: %s" % message)

#with open('/home/pi/Downloads/image.jpg', 'rb') as photo:
#    twitter.update_status_with_media(status=message, media=photo)
