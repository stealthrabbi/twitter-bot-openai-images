import os
import shutil

from BingImageCreator import ImageGen

output_path = "./output"
base_file_name = "generated_image"


def generate_image(prompt: str) -> str:
    shutil.rmtree(output_path, True)
    os.mkdir(output_path)

    auth_cookie = os.getenv("BING_AUTH_COOKIE")
    auth_cookie_SRCHHPGUSR = os.getenv("BING_AUTH_COOKIE_SRCHHPGUSR")
    image_gen = ImageGen(
        auth_cookie=auth_cookie,
        auth_cookie_SRCHHPGUSR=auth_cookie_SRCHHPGUSR,
    )
    images = image_gen.get_images(prompt)

    image_gen.save_images(
        links=images, output_dir=output_path, file_name=base_file_name, download_count=1
    )

    return os.path.join(output_path, f"{base_file_name}_0.jpeg")
