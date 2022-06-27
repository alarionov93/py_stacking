
for d in $(ls | grep d)
	do
	mkdir "$d"/photos/
	find "$d" -type f -exec echo cp "{}" "$d"/photos/
	done

