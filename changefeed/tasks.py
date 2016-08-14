# -*- coding: utf-8 -*-

from changefeed.orm import R
from changefeed.conf import DATABASE, TABLE
from celery import task
from celery_once import QueueOnce


@task(ignore_results=True)
def _push_to_db(database=DATABASE, table=TABLE, data={}):
    R.write(database, table, data)
    return

@task(ignore_results=True)
def _push_to_feed(data):
    R.write(DATABASE, TABLE, data)
    return

@task(base=QueueOnce, once={'graceful': True, 'keys': []})
def feed_listener(database, table, r_query=None):   
    R.listen(database, table, r_query)
    return

def push_to_feed(data):
    return _push_to_feed.delay(data)

def _push_to_db(database=DATABASE, table=TABLE, data={}):
    return _push_to_db.delay(database, table, data)
    


    
    
