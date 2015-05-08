#!/bin/bash

function extract_pem {
	openssl pkcs12 -in $1 -nokeys -clcerts -out $FILENAME-client.pem
	openssl pkcs12 -in $1 -nokeys -cacerts -out $FILENAME-ca.pem
}

function extract_key {
	openssl pkcs12 -in $1 -nocerts -out $FILENAME.key -nodes
	openssl rsa -in $FILENAME.key -out $FILENAME-nopass.key
}

function report {
	
	echo -e "\nExtracted client pem: $FILENAME.pem \nExtracted ca/int pem: $FILENAME-ca.pem \nExtracted key: $FILENAME-nopass.key"
}

#Main
#Check how we are called
if [ -z $1 ]; then
	echo "usage: pkcs12extract.sh <filename>"
	exit
elif [ $(echo $1 | awk -F. '{print $(NF)}') != "pfx" ]; then
	echo "Not a pkcs12 certificate"
	exit
fi

FILENAME=$(echo $1 | awk -F. '{$(NF--)=""; gsub (" ", "", $0); print}')

extract_pem $1
extract_key $1
report
