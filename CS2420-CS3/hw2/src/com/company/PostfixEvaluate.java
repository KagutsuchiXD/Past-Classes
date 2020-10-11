package com.company;

import java.util.*;

public class PostfixEvaluate {
    char[] postExp;
    PostfixEvaluate(String expression){
       postExp = expression.toCharArray();
    }

    public int evaluate(){
        int result = 0;

        Stack<Integer> calculator = new Stack<>();

        for (int i = 0; i < postExp.length; i++){
            char test = postExp[i];

            if (Character.isDigit(test)){
                calculator.push(Character.getNumericValue(test));
            }
            else if(test == '+'){
                int t1 = calculator.pop();
                int t2 = calculator.pop();
                calculator.push(t2 + t1);
            }
            else if(test == '-'){
                int t1 = calculator.pop();
                int t2 = calculator.pop();
                calculator.push(t2 - t1);
            }
            else if(test == '*'){
                int t1 = calculator.pop();
                int t2 = calculator.pop();
                calculator.push(t2 * t1);
            }
            else if(test == '/'){
                int t1 = calculator.pop();
                int t2 = calculator.pop();
                calculator.push(t2 / t1);
            }
        }
        while(!calculator.isEmpty()){
            result += calculator.pop();
        }
        return result;
    }
}
