fun main() {
//    Link to the problem: https://projecteuler.net/problem=2
//    Submitted answer: 4613732
    var first = 1
    var second = 2
    var third = 0
    // including 2 in the answer already
    var answer = 2
    do {
        third=first+second
        if (third % 2 == 0 )
            answer += third
        first = second
        second = third
    } while (third < 4000000)
    println("Answer: $answer")
}