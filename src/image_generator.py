import os
import shutil
import logging

from BingImageCreator import ImageGen
from bing_brush.bing_brush import BingBrush

base_file_name = "generated_image"
logger = logging.getLogger(__name__)


def generate_image_bing_brush(prompt: str) -> str:
    output_path = os.getenv("IMAGE_STORAGE_DIR")
    max_wait_time_seconds = int(os.getenv("BING_BRUSH_MAX_WAIT_TIME_SECONDS"))
    cookie_path = os.getenv("BING_BRUSH_COOKIE_PATH")

    if os.path.exists(output_path):
        shutil.rmtree(output_path)
        os.mkdir(output_path)

    logger.debug(
        f"Using Bing Brush, max wait time: {max_wait_time_seconds} seconds. Prompt: {prompt}"
    )
    brush = BingBrush(cookie=cookie_path, max_wait_time=max_wait_time_seconds)

    brush.process(prompt=prompt, out_folder=output_path)
    # BingBrush outputs a .svg.jpg file which is actually an .svg of a placeholder svg of a paintbrush
    # and not what we want, so only look at files starting with OIG
    image_files = [file for file in os.listdir(output_path) if file.startswith("OIG")]
    logger.info(f"generated files: {image_files}")
    selected_file = os.path.join(output_path, image_files[0])
    logger.info(f"selecting file {selected_file}")
    return selected_file


def generate_image_bing_image_creator(prompt: str) -> str:
    output_path = os.getenv("IMAGE_STORAGE_DIR")
    auth_cookie = os.getenv("BING_AUTH_COOKIE")
    auth_cookie_SRCHHPGUSR = os.getenv("BING_AUTH_COOKIE_SRCHHPGUSR")
    image_gen = ImageGen(
        auth_cookie=auth_cookie,
        auth_cookie_SRCHHPGUSR=auth_cookie_SRCHHPGUSR,
    )
    images = image_gen.get_images(prompt)

    expected_output_file = os.path.join(output_path, f"{base_file_name}_0.jpeg")
    if os.path.exists(expected_output_file):
        os.remove(expected_output_file)

    image_gen.save_images(
        links=images, output_dir=output_path, file_name=base_file_name, download_count=1
    )

    return os.path.join(output_path, f"{base_file_name}_0.jpeg")
