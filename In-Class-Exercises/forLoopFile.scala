object ForLoopFile:
    def forLoop(args: Array[String])= {
        println("for loop using Java-style iteration")

        for (i <- 0 until args.length) do
            println(args(i) + " are mine ")
        
    def main(args: Array[String]): Unit =
        forLoop(args)
        