fun main() {
//    Link to the problem: https://projecteuler.net/problem=5
//    Submitted answer: 232792560
    val limit = 20
    val divisorsMap = HashMap<Int, Int>()
    for (i in 2..limit)
    {
        divisorsMap[i] = 0
    }
    for (i in 2..limit)
    {
        combineHashMaps(divisors(i), divisorsMap)
    }
    println("Map of divisors: $divisorsMap")
    var answer =1
    for (i in 2..limit)
    {
        for (j in 1..divisorsMap[i]!!){
            answer *= i
        }
    }
    println("Answer: $answer")

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

fun combineHashMaps(mapToCombine: HashMap<Int, Int>, combinedMap: HashMap<Int, Int>){
    for (i in 2..mapToCombine.size+1)
    {
        if (mapToCombine[i]!! > combinedMap[i]!!){
            combinedMap[i] = mapToCombine[i]!!
        }
    }
}