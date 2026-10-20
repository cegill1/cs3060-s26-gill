import java.io.File
import java.io.PrintWriter
import scala.io.Source

object Write {
    def main(args: Array[String]):Unit = {
        val writer = new PrintWriter(new File("myFile.txt"))
        writer.write("Hello" + "\n")
        writer.write("Hello again" + "\n")
        writer.close()
        Source.fromFile("myFile.txt").foreach {
            x => print(x)
        }
    }
}
