import java.io.File;
import java.text.SimpleDateFormat;
import java.util.Date;

public class ListFiles {
    //list all files in current directory
    public static void ls(File cdir){
        File[] dirList = cdir.listFiles();
        for(File f: dirList){
            String drwx = "";
            String name = f.getName();
            String size = String.valueOf(f.getTotalSpace());

            StringBuilder sb = new StringBuilder();
            while((sb.length() + size.length()) <= 9){
                sb.append(" ");
            }
            sb.append(size);
            String date = new SimpleDateFormat("MMM dd, yyyy HH:mm").format(new Date(f.lastModified()));
            if (f.isDirectory()){
                drwx += "d";
            }
            else{
                drwx += "-";
            }
            if(f.canRead()){
                drwx += "r";
            }
            else{
                drwx += "-";
            }
            if(f.canWrite()){
                drwx += "w";
            }
            else{
                drwx += "-";
            }
            if(f.canExecute()){
                drwx += "x";
            }
            else{
                drwx += "-";
            }
            System.out.println(drwx + " " + sb + "  " + date + " " + name);
        }
    }
}
