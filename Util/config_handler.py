# 系统自动解析配置文件引用的包
from configparser import ConfigParser
from public.global_val import config_filePath

# 自定义解析的类
class ConfigParse(object):
    def __init__(self):
        pass

    @classmethod
    def get_db_conf(cls):
        cf = ConfigParser()
        cf.read(config_filePath)
        host = cf.get("mysqlconf", "host")
        port = cf.get("mysqlconf", "port")
        user = cf.get("mysqlconf", "user")
        password = cf.get("mysqlconf", "password")
        db = cf.get("mysqlconf", "db_name")
        return {"host":host, "port":port, "user":user,
                "password":password, "db":db}