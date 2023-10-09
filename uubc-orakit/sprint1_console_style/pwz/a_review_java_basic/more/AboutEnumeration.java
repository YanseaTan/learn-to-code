package pwz.a_review_java_basic.more;

public class AboutEnumeration {
    enum COLOR {
        RED,
        GREEN,
        BLUE
    }

    enum ERROR_CODE {
        FILE_NOT_FOUND,
        BAD_FEELINGS,
        DO_NOT_WANT_TO_WORK
    }

    public static void main(String[] args) {
        System.out.println(COLOR.BLUE);
        System.out.println(ERROR_CODE.DO_NOT_WANT_TO_WORK);
    }
    /*
        BLUE
        DO_NOT_WANT_TO_WORK

        Process finished with exit code 0
     */
}
