import json

#ví dụ với công nghệ
with open('content_congnghe.json','rb') as f:
    data = json.load(f)

print(len(data))
with open('content_congnghe_1000.json','w', encoding='utf8') as f:
     json.dump(data[:1000],f,ensure_ascii=False)