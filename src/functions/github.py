#import telebot
import requests
import os

def get_commits(message, bot):
    githubtoken = os.environ["GITHUBTOKEN"]
    hs = {"Accept":"application/vnd.github+json", "Autorization": f'Bearer {githubtoken}'}
    url = "https://api.github.com/repos/IHVH/OEMIB_PI01_19_TBOT/commits"
    response = requests.get(url, headers=hs)
    if(response):
        commits = response.json()
        for cmt in commits:
            msg = cmt["commit"]["message"]
            url = cmt["html_url"]
            name = cmt["commit"]["committer"]["name"]
            date = cmt["commit"]["committer"]["date"]
            send_msg = f'{name} - {msg} - {date} - {url}'
            bot.send_message(text=f'{send_msg}', chat_id= message.chat.id)
    else:
        bot.send_message(text=f'{response.status_code}', chat_id= message.chat.id)
