package pwz.a_review_java_basic.further;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;

/**
 * so many io classes in java,
 * see Reader & Writer, InputStream & OutputStream
 * let's try standard console io and file io using some of them
 *
 * @see Reader
 * @see Writer
 * @see InputStream
 * @see OutputStream
 *
 * @see <a href="https://www.cnblogs.com/chhyan-dream/p/10770855.html"></a>
 */
public class AboutIOStream {

    // review Scanner used before
    public static void readWithScanner(){
        Scanner in = new Scanner(System.in);
        System.out.println("readWithScanner(), enter q to exit.");
        String line;
        do {
            line = in.nextLine();
            System.out.println(line);
        }while (!line.equals("q"));
        System.out.println("byebye.");
        in.close();
    }

    public static void readWithFileReader() throws IOException {
        FileReader fr = new FileReader("C:\\Users\\2087\\Desktop\\REPO\\uubc-orakit\\sprint1\\pwz\\java_notes\\further\\AboutExceptions.java");
        int len;
        while((len = fr.read()) != -1){
            System.out.println((char)len);
        }
        fr.close();
    }

    public static void readWithFileReaderWithBuffer() throws IOException {
        FileReader fr = new FileReader("C:\\Users\\2087\\Desktop\\REPO\\uubc-orakit\\sprint1\\pwz\\java_notes\\further\\AboutExceptions.java");
        // using a homemade buffer
        int len;
        char[] buffer = new char[10];
        while ((len = fr.read(buffer)) != -1){
            System.out.println(new String(buffer, 0, len));
        }
        fr.close();
    }

    /**
     * BufferedReader offer a buffer to reader
     * @see BufferedReader
     */
    public static void readWithBufferedReader() throws IOException {
        char c;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("readWithBufferedReader(), input chars, i will repeat. enter q to exit.");
        do {
            c = (char) br.read();
            System.out.println(c);
        }while (c != 'q');
        br.close();

        FileReader fr = new FileReader("");
        BufferedReader brr = new BufferedReader(fr, 100);
        String output;
        while ((output = brr.readLine()) != null){
            System.out.println(output);
        }
        brr.close();
    }

    public static void main(String[] args) throws IOException {
        AboutIOStream.readWithScanner();
        AboutIOStream.readWithFileReader();
        AboutIOStream.readWithFileReaderWithBuffer();
        AboutIOStream.readWithBufferedReader();
        byte[] aaa = "asldkfj".getBytes(StandardCharsets.UTF_8);
        System.out.println(new String(aaa));
    }

    public static void readFirstLineOfAFile(String path) throws IOException {
        FileReader fr = new FileReader(path);
        BufferedReader br = new BufferedReader(fr);
        System.out.println(br.readLine());
    }
}
