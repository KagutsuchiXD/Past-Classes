package mon;

/**
 * 1. add our own numbers -> goto Server
 * 2. give server ip to anyone
 */

import java.io.*;
import java.net.*;
import java.util.*;

public class Client {

    public static void main(String argv[])
    {
        try{
            Socket socketClient= new Socket("129.123.29.227",5556);
            System.out.println("Client: "+"Connection Established");

            BufferedReader reader =
                    new BufferedReader(new InputStreamReader(socketClient.getInputStream()));

            BufferedWriter writer=
                    new BufferedWriter(new OutputStreamWriter(socketClient.getOutputStream()));
            String serverMsg;
            /**
            Scanner scan = new Scanner(System.in);
            String num1 = scan.next();
            System.out.println("num1: "+num1);

            writer.write("8\r\n");
            //writer.write(num1+"\r\n");
            writer.write("10\r\n");
            writer.flush();*
             */
            while((serverMsg = reader.readLine()) != null){
                System.out.println("Client: " + serverMsg);
            }

        }catch(Exception e){e.printStackTrace();}
    }
}