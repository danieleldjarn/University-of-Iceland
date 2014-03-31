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
import javax.swing.JButton;

public class Cal extends JFrame implements ActionListener {

    String date;
    JTextArea writing_area = new JTextArea();
    JCalendar calendar = new JCalendar();
    SimpleDateFormat date_format = new SimpleDateFormat("YYYY.MM.dd"); 

    Cal() {

        setDefaultCloseOperation(JFrame.HIDE_ON_CLOSE);

        date = getFormatedDate(); 
        JPanel panel = new JPanel();
        panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));
        panel.addMouseListener( new MouseAdapter() { } );
        JScrollPane scroll_pane = new JScrollPane();
        
        // Put scrollbars on
        calendar.addPropertyChangeListener(new selected_day()); 
        
        // Lets add the number of the weeks to the calendar
        calendar.setWeekOfYearVisible(true); 
        addWindowListener(new window_interaction());
        
        // Set the size of the writing area
        writing_area.setColumns(25);
        writing_area.setRows(1);
        scroll_pane.setViewportView(writing_area);

         // Setup and configure buttons
        JPanel buttonPanel = new JPanel(new BorderLayout());
        JButton returnButton = new JButton("Return");
        
        returnButton.setPreferredSize(new Dimension(100, 50));
        
        buttonPanel.add(returnButton);
        
        returnButton.addActionListener(this);
        returnButton.setActionCommand("return");
        // END Setup and configure buttons

        panel.add(calendar);
        panel.add(scroll_pane);
        panel.add(buttonPanel);
        
        setContentPane(panel);

    }

    /*
    *   The event handler for this JFrame.
    */
    @Override
    public void actionPerformed(ActionEvent ae) {
        String action = ae.getActionCommand();
        if (action.equals("return")) {
            System.out.println("returnButton pressed.");

            // Save current data
            setText(date,writing_area.getText());
            System.out.println("Text in writing area saved.")

            // Close this JFrame
            this.dispose();
            System.out.println("Cal disposed off");

            // Call the task list again
            JFrame tasklist = new TaskList();
            tasklist.pack();
            tasklist.setVisible(true);
        }

    }

    /*
    *   Save the text in the on the current date if we close the window
    */
    public class window_interaction extends WindowAdapter
    {
        public void windowClosing(WindowEvent evt)
        {
            if (!getText(date).equals(writing_area.getText()))
            {
                setText(date,writing_area.getText());
            }
        }
    }

    /*
    * Change the contents of the date variable if we choose another day
    */
    public class selected_day implements PropertyChangeListener
    {
        public void propertyChange(PropertyChangeEvent evt)
        {
            setDate(getFormatedDate());
        }
    }

    /*
    *   Write the text in the text area to a file
    */
    public void setText(String date, String text)
    {
        try
        {
            FileWriter file = new FileWriter("./data/" + date);
            file.write(text);
            file.close();
        }
        catch (Exception e)
        {
            System.out.println("Error");
        }
    }

    /*
    *   Change the date variable
    */
    public void setDate(String new_date)
    {
        if (new_date.equals(date))
            return;

        if (date != null && !getText(date).equals(writing_area.getText()))
        {
            setText(date, writing_area.getText());
        }

        date = new_date;
        writing_area.setText(getText(date));
    }

    /*
    *   Format the date correctly
    */
    public String getFormatedDate()
    {
        Date date = calendar.getDate();
        return date_format.format(date);
    }

    /*
    *   Get the text from a date file if it exists. Else return an empty string
    */
    public String getText(String date)
    {
        File file = new File("./data/" + date);
        if (!file.exists())
            return "";
        else {
            char[] temp = new char[(int)file.length()];

            try
            {
                FileReader view = new FileReader(file);
                view.read(temp);
                view.close();
            }
            catch (Exception e)
            {
                System.out.println("Error");
                return "Error";
            }
            String return_string = new String(temp);
            return return_string;
        }
    }
}