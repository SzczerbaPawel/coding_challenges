fun main() {
//    Link to the problem: https://projecteuler.net/problem=10
//    Submitted answer: 142913828922
    var answer =0L
    for (i in 2..2000000){
        if(isPrime(i)){
//            println("Prime detected: $answer + $i = ${answer+i}")
            answer+=i
        }
    }
    println("Answer: $answer")
}

fun isPrime(number: Int): Boolean {
    var i = 2
    while (i*i<=number){
        if (number % i == 0){
            return false
        }
        i++
    }
    return true
}