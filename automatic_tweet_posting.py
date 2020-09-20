import tweepy
import time 

print("Automatic tweet posting")

CONSUMER_KEY = 'DDDD'
CONSUMER_SECRET = 'MMMM'
ACCESS_KEY = 'XXXX'
ACCESS_SECRET = 'WWWW'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

mentions = api.mentions_timeline()

for mention in mentions:
    print(str(mention.id)+'-'+mention.text)



#importing packages
CONSUMER_KEY = 'DDDD'
CONSUMER_SECRET = 'XXXX'
ACCESS_KEY = 'YYYY'
ACCESS_SECRET = 'ZZZZ'



auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# automatic tweet posting recently seen id .txt file
FILE_NAME = 'recently_seen_id.txt'

#retrieving and storing recently seen ID

def retrieve_recently_seen_id(file_name):
    f_read = open(file_name, 'r')
    recently_seen_id = int(f_read.read().strip())
    f_read.close()
    return recently_seen_id

def store_recently_seen_id(recently_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(recently_seen_id))
    f_write.close()
    return
# Replying to tweets
def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
   
    recently_seen_id = retrieve_recently_seen_id(FILE_NAME)
   
    mentions = api.mentions_timeline(
                        recently_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_recently_seen_id(recently_seen_id, FILE_NAME)
        if 'true' in mention.full_text.lower():
            print('found true', flush=True)
            print('responding back...yes', flush=True)
            api.update_status('@' + mention.user.screen_name +
                    'agree!', mention.id)

while True:
    reply_to_tweets()
    time.sleep(3)
