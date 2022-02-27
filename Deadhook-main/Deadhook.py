import requests
import random
import time
import json
import os
os.system('title Deadhook - Config')
done = 1
messages = ''
try:
    with open('messages.txt') as f:
        messages = f.read()
except:
    print('\u001b[0m\u001b[31m[\u001b[0m-\u001b[31m] Failed! \u001b[33mCould not find "messages.txt", did you remove it?')
    os.system('title ERROR - Missing files! && PAUSE >nul')
    os._exit(0)

os.system('title Deadhook - Enter webhook URL!')
webhook = input('\u001b[0m\u001b[32;1m[\u001b[0m?\u001b[32;1m] To start, \u001b[0m\u001b[33menter the webhook! \u001b[0m>>>\u001b[33m ')
hookInfo = requests.get(webhook)
if hookInfo.status_code == 401:
    print('\u001b[0m\u001b[31m[\u001b[0m-\u001b[31m] Failed! \u001b[33mInvalid webhook!')
    os.system('title ERROR - Invalid webhook! && PAUSE >nul')
    os._exit(0)

hookName = hookInfo.json()['name']
os.system('title Deadhook - Enter number of messages to be sent!')
times = input('\u001b[0m\u001b[32;1m[\u001b[0m?\u001b[32;1m] (Enter a NUMBER) \u001b[0m\u001b[33mhow many times do you want to spam the webhook? \u001b[0m>>>\u001b[33m ') or 69
try:
    times = int(times)
except:
    print('\u001b[0m\u001b[31m[\u001b[0m-\u001b[31m] Failed! \u001b[33mYou did not enter a valid number, going with 69!')
    times = 69

os.system('title Deadhook - Ready')
print(f'\u001b[0m\u001b[32;1m[\u001b[0m+\u001b[32;1m] Ready! \u001b[0m\u001b[33mSpamming webhook "{hookName}" {times} times! (Press ENTER to begin)\n\u001b[0m')
os.system('PAUSE >nul')
while done < times:
    tempMsg = random.choice(messages.splitlines())
    w = requests.post(webhook, json={'content':tempMsg})
    if w.status_code == 429:
        os.system(f'title Deadhook - Error! (#{done})')
        print('\u001b[0m\u001b[31m[\u001b[0m-\u001b[31m] Failed! \u001b[33mRatelimited! Waiting a couple seconds...')
        time.sleep(3)
    else:
        os.system(f'title Deadhook - Spamming! (#{done})')
        print(f'\u001b[0m\u001b[32;1m[\u001b[0m+\u001b[32;1m] Success! \u001b[0m\u001b[33mSent message "{tempMsg}"! (#{done})\u001b[0m')
        done += 1
    time.sleep(0.6)
requests.delete(webhook)
print(f'\u001b[0m\u001b[32;1m[\u001b[0m+\u001b[32;1m] Success! \u001b[0m\u001b[33mDeleted webhook!\u001b[0m')
os.system(f'title Deadhook - Deleted webhook after spamming {done} times!')
print(f'\u001b[0m\u001b[32;1m[\u001b[0m+\u001b[32;1m] Report: \u001b[0m\u001b[33mSpammed webhook "{hookName}" {times} times!\n\u001b[0m')
os.system('PAUSE >nul')