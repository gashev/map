function map_initialize() {
    file=$(mktemp)
    map.py export 1>$file
    source $file
    rm -f $file
}

function map() {
	if [ "x$1" == 'xadd' ] ; then
		export $2="$(map.py $1 $2 $3)"
	fi
	if [ "x$1" == 'xdelete' ] ; then
		export $2="$(map.py $1 $2 $3)"
	fi
	if [ "x$1" == 'xdestroy' ] ; then
		map.py $1 $2 $3
		unset $2
	fi
}

map_initialize
