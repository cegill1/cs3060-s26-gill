import scala.io.Source
import scala.collection.mutable.HashMap
object Task:
    def main(args: Array[String]): Unit =
        val mymap = HashMap[String.Int]()
        // Get an iterator for lines in the File
        val lineIterator = Source.fromFile("items.txt").getLines()
        // Iterate over all linesfor line <- lineIterator do
            val list = line.split("\\s+")
            val item = list(0)
            val price = list(2).toInt

        // Update running total for each item
        if !mymap.contains(item) then
            mymap += (item -> price)
        else
            mymap(item) += price
        // Print results
    mymap.foreach { case (item, total) => println(s"$item -> $total)}