import java.util.Properties;

public class Java{
    public void jInfo(Properties myProps){
        System.out.println("Java Vendor: " + myProps.getProperty("java.vendor") + "\n" + "Java Runtime: " +
                myProps.getProperty("java.runtime.name") + "\n" + "Java Version: "
                + myProps.getProperty("java.version") + "\n" + "Java VM Version: " + myProps.getProperty("java.vm.version")
                + "\n" + "Java VM Name: " + myProps.getProperty("java.vm.name"));
    }
}