
function map() {
	if [ "x$1" == 'xadd' ] ; then
		export $2="$(./map $1 $2 $3)"
	fi
	if [ "x$1" == 'xdelete' ] ; then
		export $2="$(./map $1 $2 $3)"
	fi
	if [ "x$1" == 'xdestroy' ] ; then
		./map $1 $2 $3
		unset $2
	fi
}