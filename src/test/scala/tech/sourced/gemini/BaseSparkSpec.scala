package tech.sourced.gemini

import org.apache.spark.SparkConf
import org.apache.spark.sql.SparkSession
import org.scalatest.{BeforeAndAfterAll, Suite, Tag}

trait BaseSparkSpec extends BeforeAndAfterAll {
  this: Suite =>

  @transient var sparkSession: SparkSession = _
  private var _conf: SparkConf = _

  def useSparkConf(conf: SparkConf): SparkConf = {
    _conf = conf
    _conf
  }

  def useDefaultSparkConf(): SparkConf = {
    val defaultConf: SparkConf = new SparkConf(true)
      .setAppName(this.getClass.getSimpleName)
      .set("spark.cassandra.connection.host", Gemini.defaultCassandraHost)
      .set("spark.cassandra.connection.port", Gemini.defaultCassandraPort.toString)
      .set("spark.cassandra.connection.keep_alive_ms", "5000")
      .set("spark.cassandra.connection.timeout_ms", "30000")
      .set("spark.ui.showConsoleProgress", "false")
      .set("spark.ui.enabled", "false")
      .set("spark.cleaner.ttl", "3600")

    useSparkConf(defaultConf)
  }

  override protected def beforeAll(): Unit = {
    super.beforeAll()

    sparkSession = SparkSession.builder()
      .master("local[*]")
      .config(_conf)
      .config("spark.driver.host", "localhost")
      .getOrCreate()
  }

  override protected def afterAll(): Unit = {
    // commented due to "Cannot call methods on a stopped SparkContext"
    // but for tests we don't really need to stop spark
    // it will be stopped automatically when tests exit

    // resetSparkContext()
    super.afterAll()
  }

  def resetSparkContext(): Unit = {
    if (sparkSession != null) {
      sparkSession.stop()
    }
    sparkSession = null
  }
}
