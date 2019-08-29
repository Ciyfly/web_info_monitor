# 后端  
使用 pipenv进行管理  
1.安装pipenv ` sudo python3 -m pip install pipenv`  
2.创建虚拟环境  `pipenv --three` 使用当前系统环境的python3创建 我的是3.7  
3.激活虚拟环境 `pipenv shell`  
4.安装flask  `pipenv install flask`
5.安装环境设置 `pipenv install python-dotenv`

对数据库进行升级更新  

``` shell
python db.py db init
python db.py db migrate
python db.py db upgrade
```
