public class Work implements Runnable{

    private TaskQueue queue;
    private ResultTable table;

    private int taskNumber = 0;

    Work(TaskQueue tq, ResultTable rt){ // initialize usable TaskQueue and ResultTable
        queue = tq;
        table = rt;
    }

    public void run(){
        while(!queue.empty()){
            try{
                Task job = queue.pop();
                table.add(job.getIndex(), job.calculate());
                taskNumber++;
                if(taskNumber%100 == 0){
                    System.out.print(" . \n");
                    System.out.flush();
                }
                else if(taskNumber%10 == 0){
                    System.out.print(" . ");
                    System.out.flush();
                }
            }
            catch(Exception e){
                System.err.println(e);
            }
        }
    }

    public ResultTable getTable(){ //return ResultTable for value access
        return table;
    }
}
