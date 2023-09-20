#!/bin/bash

a=2
b=2
c=$((a+b))

myStrings=("abby" "soko" "motoo")

for name in "${myStrings[@]}"; do
	echo "$name"
done
echo "Bash says: Hello, World!"
echo "$a + $b = $c"

