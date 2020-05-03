from jsondata import JSON_DATA

json_list = []
for k in JSON_DATA.keys():
    val = JSON_DATA[k]
    if '将来の夢' in val.keys():
        print(k, val['name'], val['種族'], val['性格'], val['口ぐせ'], val['将来の夢'], val['座右の銘'])
    else:
       print(k, val['name'], val['種族'], val['性格'], val['口ぐせ'])


