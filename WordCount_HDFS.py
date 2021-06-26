import sys
from pyspark import SparkContext, SparkConf
if __name__ == "__main__":

	# Khoi tao SparkContext
	sc = SparkContext("spark://chihieu-master:7077","Demo spark count name news")
	# Doc du lieu va format dong theo " "
	words = sc.textFile("hdfs://chihieu-master:54310/user/hadoopuser/input/sample.txt").flatMap(lambda line: line.split(" "))
	#  Tien hanh map reduce word count
	wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b)
	# Luu ket qua ra file
	wordCounts.saveAsTextFile("hdfs://chihieu-master:54310/user/hadoopuser/Output_WordCount_Python")
