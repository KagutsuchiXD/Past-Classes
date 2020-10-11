package com.company;

public class Cube extends Shape{
    private double side;
    Cube(){
        this.side = 1;
    }
    Cube(double s){
        this.side = s;
    }
    public void setSide(double s){
        side = s;
    }
    public double getSide(){
        return side;
    }
    @Override
    public double getArea(){
        this.area = side * side* side;
        return area;
    }
}
