import requests
from bs4 import BeautifulSoup
import json
def get_time_stories():
    url = "https://time.com"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('article', class_='swipe-h')
        
        latest_stories = []
        for article in articles[:6]:
            title = article.find('h3', class_='title').text.strip()
            link = article.find('a')['href']
            if not link.startswith('https://time.com'):
                link = 'https://time.com' + link
            latest_stories.append({
                "title": title,
                "link": link
            })
        
        return latest_stories
    else:
        print("Failed to retrieve Time.com")

# Testing the function
        
if __name__ == "__main__":
    stories = get_time_stories()
    if stories:
        print(json.dumps(stories, indent=2))


# from flask import Flask, jsonify
# import requests
# from bs4 import BeautifulSoup

# app = Flask(__name__)

# def get_time_stories():
#     url = "https://time.com"
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#         articles = soup.find_all('article', class_='swipe-h')
        
#         latest_stories = []
#         for article in articles[:6]:
#             title = article.find('h3', class_='title').text.strip()
#             link = article.find('a')['href']
#             if not link.startswith('https://time.com'):
#                 link = 'https://time.com' + link
#             latest_stories.append({
#                 "title": title,
#                 "link": link
#             })
        
#         return latest_stories
#     else:
#         return None

# @app.route('/getTimeStories')
# def get_time_stories_api():
#     stories = get_time_stories()
#     if stories:
#         return jsonify(stories)
#     else:
#         return "Failed to retrieve Time.com", 500

# if __name__ == "__main__":
#     app.run(debug=True)
