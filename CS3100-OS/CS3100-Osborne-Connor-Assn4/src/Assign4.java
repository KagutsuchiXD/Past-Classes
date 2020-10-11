public class Assign4 {

    public static void main(String[] args) {
        long start_time = 0; //variables for traking the completion time
        long end_time = 0;
        TaskQueue queue = new TaskQueue();
        ResultTable table = new ResultTable();
        int processors = Runtime.getRuntime().availableProcessors();
        Thread[] workers = new Thread[processors]; // create number of threads equal to number of available processors.
        Work work = new Work(queue, table);

        try{
            start_time = java.lang.System.currentTimeMillis();
            for(int i = 0; i < processors; ++i){ //initialize threads to use the run method of Work
                workers[i] = new Thread(work);
                workers[i].start();
            }
            for (int i = 0; i < processors; ++i) {
                workers[i].join(); //waits for the threads to finish their work and end them.
            }
            end_time = java.lang.System.currentTimeMillis();
        }
        catch(Exception e){
            System.err.println(e);
        }
        long total_time = (end_time - start_time)/1000;

        StringBuilder decimalDigits = new StringBuilder(); // used to make all of the digits into one string
        for(int i = 1; i <= 1000; i++){
            decimalDigits.append(table.getValue(i));
        }

        System.out.println("\n3." + decimalDigits + "\n");

        System.out.println("Pi Computation took: " + total_time + " seconds on " + processors + " processors!");
    }
}
