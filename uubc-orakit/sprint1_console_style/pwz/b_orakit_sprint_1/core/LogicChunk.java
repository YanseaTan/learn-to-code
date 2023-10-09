package pwz.b_orakit_sprint_1.core;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.HashMap;

public class LogicChunk {
    static class Task implements Runnable{
        String token;
        HashMap<String, String> tokenInfo;

        public Task(String token) {
            this.token = token;
            this.tokenInfo = ServiceToken.tokenInfo.get(token);
        }

        @Override
        public void run() {
            // output task start greetings
            if (tokenInfo.containsKey("greetings") && !tokenInfo.get("greetings").equals("")) {
                System.out.println(tokenInfo.get("greetings"));
            }
            // System.out.println(Thread.currentThread().getName());
            // try to run the task
            try {
                String className = tokenInfo.get("class");
                Class cl = Class.forName(className);

                Method mainMethod = cl.getDeclaredMethod(tokenInfo.get("method"), String[].class);
                mainMethod.invoke(null, (Object) new String[]{});

            } catch (ClassNotFoundException | NoSuchMethodException | InvocationTargetException | IllegalAccessException e) {
                e.printStackTrace();
            }

            // output task finished greetings
            // System.out.println(tokenInfo.get("result"));

        }
    }

    public static boolean doLogic(ArrayList<String> tokens){
        try {
            for(String token: tokens){
                Task task = new Task(token);
                Thread th = new Thread(task);
                th.start();
                // System.out.println(Thread.currentThread().getName());
                if(task.tokenInfo.get("isBlockThread").equals("yes")){
                    th.join();
                }
            }
        }catch (Throwable throwable){
            throwable.printStackTrace();
            return false;
        }
        return true;
    }
}
