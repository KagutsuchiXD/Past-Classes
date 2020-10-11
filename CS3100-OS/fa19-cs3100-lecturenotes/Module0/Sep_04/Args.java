/*
 * Integer.parseInt()
 *
 * "".equals()
 *
 * System.out.format("%d\n", 1337);
 */

class Args {

    public static void add(int begin, String[] args) {
        int accum = 0;

        for (int i = begin; i < args.length; ++i) {
            int t = Integer.parseInt(args[i]);
            accum += t;
        }

        System.out.format("The sum of the arguments is %d\n", accum);
    }


    public static void mul(int begin, String[] args) {
        int accum = 1;

        for (int i = begin; i < args.length; ++i) {
            int t = Integer.parseInt(args[i]);
            accum *= t;
        }

        System.out.format("The products of the arguments is %d\n", accum);
    }

    public static void main(String[] args) {
        System.out.format("I got %d arguments\n", args.length);

        if ("-add".equals(args[0])) {
            add(1, args);
        }
        else if ("-mul".equals(args[0])) {
            mul(1, args);
        }
        else {
            for (int i = 0; i < args.length; ++i) {
                System.out.format("%d\t%s\n", i, args[i]);
            }
        }

    }
}
