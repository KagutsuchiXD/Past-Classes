import java.util.HashMap;

public class ResultTable {
    private HashMap results = new HashMap<>(1000);

    ResultTable(){
    }

    synchronized public void add(int key, int value){
        results.put(key, value);
    }

    synchronized public int getValue(int key){ //get value at specific key
        return (int)results.get(key);
    }
}
