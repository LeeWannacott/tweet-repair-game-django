from django.shortcuts import render
import random

# Consumer API keys
# API key:Cqo1hdMo0aWVvPA9ICLC0O0j6
# API secret key: M6WFlQLqpFK6P70XvPH6wpBsJrAl82hyqjzbDaqBD0smYLjoND

# Access token & access token secret
# Access token :1223190251004260352-bY4N7zRVpWjBvM7i5qKkv5Hvmstsgx
# Access token secret :fpzPeiF1kkMtpHOdL2sfgbk3pJetIJtz4b6zf3c68TsHN

# Create your views here.
def home(request):
        import tweepy
        import json
        import requests


        
        from random import shuffle

        # Authenticate to Twitter
        auth = tweepy.OAuthHandler("Cqo1hdMo0aWVvPA9ICLC0O0j6", 
            "M6WFlQLqpFK6P70XvPH6wpBsJrAl82hyqjzbDaqBD0smYLjoND")

        auth.set_access_token("1223190251004260352-bY4N7zRVpWjBvM7i5qKkv5Hvmstsgx", 
            "fpzPeiF1kkMtpHOdL2sfgbk3pJetIJtz4b6zf3c68TsHN")

        api = tweepy.API(auth)

        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")
        
        tweets_list = []
        words = []
        muddled_tweets =[]
        tweet_answers = []

        if request.method == 'POST':
                topic = request.POST['topic']
        else:
                topic = 'popular'
        
        try:
                count = 10
                for tweet in api.search(topic,lang='en', result_type= 'mixed',count=count,tweet_mode = 'extended'):
                        tweet_text = tweet.full_text
                        time = tweet.created_at
                        tweeter = tweet.user.screen_name
                        tweet_dict = {"tweet_text" : tweet_text}
                        tweet_json = json.dumps(tweet_dict)
                        tweets_list.append(tweet_dict)

                import json

                for word in tweets_list:
                        for key, value in word.items():
                                words.append(value.split())
                                
                for word in words:
                        answers = word[:]
                        tweet_answers.append(answers)
                        newwords = word[:]
                        shuffle(newwords)
                        muddled_tweets.append(newwords)
                if(len(tweet_answers)>0 and len(muddled_tweets)>0):
                        random_tweet = random.randint(0,len(tweet_answers)-1)
                        muddled_tweets = [muddled_tweets[random_tweet]]
                        tweet_answers = [tweet_answers[random_tweet]]
                 
                if(len(tweet_answers)==0 or len(muddled_tweets)==0):
                    muddled_tweets = [["No","Returned","Tweets","Topic"]]
                    tweet_answers = [["Topic","Returned","No","Tweets"]]


        except: 
            time.sleep(60)

        return render(request, 'home.html', {'api' : api, 'tweets_list':tweets_list,
                'tweet_answers':tweet_answers, 'muddled_tweets':muddled_tweets})

