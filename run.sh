#!/bin/sh

path=/home/wh75er/projects/inst2vk
cd $path/inst2vk

echo >> $path/logs
date >> $path/logs
python $path/inst2vk/main.py > $path/log 2>&1

cat $path/log >> $path/logs

