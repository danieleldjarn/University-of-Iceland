import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.beans.*;
import java.util.*;
import java.util.Calendar;
import java.util.Locale;
import java.text.*;
import java.io.*;

public class MainTaskListTest {
    public static void main(String[] args)
    {
        JFrame tasklist = new TaskList();
        tasklist.pack();
        tasklist.setVisible(true);
    }
}