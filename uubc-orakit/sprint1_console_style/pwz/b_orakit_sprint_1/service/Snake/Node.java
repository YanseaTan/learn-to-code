package pwz.b_orakit_sprint_1.service.Snake;

import java.awt.*;

public class Node {
    int row, col;

    Node prev,next;

    public Node(int row, int col) {
        this.row = row;
        this.col = col;
    }

    public void paint(Graphics g) {
        int x = Scene.x + col*Scene.NodeSize;
        int y = Scene.y + row*Scene.NodeSize;
        Color c = g.getColor();
        g.setColor(Color.black);
        g.fillRect(x, y, Scene.NodeSize, Scene.NodeSize);

        g.setColor(c);
    }
}
