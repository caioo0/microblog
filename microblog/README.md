## microblog 说明

## 本地运行

1、 如果没有安装虚拟环境，首先安装 

```

$ pip install virtualenv  # 安装虚拟环境
$ virtualenv venv

# linux / mac 环境 
$ source venv/bin/activate

# windows 环境
$ venv\Scripts\activate

```

2、运行flask  ，如果没有安装,执行命令: 

>  pip install flask  # 安装命令

>  flask run



调试模式：

```
 $ export FLASK_DEBUG=1
```

如果你使用Microsoft Windows，记得将`export`替换成`set`。

## 其他安装

> pip install flask-wtf
>
> pip install flask-sqlalchemy
>
> pip install flask-migrate
>
> pip install flask-bootstrap




## 数据迁移

每次更新数据库模块需要更新命令：

```python
 flask db migrate -m "posts table"

```

```
 flask db upgrade
```

## git

在使用git add提交多个文件的方式：

git add .   后面加一个“.”，匹配所有的文件

总结下，提交多个文件时，git add后可以有如下参数以及参数的解释:

git add .                               提交被修改的和新建的文件，但不包括被删除的文件                            

git add -u     --update          update tracked files    更新所有改变的文件，即提交所有变化的文件

git add -A    --all                  add changes from all tracked and untracked files   提交已被修改和已被删除文件



```
$ git remote add origin git@github.com:caioo0/microblog.git
```

从现在起，只要本地作了提交，就可以通过命令：

```
$ git push origin master
```

## 工具

学习地址：https://wizardforcel.gitbooks.io/the-flask-mega-tutorial-2017-zh/content/docs/5.html

SQL Design: http://ondras.zarovi.cz/sql/demo/

Git 教程：https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/0013752340242354807e192f02a44359908df8a5643103a000

