package pwz.b_orakit_sprint_1.core;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class ServiceToken {
    /**
     * service info map
     * <p>
     * key: token
     * isBlockThread: if yes, main thread need to be blocked until the task finished.
     */
    public static final HashMap<String, HashMap<String, String>> tokenInfo = new HashMap<String, HashMap<String, String>>() {
        {
            put("snake", new HashMap<String, String>() {{
                put("class", "pwz.b_orakit_sprint_1.service.Snake.Scene");
                put("method", "main");
                put("isBlockThread", "no");
                put("greetings", "enjoy the game~");
            }});
            put("weather", new HashMap<String, String>() {{
                put("class", "pwz.b_orakit_sprint_1.service.WeatherQueryUtil");
                put("method", "queryWeather");
                put("isBlockThread", "yes");
                put("greetings", "");
            }});
        }
    };
}
