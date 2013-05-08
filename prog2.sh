#!/bin/bash
x=0 
echo =====start prog2====== >> /home/bayu/prog2.log 
while [ $x -le 60 ] 
do
        #echo =====start prog2====== >> /home/bayu/prog2.log
        echo $x >> /home/bayu/prog2.log
        sleep 0.500
        hpingpid=$(pidof hping3)
        kill $hpingpid
        sleep 0.500
        echo =====finish job====== >> /home/bayu/prog2.log
        (( x++ ))
done
hpingid=$(pidof hping3)
kill -9 $hpingid




