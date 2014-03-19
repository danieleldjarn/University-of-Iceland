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


public class Main {
    public static void main(String[] args)
    {
        JFrame frame = new Drawing();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); 
        frame.setMinimumSize(new Dimension(400, 400));
        frame.setMaximumSize(new Dimension(600, 600));
        frame.pack();
        frame.setVisible(true);
    }
}