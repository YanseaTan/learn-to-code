package pwz.orakit_sprint_3.http_server;

import pwz.orakit_sprint_3.service_impl.ChatBot;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class HttpServer {
    /**
     * 后台路由，调用实际服务获取响应结果，返回
     * @param requestString 请求体（简化问题没有额外封装，直接按照String处理）
     * @return 后台响应结果response（同request，未封装，只返回String）
     */
    private static String urlRoute(String requestString){
        String response = "";

        System.out.println("===============================\nurl analyzing...\n-----------------------------");
        // System.out.println(requestString);

        // 从Request中获取URL
        String firstLine = requestString.split("\n")[0];
        System.out.println("got first line from request: " + firstLine);
        String urlString = firstLine.split(" ")[1];
        System.out.println("got url from first line: " + urlString);

        // if-else实现路由逻辑
        //if(urlString.contains("chat")){
        //    response = ChatBot.chat();
        //}

        // switch实现路由逻辑
        switch (urlString){
            case "/":response = ChatBot.getHomepage();break;
            case "/chat":response = ChatBot.chat();break;
            case "/test":response = "You just hit an useless button!";break;
            default:response = "Sorry, I don't understand.";
        }

        // 反射实现路由逻辑
        // 略（参考OriKit Sprint1聊天启动服务的实现）

        System.out.println("-----------------------------\nurl analyzing...done\n===============================");
        System.out.println("response: " + response);
        return response;
    }

    /**
     * 启动http服务器
     * @param port 监听端口
     */
    public static void start(int port){
        try {
            ServerSocket serverSocket = new ServerSocket(port);
            System.out.println("http server started successfully.");

            while (true) {
                Socket client = serverSocket.accept();
                System.out.println("===============================\nreceived a request...\n-----------------------------");

                new Thread() {
                    @Override
                    public void run() {
                        try {
                            InputStream inputStream = client.getInputStream();
                            OutputStream outputStream = client.getOutputStream();

                            StringBuilder stringBuilder = new StringBuilder();
                            byte [] buffer = new byte[1024];
                            int readOffset = 0;
                            int count = 0;
                            while ((readOffset = inputStream.read(buffer)) != -1) {
                                stringBuilder.append(new String(buffer, 0, readOffset));
                                System.out.println(stringBuilder.toString());

                                // 为了解决read阻塞问题，按照约定判断最后一个3个字节数据
                                String last3Chars = stringBuilder.substring(stringBuilder.length()-3, stringBuilder.length());
//                                System.out.println("last 3 chars: " + last3Chars);
                                if(last3Chars.equals("EOF")){
                                    break;
                                }
                            }
                            System.out.println(stringBuilder);
                            System.out.println("-----------------------------\nreceived over.\n===============================");

                            String respText = urlRoute(stringBuilder.toString());

                            outputStream.write(
                                    ("HTTP/1.1 200\n"
                                    + "Content-Type: text/html\n"
                                    + "Access-Control-Allow-Origin: *\n"
                                    + "\n"
                                    + respText).getBytes()
                            );
                            outputStream.flush();
                            inputStream.close();
                            outputStream.close();
                        }catch (Throwable throwable){
                            throwable.printStackTrace();
                        }
                    }
                }.start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        start(8077);
    }
}