#!/bin/sh
while true
do
        log_num=$(tail -n 1 /data/log.txt | awk '{print $7}');
        conf=$(cat /data/config.txt)
        if [ "$conf" = "" ]; then
                echo $log_num > /data/config.txt
                echo "config file is wrong"
        else
                echo "config file is ok"
        fi
        process=$(ps -ef | grep prod.py | grep -v grep);
        if [ "$process" = "" ]; then
                sleep 5;
                echo "not running";
                nohup python /root/prod.py & 
        else
                sleep 5;
                echo "prod.py is running";
        fi
done
