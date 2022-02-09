hadoop fs -ls $1 > temp.txt
cat temp.txt | while read quanxian temp user group size day hour filepath
do
hadoop fs -du -s -h $filepath
done
