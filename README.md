# AutomaticTweetPosting
In today's world, everyone is using social media and twitter is one of the most trending one but what if you wouldn't have to reply to every tweet? That's possible by making an automatic tweet generator program.

Automatic tweet posting is one of the most interesting things as it is easy to implement and can save your time if you don't want to reply to the same type of tweets, it is also easy to implement as you only have to get your hands on the python package tweepy and Twitter APIs.

First, make sure you have a Twitter account with a verified phone number and Email Id. Now search for a Twitter developer account on any web browser. Click on "Apply for a developer Account", while doing this you should be logged in to your Twitter account. Once you have created your twitter developer account, create a new project and see if you have access to keys of not. Make your that access token and secret should have read and write permissions.

The easiest way to install tweepy is using:   pip install tweepy or install directly from the GitHub repository:   pip install -U git+https://github.com/tweepy/tweepy.git@2efe385fc69385b57733f747ee62e6be12a1338b

The first step is to import the packages, we will be using tweepy and time for this project. The next step involves making an OuthHandler instance, into this we will pass our consumer key and secret key. The API class provides access to entire twitter RESTful API methods.  We will be using auth as a parameter for our API class and will sue the keys from Twitter Developer account.

Now we will be using API.mentions_timeline, it returns 20 most recent mentions, including retweets, furthermore, we will be printing tweet id and mentions using this API class.

Now make a recently_seen_id.txt file. This will contain the ID of the tweet that our project has seen last. If you see any errors when running the main file, try replacing the content with the ID of one of the tweets you want to assess. Make sure it is in the same directory or folder as your Python script. Moreover, we will retrieve and store the recently seen ID. Finally, make a reply_to_tweet function, firstly it will be retrieving the recently seen ID. In mentions, we need to use tweet_mode= 'extended ' to show all full tweets or long tweets would get cut off. Specify the keyword for which you want to generate a particular reply, here we have use ‘true’ as keyword and ‘agree’ as tweet reply and at last set the sleep time, it would generate the tweets in that particular interval. 
