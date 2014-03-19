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

public class Cal extends JFrame
{
    String date; // Contains the current date
    JTextArea writing_area = new JTextArea(); // The writing area
    //    boolean weekOfYearVisible = True;
    JCalendar calendar = new JCalendar(); // The calendar app
    SimpleDateFormat date_format = new SimpleDateFormat("YYYY.MM.dd"); // The date format

    // The calendar class
    Cal()
    {
        date = getFormatedDate(); 
        JPanel panel = new JPanel(new BorderLayout());
        JScrollPane scroll_pane = new JScrollPane();
        
        // Put scrollbars on
        scroll_pane.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
        scroll_pane.setHorizontalScrollBarPolicy(ScrollPaneConstants.HORIZONTAL_SCROLLBAR_ALWAYS);
        calendar.addPropertyChangeListener(new selected_day()); 
        
        // Lets add the number of the weeks to the calendar
        calendar.setWeekOfYearVisible(true); 
        addWindowListener(new window_interaction());
        
        // Set the size of the writing area
        writing_area.setColumns(80);
        writing_area.setRows(30);
        scroll_pane.setViewportView(writing_area);
        panel.add(scroll_pane, BorderLayout.EAST);
        panel.add(calendar, BorderLayout.WEST);
        setContentPane(panel);

    }

    // Save the text in the on the current date if we close the window
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

    // Change the contents of the date variable if we choose another day
    public class selected_day implements PropertyChangeListener
    {
        public void propertyChange(PropertyChangeEvent evt)
        {
            setDate(getFormatedDate());
        }
    }

    // Write the text that we have written to a file
    public void setText(String date, String text)
    {
        try
        {
            FileWriter file = new FileWriter("./" + date);
            file.write(text);
            file.close();
        }
        catch (Exception e)
        {
            System.out.println("Villa");
        }
    }

    // Change the date variable
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

    // Format the date correctly
    public String getFormatedDate()
    {
        Date date = calendar.getDate();
        return date_format.format(date);
    }

    // Get the text from a date file if it exists. Else return an empty string
    public String getText(String date)
    {
        File file = new File("./" + date);
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
                System.out.println("Villa");
                return "Villa";
            }
            String return_string = new String(temp);
            return return_string;
        }
    }
}