package pwz.a_review_java_basic.other;

import javax.swing.*;
import java.awt.*;

/**
 * roadmap of java GUI:
 *  1. AWT ~  Abstract Window Toolkit
 *  2. IFC (Internet Foundation Classes)
 *  3. SWING
 *  4. JavaFX
 */
public class SkimGUI {
    public static void main(String [] args){
        EventQueue.invokeLater(()->
        {
            MyFrame myFrame = new MyFrame();
            myFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            myFrame.setVisible(true);
        });
    }
}

/**
 * A frame that contains a message panel.
 */
class MyFrame extends JFrame{
    private static final int DEFAULT_WIDTH = 900;
    private static final int DEFAULT_HEIGHT = 600;

    public MyFrame(){
        setSize(DEFAULT_WIDTH, DEFAULT_HEIGHT);
        setLocation(700, 400);
        setTitle("GUI DEMO for OraKit");

        add(new MyComponent());
        pack();
    }
}

/**
 * A component that displays a message.
 */
class MyComponent extends JComponent{
    public static final int MESSAGE_X = 400;
    public static final int MESSAGE_Y = 300;

    private static final int DEFAULT_WIDTH = 900;
    private static final int DEFAULT_HEIGHT = 600;

    public void paintComponent(Graphics g){
        g.drawString("Hello AWT & Swing ~", MESSAGE_X, MESSAGE_Y);
    }

    public Dimension getPreferredSize(){
        return new Dimension(DEFAULT_WIDTH, DEFAULT_HEIGHT);
    }
}
