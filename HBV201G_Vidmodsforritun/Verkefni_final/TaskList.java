import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.beans.*;
import java.util.*;
import java.util.Calendar;
import java.util.Locale;
import java.text.*;
import java.io.*;
import com.toedter.calendar.JCalendar;
import java.util.List;


import javax.swing.JButton;

public class TaskList extends JFrame implements ActionListener {

    private JPanel          panel;
    private JList   myList;
    
    public TaskList() {
        
        // Set various JFrame behaviour
        //setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setDefaultCloseOperation(JFrame.HIDE_ON_CLOSE);

        setPreferredSize(new Dimension(300,300));

        panel = new JPanel(new BorderLayout());
        
        String[] taskList = generateTaskList();

        myList = new JList<String>(taskList);

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
        
        addEventButton.addActionListener(this);
        addEventButton.setActionCommand("addEvent");

        deleteEventButton.addActionListener(this);
        deleteEventButton.setActionCommand("deleteEvent");
        setContentPane(panel);

        generateTaskList();
    }

    @Override
    public void actionPerformed(ActionEvent ae) {
        String action = ae.getActionCommand();
        if (action.equals("addEvent")) {

            // Debug code
            System.out.println("addEventButton pressed");
            System.out.println("starting calendar");

            // Dispose of the current frame
            this.dispose();

            // Call calendar app
            JFrame calendar = new Cal();
            calendar.pack();
            calendar.setVisible(true);
        }
        if (action.equals("deleteEvent")) {

            System.out.println("deleteEventButton pressed");

            deleteEventData();

            // Restart the app to refresh the task list
            System.out.println("starting task list");

            // Dispose of the current frame
            this.dispose();

            // Call the task list again
            JFrame tasklist = new TaskList();
            tasklist.pack();
            tasklist.setVisible(true);
        }
    }

    private void deleteEventData() {

        String selected = myList.getSelectedValue().toString();
        String fileName = selected.substring(0,10);

        try {
            File file = new File("./data/" + fileName);

            if(file.delete()) {
                System.out.println("File " + fileName + " has been deleted.");

            } else {
                System.out.println("Unable to delete file.");
            }
        } catch (Exception e) {
            System.out.println("Unable to delete file " + fileName + ". File does not exist.");
        }

    }

    private String[] generateTaskList() {
        
        final File folder = new File("./data");
        List<String> taskList = new ArrayList<String>();

        try {
            for(final File fileEntry : folder.listFiles()) {
            
            String fileName = new String(fileEntry.getName());
            
            System.out.println(fileName);
            
            File file = new File("./data/" + fileName);
            char[] temp = new char[(int)file.length()];

            try
            {
                FileReader view = new FileReader(file);
                view.read(temp);
                view.close();
            }
            catch (Exception e)
            {
                System.out.println("Error, unable to open file in generateTaskList() The directory 'data' might be missing");
            }
            
            String fileContents = new String(temp);

            taskList.add(fileName + " - " + fileContents);
        }

        }
        catch (Exception e) {
            System.out.println("Error, unable to open file in generateTaskList(). The directory 'data' might be missing");
        }

        String[] taskListArray = new String[taskList.size()];
        taskList.toArray(taskListArray);
        return taskListArray;
        
    }
}