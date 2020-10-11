import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;

public class TaskQueue {
    private LinkedList<Task> queue = new LinkedList<>();
    private ArrayList<Task> taskList = new ArrayList<>(1000);


    TaskQueue(){ //populate the queue and shuffle its contents
        for (int i = 1; i <= 1000; i++){
            Task t = new Task(i);
            taskList.add(t);
        }
        Collections.shuffle(taskList);

        for(Task t : taskList){
            queue.add(t);
        }
    }

    synchronized public Task pop(){
        return queue.removeFirst();
    }

    synchronized public boolean empty(){
        return queue.isEmpty();
    }

}
