import scala.util.control.TailCalls._

def factorial(n: Int, acc: BigInt = 1): TailRec[BigInt] = {
    if (n <= 1) done(acc)
    else tailcall(factorial(n - 1, n * acc))
}

println(factorial(5).result)