import java.math.BigInteger

fun main() {
//    Link to the problem: https://projecteuler.net/problem=16
//    Submitted answer: 1366
    var result = BigInteger("2")
    for(i in 1..1000-1)
        result*=BigInteger("2")
    var answer =0
    for (i in 0 until result.toString().length){
        answer+=Integer.parseInt(result.toString()[i].toString())
    }
    println("Answer: $answer")
}