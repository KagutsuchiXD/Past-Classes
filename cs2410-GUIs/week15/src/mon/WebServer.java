package mon;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class WebServer {

    public static void main(String argv[]) throws Exception
    {
        ServerSocket mysocket = new ServerSocket(5556);
        while(true)
        {
            Socket connectionSocket = mysocket.accept();

            BufferedReader reader =
                    new BufferedReader(new InputStreamReader(connectionSocket.getInputStream()));
            BufferedWriter writer=
                    new BufferedWriter(new OutputStreamWriter(connectionSocket.getOutputStream()));

            writer.write("<html><h1>Hello World</h1></html>" + "\r\n");
            writer.flush();

            connectionSocket.close();
        }
    }
}
