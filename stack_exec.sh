#!/bin/zsh

p="$1"
n=0

f_cnt=$(find "$p" -type d -a -name '*_imgf' | wc -l)

while true
	do
	python3 main.py "$p"/"$n"_imgf;
	n=$(( n+1 ));
	[ "$n" -ge "$f_cnt" ] && break
	done



# helpers for sum and medain groups from iphone
# n=0
# dirn=0
# find . -type f -name '*.jpg' | while read f
# do
# mkdir $dirn; mv "$f" "$dirn";
# n=$(( n+1 ));
# [[ n -eq 4 ]] && { dirn=$(( dirn + 1 )); n=0; }
# done

# for d in /Volumes/Data/MobilePhotoTests/4581-4608/*	
# do
# python3 main.py $d/
# done