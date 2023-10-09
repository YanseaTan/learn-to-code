package pwz.a_review_java_basic.more;

import java.util.ArrayList;

/**
 * Java Generic Programming
 * @since JDK5
 */
public class AboutGenericProgramming {

    /** ~1
     * defining and using a generic class
     * just put the Type into "<>"
     */
    Stack<Integer> stack;

    public AboutGenericProgramming() {
        stack = new Stack<>();
    }

    /** ~2
     * using an existing generic class
     */
    public static void usingExistingGenericClass(){
        ArrayList<String> arrayList = new ArrayList<>();
        // arrayList.add(0,34); // Error, type not satisfied
        arrayList.add(0,"34");
        System.out.println(arrayList.get(0));
    }

    /** ~3
     * defining a generic method
     */
    public static <T> void printMiddle(T... list){
        T x = list[list.length / 2];
        try{
            String reslut = x.toString();
            System.out.println(reslut);
        }catch (NullPointerException ne){
            System.out.println("can't deal with 'null'");
        }catch (Exception e){
            e.printStackTrace();
            System.out.println(x.getClass().getName() + " can't convert into String.");
        }
    }

    /** ~4
     * you can use <T extends BoundingType> to restrict T.
     */
    static class TempClass<T extends String>{ T x;}
    //Both T and the bounding type can be either a class or an interface.
    static class TempClass2<T extends Comparable<String>>{ T x;}


    /** ~5
     * learn about Type Erasure
     */
    public static void aboutTypeErasure(){
        // to read...
    }

    /** ~6
     * generic programming has so many restrictions and limitations
     */
    public static void aboutRestrictionsAndLimitations(){
        // to read...
    }

    /**
     * what's more?
     */
    public static void whatMore(){
        // 8.7 Inheritance Rules for Generic Types
        // 8.8 Wildcard Types
        // 8.9 Reflection and Generics
    }


    public static void main(String[] args) {
        AboutGenericProgramming agp = new AboutGenericProgramming();
        AboutGenericProgramming.<String>printMiddle("test1", "test2", "test3");
        AboutGenericProgramming.<Integer>printMiddle(123, 345, 4356, 546, 1);
        printMiddle(123, 345, 4356, 546, 1); //type info can be inferred
        printMiddle("123", null, "345");

        class Temp{
            @Override
            public String toString(){ // can't throw an exception here
                // throw new Exception("homemade exception"); // so can't throw an exception here too
                return "";
            }
        }
        // printMiddle("123", new Temp(), "345"); //
    }
}

/**
 * define a generic class
 * (an unfinished example where generic programming will be used)
 * @param <T>
 */
class Stack<T>{
    private T[] stack;
    private int capacity;
    private int size;
    private void expand(){}

    public Stack() {
        capacity = 5;
        // stack = new T[capacity]; //ERROR, see: 8.6.6 You Cannot Construct a Generic Array
        // just stop here for now
    }

    public void push(){}
    public void pop(){}
}
