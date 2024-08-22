import requests,csv,numpy as np,os

def init():
    if not os.path.exists('./navData.csv'):
        with open('./navData','w',encoding='utf-8',newline='') as csvFile:
            writer=csv.writer(csvFile)
            writer.writerow([
                'typeName',
                'gid',
                'containerid'
            ])

def writerRow(row):
    if not os.path.exists('./navData.csv'):
        with open('./navData', 'a', encoding='utf-8', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)

def get_data(url):
    headers={
        'cookie':'SCF=Ajn5w3I6vr72GCjy1qfOU4cjM4wV3tR8cMUaX2-fqvgor2-F-6TCZV-NuH2vtmjcTwORI1RBvrm15867cDrBkdE.; SINAGLOBAL=8529245482618.222.1724036068243; ULV=1724036068245:1:1:1:8529245482618.222.1724036068243:; SUB=_2A25LxsRJDeRhGeNI6FEX9SvLzDqIHXVoulmBrDV8PUNbmtAbLWbgkW9NSGrjPyDHwtAEpZwgq_ciCnjhkIuQahCG; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W51EBH0wQW9pfSSaF97wf.T5NHD95QfSoe0So-fS0McWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNSKq0e0qfSKMNSntt; ALF=02_1726628122; XSRF-TOKEN=t3EzMWAe3Xw0MZx-K1w2j6JH; WBPSESS=Dt2hbAUaXfkVprjyrAZT_BlY3VvkjS25J6_bASM0Ywm59uiBxLRUOJp14r5VXqeYu_JEVouMYygdvpeAcpQjUCziqdLNLkWoTchbFoQfG3vO1-bXxN4pf_qjbVeBp7C8i131pwL6dn3glNCAR4wGHuTxFjV7uG9YsMJS-1DYPmfjinrOK8ytokm33C4UGKt-tbi_iq0jK-4-LRL3exNDkw==',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }
    params={
        'is_new_segment':1,
        'fetch_hot':1
    }
    response= requests.get(url,headers=headers,params=params)
    if response.status_code==200:
        return  response.json()

def parse_json(response):
    navlist=np.append(response['groups'][3]['group'],response['groups'][4]['group'])
    for nav in navlist:#
        navName=nav['title']
        navgid=nav['gid']
        navcontainedid=['containerid']
        writerRow([navName,navgid,navcontainedid])



if __name__=='__main__':
    init()
    response=get_data('https://weibo.com/ajax/feed/allGroups?is_new_segment=1&fetch_hot=1')
    parse_json(response)
