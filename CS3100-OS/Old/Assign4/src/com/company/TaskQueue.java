package com.company;

import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;

public class TaskQueue {
    private LinkedList<Task> queue = new LinkedList<>();
    private ArrayList<Task> taskList = new ArrayList<>(1000);


    public TaskQueue(){
        for (int i = 0; i <= 999; i++){
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

    public int size(){
        return queue.size();
    }

    public boolean empty(){
        return queue.isEmpty();
    }

}
