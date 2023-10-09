package pwz.a_review_java_basic.further;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

public class AboutLambdaExpressions {
    public static void main(String[] args) {
        ComparableStuff[] cs = new ComparableStuff[5];
        cs[0] = new ComparableStuff("1");
        cs[1] = new ComparableStuff("12345");
        cs[2] = new ComparableStuff("123");
        cs[3] = new ComparableStuff("12");
        cs[4] = new ComparableStuff("1234");
        System.out.println("before sort:");
        for(ComparableStuff c: cs){
            System.out.println(c.describe);
        }

        System.out.println("\nafter sort:");
        Arrays.sort(cs);
        for(ComparableStuff c: cs){
            System.out.println(c.describe);
        }

        System.out.println("\nsorted by Arrays.sort(cs, new MyComparator())");
        Arrays.sort(cs, new MyComparator());
        for(ComparableStuff c: cs){
            System.out.println(c.describe);
        }

        System.out.println("\nsorted by Lambda Expression");
        Arrays.sort(cs, (ComparableStuff c1, ComparableStuff c2) -> {
            if(c1.describe.length() == 2) return 10;
            else return c1.describe.length() - c2.describe.length();
        });
        for(ComparableStuff c: cs){
            System.out.println(c.describe);
        }
    }
}

class ComparableStuff implements Comparable<ComparableStuff>{
    String describe;

    public ComparableStuff(String describe) {
        this.describe = describe;
    }

    @Override
    public int compareTo(ComparableStuff o) {
        return describe.length() - o.describe.length();
    }
}

class MyComparator implements Comparator<ComparableStuff> {
    @Override
    public int compare(ComparableStuff o1, ComparableStuff o2) {
        return o2.compareTo(o1);
    }
}
