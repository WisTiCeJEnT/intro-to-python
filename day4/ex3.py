import requests
page = requests.get('https://www.niceoppai.net/tsuyokute_new_saga')
text = page.text
a = text.split('\n')
for i in range(len(a)):
    if 'ตอนที่' in a[i]:
        print(a[i])
        break
