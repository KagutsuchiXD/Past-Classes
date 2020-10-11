import java.util.LinkedList;
import java.util.Queue;

public class SchedulerRR extends SchedulerBase implements Scheduler {
    private Platform platform;
    private Queue<Process> processes = new LinkedList<>();
    private int timeslice;

    SchedulerRR(Platform platform, int time) {
        this.platform = platform;
        this.timeslice = time;
    }

    @Override
    public void notifyNewProcess(Process p) {
        processes.add(p);
    }

    @Override
    public Process update(Process cpu) {
        //check to see if we are passed a process or null
        if (cpu == null) { //if passed a null
            //check to see if the queue is empty
            if (processes.isEmpty()) { //if it is return null
                return null;
            } else { // if not remove the next process in the queue and return it
                Process p = processes.remove();
                contextSwitches++;
                platform.log("Scheduled: " + p.getName());
                return p;
            }
        } else {// if passed a process
            if (!cpu.isExecutionComplete()) { // check if the process is finished
                if ((cpu.getElapsedTotal()%timeslice) == 0) { //check if the process has finished  a time quantum
                    contextSwitches++;
                    platform.log("Time quantum complete for process  " + cpu.getName());
                    processes.add(cpu);
                    if (processes.isEmpty()) {
                        return null;
                    } else {
                        contextSwitches++;
                        Process p = processes.remove();
                        platform.log("Scheduled: " + p.getName());
                        return p;
                    }
                } else {
                    return cpu;
                }
            } else {
                if (processes.isEmpty()) { // if process is done and the queue is empty return null
                    platform.log("Process" + cpu.getName() + " execution complete");
                    contextSwitches++;
                    return null;
                } else {// if process is done and the queue is not empty return the next process from queue
                    contextSwitches += 2;
                    platform.log("Process " + cpu.getName() + " execution complete");
                    Process p = processes.remove();
                    platform.log("Scheduled: " + p.getName());
                    return p;
                }
            }
        }
    }
}