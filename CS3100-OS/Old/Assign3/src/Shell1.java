package com.company;

import java.io.*;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;

public class Shell {

    public static void main(String[] args) throws java.io.IOException{
        String commandLine;
        long ptime = 0;
        BufferedReader console = new BufferedReader
                (new InputStreamReader(System.in));

        ProcessBuilder pb = new ProcessBuilder();

        ArrayList<ArrayList> history = new ArrayList<ArrayList>();
        boolean go = true;
        while(go){
            pb.directory(new File(System.getProperty("user.dir")));
            System.out.print("[" + pb.directory() + "]:");
            commandLine = console.readLine();
            String[] commands = commandLine.split(" ");
            ArrayList<String> clist = new ArrayList<String>();

            for(int i = 0;i<commands.length;i++){
                clist.add(commands[i]);
            }
            history.add(clist);
            try{
                //if the user entered a return, just loop again
                if(commandLine.equals(""))
                    continue;
                //display history of shell with index
                else if(clist.get(0).equals("ptime")){
                    long start = System.currentTimeMillis();
                    totalTime(ptime);
                    long stop = System.currentTimeMillis();
                    ptime += (stop - start);
                    continue;
                }
                else if(clist.get(0).equals("history")){
                    long start = System.currentTimeMillis();
                    history(history);
                    long stop = System.currentTimeMillis();
                    ptime += (stop - start);
                    continue;
                }
                else if(clist.contains("|")){
                    long start = System.currentTimeMillis();
                    piper(clist);
                    long stop = System.currentTimeMillis();
                    ptime += (stop - start);
                    continue;
                }
                else if(clist.contains("list")){
                    long start = System.currentTimeMillis();
                    ls(pb.directory());
                    long stop = System.currentTimeMillis();
                    ptime += (stop - start);
                    continue;
                }
                else if(clist.contains("cd")){
                    long start = System.currentTimeMillis();
                    cd(clist);
                    long stop = System.currentTimeMillis();
                    ptime += (stop - start);
                    continue;
                }
                else if(clist.get(0).equals("^")){//^ <integer value i> command
                    long start = System.currentTimeMillis();
                    recall(ptime, pb, history, clist);
                    long stop = System.currentTimeMillis();
                    ptime += (stop - start);
                    continue;
                }
                else if(clist.get(clist.size()-1).equals("exit")){
                    System.out.println("Goodbye!");
                    go = false;
                    continue;
                }
                else{
                    pb.command(clist);
                }

                Process process = pb.start();

                //obtain the input stream
                InputStream is = process.getInputStream();
                InputStreamReader isr = new InputStreamReader(is);
                BufferedReader br = new BufferedReader(isr);

                //read output of the process
                String line;
                while((line = br.readLine()) != null)
                    System.out.println(line);
                br.close();

            }
            catch (IOException e){
                System.out.println("Input Error, Please try again! \nValid commands include: ptime, history," +
                        "^ <history number>, list, cd <directory path>, | for piping, exit");
            }
        }
    }
    private static void totalTime(Long ptime){
        float timeInSecs = (ptime.floatValue() / 1000);
        System.out.printf("Total time in child processes: %.4f seconds\n", timeInSecs);
    }
    private static void history(ArrayList<ArrayList> history){
        int index = 1;
        for(ArrayList s : history) {
            System.out.println((index) + ": " + s);
            index++;
        }
    }
    private static void ls(File cdir){
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
    private static void cd(ArrayList<String> clist){
        if(clist.get(clist.size()-1).equals("cd")){
            File home = new File(System.getProperty("user.home"));
            System.setProperty("user.dir", home.getAbsolutePath());
        }
        else if (clist.get(1).equals("..")){
            File current = new File(System.getProperty("user.dir"));
            File parent = current.getParentFile();
            if(parent.exists()){
                System.setProperty("user.dir", parent.getAbsolutePath());
            }
            else{   		//if directory doesn't exist
                System.out.println("Parent folder does not exist");
            }
        }
        else{
            File newPath = new File(clist.get(1));
            File path = newPath.getAbsoluteFile();

            if(path.exists()){
                System.setProperty("user.dir", newPath.getAbsolutePath());
            }
            else{   		//if directory doesn't exist
                System.out.println("Path " + clist.get(1) + " does not exist");
            }
        }
    }
    private static void recall(Long ptime, ProcessBuilder pb, ArrayList<ArrayList> history, ArrayList<String> clist)
    throws java.io.IOException{
        if(clist.size() > 1){
            if(clist.get(1).matches("[0-9]+")){
                try{
                    int b = Integer.parseInt(clist.get(1));
                    if (b <= history.size())//check if integer entered isn't bigger than history size
                    {
                        checker(ptime, history, history.get(b -1), pb);
                    }
                }
                catch (IOException e){
                    System.out.println("Input Error, Please try again! \nValid commands include: ptime, history," +
                            "^ <history number>, list, cd <directory path>, | for piping, exit");
                }
            }
            else{
                System.out.println("Please input this command in this format \"^ <number>\".");
            }
        }
        else{
            System.out.println("You must input a number that corresponds to a command in history.");
        }
    }

    private static void piper(ArrayList<String> clist){
        System.out.println("Piping " + clist.get(0) + " to " + clist.get(2));
    }

    private static void checker(long ptime, ArrayList<ArrayList> history, ArrayList<String> command, ProcessBuilder pb)
            throws IOException {
        if(command.get(0).equals("history")){
            history(history);
        }
        else if(command.get(0).equals("ptime")){
            totalTime(ptime);
        }
        else if(command.contains("|")){
            piper(command);
        }
        else if(command.contains("list")){
            ls(pb.directory());
        }
        else if(command.contains("cd")){
            cd(command);
        }
        else if(command.get(0).equals("^")){//^ <integer value i> command
            recall(ptime, pb, history, command);
        }
        else{
            pb.command(command);
        }
    }
}
