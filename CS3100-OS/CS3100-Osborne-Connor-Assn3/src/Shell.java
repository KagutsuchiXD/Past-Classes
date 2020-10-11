import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Shell {
    public static void main(String[] args) throws java.io.IOException{
        String commandLine;
        Ptime time = new Ptime();
        BufferedReader console = new BufferedReader(new InputStreamReader(System.in));
        ProcessBuilder pb = new ProcessBuilder();

        ArrayList<ArrayList<String>> history = new ArrayList<>();
        boolean go = true;
        while(go){
            pb.directory(new File(System.getProperty("user.dir")));
            System.out.print("[" + pb.directory() + "]:");
            commandLine = console.readLine();
            String[] commands = splitCommand(commandLine);
            ArrayList<String> clist = new ArrayList<String>();

            Collections.addAll(clist, commands);
            history.add(clist);
            try{
                //if the user entered a return, just loop again
                if(commandLine.equals("")) {
                }
                else if(clist.contains("list")){
                    ListFiles files = new ListFiles();
                    files.ls(pb.directory());
                }
                else if(clist.contains("cd")){
                    Cd changer = new Cd();
                    changer.changeDir(clist);
                }
                else if(clist.contains("pwd")){
                    Pwd shellDir = new Pwd();
                    shellDir.pwd();
                }
                else if(clist.contains("ptime")){

                    time.totalTime(time.timer);
                }
                else if(clist.contains("history")){
                    History hlist = new History();
                    hlist.history(history);
                }
                else if(clist.get(0).equals("^")){//^ <integer value i> command
                    recall(time, pb, history, clist);
                }
                else if(clist.contains("|")){
                    long start = System.currentTimeMillis();
                    piper(clist);
                    long stop = System.currentTimeMillis();
                    time.timer += (stop - start);
                }
                else if(clist.get(clist.size()-1).equals("exit")){
                    System.out.println("Goodbye!");
                    go = false;
                }
                else{
                    try{
                        pb.command(clist);
                        if (clist.contains("&")){
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
                        time.start = System.currentTimeMillis();
                        Process process = pb.start();
                        process.waitFor();

                        //obtain the input stream
                        InputStream is = process.getInputStream();
                        InputStreamReader isr = new InputStreamReader(is);
                        BufferedReader br = new BufferedReader(isr);

                        //read output of the process
                        String line;
                        while((line = br.readLine()) != null)
                            System.out.println(line);
                        br.close();
                        time.stop = System.currentTimeMillis();
                        time.timer += (time.stop - time.start);
                    }
                    catch(InterruptedException e){
                        e.printStackTrace();
                    }
                }
            }
            catch (IOException e){
                System.out.println("Input Error, Please try again! \nValid commands include: ptime, history," +
                        "^ <history number>, list, cd <directory path>, | for piping, exit");
            }
        }
    }
    /**
     * Split the user command by spaces, but preserving them when inside double-quotes.
     * Code Adapted from: https://stackoverflow.com/questions/366202/regex-for-splitting-a-
     * string-using-space-when-not-surrounded-by-single-or-double
     */
    private static String[] splitCommand(String command) {
        java.util.List<String> matchList = new java.util.ArrayList<>();

        Pattern regex = Pattern.compile("[^\\s\"']+|\"([^\"]*)\"|'([^']*)'");
        Matcher regexMatcher = regex.matcher(command);
        while (regexMatcher.find()) {
            if (regexMatcher.group(1) != null) {
                // Add double-quoted string without the quotes
                matchList.add(regexMatcher.group(1));
            } else if (regexMatcher.group(2) != null) {
                // Add single-quoted string without the quotes
                matchList.add(regexMatcher.group(2));
            } else {
                // Add unquoted word
                matchList.add(regexMatcher.group());
            }
        }

        return matchList.toArray(new String[matchList.size()]);
    }

    private static void recall(Ptime time, ProcessBuilder pb, ArrayList<ArrayList<String>> history, ArrayList<String> clist)
            throws java.io.IOException{
        if(clist.size() > 1){
            if(clist.get(1).matches("[0-9]+")){
                try{
                    int b = Integer.parseInt(clist.get(1));
                    if (b <= history.size())//make sure integer entered isn't bigger than history size
                    {
                        ArrayList<String> hist = history.get(b -1);
                        checker(time, history, hist, pb);
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

    private static void checker(Ptime time, ArrayList<ArrayList<String>> history, ArrayList<String> command, ProcessBuilder pb)
            throws IOException {
        if(command.contains("list")){
            ListFiles files = new ListFiles();
            files.ls(pb.directory());
        }
        else if(command.contains("cd")){
            Cd changer = new Cd();
            changer.changeDir(command);
        }
        else if(command.contains("history")){
            History hlist = new History();
            hlist.history(history);
        }
        else if(command.contains("pwd")){
            Pwd shellDir = new Pwd();
            shellDir.pwd();
        }
        else if(command.contains("ptime")){
            time.totalTime(time.timer);
        }
        else if(command.contains("|")){
            long start = System.currentTimeMillis();
            piper(command);
            long stop = System.currentTimeMillis();
            time.timer += (stop - start);
        }
        else if(command.get(0).equals("^")){//^ <integer value i> command
            recall(time, pb, history, command);
        }
        else{
            try{
                pb.command(command);
                if (command.contains("&")){
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
                time.start = System.currentTimeMillis();
                Process process = pb.start();
                process.waitFor();

                //obtain the input stream
                InputStream is = process.getInputStream();
                InputStreamReader isr = new InputStreamReader(is);
                BufferedReader br = new BufferedReader(isr);

                //read output of the process
                String line;
                while((line = br.readLine()) != null)
                    System.out.println(line);
                br.close();
                time.stop = System.currentTimeMillis();
                time.timer += (time.stop - time.start);
            }
            catch(InterruptedException e){
                e.printStackTrace();
            }
        }
    }

    private static void piper(ArrayList<String> clist){
        try {
            //splitting our command_list into two sets of commands for both of our processes
            int splitter = clist.indexOf("|");
            ArrayList<String> command1 =  (ArrayList<String>) clist.subList(0, splitter);
            ArrayList<String> command2 = (ArrayList<String>) clist.subList(splitter + 1, clist.size());
            //creating our first process in our current directory
            ProcessBuilder pb1 = new ProcessBuilder();
            pb1.directory(new File(System.getProperty("user.dir")));
            //setting arguments and which process to execute
            pb1.command(command1);
            //Same thing for our second process here
            ProcessBuilder pb2 = new ProcessBuilder();
            pb2.directory(new File(System.getProperty("user.dir")));
            pb2.command(command2);
            //Creating a list of ProcessBuiders
            ArrayList<ProcessBuilder> builders = new ArrayList<>();
            builders.add(pb1);
            builders.add(pb2);
            List<Process> processes = ProcessBuilder.startPipeline(builders);
            Process last = processes.get(processes.size()-1);
            //getting the input stream so we can display output in our terminal
            InputStream is = last.getInputStream();
            String output = new String(is.readAllBytes(), StandardCharsets.UTF_8);
            System.out.println(output);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
