#coding: utf-8

from gluon.storage import Storage

config = Storage(
    bd = Storage(),
    mail = Storage(),
    aut = Storate()
)

config.bd.uri = "oracle://asiwebcons/asiwebcons@10.13.1.1/adm"
config.bd.pool_size = 10
config.bd.check_reserved = ["all"]
