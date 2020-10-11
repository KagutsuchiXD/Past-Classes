import java.util.Properties;

public class OS{
    public void osInfo(Properties myProps){
        System.out.println("OS Name: " + myProps.getProperty("os.name") + "\n"
                + "OS Version: " + myProps.getProperty("os.version"));
    }
}