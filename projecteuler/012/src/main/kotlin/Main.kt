fun main() {
//    Link to the problem: https://projecteuler.net/problem=12
//    Submitted answer: 76576500
    var iter = 1
    var triangleNumber=0
    var conditionNotMet = true
    while (conditionNotMet){
        triangleNumber += iter
        if (numberOfDivisors(triangleNumber) > 500)
            conditionNotMet = false
        iter++
    }
    println(triangleNumber)
}

fun numberOfDivisors(number: Int): Int {
    var counter = 0
    var iter = 1
    while ( iter*iter <= number){
        if (number % iter == 0)
            counter += 2
        iter++
    }
//    println("Number $number has $counter divisors")
    return counter
}
