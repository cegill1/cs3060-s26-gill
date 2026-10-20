object MyWhileCompileStyle:
  def foo(): Unit =
    var i = 1
    while i <= 3 do
      println(i)
      i += 1

  def main(args: Array[String]): Unit =
    foo()