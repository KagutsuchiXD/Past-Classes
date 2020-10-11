import java.util.*;

public class SchedulerPriority extends SchedulerBase implements Scheduler {
    private Platform platform;
    private ArrayList<Process> processes = new ArrayList<>();

    SchedulerPriority(Platform platform){
        this.platform = platform;
    }

    @Override
    public void notifyNewProcess(Process p) { // adds processes to the queue
        processes.add(p);
        if(!processes.isEmpty()){
            Collections.sort(processes, rator);
        }
    }

    @Override
    public Process update(Process cpu) {
        //check to see if we are passed a process or null
        if (cpu == null){ //if passed a null
            //check to see if the queue is empty
            if(processes.isEmpty()){ //if it is return null
                return null;
            }
            else{ // if not remove the next process in the queue and return it
                Process p = processes.remove(0);
                contextSwitches++;
                platform.log("Scheduled: "+ p.getName());
                return p;
            }
        }
        else{// if passed a process
            if(!cpu.isExecutionComplete()){ // check if the process is finished
                if(!cpu.isBurstComplete()){ //check if the process has finished a burst
                    return cpu; //if burst isn't over send process back
                }
                else{
                    contextSwitches++; //if burst is over add it to the queue and send the next process
                    platform.log("Process " + cpu.getName() + " burst complete");
                    processes.add(cpu);

                    if(processes.isEmpty()){
                        return null;
                    }
                    else{
                        contextSwitches++;
                        Process p = processes.remove(0);
                        platform.log("Scheduled: " + p.getName());
                        return p;
                    }
                }
            }
            else{
                if(processes.isEmpty()){ // if process is done and the queue is empty return null
                    platform.log("Process" + cpu.getName() + " burst complete");
                    platform.log("Process" + cpu.getName() + " execution complete");
                    contextSwitches++;
                    return null;
                }
                else{// if process is done and the queue is not empty return the next process from queue
                    contextSwitches+=2;
                    platform.log("Process " + cpu.getName() + " burst complete");
                    platform.log("Process " + cpu.getName() + " execution complete");
                    Process p = processes.remove(0);
                    platform.log("Scheduled: " + p.getName());
                    return p;
                }
            }
        }
    }

    Comparator<Process> rator = new Comparator<Process>() {
        @Override
        public int compare(Process p1, Process p2) {
            if(p1.getPriority() < p2.getPriority()){
                return -1;
            }
            else if(p1.getBurstTime() == p2.getBurstTime()){
                return 0;
            }
            else{
                return 1;
            }
        }
    };
}
