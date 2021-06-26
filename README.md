# Spark
## Question: count the number of times the word appears in the title of the article
## Description about data: All titles of articles from 2013 - 2020(about 1 million lines data)
## Run with scala on spark-shell:
- Install hadoop cluster node:https://medium.com/@jootorres_11979/how-to-set-up-a-hadoop-3-2-1-multi-node-cluster-on-ubuntu-18-04-2-nodes-567ca44a3b12
- Install spark on ubuntu: https://phoenixnap.com/kb/install-spark-on-ubuntu
- Prepare data and load file data on HDFS(Hadoop Distributed File System): hdfs dfs –mkdir –p /user/hadoopuser/input (create folder "input" on HDFS) and hdfs dfs –put sample.txt /user/hadoopuser/input (Load file data "sample.txt" on HDFS).
- Create a file NameProgram.scala (Ex: nano/vim demo.scala)
- Run spark-shell (spark-shell)
- Load file: (":load /home/hadoopuser/demo.scala")
- Run local: Class.main(Array("Local input path","Local output path")) (Ex:"WordCount.main(Array("/home/hadoopuser/Input.txt","Output_WOrdCount_Scala"))")
- Run HDFS:  Class.main(Array("HDFS input path","HDFS output path")) - (Ex:"WordCount.main(Array("hdfs://chihieu-master:54310/user/hadoopuser/input/Input.txt","hdfs://chihieu-master:54310/user/hadoopuser/Output_NameNews_Scala"))")
- On Website open: ip_master:8080 to check job of spark and ip_slave:4040 to check process.
- Show result: hdfs dfs -cat output/part-r-00000
- When you run it a again, you must delete file Output on HDFS it will notify error file output already exists so you handle: "hadoop fs -rm -r output". Now you can run it again.
## Run with python on pyspark:
- Create a file NameProgram.py (Ex: nano/vim demo.py)
- After run file by: "spark-submit NameProgram.py"
- You can check job by: ip_master:8080 to check job of spark and ip_slave:4040 to check process.
- Show result:  hdfs dfs -cat output/part-r-00000
## Good luck 
