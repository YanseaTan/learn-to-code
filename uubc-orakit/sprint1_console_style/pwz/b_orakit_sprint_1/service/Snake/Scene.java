package pwz.b_orakit_sprint_1.service.Snake;

import java.awt.*;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

public class Scene extends Frame {
    private boolean isAlive = true;

    public static final int NodeSize = 10;
    public static final int NodeCount = 50;
    public static final int SceneSize = NodeSize*NodeCount;

    public static int x = SceneSize/2;
    public static int y = SceneSize/2;

    Snake s;
    Egg e;

    public Scene() {
        this.s = new Snake(true);
        this.e = new Egg(30, 30);
        this.setSize(2*SceneSize, 2*SceneSize);
        this.setVisible(true);
        this.setTitle("Snake");
        this.setLocation(600, 300);
        this.setAlwaysOnTop(true);
        this.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                // don't use System.exit() here, that will kill the jvm then the OriKit down also
                isAlive = false;
            }
        });

        this.addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                s.keyPressed(e);
            }
        });

        while (isAlive) {
            try {
                Thread.sleep(50);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            this.repaint();
        }
    }

    @Override
    public void paint(Graphics g) {
        Color c = g.getColor();
        g.setColor(Color.WHITE);
        g.fillRect(0,0,this.getWidth(),this.getHeight());

        g.setColor(Color.BLACK);
        for(int i=0; i<=NodeCount; ++i){
            /*
             * Draws a line, using the current color,
             * between the points (x1, y1) and (x2, y2) in this graphics context's coordinate system.
             */
            g.drawLine(x,y+NodeSize*i,x+SceneSize,y+NodeSize*i);
            g.drawLine(x+NodeSize*i, y,x+NodeSize*i, y+SceneSize);
        }

        e.paint(g);
        s.paint(g);

        s.eat(e);
        g.setColor(c);
    }

    /** double buffer...
     * deal with the problem that the Scene keeps flipping
     * @see <a href=https://docs.oracle.com/javase/tutorial/extra/fullscreen/doublebuf.html></a>
     */
    Image offScreenImage = null;
    @Override
    public void update(Graphics g) {
        if(offScreenImage == null){
            offScreenImage = this.createImage(this.getWidth(), this.getHeight());
        }
        Graphics gOff = offScreenImage.getGraphics();
        paint(gOff);
        g.drawImage(offScreenImage, 0, 0, null);
    }

    public static void main(String[] args) {
        Scene s = new Scene();
        s.setVisible(false);
        s = null;
    }
}
