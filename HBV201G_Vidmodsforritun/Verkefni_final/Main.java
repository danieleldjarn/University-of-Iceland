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

public class Main {
    public static void main(String[] args)
    {
        JFrame calendar = new Cal();
        calendar.pack();
        calendar.setVisible(true);
    }
}