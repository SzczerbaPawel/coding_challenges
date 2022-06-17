fun main() {
//    Link to the problem: https://projecteuler.net/problem=14
//    Submitted answer: 837799
    var max=0
    var maxCounter=0
    for (i in 2..999999){
        var counter = 1
        var temp=i.toLong()
        while(temp!=1L){
            temp=collatz(temp)
            counter++
        }
//        println("i=$i counter=$counter maxCounter=$maxCounter max=$max")
        if(counter>maxCounter){
            maxCounter=counter
            max=i
        }
    }
    println("Answer: $max")

}

fun collatz(num: Long): Long {
    if (num % 2L ==0L ){
//        println("Returning ${num/2} for $num")
        return num/2
    }
    else{
//        println("Returning ${3*num +1} for $num")
        return 3*num +1
    }
}