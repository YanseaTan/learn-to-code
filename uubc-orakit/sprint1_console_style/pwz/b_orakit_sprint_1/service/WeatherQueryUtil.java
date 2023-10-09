package pwz.b_orakit_sprint_1.service;

import com.google.gson.Gson;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class WeatherQueryUtil {

    // see more: https://api.sumt.cn/
    private static final String url = "https://api.66mz8.com/api/weather.php?location=";

    public static void queryWeather(String[] args){
        // System.out.println("where do you want to check the weather?");
        System.out.println("where?");
        Scanner in = new Scanner(System.in);
        String location = in.nextLine();
        // System.out.println("checking  " + location + "'s weather...");

        String queryUrl = url + location;
        String jsonString = get(queryUrl);
        // System.out.println(jsonString);

        Gson gson = new Gson();
        try {
            HashMap<String, Object> resultMap = gson.fromJson(jsonString, HashMap.class);
            // System.out.println(resultMap);
            String weather = (String) ((Map)((ArrayList)resultMap.get("data")).get(0)).get("weather");
            System.out.println(weather);
        }catch (Exception e){
            System.out.println("you sure '" + location + "'? I can't get it's weather info.");
            // e.printStackTrace();
        }

    }

    /**
     * impl http get method with native java lib
     *
     * 1.create connection
     * 2.set method
     * 3.set timeout
     *
     * @return json string
     */
    public static String get(String targetUrl) {
        HttpURLConnection conn = null;
        InputStream is = null;
        BufferedReader bfr = null;
        StringBuilder result = new StringBuilder();
        String buffer;

        try{
            URL _url = new URL(targetUrl);
            conn = (HttpURLConnection) _url.openConnection();
            conn.setRequestMethod("GET");
            conn.setReadTimeout(3000);
            conn.connect();

            if(conn.getResponseCode() == 200){
                is = conn.getInputStream();
                if(is != null) {
                    bfr = new BufferedReader(new InputStreamReader(is, StandardCharsets.UTF_8));
                    while((buffer = bfr.readLine()) != null){
                        result.append(buffer);
                    }
                }
            }

        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                is.close();
                bfr.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
            conn.disconnect();
        }
        return result.toString();
    }

    public static void main(String[] args) throws InterruptedException {
        queryWeather(null);
    }
}
