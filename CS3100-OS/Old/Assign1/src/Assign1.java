import java.math.BigDecimal;
import java.math.BigInteger;
import java.math.RoundingMode;

public class Assign1 {
    public static void main(String[] args){
        if((args.length == 0)){           //output for 0 arguments
            System.out.println("\n--- Assign 1 Help ---\n" +
                    "  -fib [n] : Compute the Fibonacci of [n]; valid range [0, 40]\n" +
                    "  -fac [n] : Compute the factorial of [n]; valid range, [0, 2147483647]\n" +
                    "  -e [n] : Compute the value of 'e' using [n] iterations; valid range [1, 2147483647]");
        }
        else if((args.length % 2) == 0){
            for(int i = 0; i < args.length; i+=2){
                if(!args[i].matches("[0-9]+")){ // make sure there are no numbers in the argument so it doesn't blow up the world
                    if(args[i].equals("-fib")){ // See if -fib argument is valid then perform fibonacci
                        if(args[i+1].matches("[0-9]+")){
                            if(Integer.parseInt(args[i+1]) <= 0 || Integer.parseInt(args[i+1]) >= 40){
                                System.out.println("Fibonacci valid range is [0, 40]");
                            }
                            else{
                                System.out.println("Fibonacci of " + args[i+1] + " is " + fib(Integer.parseInt(args[i+1])));
                            }
                        }
                        else{
                            System.out.println("Fibonacci valid range is [0, 40]");
                        }
                    }
                    else if(args[i].equals("-e")){
                        if(args[i+1].matches("[0-9]+")){ // See if -e argument is valid then perform e iterations
                            if(Integer.parseInt(args[i+1]) < 1 || Integer.parseInt(args[i+1])  >= Integer.MAX_VALUE){
                                System.out.println("Valid e iterations range is [1, 2147483647]");
                            }
                            else{
                                System.out.println("The value of e using " + args[i+1] + " iterations is " + e(Integer.parseInt(args[i+1])));
                            }
                        }
                        else{
                            System.out.println("Valid e iterations range is [1, 2147483647]");
                        }
                    }
                    else if(args[i].equals("-fac")){  // See if -fac argument is valid then perform factorial
                        if(args[i+1].matches("[0-9]+")){
                            System.out.println("Factorial of " + args[i+1] + " is " + factorial(BigInteger.valueOf(Integer.parseInt(args[i+1]))));
                        }
                        else{
                            System.out.println("Factorial valid range: [0, 2147483647]");
                        }
                    }
                    else {
                        System.out.println("Unknown command line argument: " + args[i] + "\n--- Assign 1 Help ---\n" +
                                "  -fib [n] : Compute the Fibonacci of [n]; valid range [0, 40]\n" +
                                "  -fac [n] : Compute the factorial of [n]; valid range, [0, 2147483647]\n" +
                                "  -e [n] : Compute the value of 'e' using [n] iterations; valid range [1, 2147483647]");
                    }
                }

            }
        }
        else{
            System.out.println("--- Assign 1 Help ---\n" +
                    "  -fib [n] : Compute the Fibonacci of [n]; valid range [0, 40]\n" +
                    "  -fac [n] : Compute the factorial of [n]; valid range, [0, 2147483647]\n" +
                    "  -e [n] : Compute the value of 'e' using [n] iterations; valid range [1, 2147483647]");
        }
    }
    private static BigInteger factorial(BigInteger num){ // performs factorial
        BigInteger fac;
        if(num.equals(BigInteger.valueOf(0))){
            return BigInteger.valueOf(1);
        }
        else{
           fac = num.multiply(factorial(num.subtract(BigInteger.valueOf(1))));
        }
        return fac;
    }
    private static int fib(int num){ // performs fibonacci
        if(num <= 1){
            return num;
        }
        else{
            return fib(num - 1) + fib(num -2);
        }
    }
    private static BigDecimal e(int iterations){ // performs e
        BigDecimal factor = new BigDecimal(1.0);
        BigDecimal e = BigDecimal.valueOf(1);
        for(int i = 1; i <= iterations; i++){
            factor = factor.multiply(BigDecimal.valueOf(i));
            e = e.add(BigDecimal.valueOf(1).divide(factor, 16, RoundingMode.HALF_UP));
        }
        return e;
    }
}
