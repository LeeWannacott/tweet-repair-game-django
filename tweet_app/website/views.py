from django.shortcuts import render

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
	
	print('test')

	tweets_list = []
	testcrap = []
	muddled_tweets =[]
	# user = api.get_user(screen_name = 'theresa_may')  
	# print(user.id)
	try:
		for tweet in api.search('airplanes',result_type='popular',count=5):
			#print(tweet.text)
			tweet_text = tweet.text
			time = tweet.created_at
			tweeter = tweet.user.screen_name
			tweet_dict = {"tweet_text" : tweet_text}
			#print(type(tweet_dict))
			tweet_json = json.dumps(tweet_dict)
			#print(type(tweet_json))
			tweets_list.append(tweet_dict)
			#print(type(tweets_list))

		for word in tweets_list:
			#print(word)
			for key, value in word.items():
				testcrap.append(value.split())
				#print(testcrap)

			
		for words in testcrap:
			#print(word)
			answers = words[:-1]
			newwords = words[:-1]
			shuffle(newwords)
		
			muddled_tweets.append(newwords)
			#print(testcrap2)

	except:
	    time.sleep(60)

	return render(request, 'home.html', {'api' : api, 'tweets_list':tweets_list,
		'testcrap':testcrap, 'muddled_tweets':muddled_tweets, 'answers':answers,'newwords':newwords})