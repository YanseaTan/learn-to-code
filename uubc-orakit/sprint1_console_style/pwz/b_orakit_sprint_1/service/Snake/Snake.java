package pwz.b_orakit_sprint_1.service.Snake;

import java.awt.*;
import java.awt.event.KeyEvent;
import java.util.Random;

import static java.lang.Thread.sleep;

public class Snake {
    Node head, tail;
    Direction dir = Direction.RIGHT;
    Random r = new Random();
    boolean isAutoPilot = false;

    Snake() {
        head = new Node(10, 10);
        tail = head;
    }

    public Snake(boolean isAutoPilot) {
        this.isAutoPilot = isAutoPilot;
        head = new Node(10, 10);
        tail = head;

        Thread t = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    while (true){
                        sleep(666);
                        autoPilot();
                    }
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });
        t.start();
    }

    public void addToHead() {
        Node n = null;
        switch (dir){
            case UP: {
                n = new Node(head.row-1, head.col);break;
            }
            case DOWN: {
                n = new Node(head.row+1, head.col);break;
            }
            case LEFT: {
                n = new Node(head.row, head.col-1);break;
            }
            case RIGHT: {
                n = new Node(head.row, head.col+1);break;
            }
        }
        n.next = head;
        head.prev = n;
        head = n;
    }

    public void paint(Graphics g) {
        Node n = head;
        while (n != null){
            n.paint(g);
            n = n.next;
        }

        move();
    }

    private void autoPilot(){
        int d = r.nextInt(4);
        String dd;
        switch (d){
            case 0:{
                dd = "UP";
                dir = Direction.UP;
                break;
            }
            case 1:{
                dd = "DOWN";
                dir = Direction.DOWN;
                break;
            }
            case 2:{
                dd = "LEFT";
                dir = Direction.LEFT;
                break;
            }
            case 3:{
                dd = "RIGHT";
                dir = Direction.RIGHT;
                break;
            }
        }
    }

    private void move() {
        addToHead();
        deleteTail();
        boundaryCheck();
    }

    private void boundaryCheck() {
        if(head.row < 0)head.row = Scene.NodeCount-1;
        if(head.col < 0)head.col = Scene.NodeCount-1;
        if(head.row > Scene.NodeCount-1) head.row=0;
        if(head.col > Scene.NodeCount-1) head.col=0;
    }

    private void deleteTail() {
        if(tail == null) return;
        tail = tail.prev;
        tail.next.prev = null; // make sure no reference refer to old tail
        tail.next = null; // then GC works...

    }

    public void keyPressed(KeyEvent e) {
        int key = e.getKeyCode();
        switch (key){
            case KeyEvent.VK_UP:
                dir = Direction.UP;
                break;
            case KeyEvent.VK_DOWN:
                dir = Direction.DOWN;
                break;
            case KeyEvent.VK_LEFT:
                dir = Direction.LEFT;
                break;
            case KeyEvent.VK_RIGHT:
                dir = Direction.RIGHT;
                break;
        }
    }

    public void eat(Egg e) {
        if(head.row == e.row && head.col == e.col){
            addToHead();
            e.reAppear();
        }
    }
}
