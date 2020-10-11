import java.io.IOException;
import java.lang.Process;
import java.lang.ProcessBuilder;
import java.util.concurrent.TimeUnit;
import java.io.File;

public class ProcessExample {
    public static void main(String[] args) {

        execProcess();
    }

    public static void execProcess() {
        System.out.printf("Current Directory: %s\n", System.getProperty("user.dir"));
        String currentDir = System.getProperty("user.dir");
        File fileDir = new File(currentDir);
        System.out.printf("The parent folder is: %s\n", fileDir.getParent());

        java.nio.file.Path proposed = java.nio.file.Paths.get(currentDir, "test");
        System.setProperty("user.dir", proposed.toString());
        System.out.printf("Updated Directory: %s\n", System.getProperty("user.dir"));

        String[] command = {"nanoabc", "ProcessExample.java"};
        ProcessBuilder pb = new ProcessBuilder(command);
        pb.redirectInput(ProcessBuilder.Redirect.INHERIT);
        pb.redirectOutput(ProcessBuilder.Redirect.INHERIT);

        try {
            long start = System.currentTimeMillis();
            Process p = pb.start();

            System.out.println("Starting to wait");
            p.waitFor();
            long end = System.currentTimeMillis();
            System.out.printf("Waited for %d milliseconds\n", end - start);
        }
        catch (IOException ex) {
            System.out.println("Illegal command");
        }
        catch (Exception ex) {
            System.out.println("Something else bad happened");
        }
    }
}