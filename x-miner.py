import streamlit as st
import tweepy
from dotenv import load_dotenv
import os

load_dotenv()

bearer_token = os.getenv('bearer_token')

client = tweepy.Client(bearer_token=bearer_token)

st.title("X (Twitter) User's Recent Tweets")

username = st.text_input("Enter X (Twitter) username:")

if username:
    try:
        user = client.get_user(username=username)
        user_id = user.data.id
        tweets = client.get_users_tweets(id=user_id, max_results=5, tweet_fields=["created_at"])
        if tweets.data:
            st.subheader(f"Latest Tweets from @{username}:")
            for tweet in tweets.data:
                st.write(f"**{tweet.created_at.strftime('%Y-%m-%d %H:%M:%S')}**: {tweet.text}")
        else:
            st.info("No tweets found for this user.")
    except tweepy.TooManyRequests:
        st.error("Rate limit exceeded. Please wait a few minutes and try again.")
    except Exception as e:
        st.error(f"Error: {e}")

