package com.company;

import java.util.ArrayList;

public class TestShape {

    public static void main(String[] args) {
        ArrayList<Shape> shapes = new ArrayList<>();
        Square square1 = new Square(5);
        Square square2 = new Square(25);
        Cube cube1 = new Cube(3);
        Cube cube2 = new Cube(9);
        Triangle tri1 = new Triangle(4);
        Triangle tri2 = new Triangle(16);
        Pyramid pyr1 = new Pyramid(6);
        Pyramid pyr2 = new Pyramid(36);
        shapes.add(square1);
        shapes.add(square2);
        shapes.add(cube1);
        shapes.add(cube2);
        shapes.add(tri1);
        shapes.add(tri2);
        shapes.add(pyr1);
        shapes.add(pyr2);
        for (Shape s : shapes){
            System.out.println("Area of shape: " + s.getArea());
        }
    }
}
