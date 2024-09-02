import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class Shape {
    int length;
    int breadth;

    Shape(int length, int breadth) {
        this.length = length;
        this.breadth = breadth;
    }

    void area() {
        System.out.println(length + " " + breadth);
    }
}

class Rectangle extends Shape {
    Rectangle(int length, int breadth) {
        super(length, breadth);
    }

    @Override
    void area() {
        int area = length * breadth;
        System.out.println(length + " " + breadth);
        System.out.println(area);
    }
}

public class JavaShape {
    public static void main(String args[]) throws Exception {
        // Read input from STDIN
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        String[] parts = input.split(" ");
        int length = Integer.parseInt(parts[0]);
        int breadth = Integer.parseInt(parts[1]);

        Rectangle rectangle = new Rectangle(length, breadth);
        rectangle.area();

        
    }
}