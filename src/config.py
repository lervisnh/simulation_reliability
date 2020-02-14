import os
import json


base_dir = os.path.abspath(os.path.dirname(__file__))

# 使用 sqlite 数据库
db_url = 'sqlite:///{}'.format(os.path.join(base_dir, 'data.db'))  #

# 使用 mysql 数据库
def get_mysql_configs(mysql_json):
    if not os.path.exists(mysql_json):
        return None, None
    with open(mysql_json, 'r', encoding='utf-8') as f:
        configs = json.load(f)
        DB_USER = configs['DB_USER']
        DB_PASS = configs['DB_PASS']
        DB_HOST = configs['DB_HOST']
        DB_PORT = int(configs['DB_PORT'])
        DATABASE = configs['DATABASE']
        return DB_USER, DB_PASS, DB_HOST, DB_PORT, DATABASE

mysql_json = os.path.join(base_dir, 'database_config.json')
DB_USER, DB_PASS, DB_HOST, DB_PORT, DATABASE = get_mysql_configs(mysql_json)
db_url = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(DB_USER, DB_PASS, DB_HOST, DB_PORT, DATABASE)


config_json = os.path.join(base_dir, 'run_env.json')  # 中间件路径 和 有限元软件路径 配置的存储文件


def get_run_environ():
    if not os.path.exists(config_json):
        return None, None
    with open(config_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
        temp_path = data['temp_path']  # 中间件路径
        app_path = data['app_path']  # 有限元软件路径
        return temp_path, app_path


def write_run_environ(temp_path, app_path):
    data = {
        'temp_path': temp_path,  # 中间件路径
        'app_path': app_path  # 有限元软件路径
    }

    with open(config_json, 'w', encoding='utf-8') as f:
        json.dump(data, f)
