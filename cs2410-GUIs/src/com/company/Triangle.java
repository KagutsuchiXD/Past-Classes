package com.company;

public class Triangle extends Shape {
    private double side;
    Triangle(){
        this.side = 1;
    }
    Triangle(double s){
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
        this.area = side * (.5 * side);
        return area;
    }
}
