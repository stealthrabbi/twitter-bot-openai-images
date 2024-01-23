import logging
import os

from dotenv import load_dotenv

from src.image_generator import (
    generate_image_bing_brush,
    generate_image_bing_image_creator,
)
from src.twitter_bot import TwitterBot
from src.prompt_generator import generate_prompt


def _configure_logger() -> None:
    # Configure the root logger
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )


def post_image_tweet():
    logger = logging.getLogger(__name__)
    # prompt = get_random_prompt()
    base_prompt = os.getenv("BASE_PROMPT")
    description = generate_prompt("image_prompt_list.txt")
    prompt = base_prompt + description

    logger.info(f"prompt: {prompt}")

    try:
        logger.debug("using BingBrush")
        image_file_path = generate_image_bing_brush(prompt)
        _post_tweet_image_at_path(logger, description, image_file_path)
    except BaseException as err:
        logger.error(f"Error using bing brush: {err}")
        logger.debug("Bing Brush failed. Trying Bing Image Creator")
        image_file_path = generate_image_bing_brush(prompt)
        _post_tweet_image_at_path(logger, description, image_file_path)


def _post_tweet_image_at_path(logger, description, image_file_path):
    logger = logging.getLogger(__name__)
    twitter_bot = TwitterBot()

    tweet_suffix = os.getenv("TWEET_SUFFIX") or ""

    description = description + tweet_suffix
    logger.info(f"posting AI tweet: {description}")

    twitter_bot.post_image_tweet(description, image_file_path)


def main(request=None):
    _configure_logger()
    logger = logging.getLogger(__name__)
    load_dotenv()
    post_image_tweet()
    logger.info("DONE")
    return "Successful tweet! Done main"


if __name__ == "__main__":
    main()
