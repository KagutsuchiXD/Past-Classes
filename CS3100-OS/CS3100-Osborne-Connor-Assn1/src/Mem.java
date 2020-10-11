public class Mem{
    public void memory(Runtime runner){
        System.out.println("Free Memory: " + runner.freeMemory() + "\n"
                + "Total Memory: " + runner.totalMemory() + "\n" + "Max Memory: " +
                runner.maxMemory());
    }
}