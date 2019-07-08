import os
mysql_username = os.environ("mysql_username")
mysql_password = os.environ("mysql_password")
'SQLALCHEMY_DATABASE_URI' = f'mysql://{mysql_username}:{mysql_password}@127.0.0.1:3306/web_info_monitor?charset=utf8'

'SQLALCHEMY_TRACK_MODIFICATIONS' = True