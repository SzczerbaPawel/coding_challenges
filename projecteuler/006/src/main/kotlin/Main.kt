fun main() {
//    Link to the problem: https://projecteuler.net/problem=6
//    Submitted answer: 25164150
    var sumOfSquares = 0
    for (i in 1..100){
        sumOfSquares += i*i
    }

    var squareOfSum = 0
    for (i in 1..100){
        squareOfSum += i
    }
    squareOfSum *= squareOfSum

    println("Answer: ${squareOfSum-sumOfSquares}")
}