import json

if __name__ == "__main__":
    f = open('/Users/zhangyu/Desktop/安全教育题库.json')
    data = json.load(f)
    for item in data:
        item['title'] = item['title'].replace(' ','').replace(',', '，').replace('(', '（').replace(')', '）').replace(':', '：').replace('?', '？')
    out = open('ret.json', 'w')
    json.dump(data, out, indent=4, ensure_ascii=False)
    f.close()
    out.close()