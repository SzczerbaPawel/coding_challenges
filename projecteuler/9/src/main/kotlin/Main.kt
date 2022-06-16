fun main() {
//    Link to the problem: https://projecteuler.net/problem=9
//    Submitted answer: 31875000
    println(findFirstSolution())
}

private fun findFirstSolution(): Int {
    for (i in 1..999) {
        for (j in 1..999 - i) {
            val k = 1000 - i - j
            val intArray = intArrayOf(i, j, k)
            intArray.sort()
            if (intArray[0] * intArray[0] + intArray[1] * intArray[1] == intArray[2] * intArray[2]) {
                println("Found solution: $i, $j, $k")
                return i * j * k
            }
        }
    }
    return -1
}