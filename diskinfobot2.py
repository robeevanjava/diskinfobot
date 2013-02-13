import tweepy
from time import localtime, strftime
import os

def FreeSpace(drive):
    try:
        s = os.statvfs(drive)
        freespace = (s.f_bavail * s.f_frsize) / (1024*1024*1024)
	return freespace
    except:
        return 0

def TotalSpace(drive):
    try:
	s = os.statvfs(drive)
	totalspace = (s.f_blocks * s.f_frsize) / (1024*1024*1024)
	return totalspace
    except:
	return 0


def main():
    drivefree = FreeSpace("/storage/nas")
    totalspaces = TotalSpace("/storage/nas")
    timenows = strftime("%a, %d %b %Y %H:%M:%S", localtime())
    hostnm = os.uname()
    tweets = "@robeevanjava /storage/nas TOTAL: %d GB;FREE  %d GB. hostname %s. on %s" %(totalspaces,drivefree,hostnm[1],timenows)
    
    CONSUMER_KEY = '#'
    CONSUMER_SECRET = '#'
    ACCESS_KEY = '#'
    ACCESS_SECRET = '#'

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_status(tweets)
    
if __name__ == '__main__':
    main()

