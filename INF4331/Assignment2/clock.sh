#!/bin/bash
option=$1;
shift;
while true;
do 
	case "$option" in
	us) 
		clear
		TZ=":US/Eastern" date +%T
		
		echo $TZ
		sleep 1
	;;
	no)
		clear
		TZ=":Europe/Oslo" date +%T
		
		echo $TZ
		sleep 1
	;;

	sk)
		clear
		TZ=":Asia/Seoul" date +%T
		
		echo $TZ
		sleep 1
	;;
	
	*)
		"Choose what time you wish to see. After program name write: no=Norway, us=US easter time or sk=South Korea"
		break
	esac

done

