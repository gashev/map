# Paths mapping tool.

    Usage: map <command> <list> [<item>] ...

    Commands:
      add         add item to list
      delete      delete item from list
      destroy     destroy list
      export      export to bash code
      show        show details from list

Export lists to bash code:

    $ ./map export
    declare -x logs="/var/log/messages /var/log/secure /var/log/maillog"
    declare -x servers="master node-1 node-2"

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

