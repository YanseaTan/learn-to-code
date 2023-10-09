package pwz.b_orakit_sprint_1.core;

import java.util.ArrayList;

public class NLPChunk {
    public static void sayHello(){
        System.out.println("what can I do for you?");
    }

    public static void say404(){
        System.out.println("I don't understand.");
    }

    public static ArrayList<String> tokenAnalyze(String sentence){
        ArrayList<String> tokens = new ArrayList<>();
        for (String token: ServiceToken.tokenInfo.keySet()){
            if (sentence.contains(token)){
                tokens.add(token);
            }
        }
        if (tokens.size() == 0) say404();
        return tokens;
    }
}