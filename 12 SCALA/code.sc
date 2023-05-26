import org.apache.spark.{SparkConf, SparkContext}

object WordCount {
  def main(args: Array[String]): Unit = {
    // Create a Spark configuration
    val conf = new SparkConf()
      .setAppName("WordCount")
      .setMaster("local[*]") // Run Spark locally using all available cores

    // Create a Spark context
    val sc = new SparkContext(conf)

    // Load the input text file
    val lines = sc.textFile("input.txt")

    // Perform word count
    val wordCounts = lines
      .flatMap(line => line.split(" "))
      .map(word => (word, 1))
      .reduceByKey(_ + _)

    // Print the word counts
    wordCounts.foreach(println)

    // Stop the Spark context
    sc.stop()
  }
}
