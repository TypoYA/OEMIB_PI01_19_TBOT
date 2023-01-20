import json
import requests

API = "http://www.boredapi.com/api/activity/"


def main():
    response = requests.get(API).json()
    answer_for_user = "Занятие: " + str(response["activity"]) + ", вид деятельности: " + str(response["type"]) + \
        ", численность: " + str(response["participants"]) + \
        ", примерная стоимость: " + str(response["price"]) + " долларов."

    return answer_for_user
