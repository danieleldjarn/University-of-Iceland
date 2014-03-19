import java.awt.*;
import java.awt.event.*;
import java.awt.image.*;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics; 

import javax.imageio.*;
import javax.swing.*;

import java.beans.*;
import java.util.*;
import java.util.Locale;
import java.text.*;
import java.io.*;

public class Drawing extends JFrame
{
    
    private BufferedImage image;
    Person girl = new Person();
    Person boy = new Person();

    Drawing()
    {
        JPanel panel = new JPanel(new BorderLayout());
        JScrollPane scroll_pane = new JScrollPane();

        // Load image
        try {                
          image = ImageIO.read(new File("test.png"));
       } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
       }

        // Display image
        JLabel picLabel = new JLabel(new ImageIcon(image));
        picLabel.setPreferredSize(new Dimension(500,500));
        panel.add(picLabel);

        // Display girl

        PaintPanel girlPanel = new PaintPanel();
        girlPanel.paintComponent()
//        addWindowListener(new window_interaction());
        setContentPane(panel);

    }

    // public void paintComponent(Graphics g) {
    //     Image.paintComponent(g);       
    //     g.drawString("This is my custom Panel!",10,20);

    //     girl.paintComponent(g);
    // } 

/*    // Change the contents of the date variable if we choose another day
    public class selected_day implements PropertyChangeListener
    {
        public void propertyChange(PropertyChangeEvent evt)
        {
            // setDate(getFormatedDate());
        }
    }
*/
}

class PaintPanel extends JPanel{
    Person girl = new Person();
    // public PaintPanel(){
    //     // Person girl = new Person();

    // }
 
    public void paintComponent(Graphics g){
        super.paintComponent(g);
        g.drawString("This is my custom Panel!",10,20);
        girl.paintPerson(g);
    }
}

class Person{
    
    private int xPos = 50;
    private int yPos = 50;
    private int width = 20;
    private int height = 20;

    public void setX(int xPos){ 
        this.xPos = xPos;
    }

    public int getX(){
        return xPos;
    }

    public void setY(int yPos){
        this.yPos = yPos;
    }

    public int getY(){
        return yPos;
    }

    public int getWidth(){
        return width;
    } 

    public int getHeight(){
        return height;
    }

    public void paintPerson(Graphics g){
        g.setColor(Color.RED);
        g.fillRect(xPos,yPos,width,height);
        g.setColor(Color.BLACK);
        g.drawRect(xPos,yPos,width,height);  
    }
}