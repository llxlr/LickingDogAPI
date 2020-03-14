from dotenv import load_dotenv
import os

load_dotenv(verbose=True)
# Pixiv
PIXIV_EMAIL = os.getenv("PIXIV_EMAIL")
PIXIV_PASSWD = os.getenv("PIXIV_PASSWD")
# CloudFlare
cf_zone_id = os.getenv("cf_zone_id")
cf_email = os.getenv("cf_email")
cf_auth_key = os.getenv("cf_auth_key")
# Baidu AI API
Baidu_APP_ID = os.getenv("APP_ID")
Baidu_API_KEY = os.getenv("API_KEY")
Baidu_SECRET_KEY = os.getenv("SECRET_KEY")


if __name__ == "__main__":
    pass
