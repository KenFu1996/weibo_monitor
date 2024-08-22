import time,requests,csv,os,numpy as np
from datetime import datetime

def init():
    if not os.path.exists('./articleData.csv'):
        with open('./articleData','w',encoding='utf-8',newline='') as csvFile:
            writer=csv.writer(csvFile)
            writer.writerow([
                'id'
                'region_name',
                'text_raw',
                'screen_name'
            ])

def writerRow(row):
    if not os.path.exists('./articleData.csv'):
        with open('./articleData', 'a', encoding='utf-8', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)

def get_data(url,params):
    headers={
        'cookie':'SCF=Ajn5w3I6vr72GCjy1qfOU4cjM4wV3tR8cMUaX2-fqvgor2-F-6TCZV-NuH2vtmjcTwORI1RBvrm15867cDrBkdE.; SINAGLOBAL=8529245482618.222.1724036068243; ULV=1724036068245:1:1:1:8529245482618.222.1724036068243:; SUB=_2A25LxsRJDeRhGeNI6FEX9SvLzDqIHXVoulmBrDV8PUNbmtAbLWbgkW9NSGrjPyDHwtAEpZwgq_ciCnjhkIuQahCG; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W51EBH0wQW9pfSSaF97wf.T5NHD95QfSoe0So-fS0McWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNSKq0e0qfSKMNSntt; ALF=02_1726628122; XSRF-TOKEN=t3EzMWAe3Xw0MZx-K1w2j6JH; WBPSESS=Dt2hbAUaXfkVprjyrAZT_BlY3VvkjS25J6_bASM0Ywm59uiBxLRUOJp14r5VXqeYu_JEVouMYygdvpeAcpQjUCziqdLNLkWoTchbFoQfG3vO1-bXxN4pf_qjbVeBp7C8i131pwL6dn3glNCAR4wGHuTxFjV7uG9YsMJS-1DYPmfjinrOK8ytokm33C4UGKt-tbi_iq0jK-4-LRL3exNDkw==',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
    }
    params = {
        'is_new_segment': 1,
        'fetch_hot': 1
    }
    response= requests.get(url,headers=headers,params=params)
    if response.status_code==200:
        return  response.json()['statuses']
    else:
        return None

def getALLTypeList():
    typelist=[]
    with open('./navData','r',encoding='utf-8') as reader:
        readerCSV=csv.reader(reader)
        next(reader)
        for nav in readerCSV:
            typelist.append(nav)
    return typelist


def parse_json(response):
    for article in response:
        id=article['id']
        try:
            region_name=article['region_name'].replace('发布于','')
        except:
            region_name='无'
        content=article['text_raw']
        name=article['user']['screen_name']
        writerRow([ id,region_name,content,name])
        print(name)


def start(typenum=3,pagenum=2):
    articleURL='https://weibo.com/ajax/feed/hottimeline?since_id=0&refresh=0&group_id=102803&containerid=102803&extparam=discover%7Cnew_feed&max_id=0&count=10'
    init()
    typelist=getALLTypeList()
    typenumcount=0
    for type in typelist:
        if typenumcount > typenum:return
        for page in range(0, pagenum):
            print('正在打印：%s 中的第 %s 页文章数据' % (type[0], page+1))
            params={
                'group_id':type[1],
                'containerid':type[2],
                'max_id':page,
                'count':10,
                'extparam':'discover|new_feed'
            }
            response=get_data(articleURL,params)
            parse_json(response)



if __name__=='__main__':
    start()
