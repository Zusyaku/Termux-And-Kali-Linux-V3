#!/bin/bash

kword=$1

while IFS= read tar; do if curl -s "$tar" | grep -i "$kword" &> /dev/null; then echo "$tar"; fi & done < urls.log
wait
