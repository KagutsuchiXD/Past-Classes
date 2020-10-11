package week14;

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

            writer.write("*** Calculating Loan Payment ***\r\n");

            writer.flush();

            String data1 = reader.readLine().trim();
            String data2 = reader.readLine().trim();
            String data3 = reader.readLine().trim();

            double interest =
                    Double.parseDouble(data1);
            int year = Integer.parseInt(data2);
            double loanAmount =
                    Double.parseDouble(data3);

            Loan loan = new Loan(interest, year, loanAmount);

            int num1=Integer.parseInt(data1);
            int num2=Integer.parseInt(data2);


            System.out.println("Addition operation done " );

            writer.write("\r\n=== Result is  : "+result);
            writer.flush();
            connectionSocket.close();
        }
    }
}
