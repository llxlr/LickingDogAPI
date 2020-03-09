from dotenv import load_dotenv
load_dotenv(verbose=True)
import os

PIXIV_EMAIL = os.getenv("PIXIV_EMAIL")
PIXIV_PASSWD = os.getenv("PIXIV_PASSWD")

cf_zone_id = os.getenv("cf_zone_id")
cf_email = os.getenv("cf_email")
cf_auth_key = os.getenv("cf_auth_key")


if __name__ == "__main__":
    # print(PIXIV_EMAIL)
    # print(PIXIV_PASSWD)

    print(cf_zone_id)
    print(cf_email)
    print(cf_auth_key)

    pass
