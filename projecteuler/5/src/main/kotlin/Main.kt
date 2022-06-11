fun main() {
    println(divisors(100))
}

fun divisors(number: Int): HashMap<Int, Int> {
    val theMap = HashMap<Int, Int>()
    var num = number

    var divisor=2
    while (num != 1) {
        var iterator=0
        while (num % divisor == 0){
            num /= divisor
            iterator++
        }
        theMap[divisor]=iterator
        divisor++
    }

    return theMap
}