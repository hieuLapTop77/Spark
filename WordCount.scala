import org.apache.spark.sql._
import org.apache.spark._

import org.apache.spark.{SparkConf, SparkContext}

object WordCount {
     
   def main(args: Array[String]) 
   {
      val input = spark.sparkContext.textFile(args(0))
      val words = input.flatMap(line => line.split(" "))
      val counts = words.map(word => (word, 1)).reduceByKey{case (x,y) => x + y}
      counts.saveAsTextFile(args(1))
    }
}
