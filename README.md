# Paths mapping tool.

.. code:: bash

    Usage: map <command> <list> [<item>] ...

    Commands:
      add      add item to list
      delete   delete item from list
      destroy  destroy list
      show     show details about list


# Examples:

.. code:: bash

    $ map add servers master
    $ map add servers node-1
    $ map add servers node-2
    $ openstack server start $servers
    $ cat ~/.map

    {
        "servers": [
            "master",
            "node-1",
            "node-2"
        ]
    }


