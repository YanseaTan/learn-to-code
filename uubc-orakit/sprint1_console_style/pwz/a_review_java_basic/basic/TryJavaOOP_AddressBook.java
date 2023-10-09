package pwz.a_review_java_basic.basic;

import java.util.ArrayList;
import java.util.Scanner;

/**
 * just java version of uubc-orakit.sprint1.hlt.learn_cpp_basic.address-book
 */
public class TryJavaOOP_AddressBook {
    public static Person createPerson(){
        try {
            Person p = new Person();
            Scanner cin = new Scanner(System.in);
            System.out.print("Input the name: ");
            p.setName(cin.nextLine());
            System.out.print("Input the sex (1=male, 0=female): ");
            p.setSex(cin.nextInt());
            System.out.print("Input the age: ");
            p.setAge(cin.nextInt());
            cin.nextLine(); // deal with the \n left by nextInt()
            System.out.print("Input the phone number: ");
            p.setPhone(cin.nextLine());
            System.out.print("Input the address: ");
            p.setAddress(cin.nextLine());
            return p;
        }catch (Exception e){
            System.out.println(e.toString());
            return new Person();
        }
    }

    /**
     *     cout<<"Welcome to the AddressBook system!"<<endl;
     *     cout<<"1. Add new person"<<endl;
     *     cout<<"2. Show all person"<<endl;
     *     cout<<"0. Exit"<<endl;
     * @return 1 = add, 2=show, 0=bye
     */
    public static int showMenuAndAcceptCommand(){
        System.out.println("Welcome to the AddressBook system!");
        System.out.println("1. Add new person");
        System.out.println("2. Show all person");
        System.out.println("0. Exit");
        Scanner cin = new Scanner(System.in);
        int command = cin.nextInt();
        if(command != 1 && command != 2 && command != 0) return -1;
        return command;
    }

    public static void main(String[] args) {
        AddressBook addressBook = new AddressBook();
        int command;
        while (true){
            command = showMenuAndAcceptCommand();
            switch (command){
                case 1: {
                    Person p = createPerson();
                    if(p.getName().equals("DefaultNameMeansThisPersonIsNotARealPerson")){
                        System.out.println("Error while input the person information...\n try again please");
                        break;
                    }
                    addressBook.addPerson(p);
                    System.out.printf("Add person [%s] ~ success\n", p.getName());
                    break;
                }

                case 2: {
                    addressBook.showAllPerson();
                    break;
                }

                case 0: {
                    return;
                }

                default: {
                    System.out.println("I can't understand your command, please try again~");
                    break;
                }
            }
        }
    }
}
/** debug record:
 * Welcome to the AddressBook system!
 * 1. Add new person
 * 2. Show all person
 * 0. Exit
 * 2
 * Your AddressBook is empty!
 * Welcome to the AddressBook system!
 * 1. Add new person
 * 2. Show all person
 * 0. Exit
 * 5
 * I can't understand your command, please try again~
 * Welcome to the AddressBook system!
 * 1. Add new person
 * 2. Show all person
 * 0. Exit
 * 1
 * Input the name: The Kvass Master！
 * Input the sex (1=male, 0=female): 1
 * Input the age: 9
 * Input the phone number: 15212349876
 * Input the address: WHATEVER Building.
 * Add person [The Kvass Master！] ~ success
 * Welcome to the AddressBook system!
 * 1. Add new person
 * 2. Show all person
 * 0. Exit
 * 2
 * [Name: ]The Kvass Master！	Sex: Female	Age: 9	Phone: 15212349876	Address: WHATEVER Building.
 * Welcome to the AddressBook system!
 * 1. Add new person
 * 2. Show all person
 * 0. Exit
 * 1
 * Input the name: TestPerson
 * Input the sex (1=male, 0=female): 0
 * Input the age: 10
 * Input the phone number: 15166667777
 * Input the address: qwertyui
 * Add person [TestPerson] ~ success
 * Welcome to the AddressBook system!
 * 1. Add new person
 * 2. Show all person
 * 0. Exit
 * 2
 * [Name: ]The Kvass Master！	Sex: Female	Age: 9	Phone: 15212349876	Address: WHATEVER Building.
 * [Name: ]TestPerson	Sex: Female	Age: 10	Phone: 15166667777	Address: qwertyui
 * Welcome to the AddressBook system!
 * 1. Add new person
 * 2. Show all person
 * 0. Exit
 * 0
 *
 * Process finished with exit code 0
 */

class Person{
    private String name;
    private int sex;
    private int age;
    private String phone;
    private String address;

    public Person() {
        this.name = "DefaultNameMeansThisPersonIsNotARealPerson";
    }

    public Person(String name, int sex, int age, String phone, String address) {
        this.name = name;
        this.sex = sex;
        this.age = age;
        this.phone = phone;
        this.address = address;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getSex() {
        return sex;
    }

    public void setSex(int sex) {
        this.sex = sex;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
}

class AddressBook{
    private ArrayList<Person> people;
    private Integer size;

    AddressBook(Person p){
        this.people = new ArrayList<Person>();
        this.people.add(p);
        this.size = 1;
    }
    AddressBook(){
        this.people = new ArrayList<Person>();
        this.size = 0;
    }

    public boolean addPerson(Person p){
        try {
            people.add(p);
            this.size++;
        }catch (Exception e){
            System.out.println(e.toString());
            return false;
        }
        return true;
    }

    public boolean removePersonByName(String name){
        System.out.println("This function is not implemented yet~");
        return true;
    }

    public boolean removePersonByPhone(String name){
        System.out.println("This function is not implemented yet~");
        return true;
    }

    /**
     *
     * cout<<"Name: "<<abs->personArray[i].m_Name<<"\t";
     * cout<<"Sex: "<<(abs->personArray[i].m_Sex == 1 ? "man" : "woman")<<"\t";
     * cout<<"Age: "<<abs->personArray[i].m_Age<<"\t";
     * cout<<"Phone: "<<abs->personArray[i].m_Phone<<"\t";
     * cout<<"Address: "<<abs->personArray[i].m_Addr<<endl;
     */
    public void showAllPerson(){
        if(this.size < 1) {
            System.out.println("Your AddressBook is empty!");
            return;
        }
        for (Person p :
                this.people) {
            System.out.printf("[Name: ]%s\tSex: %s\tAge: %d\tPhone: %s\tAddress: %s\n",
                    p.getName(),
                    p.getAge()==1 ? "Male":"Female",
                    p.getAge(),
                    p.getPhone(),
                    p.getAddress());
        }
    }
}
