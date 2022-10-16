import java.math.BigInteger

fun main() {
//    Link to the problem: https://projecteuler.net/problem=15
//    Submitted answer: 137846528820
//    Comment: answer is simply binomial coefficient
    println(newton(BigInteger("40"),BigInteger("20")))
}

fun factorial(num: BigInteger): BigInteger {
    return if (num==BigInteger("1"))
        BigInteger("1")
    else
        factorial(num-BigInteger("1"))*num
}

fun newton(a: BigInteger, b: BigInteger): BigInteger {
    return factorial(a)/(factorial(b)*factorial(a-b))
}