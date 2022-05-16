from dotenv import load_dotenv
import os

load_dotenv()
CLIENT_SECRET = os.environ["SPOTIFY_SECRET"]
CLIENT_ID = os.environ["SPOTIFY_ID"]
