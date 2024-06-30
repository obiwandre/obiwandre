import subprocess
import sys
import time
from dotenv import load_dotenv
import os

load_dotenv()
GITHUB_USER = os.getenv("GITHUB_USER")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
print(GITHUB_USER)
print(GITHUB_TOKEN)

def pip_reinstalar_sauron():
    package_url = f"https://{GITHUB_USER}:{GITHUB_TOKEN}@github.com/{GITHUB_USER}/sauron.git@main" 
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "--force-reinstall", f"git+{package_url}"])

