import twitter
import time

api = twitter.Api(consumer_key='0Hmdz14YxHWFoLnv771r1QBpc',
    consumer_secret='RrD468SWM0Y4h2VZKd9FqESvlbyUeNul0TdCxYJPiyaWAuNKZp',
    access_token_key='3034207177-v77OfvESxcyiyDMxzExpJbiRKDhB9m7lLq5STQ6',
    access_token_secret='kqhXseRPYWIhpJKclWpyEpQ1yZpDeCdP3hwUsyNsBZMr4')

thetime = time.strftime("%I-%M")

print('welcome to the tweeter!')

content = ''

while content != 'no more':
    content = raw_input('what do you want to tweet? if nothing, type "no more"')
    if content == 'no more': break
    status = api.PostUpdate(content)
