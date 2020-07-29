import tweepy
consumer_key = "wXXXXXXXXXXXXXXXXXXXXXXX1"
consumer_secret = "qXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXh"
access_token = "9XXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXi"
access_token_secret = "kXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXT"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


nama = "NamaOrang"
jumlahtweet = 85
keyword = ['covid', 'corona', 'odp']
tweet = []
covid = []

hasil = api.user_timeline(id=nama, count=jumlahtweet)

for tweet in hasil:
    tweet.append(tweet.text)


for i in tweet:
    for x in keyword:
        if x in i.lower():
            covid.append(i)

print(len(covid))
