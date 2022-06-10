fun main() {
    var max = 0
    for ( i in 100..999 ) {
        for ( j in 100..999 ) {
            if (isPalindrome(i*j))
                if (i*j > max)
                    max = i*j
        }
    }
    println("Answer: $max")
}

fun isPalindrome(number: Int): Boolean {
    var num = number
    var remainder = 0
    var reversedInteger = 0
    val originalInteger = num
    while (num != 0) {
        remainder = num % 10
        reversedInteger = reversedInteger * 10 + remainder
        num /= 10
    }
    return originalInteger == reversedInteger
}