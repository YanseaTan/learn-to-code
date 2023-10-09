package pwz.b_orakit_sprint_1.service.Snake;

import java.awt.*;
import java.util.Random;

public class Egg {
    int row, col;
    Random r = new Random();

    public Egg(int row, int col) {
        this.row = row;
        this.col = col;
    }

    public void paint(Graphics g) {
        int x = Scene.x + col*Scene.NodeSize;
        int y = Scene.y + row*Scene.NodeSize;
        Color c = g.getColor();
        g.setColor(Color.RED);
        g.fillOval(x, y, Scene.NodeSize, Scene.NodeSize);

        g.setColor(c);
    }

    public void reAppear() {
        this.row = r.nextInt(Scene.NodeCount);
        this.col = r.nextInt(Scene.NodeCount);
    }
}
