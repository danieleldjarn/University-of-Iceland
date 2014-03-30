import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.beans.*;
import java.util.*;
import java.util.Calendar;
import java.util.Locale;
import java.text.*;
import java.io.*;

public class TaskList extends JFrame {

    private JPanel  panel;
    private JList   list;
    
    public TaskList() {
        
        // Set various JFrame behaviour
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        setPreferredSize(new Dimension(300,300));

        panel = new JPanel(new BorderLayout());
        
        String[] data = {"one", "two", "three", "four"};
        JList<String> myList = new JList<String>(data);

        // Setup and configure buttons
        JPanel buttonPanel = new JPanel(new BorderLayout());
        JButton addEventButton = new JButton("Add");
        JButton deleteEventButton = new JButton("Delete");
        addEventButton.setPreferredSize(new Dimension(100, 50));
        deleteEventButton.setPreferredSize(new Dimension(100, 50));
        buttonPanel.add(addEventButton, BorderLayout.WEST);
        buttonPanel.add(deleteEventButton, BorderLayout.EAST);

        panel.add(myList, BorderLayout.CENTER);
        panel.add(buttonPanel, BorderLayout.SOUTH);
        setContentPane(panel);
    }
}