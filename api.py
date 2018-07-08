#Q1
#An access token is an object that describes the security context of a process or thread.
#The information in a token includes the identity and privileges of the user account associated with the process or thread
#accesstoken of my twitter app-1014136076305395713-NPYj9iQWBvMmJdY35itR3iKloQsjUR


#Q2
import socket

webs1 = socket.gethostbyname('google.com')
webs2 = socket.gethostbyname('Facebook.com')

print(webs1, webs2)

#Q3
import tweepy 
ckey= 'pWsU0qAXtMrSWYnDAgH0JenAO'
csecret='BP07hWcDK8o6FZnEiclMBqMMzUQgr2bdjA1OEQOiPimhUCR0ZI'
atoken='1014136076305395713-NPYj9iQWBvMmJdY35itR3iKloQsjUR'
asecret='g0T181VuFPYQIXIfoCzv3wn3tu7BQKJOMFjBuQ65kyJlz'
auth=tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
api=tweepy.API(auth)
public_tweets=api.search('world cup')
for i in public_tweets:
    print(i)                     
                         
                         
#Q4
'''The library contains built-in modules (written in C) that provide access to system functionality such as file I/O that would otherwise be inaccessible to Python
programmers,as well as modules written in Python that provide standardized solutions for many problems that occur in everyday programming.'''
'''API-a set of functions and procedures that allow the creation of applications which access the features or data of an operating system, application, or other service.'''
    
