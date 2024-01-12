from BingImageCreator import ImageGen


auth_cookie = "1z34Ed1ufknHorpE1Xx-4OctB01AQqfVTb4yB4-CIR6Xnorpk2tE6WJzLFdp2DMDI8nzLfO9joSWdWF-XThysJLDQrUyNNHb0pQEpRC8Tt54gIiEc9qyTcfDq1CFXikviOGZ2aLHCr2aLUpf2inGz86aRE5Qa7gSgdyPzPLMabqvSDEhLJ_yfgof_UH8QD0LVf28Hx6oBMjJOOewqMyog2rwZaB6G8u1L1nbVuTNeoGo"
#   "1z34Ed1ufknHorpE1Xx-4OctB01AQqfVTb4yB4-CIR6Xnorpk2tE6WJzLFdp2DMDI8nzLfO9joSWdWF-XThysJLDQrUyNNHb0pQEpRC8Tt54gIiEc9qyTcfDq1CFXikviOGZ2aLHCr2aLUpf2inGz86aRE5Qa7gSgdyPzPLMabqvSDEhLJ_yfgof_UH8QD0LVf28Hx6oBMjJOOewqMyog2rwZaB6G8u1L1nbVuTNeoGo"
# zzzzzzzzzzz = "1z34Ed1ufknHorpE1Xx-4OctB01AQqfVTb4yB4-CIR6Xnorpk2tE6WJzLFdp2DMDI8nzLfO9joSWdWF-XThysJLDQrUyNNHb0pQEpRC8Tt54gIiEc9qyTcfDq1CFXikviOGZ2aLHCr2aLUpf2inGz86aRE5Qa7gSgdyPzPLMabqvSDEhLJ_yfgof_UH8QD0LVf28Hx6oBMjJOOewqMyog2rwZaB6G8u1L1nbVuTNeoGo"
# auth_cookie_SRCHHPGUSR = "SRCHLANG=en&IG=46FEA7028A584CC2A7DB6E1DB45610DC&BRW=XW&BRH=S&CW=1920&CH=505&SCW=1920&SCH=112&DPR=1.0&UTC=-300&DM=1&WTS=63840686312&HV=1705089620&PRVCW=1920&PRVCH=1047&CIBV=1.1467.3&EXLTT=1&cdxtone=Creative&cdxtoneopts=,memdefadcst2"
auth_cookie_SRCHHPGUSR = "zzqwerewr"


def generate_image(prompt: str) -> None:
    image_gen = ImageGen(
        auth_cookie=auth_cookie, auth_cookie_SRCHHPGUSR=auth_cookie_SRCHHPGUSR
    )
    images = image_gen.get_images(prompt)

    image_gen.save_images(
        links=images, output_dir="./", file_name="generated_image", download_count=1
    )


if __name__ == "__main__":
    generate_image(
        "Create a realistic image of Barney the Dinsoaur folding the laundry"
    )
