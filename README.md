# Paths mapping tool.

    Usage: map <command> <list> [<item>] ...

    Commands:
      add      add item to list
      delete   delete item from list
      destroy  destroy list
      show     show details about list


# Examples

Read logs:

    # map add logs /var/log/messages
    # map add logs /var/log/secure
    # tail -f $logs

Start servers:

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


