#!/bin/bash
filename="$HOME/.bookmarks"
option=$1;
shift;
while read -r line
do
	IFS="|" read -r -a array <<< "$line"
	export ${array[0]}="${array[1]}"

done <$filename
case "$option" in
	-a)
		MYPWD=${PWD}
		echo "${1}|"$MYPWD >>$filename
	;;
	-r)
		sed -i "/${1}/ d" $filename
	;;
	*) echo "use: -a Bookmarkname to add new bookmark or -r Bookmarkname to remove
	bookmark"
esac
