fun main(args: Array<String>) {
//    Link to the problem: https://projecteuler.net/problem=1
//    Submitted answer: 233168
    val start = System.currentTimeMillis()
    var sum=0

//     1324 ms for range 1-1000000000:
//    for (i in 3..1000) {
//        if(i%3==0 || i%5==0)
//            sum+=i
//    }

//    312 ms for range 1-1000000000
    for (i in 3..1000 step 3) {
        sum+=i
    }
    for (i in 5..1000 step 5) {
        sum+=i
    }
    for (i in 15..1000 step 15) {
        sum-=i
    }

    val end = System.currentTimeMillis()
    println("Answer: $sum")
    println("Time: ${end - start} ms")
}