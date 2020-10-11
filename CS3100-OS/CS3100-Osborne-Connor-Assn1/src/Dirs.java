import java.util.Properties;

public class Dirs{
    public void dirInfo(Properties myProps){
        System.out.println("Working Directory: " + myProps.getProperty("user.dir")
                + "\n" + "User Home Directory: " + myProps.getProperty("user.home"));
    }
}
