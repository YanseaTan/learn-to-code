package pwz.a_review_java_basic.basic;

public class TryJavaOOP_Inheritance {
    public static void main(String[] args) {
        Creature creature = new Creature();
        creature.attack();

        Human human = new Human();
        human.attack();

        human.addWealth(10000000);  // stack overflow
        human.attack();
    }
}

abstract class Thing {
    public abstract void attack();
}

class Creature extends Thing{

    private final String name;
    private final int health;
    private final int attack;
    private final String skill;

    public Creature() {
        this.name = "UnknownCreature";
        this.health = 100;
        this.attack = 10;
        this.skill = "Hit";
    }

    public Creature(String name, int health, int attack, String skill) {
        this.name = name;
        this.health = health;
        this.attack = attack;
        this.skill = skill;
    }

    public void attack(){
        System.out.println(name + " can " + skill);
        System.out.println(skill + " makes " + attack + " harm.");
    }

    public String getName() {
        return name;
    }

    public int getHealth() {
        return health;
    }

    public int getAttack() {
        return attack;
    }

    public String getSkill() {
        return skill;
    }
}

class Human extends Creature {
    protected int wealth;

    public Human() {
        super("Human", 50, 5, "SpendMoney");
        this.wealth = 0;
    }

    public Human(String name, int health, int attack, String skill, int wealth) {
        super(name, health, attack, skill);
        this.wealth = wealth;
    }

    // Overriding Methods
    public void attack(){
        int att = super.getAttack();
        System.out.println(super.getName() + " can " + super.getSkill());
        System.out.println(super.getSkill() + " makes " + (super.getAttack()+wealth*wealth) + " harm.");
    }

    public void addWealth(int money){
        wealth += money;
    }
}