hdfs dfs -rm -r input 
hdfs dfs -put input
hadoop jar hadoop-streaming-2.6.0.jar \
    -file mapper.py    -mapper mapper.py \
    -file reducer.py   -reducer reducer.py \
    -input input -output output
rm -rf output
hdfs dfs -get output
hdfs dfs -rm -r output
