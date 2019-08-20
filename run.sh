#!/bin/sh

path=/home/wh75er/projects/inst2vk

echo >> $path/logs
date >> $path/logs
python $path/inst2vk/main.py >> $path/logs

