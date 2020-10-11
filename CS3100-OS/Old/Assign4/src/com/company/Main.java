import java.util.*;

public class Main {
    int processors = Runtime.getRuntime().availableProcessors();

    public static void main(String[] args) {
        Thread[] workers = new Thread[Runtime.getRuntime().availableProcessors()];

        for(Thread t: workers){
            t = new Thread(new Work());
            t.start();

        }



    }
}
