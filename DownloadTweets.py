import tweepy 
  
# Fill the X's with the credentials obtained by  
# following the above mentioned procedure. 
consumer_key = "27XwHqnsrrzIYLrAjdXrJN5Er" 
consumer_secret = "P6yrmt5Wg02MGaamGEnMdvBzQfSZrYUtW7CQ3L3BOBr7c7arOL"
access_key = "1369966434-FQDO65sm9sxsdpg4WJwGAcfjYkM1SGYLaeeZvWN"
access_secret = "2b7SJJSMnxie2wu7nEzzNX9LuFaO6xoAWg01xkj17Pus1"
  
# Function to extract tweets 
def get_tweets(username): 
          
        # Authorization to consumer key and consumer secret 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
        # Access to user's access key and access secret 
        auth.set_access_token(access_key, access_secret) 
  
        # Calling api 
        api = tweepy.API(auth) 
        search_words = "#wildfires"
        date_since = "2018-11-16"
        tweets = tweepy.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(50)
        print(tweets)
        for tweet in tweets:
            print(tweet.text)
            with open('Tweets.txt', 'a', encoding='utf-8') as f:
                print(tweet.text, file=f)
        
  
  
# Driver code 
if __name__ == '__main__': 
  
    # Here goes the twitter handle for the user 
    # whose tweets are to be extracted. 
    get_tweets("MujeebullahKLWR")  