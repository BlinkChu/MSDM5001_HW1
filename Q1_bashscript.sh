cd ~/Desktop
mkdir ./test
cd ./test
for i in $(seq 1 100)
do 
	mkdir ~/Desktop/test/DDM${i}
	cd ~/Desktop/test/DDM${i}
	touch time_till_now.txt
	echo "nanoseconds since 1970-01-01 00:00:00 UTC:" >>./time_till_now.txt
	echo "<"$(date +%s)">" >>./time_till_now.txt
done
