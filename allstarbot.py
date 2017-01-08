import twitter
import time
from datetime import datetime
from threading import Timer

api = twitter.Api(consumer_key='0Hmdz14YxHWFoLnv771r1QBpc',
    consumer_secret='RrD468SWM0Y4h2VZKd9FqESvlbyUeNul0TdCxYJPiyaWAuNKZp',
    access_token_key='3034207177-v77OfvESxcyiyDMxzExpJbiRKDhB9m7lLq5STQ6',
    access_token_secret='kqhXseRPYWIhpJKclWpyEpQ1yZpDeCdP3hwUsyNsBZMr4')

def getsecs():
    x=datetime.today()
    y=x.replace(day=x.day+1, hour=1, minute=0, second=0, microsecond=0)
    t=y-x
    return t.seconds+1

def vote():
    print('voting...')
    status = api.PostUpdate('Zaza Pachulia #NBAVote')
    status = api.PostUpdate('Stephen Curry #NBAVote')
    status = api.PostUpdate('Russell Westbrook #NBAVote')
    status = api.PostUpdate('Anthony Davis #NBAVote')
    status = api.PostUpdate('James Harden #NBAVote')
    status = api.PostUpdate('Giannis Antetokounmpo #NBAVote')
    status = api.PostUpdate('Draymond Green #NBAVote')
    status = api.PostUpdate('Kevin Durant #NBAVote')
    print('...your votes have been tweeted')
    secs = getsecs()
    t = Timer(secs, vote)
    t.start()

vote()
