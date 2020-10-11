public class Task {
    private BPP calculator = new BPP();
    private long index;

    Task(long index){
        this.index = index;
    }

    public int calculate(){
        String digit = Integer.toString(calculator.getDecimal(index)); // use BPP to calculate the nth digit of pi
        //get the first number of the 9 digits returned by BPP
        if(digit.length()==9){
            return Integer.parseInt(digit.substring(0,1));
        }
        else{//if the returned value doesn't have 9 digits then the nth digit of pi is 0
            return 0;
        }
    }

    public int getIndex(){
        return (int)index;
    }
}
