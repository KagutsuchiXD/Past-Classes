import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;


public class threads {

    public static class Maths implements Runnable {
        private String name;

        public Maths(String name) {
            this.name = "Maths #" + name;
        }

        public void run() {
            Thread.currentThread().setName(this.name);
            int a = 0;
            while (true)
                a++;
        }
    }

    public static class SlowIO implements Runnable {
        private static final int BUFSIZ = 8192;

        private String name;
        private String dev;


        public SlowIO(String dev) {
            this.name = "Slow I/O thread [" + dev + "]";
            this.dev = dev;
        }

        public void run() {
            Thread.currentThread().setName(this.name);
            System.out.format("\n\nWasting time with a cutting-edge I/O-Bound algorithm on the slow data source %s\n%d bytes at a time\n",
                    this.dev, SlowIO.BUFSIZ);

            byte[] buffer = new byte[SlowIO.BUFSIZ];
            while (true) {
                try {
                    FileInputStream slow = new FileInputStream(this.dev);
                    slow.read(buffer);
                    slow.close();

                    FileOutputStream devNull = new FileOutputStream("/dev/null");
                    devNull.write(buffer);
                    devNull.close();
                }
                catch (Exception e) {
                    System.err.println(e);
                }
            }
        }
    }


    public static void main(String[] args) {
        String IO_DEV = "/dev/sda";
        String device;

        if (args.length >= 1)
            device = args[0];
        else
            device = IO_DEV;

        try {
            // Create an array of 6 thread objects running the the 'maths' method
            Thread[] threads = new Thread[6];
            for (int i = 0; i < 6; ++i) {
                threads[i] = new Thread(new Maths(String.format("%d", i)));
                threads[i].start();
                System.out.format("Spawning maths thread #%d\n", i);
            }

            Thread tio = new Thread(new SlowIO(device));
            tio.start();
            System.out.format("Spawning Slow I/O thread on device %s\n", device);

            System.out.println("Press Ctrl-C to quit");

            for (int i = 0; i < 6; ++i) {
                threads[i].join();
                System.out.format("Joined maths thread #%d\n", i);
            }

            tio.join();
            System.out.println("Joined Slow I/O thread");
        }
        catch (Exception e) {
            System.err.println(e);
        }
    }
}
