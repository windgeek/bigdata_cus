date=`date "+%Y-%m-%d"`
function dusort() {
    echo "统计目录$dir:" >> report$date.txt
    hadoop fs -du -h $dir | grep T | sort -nr >> report$date.txt
    echo -e "\n" >> report$date.txt
}
for i in `cat dir.txt`
do
dir="$i"
dusort
done
