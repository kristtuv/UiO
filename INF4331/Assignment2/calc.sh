#!/bin/bash
option=$1;
shift;

case "$option" in
		
	S)
		S=0
		for var in "$@"
		do
    			let S+=$var
		done
		echo $S
	;;
	P)
		P=1
		for var in "$@"
		do
    			let P*=$var
		done
		echo $P
	;;

	M)
		M=-999999999
		for var in "$@"
		do
			if [ $var -gt $M ]
			then
				M=$var
			else
				continue
			fi
		done
		echo $M
	;;
	m)
		m=999999999
		for var in "$@"
		do
			if [ $var -lt $m ]
			then
				m=$var
			else
				continue
			fi
		done
		echo $m
	;;
	
	*)
		echo "First argument after filename must be either S=sum, P=product, M=maximum or m=minimum"
esac

