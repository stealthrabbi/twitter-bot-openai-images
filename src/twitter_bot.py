import os
from datetime import datetime
import logging
import time
from typing import List

import tweepy


logger = logging.getLogger(__name__)

# see https://docs.tweepy.org/en/stable/examples.html


class TwitterBot:
    """Handles authentication and sending of tweets"""

    def __init__(self):
        access_token = os.getenv("IMAGE_BOT_ACCESS_TOKEN")
        access_token_secret = os.getenv("IMAGE_BOT_ACCESS_TOKEN_secret")

        # AKA consumer key/secret
        consumer_key = os.getenv("IMAGE_BOT_CONSUMER_KEY")
        consumer_secret = os.getenv("IMAGE_BOT_CONSUMER_SECRET")

        bearer_token = os.getenv("image_bot_bearer_token")

        self.client = tweepy.Client(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token,
            access_token_secret=access_token_secret,
            bearer_token=bearer_token,
        )
        auth = tweepy.OAuth1UserHandler(
            consumer_key, consumer_secret, access_token, access_token_secret
        )
        self.api = tweepy.API(auth)

    def post_image_tweet(self, message: str, image_path: str):
        logger.info(f"creating image twee with text {message}")
        logger.info(f"uploading image at {image_path}")
        media = self.api.media_upload(image_path)
        tweet = self.client.create_tweet(text=message, media_ids=[media.media_id])
        logger.debug(f"created tweet: {tweet}")
