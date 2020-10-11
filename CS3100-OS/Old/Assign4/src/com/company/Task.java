package com.company;

public class Task {
    private BPP calculator = new BPP();
    private long index;

    Task(long index){
        this.index = index;
    }

    public int calculate(){
        String digit = Integer.toString(calculator.getDecimal(index));

        if(digit.length()==9){
            return Integer.parseInt(digit.substring(0,1));
        }
        else{
            return 0;
        }
    }

    public int getIndex(){
        return (int)index;
    }
}
