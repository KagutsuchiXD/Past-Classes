package com.company;

public class Work implements Runnable{

    private TaskQueue queue = new TaskQueue();
    private ResultTable table = new ResultTable();

    public void run(){
        while(!queue.empty()){
            try{
                Task job = queue.pop();
                table.add(job.getIndex(), job.calculate());
            }
            catch(Exception e){
                System.err.println(e);
            }
        }

    }
}
