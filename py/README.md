# UENC区块链浏览器配置说明

## config.py相关配置说明

```python
HOSTNAME = '数据库所在服务器IP地址'    # 例如 192.168.1.12
PORT = '数据库端口'                  # 例如 3306
DATABASE = '数据库名称'              # 例如 db_demo
USERNAME = '数据库登录用户名'         # 例如 123 
PASSWORD = '数据库登录密码'           # 例如 123456

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?        charset=UTF8".format(username=USERNAME,                                          password=PASSWORD,                                                                     host=HOSTNAME, port=PORT,                                                                 db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

## 数据库生成说明

数据库版本：5.7.31

数据库脚本文件：db.sql