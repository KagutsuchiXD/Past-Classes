package com.company;

import java.util.*;
import java.io.*;

public class TestInfixtoPostfix {
	public static void main(String[] args) throws FileNotFoundException {
		Scanner file = new Scanner(new FileReader("input.txt"));
		while(file.hasNext()){
			String testExp = file.nextLine();
			InfixToPostfix pf = new InfixToPostfix(testExp);
			System.out.println("Postfix Expression: " + pf.convert());
			PostfixEvaluate postResult = new PostfixEvaluate(pf.convert());
			System.out.println("Result: " + postResult.evaluate());

		}

    }
}
