from pymysql import *

conn = connect(
    host='localhost',  # 主机名（或IP地址）
    port=3306,  # 端口号，默认为3306
    user='root',  # 用户名
    password='618600fuken',  # 密码
    charset='utf8mb4',  # 设置字符编码
    database='weibo_monitor'
)
# 获取mysql服务信息（测试连接，会输出MySQL版本号）
print(conn.get_server_info())

cursor=conn.cursor()

def query(sql,params):
    params=tuple(params)
    cursor.execute(sql,params)
    conn.ping(reconnect=True)
    data_list=cursor.fetchall()
    conn.commit()
    return  data_list

