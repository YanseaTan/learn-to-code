package pwz.a_review_java_basic.further;

import java.io.IOException;

/**
 * about exception,
 * checked exception, unchecked exception
 * runtime exception, non-runtime exception
 * ...
 * so much to read ... sleeppppy
 */
public class AboutExceptions {

    static class WhateverException extends Exception {
        public WhateverException() {
        }

        public WhateverException(String message) {
            super("Message from WhateverException: " + message);
        }
    }

    public static void makeIOException() throws IOException {
        AboutIOStream.readFirstLineOfAFile("test");
    }

    public static void makeMyOwnException() throws WhateverException {
        throw new WhateverException("whatever...");
    }

    public static void main(String[] args) {
        try {
            makeIOException();
        } catch (IOException e) {
            System.out.println("Oops, IOException:");
            e.printStackTrace();
        }

        try {
            makeMyOwnException();
        }catch (WhateverException we){
            System.out.println("Oops, WhateverException:");
            we.printStackTrace();
        }
    }
}
