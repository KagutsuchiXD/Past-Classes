package com.company;

public class Pyramid extends Shape {
    private double side;
    Pyramid(){
        this.side = 1;
    }
    Pyramid(double s){
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
        this.area = 4 * side * (.5 * side);
        return area;
    }
}
