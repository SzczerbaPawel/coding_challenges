fun main() {
//    Link to the problem: https://projecteuler.net/problem=7
//    Submitted answer: 104743
    var primeCounter=1
    var counter=2
    while (primeCounter<=10001){
        if (isPrime(counter)){
//            println("Prime counter number $primeCounter is $counter")
            counter++
            primeCounter++
        } else {
            counter++
        }
    }
    println("Answer: ${counter-1}")
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