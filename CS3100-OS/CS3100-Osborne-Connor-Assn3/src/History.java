import java.util.ArrayList;

public class History {
    //display history of shell with index
    public static void history(ArrayList<ArrayList<String>> history){
        int index = 1;
        for(ArrayList s : history) {
            System.out.println((index) + ": " + s);
            index++;
        }
    }
}
