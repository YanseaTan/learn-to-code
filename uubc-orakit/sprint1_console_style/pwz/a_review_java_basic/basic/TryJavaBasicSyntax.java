package pwz.a_review_java_basic.basic;

import java.util.Scanner;
import static java.lang.Math.*;

/**
 * this is Documentation Comments used to generate documentation automatically
 * Core Java --> Chapter1~3 reading notes
 * @author pengwei.zhang
 * @version 2022.01.21
 * @see <a href="www.horstmann.com/corejava.html">Core Java</a>
 */
public class TryJavaBasicSyntax {

    /**
     * documentation comment contains free-form text followed by tags.
     * A tag starts with an @, such as @since or @param.
     *
     * 8 primitive type in java: integer*4 + floating-point*2 + char + boolean
     *
     * @author pengwei.zhang
     * @return well, always -1
     */
    public int tryPrimitiveType(){
        // JAVA is a kind of strongly type programming language, that means every variable
        // ~~should~~ must be declared a type

        // Java is a strongly typed language. This means that every variable must have a
        // declared type.

        // integer types
        int a = abs(-4); //int ~ 4 bytes ~ –2,147,483,648 to 2,147,483,647
        short b = 2; // short int ~ 2 bytes ~ –32,768 to 32,767
        long c = 8; // long int ~ 8 bytes ~ –9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
        byte d = 1; // byte is just a byte ~ –128 to 127
        // note: no unsigned int in java
        // tips: you can write big int in this way: 100_0000_0000
        long people_on_earth = 9_000_000_000L; // note: add suffix 'L' after a long type integer

        // Floating-Point Types
        float ff = 4.0f;
        double dd = 8.0; // a floating point number will be process as double type in default
        double ddd = 8.0d; // add a 'd' after a double number to make it more clear, however that's unnecessary
        // clearer ~ more clear ~ both ok

        // char is just char
        char aaa = ' '; // ' ' = 32, first visible ascii character
        char zzz = 'z';
        for (int i = aaa;; i++){
            if(i > (int)zzz)break;
            System.out.printf("%d  =  %c\n",i,(char)i);
        }

        // boolean
        boolean t = true;
        boolean f = false;
        // you can't do this: boolean x = 0 or 1;
        // boolean x = 0; won't work...

        return -1;
    }

    /**
     * Conceptually, Java strings are sequences of Unicode characters.
     */
    public void tryString(){
        String ss = "this is a test sentence.";
        System.out.println(ss);

        // substring
        String ss_sub = ss.substring(0, 4);
        System.out.println(ss_sub);

        // concat
        String ss_concat = ss + " " + ss_sub;
        System.out.println(ss_concat);
        System.out.println("you can also do it here +++ " + ss_concat);

        // !! Strings Are Immutable
        String test_1 = "test 1";
        System.out.println(test_1.hashCode());
        test_1 = "test 2";
        String test_2 = "test 2";
        System.out.println(test_1.hashCode());
        System.out.println(test_2.hashCode());
        test_2 = "test 1";
        System.out.println(test_2.hashCode());
        // -877171677
        // -877171676
        // -877171676
        // -877171677

        // equal
        String e1 = "abcd";
        String e2 = "abc";
        System.out.printf("e1.substring(0,3): %s\n", e1.substring(0,3));
        System.out.println(e2.equals(e1.substring(0,3))); // using equal!
        System.out.println(e2 == e1.substring(0,3)); // stop using "==" for equal
        // e1.substring(0,3): abc
        // true
        // false

        // > The String class in Java contains more than 50 methods. A surprisingly large
        // > number of them are sufficiently useful that we can imagine using them
        // > frequently.
    }

    /**
     * cout is easy, now try cin. :)
     */
    public void tryStandardIO(){
        // > Whenever you use a class that is not defined in the basic
        // > java.lang package, you need to use an import directive.
        // import java.util.Scanner
        Scanner cin = new Scanner(System.in);
        System.out.println("please input something, whatever:");
        String sentence_input = cin.nextLine();
        System.out.println("Your input: " + sentence_input);
        try {
            System.out.println("please input a int:");
            int int_input = cin.nextInt();
            System.out.println(int_input);
            System.out.println("please input a float:");
            float float_input = cin.nextFloat();
            System.out.println(float_input);
        }catch (Exception e){
            System.out.println("oops, illegal input.");
        }

        System.out.println("Now I will repeat your input, enter \"bye\" to exit.");
        String whatever_input = cin.next();
        while (!whatever_input.equals("bye")){
            System.out.println(":) " + whatever_input);
            whatever_input = cin.next();
        }
        System.out.println("byebye~");
    }

    /**
     * try control flow
     */
    public void tryControlFlow(){
        int k;
        { // this is a code block
            // int k; can't define another k in the block
            int i=0; // this i is only valid in this block

            // for
            System.out.printf("now i = %d\n", i);
            for(;i<5;++i){
                System.out.printf("for loop... just like c... %d\n", i);
            }

            // while
            System.out.printf("now i = %d\n", i);
            while (i>0){
                System.out.printf("well, while...ing... %d\n", i--);
            }

            // do-while
            System.out.printf("now i = %d\n", i);
            do{
                System.out.printf("well, do-while...ing... %d\n", i++);
            }while (i < 3);
        }
        // System.out.println(i); // can't find the i out of the block

        // switch
        int outer_flag = -1;
        do{
            int random_number = (int) (random()*10);
            switch (random_number){
                case 0:
                    System.out.println("0! cool! but not 3.");
                    break;
                case 1:
                    System.out.println("1! cool! but not 3.");
                    break;
                case 2:
                    System.out.println("2! cool! but not 3.");
                    break;
                case 5:
                    System.out.println("5! cool! but not 3.");
                    break;
                case 6:
                    System.out.println("6! cool! but not 3.");
                    break;
                case 7:
                    System.out.println("7! cool! but not 3.");
                    break;
                case 8:
                    System.out.println("8! cool! but not 3.");
                    break;
                case 9:
                    System.out.println("9! cool! but not 3.");
                    break;
                case 10:
                    System.out.println("10! nice! but not 3.");
                    break;
            }
            outer_flag = random_number;
        } while (outer_flag != 3);
        System.out.println("3!!!!!");

        // foreach
        // for (variable : collection) statement
        int[] a = new int[10];
        for (int i = 0; i< 10; ++i)a[i] = i;
        for (int x: a)  System.out.println(x);

    }

    public static void main(String[] args) {
        TryJavaBasicSyntax tjbs = new TryJavaBasicSyntax();
        // tjbs.tryPrimitiveType();
        // tjbs.tryString();
        // tjbs.tryStandardIO();
        tjbs.tryControlFlow();
    }

}
