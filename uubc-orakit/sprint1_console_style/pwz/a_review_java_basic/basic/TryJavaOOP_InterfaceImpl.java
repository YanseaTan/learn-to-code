package pwz.a_review_java_basic.basic;

import java.util.function.BiFunction;

public class TryJavaOOP_InterfaceImpl implements TryJavaOOP_Interface, Comparable{
    @Override
    public void helloInterface() {
        System.out.println("this is the helloInterface from " + this.getClass().getName());
    }

    @Override
    public void anotherFunction() {
        System.out.println(this.getClass().getName());
    }

    @Override
    public int comparable(String s1, String s2) {
        return s1.length() - s2.length();
    }

    @Override
    public void meaningless() {
        System.out.println(this.getClass().getName());
    }

    public static void main(String[] args) {
        TryJavaOOP_InterfaceImpl tji = new TryJavaOOP_InterfaceImpl();
        tji.helloInterface();
        int result = tji.comparable("123", "1234");
        System.out.println(result);

        BiFunction<String, String, Integer> comp = (s1, s2)
                -> s1.length() - s2.length();


    }

    @Override
    public int compareTo(Object o) {
        return 0;
    }
}
