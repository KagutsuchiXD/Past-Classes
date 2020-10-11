package com.company;

import java.util.HashMap;

public class ResultTable {
    private HashMap results = new HashMap<>(1000);

    ResultTable(){

    }

    synchronized public void add(int key, int value){
        results.put(key, value);
    }

}
