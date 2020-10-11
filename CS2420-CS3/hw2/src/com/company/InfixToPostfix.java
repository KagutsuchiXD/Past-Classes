package com.company;

import java.util.*;

public class InfixToPostfix {
    char[] sepex;
    InfixToPostfix(String expression){
        sepex = expression.toCharArray();
    }

    public String convert(){
        String postfix = "";

        Stack<Character> reader = new Stack<>();

        for (int i = 1; i < sepex.length; i++){
            char test = sepex[i];

            if (Character.isLetterOrDigit(test)){
                postfix += test;
            }
            else if (test == '('){
                reader.push(test);
            }
            else if (test == ')'){
                while (!reader.isEmpty() && reader.peek() != '(')
                    postfix += reader.pop();
            }
            else{
                while (!reader.isEmpty() && weight(test) <= weight(reader.peek())){
                    postfix += reader.pop();
                }
                reader.push(test);
            }
        }

        while (!reader.isEmpty()){
            postfix += reader.pop();
        }

        return postfix;
    }
    static int weight(char n){  //determine weight of characters
        switch (n){
            case '+':
            case '-':
                return 1;

            case '*':
            case '/':
                return 2;

        }
        return -1;
    }


}
