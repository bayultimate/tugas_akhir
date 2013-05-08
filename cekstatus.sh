#!/bin/bash

x=30
delay=30
stop=0
blank=''
congest=11000000
while [ $x -le 30 ]
do
        bwm-ng -o csv -c 1 -T rate -I eth0 > bandwidth.log
        condition=$(awk -F';' '{print $4}' /home/bayu/bandwidth.log)
        condition=$(echo $condition | cut -f1 -d.)
        echo $condition
        echo $congest
        if [ $congest -le $condition ];
        then
                sniffexid=$(pgrep sniffex.out)
                stop=0
                sniff=1
                if [ $sniffexid -ne $blank ];
                then
                        echo "start sniff"
                        /home/bayu/sniffex.out >> sniff.txt
                fi
        else
                if [ $stop -ge $delay ]; 
                then
                        echo "stop sniff"
                        sniffexid=$(pgrep sniffex.out)
                        kill $sniffexid
                        sniff=0
                fi
        else
                if [ $sniff -eq "1" ];
                then
                        (( stop++ ))
                        echo "counting $stop"
                fi
        fi

sleep 1
done
