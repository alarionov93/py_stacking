#!/bin/zsh

p="$1"
n=0

f_cnt=$(find "$p" -type d -a -name 'stack*' | wc -l)

while true
	do
	python3 main.py "$p"/stack"$n";
	n=$(( n+1 ));
	[ "$n" -ge "$f_cnt" ] && break
	done

