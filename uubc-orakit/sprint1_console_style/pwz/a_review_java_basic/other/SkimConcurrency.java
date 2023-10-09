package pwz.a_review_java_basic.other;

public class SkimConcurrency {

    /**
     * init and start two threads
     */
    public static void helloThread(){
        Runnable r = ()->{
            for(int i=0;i<3;++i){
                System.out.println(Thread.currentThread() + ": " + i);
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        };

        Runnable x = ()->{
            for(int i=0;i<15;++i){
                System.out.println(Thread.currentThread() + ": " + i);
                try {
                    Thread.sleep(200);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        };

        Thread rr = new Thread(r);
        Thread xx = new Thread(x);
        rr.start();
        xx.start();
    }
    /*
    Thread[Thread-1,5,main]: 0
    Thread[Thread-0,5,main]: 0
    Thread[Thread-1,5,main]: 1
    Thread[Thread-1,5,main]: 2
    Thread[Thread-1,5,main]: 3
    Thread[Thread-1,5,main]: 4
    Thread[Thread-0,5,main]: 1
    Thread[Thread-1,5,main]: 5
    Thread[Thread-1,5,main]: 6
    Thread[Thread-1,5,main]: 7
    Thread[Thread-1,5,main]: 8
    Thread[Thread-1,5,main]: 9
    Thread[Thread-0,5,main]: 2
    Thread[Thread-1,5,main]: 10
    Thread[Thread-1,5,main]: 11
    Thread[Thread-1,5,main]: 12
    Thread[Thread-1,5,main]: 13
    Thread[Thread-1,5,main]: 14
     */

    public static void main(String[] args) {
        helloThread();
    }
}
