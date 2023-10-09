package pwz.a_review_java_basic.basic;

import java.time.LocalDate;
import java.util.Date;

/**
 * Core Java --> Chapter4 reading notes
 * @author pengwei.zhang
 * @version 2022.01.24
 * @see <a href="www.horstmann.com/corejava.html">Core Java</a>
 */
public class TryJavaOOP {


    /**
     * the first method of this Class
     */
    public void tryObjectVariable(){
        Date deadline;
        // using an object variable which does not refer to an object would cause a compile-time error
        // deadline.toString(); // compile-time error
        deadline = new Date();
        System.out.println("Hello, now is " + deadline.toString()); // fine

        // !An object variable doesn’t actually contain an object. It only refers to an object.
        Date deadline2 = deadline; // deadline & deadline2 ~ all refer to that Date ob.
        System.out.println(System.identityHashCode(deadline)); // print address in flash
        System.out.println(System.identityHashCode(deadline2));

        deadline = null; // this makes
        // System.out.println(deadline.toString()); // NullPointerException
    }

    /**
     * Try the LocalDate Class of the Java Library
     */
    public void tryPredefinedClasses(){
        // Date: ~ a point in time
        // LocalDate ~ calendar
        LocalDate localDateNow = LocalDate.now();
        System.out.println(localDateNow);
        LocalDate localDateSpec = LocalDate.of(2021, 1, 4);
        System.out.println(localDateSpec);
        int year = localDateNow.getYear();
        int month = localDateNow.getMonthValue();
        int day = localDateNow.getDayOfMonth();
        System.out.println(year);
        LocalDate tenDaysLater = localDateNow.plusDays(10);
        System.out.println(tenDaysLater);
    }

    /**
     * print the calendar of current month using LocalDate Class
     * my own implementation
     *
     * 1. get the date of today
     * 2. get the first day of this month
     * 3. printf
     */
    public void printCalendarOfCurrentMonth(){
        // prepare basic information
        LocalDate datePointer = LocalDate.now();
        int today = datePointer.getDayOfMonth();
        int month = datePointer.getMonthValue();
        // set the pointer to the first day of this month
        datePointer = LocalDate.now().minusDays(today-1);

        System.out.println("Mo. Tu. We. Th. Fr. Sa. Su. ");
        int dayOfWeek = datePointer.getDayOfWeek().getValue();
        for(int i=0; i<dayOfWeek-1; ++i) System.out.print("    ");
        while (datePointer.getMonthValue() == month){
            // print day
            int day = datePointer.getDayOfMonth();
            System.out.printf("%4d",day);
            // tag today
            if(day == today) System.out.print("*");
            // change week
            if(datePointer.getDayOfWeek().getValue() == 7) System.out.print("\n");
            // update date
            datePointer = datePointer.plusDays(1);
        }
    }
    /* the format has a little problem...
     * Mo. Tu. We. Th. Fr. Sa. Su.
     *                        1   2
     *    3   4   5   6   7   8   9
     *   10  11  12  13  14  15  16
     *   17  18  19  20  21  22  23
     *   24*  25  26  27  28  29  30
     *   31
     * Process finished with exit code 0
     */

    public void printCalendarOfCurrentMonthPretty(){
        // prepare basic information
        LocalDate datePointer = LocalDate.now();
        int today = datePointer.getDayOfMonth();
        int month = datePointer.getMonthValue();
        // set the pointer to the first day of this month
        datePointer = LocalDate.now().minusDays(today-1);

        System.out.println("Mo. Tu. We. Th. Fr. Sa. Su. ");
        int dayOfWeek = datePointer.getDayOfWeek().getValue();
        for(int i=0; i<dayOfWeek-1; ++i) System.out.print("    ");
        while (datePointer.getMonthValue() == month){
            // print day
            int day = datePointer.getDayOfMonth();
            System.out.printf("%3d",day);
            // tag today
            if(day == today) System.out.print("*");
            else System.out.print(" ");
            // update date
            datePointer = datePointer.plusDays(1);
            // change week
            if(datePointer.getDayOfWeek().getValue() == 1) System.out.print("\n");
        }

        // Days of the Week
        System.out.println("\n");
        System.out.println("Mo. ~ Monday");
        System.out.println("Tu. ~ Tuesday");
        System.out.println("We. ~ Wednesday");
        System.out.println("Th. ~ Thursday");
        System.out.println("Fr. ~ Friday");
        System.out.println("Sa. ~ Saturday");
        System.out.println("Su. ~ Sunday");
    }
    /* ~~
     * Mo. Tu. We. Th. Fr. Sa. Su.
     *                       1   2
     *   3   4   5   6   7   8   9
     *  10  11  12  13  14  15  16
     *  17  18  19  20  21  22  23
     *  24* 25  26  27  28  29  30
     *  31
     */
}

class TestTryJavaOOP{
    public static void main(String[] args) {
        TryJavaOOP tjo = new TryJavaOOP();
        // tjo.tryObjectVariable();
        // tjo.tryPredefinedClasses();
        // tjo.printCalendarOfCurrentMonth();
        tjo.printCalendarOfCurrentMonthPretty();
    }
}