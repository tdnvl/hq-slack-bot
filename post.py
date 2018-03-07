import requests

payload = {'channel':'random', 'username':'HQ Bot', 'icon_emoji':'clock3:', 'text':'[TEST] HQ starts in 15 minutes!'}

r = requests.post("http://httpbin.org/post", data=payload)

print(r)

r.status_code
