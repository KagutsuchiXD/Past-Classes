import java.io.File;
import java.util.ArrayList;

public class Cd {
    //"change" working directory
    public static void changeDir(ArrayList<String> clist){
        if(clist.get(clist.size()-1).equals("cd")){
            File home = new File(System.getProperty("user.home"));
            System.setProperty("user.dir", home.getAbsolutePath());
        }
        else if(clist.get(1).equals("..")){
            File current = new File(System.getProperty("user.dir"));
            File parent = current.getParentFile();
            if(parent.exists()){
                System.setProperty("user.dir", parent.getAbsolutePath());
            }
            else{   		//if directory doesn't exist
                System.out.println("Parent folder does not exist");
            }
        }
        else if(clist.get(1).contains("/")){
            File newPath = new File(clist.get(1));
            File path = newPath.getAbsoluteFile();

            if(path.exists()){
                System.setProperty("user.dir", newPath.getAbsolutePath());
            }
            else{   		//if directory doesn't exist
                System.out.println("Path " + clist.get(1) + " does not exist");
            }
        }
        else{
            File newPath = new File(System.getProperty("user.dir") + "\\" +clist.get(1));
            File path = newPath.getAbsoluteFile();

            if(path.exists()){
                System.setProperty("user.dir", newPath.getAbsolutePath());
            }
            else{   		//if directory doesn't exist
                System.out.println("Path " + path + " does not exist");
            }
        }
    }
}

