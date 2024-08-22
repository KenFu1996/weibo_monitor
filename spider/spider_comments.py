import time,requests,csv,os,numpy as np
from datetime import datetime

def init():
    if not os.path.exists('./articleCommentsData.csv'):
        with open('./articleCommentsData','w',encoding='utf-8',newline='') as csvFile:
            writer=csv.writer(csvFile)
            writer.writerow([
                'articleid',
                'region',
                'content',
                'authorName',
                'authorAddress',
                'authorAvatar'
            ])

def writerRow(row):
    if not os.path.exists('./articleCommentsData.csv'):
        with open('./articleCommentsData', 'a', encoding='utf-8', newline='') as csvFile:
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
        return  response.json()['data']
    else:
        return None

def getAllarticleList():
    articlelist=[]
    with open('./articleData','r',encoding='utf-8') as reader:
        readerCSV=csv.reader(reader)
        next(reader)
        for nav in readerCSV:
            articlelist.append(nav)
    return articlelist


def parse_json(response,articleId):
    for comments in response:
        try:
            region=comments['source']
        except:
            region='无'
        id=comments['id']
        content=comments['text_raw']
        author_name=comments['user']['screen_name']
        author_address=comments['user']['location']
        author_avatar=comments['user']['avatar_large']
        writerRow([id,content,author_name,author_address,author_avatar])
        print(id)



def start():
    articlecommentsurl='https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=5070137512428187&is_show_bulletin=2&is_mix=0&count=10&uid=1266321801&fetch_level=0&locale=zh-CN'
    init()
    articlelist=getAllarticleList()
    for article in articlelist:
        article_id=article[0]
        params={
            'id':int(article_id),
            'is_show_bulletin':2
        }
        response=get_data(articlecommentsurl,params)
        print(parse_json(response,article_id))





if __name__=='__main__':
    start()
