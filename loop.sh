#!/bin/bash
for (( ; ; ))
do
   echo "Cover and Import"
   curl -F files[]=@node_monitor.sqlite3 'https://www.rebasedata.com/api/v1/convert?outputFormat=mysql&errorResponse=zip' -o output.zip
   unzip -o  output.zip 
   mysql --defaults-extra-file=configmysql.conf < data.sql
   sleep  10m

done
