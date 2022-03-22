#!/bin/bash
#WANT_JSON

addr=$(cat $1 | grep -Po '(?<="addr": ")(.*?)(?=")')
addr_str="$addr"

result=$(curl -s -o /dev/null -w "%{http_code}" $addr_str)

echo "$addr Response Result is : $result"

