import tweepy
import sys
import webbrowser 
import urllib



CONSUMER_KEY = 'VQLDtkDTlbAmT95m5cMsYQ'
CONSUMER_SECRET = 'bAC0BF69qiEVARJlfFJZZCDQ9mrcqofq16ilQ4OjU'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth_url =auth.get_authorization_url()
print 'Go to the browser to autanticate '
webbrowser.open(auth_url)
print  auth_url
shost = raw_input('AFTER AUTENTICATION PRESS ENTTER  ').strip()
try:
	auth.get_access_token(shost)
except tweepy.TweepError:
    print 'Error! Failed to get request token'
api = tweepy.API(auth)
f=open('ACCESS_KEY' ,'w')
f1=open('ACCESS_SECRET','w')
f2=open('user_info' ,'w')

f.write(auth.access_token.key)
f1.write(auth.access_token.secret)

f.close()
auser=api.me()
print auser.id
f2.write('%s\n' % auser.screen_name)
f2.write('%s' % auser.id)
f2.close
f1.close 

urllib.urlretrieve (auser.profile_image_url, "%s.jpg" % auser.id)
















