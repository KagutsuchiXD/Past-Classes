package com.company;

public class Square extends Shape{
    private double side;
    Square(){
        side = 1;
    }
    Square(double s){
        side = s;
    }
     public void setSide(double s){
        side = s;
     }
     public double getSide(){
        return side;
     }
     @Override
    public double getArea(){
         this.area = side * side;
         return area;
     }
}
