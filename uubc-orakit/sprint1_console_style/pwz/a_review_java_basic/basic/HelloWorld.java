package pwz.a_review_java_basic.basic;

public class HelloWorld{
    public static void main(String[] args) {
        System.out.println("HELLO WORLD!");
        int count = 100;
        for (int i = 0; i < count; ++i){
            if(i %10 == 0){
                System.out.print("\n");
            }
            System.out.print("*");
        }
        System.out.print("*");
        while (count > 0){
            System.out.println(count);
            count-=10;
        }
        
    }
}

/**
 * 
pwz@test MINGW64 ~/Desktop/REPO/uubc-orakit/sprint1/pwz/learn_java_basic (main)
$ ls
HelloWorld.java

pwz@test MINGW64 ~/Desktop/REPO/uubc-orakit/sprint1/pwz/learn_java_basic (main)
$ javac HelloWorld.java 

pwz@test MINGW64 ~/Desktop/REPO/uubc-orakit/sprint1/pwz/learn_java_basic (main)
$ java HelloWorld
HELLO WORLD!

**********    
**********    
**********    
**********    
**********    
**********    
**********    
**********    
**********    
***********100
90
80
70
60
50
40
30
20
10
 */