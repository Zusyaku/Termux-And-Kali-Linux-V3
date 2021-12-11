#!/bin/bash

# request

#/// webview

mode=( [1]="--view" [2]="--send" [3]="--chooser" [4]="--content-type" )

function req.1 {
	case $1 in
	           GET)https GET --body "$2" $3 $4 $5 $6 $7 $8 $9 $10 $11 $12 $13 $14 $15 $16 $17 $18 ;;
	           POST)https POST --body "$2" $3 $4 $5 $6 $7 $8 $9 $10 $11 $12 $13 $14 $15 $16 $17 $18 ;;
	           *)sleep 2s; exit 5 ;;
	             esac
}


function download {
     https --download "$2"
}

url="curl"


function WebOpen {
	case $1 in
	           view)xdg-open ${mode[1]} "$2" ;;
	           send)xdg-open ${mode[2]}  "$2" ;;
	           chooser)xdg-open ${mode[3]} "$2" ;;
	           content-type)xdg-open ${mode[4]} "$2" ;;
	           *)sleep 2s;exit 5 ;;
	           esac
	           
}

# Code by polygon
# ubah code denda 5k :v
