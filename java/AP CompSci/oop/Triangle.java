
//Name - Connor Gannaway
//Date - 9/19
//Class -AP1
//Lab  - OOP

import java.util.Scanner; 
import java.lang.Math.*;

public class Triangle
{
	private int sideA, sideB, sideC;
	private double perimeter;
	private double theArea;


	public Triangle()
	{
		setSides(0,0,0);
		perimeter=0;
		theArea=0;
	}

	public Triangle(int a, int b, int c)
	{
		setSides(a,b,c);
		calcPerimeter();
		calcArea();
	}


	public void setSides(int a, int b, int c)
	{
		sideA = a;
		sideB = b;
		sideC = c;
	}

	public void calcPerimeter( )
	{
		perimeter = sideA + sideB + sideC;
	}

	public void calcArea( )
	{
		double s = perimeter/2;
		theArea = Math.sqrt(s*(s-sideA)*(s-sideB)*(s-sideC));

	}

	public void print()
	{
		System.out.println("\n\nSides:");
		System.out.print(sideA );
		System.out.print(" "+ sideB );
		System.out.print(" "+ sideC );
		System.out.println("\nArea == " + theArea);

	}
	
	//create a print method or toString or both
	
	public String toString()
	{
		return "";
	}
}