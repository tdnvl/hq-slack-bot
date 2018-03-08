import requests


def lambda_handler(event, context):
    url = open("url.txt", "r")
    url_request = url.readline()
    payload = {'channel': 'testest', 'username': 'HQ Bot', 'icon_emoji': ':clock3:',
               'text': '[TEST] HQ starts in 15 minutes!'}
    r = requests.post(url_request, json=payload)
    url.close()


lambda_handler(0, 0)
