#!/bin/bash
FILE=""
DIR="/home/bayu/scp2"
if [ "$(ls -A $DIR)" ]; then
        echo "ada isinya nih"
else
        echo "kosong"
fi
