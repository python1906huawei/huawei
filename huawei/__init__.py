import pymysql

from huawei.mysignal import my_signal

pymysql.install_as_MySQLdb()

from django.dispatch import Signal,receiver


@receiver(my_signal)
def process_signal(sender,**kwargs):
    pass