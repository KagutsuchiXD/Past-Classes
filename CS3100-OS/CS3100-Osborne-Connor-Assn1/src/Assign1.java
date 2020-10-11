
import java.util.Properties;

public class Assign1 {
    public static void main(String[] args) {
        Properties myProps = System.getProperties();
        Runtime runner = Runtime.getRuntime();
        for(int i = 0; i < args.length; i+=1){
            if(args[i].equals("-cpu")){
                CPU cpu = new CPU();
                cpu.numCPU(runner);
            }
            else if(args[i].equals("-mem")){
                Mem mem = new Mem();
                mem.memory(runner);
            }
            else if(args[i].equals("-dirs")){
                Dirs dirs = new Dirs();
                dirs.dirInfo(myProps);
            }
            else if(args[i].equals("-os")){
                OS os = new OS();
                os.osInfo(myProps);
            }
            else if(args[i].equals("-java")){
                Java java = new Java();
                java.jInfo(myProps);
            }
            else{
                System.out.println("Invalid input.");
            }
        }
    }
}