package pwz.b_orakit_sprint_1.core;

import java.util.ArrayList;
import java.util.Scanner;

public class OriKit {
    //private static NLPChunk nlpc;

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        String input;
        ArrayList<String> tokens;
        NLPChunk.sayHello();

        while(true) {
            input = in.nextLine();
            tokens = NLPChunk.tokenAnalyze(input);
            LogicChunk.doLogic(tokens);
        }
    }
}
