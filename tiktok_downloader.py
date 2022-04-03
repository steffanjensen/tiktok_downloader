import requests
import re
import time
import os


# Connects to animemoe api (video without watermark) and your video
urls = [
    "https://tiktod.animemoe.us/api/?url=https://www.tiktok.com/@yourusername/video/video_id",
  
]

payload={}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'
}

number = 1
for url in urls:
    response = requests.request("GET", url, headers=headers, data=payload)
    res = response.text
    m = re.findall('video":"(.+?)"}', res)
    nym = str(m)
    nymm = nym.replace("['", "").replace("']", "")
    print(nymm)
    time.sleep(2)
    nyeste = nymm.encode()
    os.system('wget -O tiktok' + str(number) + ".mp4 " + nymm)
    newnumber = int(number)
    number = newnumber + 1
    print(str(number))
    time.sleep(5)
