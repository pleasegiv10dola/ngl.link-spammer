import json, requests, colorama, secrets, asyncio, os
from threading import Thread
count = 0

a = open("config.json", "r", encoding="utf-8")
p = json.load(a)

user = p["user"]
text = p["text"] + secrets.token_hex(16)

def title():
    os.system(f"title NGL Spammer by dart sent: {count} currently spamming @{user}")
    
title()

def Main():
    global count, count
    try:
        data = {
            "question": text,
            "deviceId": f"dd914f65-5014-4294-8139-9b48ea8bd307{secrets.token_hex(12)}{secrets.token_hex(12)}{secrets.token_hex(12)}{secrets.token_hex(12)}"
        }
        headers = {
            "User-agent": "idk"
        }
        count += 1
        r = requests.post(url=f"https://ngl.link/{user}", headers=headers, data=data)
        print(colorama.Fore.GREEN + str(r), f"SENT! " + text)
    except Exception as e:
        print(e)
    title()

def pp():
        t = Thread(target = Main)
        t.start()

while True:
    for i in range(50):
        pp()