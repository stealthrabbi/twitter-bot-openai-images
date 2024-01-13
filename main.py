import logging
import os

from dotenv import load_dotenv

from src.image_generator import generate_image
from src.twitter_bot import TwitterBot
from src.prompt_generator import generate_prompt


def _configure_logger() -> None:
    # Configure the root logger
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )


def post_image_tweet():
    logger = logging.getLogger(__name__)
    # prompt = get_random_prompt()
    base_prompt = os.getenv("BASE_PROMPT")
    description = generate_prompt("image_prompt_list.txt")
    prompt = base_prompt + description

    logger.debug(f"prompt: {prompt}")
    image_file_path = generate_image(prompt)
    twitter_bot = TwitterBot()

    logger.info(f"posting AI tweet: {description}")
    twitter_bot.post_image_tweet(description, image_file_path)


def main(request=None):
    _configure_logger()
    logger = logging.getLogger(__name__)
    load_dotenv()
    post_image_tweet()
    logger.info("DONE")


if __name__ == "__main__":
    main()
