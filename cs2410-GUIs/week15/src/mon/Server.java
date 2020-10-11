package mon;

/*
2. add our own logic
 */

import java.io.*;
import java.net.*;

class Server
{
    public static void main(String argv[]) throws Exception
    {

        System.out.println(" Server is Running  " );
        ServerSocket mysocket = new ServerSocket(5555);

        while(true)
        {
            Socket connectionSocket = mysocket.accept();

            BufferedReader reader =
                    new BufferedReader(new InputStreamReader(connectionSocket.getInputStream()));
            BufferedWriter writer=
                    new BufferedWriter(new OutputStreamWriter(connectionSocket.getOutputStream()));


            String data1 = reader.readLine().trim();
            String data2 = reader.readLine().trim();
            String data3 = reader.readLine().trim();

            double num1=Double.parseDouble(data1);
            int num2=Integer.parseInt(data2);
            double num3=Double.parseDouble(data3);

            Loan loan = new Loan(num1, num2, num3);

            double monthlyPayment = loan.getMonthlyPayment();
            double totalPayment = loan.getTotalPayment();

            writer.write(monthlyPayment + "\r\n");
            writer.flush();
            writer.write(totalPayment + "\r\n");
            writer.flush();

            System.out.println("Loan received.  Interest: " + data1 + ", Years: " + data2 + ", Loan Amount: " + data3 + ".");
            System.out.println("Calculating... Monthly Payment: " + monthlyPayment + ", Total Payment: " + totalPayment);

            connectionSocket.close();
        }
    }
}
