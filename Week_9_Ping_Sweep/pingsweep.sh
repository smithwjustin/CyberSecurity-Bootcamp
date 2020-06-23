PREFIX=$1	
echo "Scanning $PREFIX.0/24"

for i in $(seq 1 255)
	do echo "$PREFIX.$i"
#	do Target =
	ping -c 1 $PREFIX.$i

done
