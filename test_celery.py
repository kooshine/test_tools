#/bin/python
#coding:utf-8

from celery import Celery

app = Celery(
    'test-celery', 
    broker="redis://{}:{}/7".format("127.0.0.1", "6379"),
    backend="redis://{}:{}/7".format("127.0.0.1", "6379")
)
@app.task
def add(x, y):
    return x+y

add.apply_async((30, 100), countdown=10)  # 延迟10s执行
