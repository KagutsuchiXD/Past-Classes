
import java.util.Properties;

public class Assign2 {

    public static void main(String[] args) {
        Properties myProps = System.getProperties();
        Runtime runner = Runtime.getRuntime();
        for(int i = 0; i < args.length; i+=1){
            if(args[i].equals("-cpu")){
                System.out.println("Processors:  " + runner.availableProcessors());
            }
            else if(args[i].equals("-mem")){
                System.out.println("Free Memory: " + runner.freeMemory() + "\n"
                + "Total Memory: " + runner.totalMemory() + "\n" + "Max Memory: " +
                runner.maxMemory());
            }
            else if(args[i].equals("-dirs")){
                System.out.println("Working Directory: " + myProps.getProperty("user.dir")
                + "\n" + "User Home Directory: " + myProps.getProperty("user.home"));
            }
            else if(args[i].equals("-os")){
                System.out.println("OS Name: " + myProps.getProperty("os.name") + "\n"
                + "OS Version: " + myProps.getProperty("os.version"));
            }
            else if(args[i].equals("-java")){
                System.out.println("Java Vendor: " + myProps.getProperty("java.vendor") + "\n" + "Java Runtime: " +
                        myProps.getProperty("java.runtime.name") + "\n" + "Java Version: "
                + myProps.getProperty("java.version") + "\n" + "Java VM Version: " + myProps.getProperty("java.vm.version")
                        + "\n" + "Java VM Name: " + myProps.getProperty("java.vm.name"));
            }
            else{
                System.out.println("Invalid input.");
            }
        }
    }

}
