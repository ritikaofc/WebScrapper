import requests
from bs4 import BeautifulSoup


YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending'

response = requests.get(YOUTUBE_TRENDING_URL)

print('status code', response.status_code)

with open('trending.html','w') as f:
  f.write(response.text)

doc = BeautifulSoup(response.text,'html.parser')

print('Page Title:', doc.title.text)

#Find all the video divs
video_divs = doc.find_all('div',class_ = 'ytd-video-renderer')


print(f'Found {len(video_divs)} videos')