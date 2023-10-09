package pwz.orakit_sprint_3.service_impl;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class ChatBot {
    public static String chat(){
        return "default response from chatbot";
    }
    public static String getHomepage(){
        try {
            String filePath = "../static_site/index.html";
            Path path = Paths.get(filePath);
            byte[] bytes = Files.readAllBytes(path);
            return new String(bytes);
        } catch (IOException e) {
            e.printStackTrace();
            return "";
        }
    }
}
