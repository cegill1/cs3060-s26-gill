import scala.io.Source  // Import package

object ReadFile:
    def main(args: Array[String]): Unit =
        val filename = "file.txt"
        val lines = Source.fromFile(filename).getLines()
        for line <- lines do
            print(line)
            // You can process line here
