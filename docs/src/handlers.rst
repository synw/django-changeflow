Handle the changes events
=========================

To handle the data changes create a ``r_handlers.py`` file in your project directory (where settings.py is).

Set the ReQL query
^^^^^^^^^^^^^^^^^^

The listener will use by default the following ReQL query, listening to all changes in the table:

.. highlight:: python

::

   r.db(database).table(table).changes()

You can set a custom ReQL query for the listener in ``r_handlers.py`` with a ``r_query`` function:

.. highlight:: python

::

   def r_query():
   	return r.db("mydb").table("mytable").pluck('message').changes()
   	
Write the handlers
^^^^^^^^^^^^^^^^^^

.. highlight:: python

::

   # in settings.py
   CHANGEFEED_LISTEN = True

In your root directory (SITE_SLUG) create a ``r_handlers.py`` file and a ``feed_handlers`` function to do 
whatever you want, like to broadcast the data to a websocket:

.. highlight:: python

::

   # this function will be triggered on every change in the Rethinkdb data
   def feed_handlers(database, table, change):
       print database
       print table
       print str(change['old_val'])
       print str(change['new_val'])
       return
       
You can also manage handlers directly from your apps by creating a file with a ``feed_handlers`` function, 
and launch a listener from the ``__init__.py`` file of your app:

.. highlight:: python

::

   from changefeed.tasks import feed_listener
   feed_listener.delay("database", "table", "mymodule.r_handlers")

