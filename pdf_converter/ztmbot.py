import tweepy
import time

auth = tweepy.OAuthHandler('key', 'secret_key')
auth.set_access_token('acccesskey',
                      'secretaccesskey')

api = tweepy.API(auth)
user = api.me()


def limit_handle(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(2 * 60)


number = 10

for follower in limit_handle(tweepy.Cursor(api.followers).items()):

    api.destroy_friendship(follower.id)
    number += 1
    print(number)
