public class Ptime {
    long timer = 0;
    long start = 0;
    long stop = 0;
    //display time spent in child processes
    public static void totalTime(Long ptime){
        float timeInSecs = (ptime.floatValue() / 1000);
        System.out.printf("Total time in child processes: %.4f seconds\n", timeInSecs);
    }
}
