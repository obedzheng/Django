[TOC]
# 数据库连接错误

### 报错1

```
django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have 0.9.3.
```
解决方法：

修改文件：```C:\Users\username\Anaconda3\Lib\site-packages\django\db\backends\mysql\base.py``` 

注释掉以下内容：

```
# version = Database.version_info
# if version < (1, 3, 13):
#     raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)
```

### 报错2

```
File "C:\Users\username\Anaconda3\lib\site-packages\django\db\backends\mysql\operations.py", line 146, in last_executed_query
query = query.decode(errors='replace')
AttributeError: 'str' object has no attribute 'decode'
```

解决方法：将decode改为encode

