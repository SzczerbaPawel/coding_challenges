fun main() {
    var number = 600851475143
    // Starting with 3 because number is not divisible by 2
    var divisor = 3
    while (number != 1L){
        if (number % divisor == 0L)
            number /= divisor
        else
            divisor++
    }
    println("Answer: $divisor")
}