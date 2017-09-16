import tweepy

from inigo_secrets import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_KEY_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_KEY_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# get max of 15 since the last tweet on my home timeline                                                                                           \
                                                                                                                                                    
timeline = api.home_timeline()
matches = api.search(q="inconceivable",rpp=15, since_id=timeline[0].id)

for tweet in matches:
    #dont respond to your own tweets, inigobot!                                                                                                     
    if not tweet.user.id == 908060967061377024:
        try:
            if tweet.retweeted_status:
                isRetweet = True
        except AttributeError:
            isRetweet = False

        link = "https://twitter.com/%s/status/%d" %(tweet.user.screen_name,tweet.id)
        try:
            if not isRetweet:
                t=api.update_status("You keep using that word, I do not think it means what you think it means...%s" %(link,))
            else:
                print "I will not reply to this retweet"
        except tweepy.error.TweepError, e:
            print e