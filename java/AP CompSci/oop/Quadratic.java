
//Name - Connor Gannaway
//Date - 9/19
//Class -AP1
//Lab  - OOP

import java.util.Scanner; 
import static java.lang.System.*;
import static java.lang.Math.*;

public class Quadratic
{
	private int a, b, c;
	private double rootOne;
	private double rootTwo;

	public Quadratic()
	{
		setEquation(0, 0, 0);
		calcRoots();
	}

	public Quadratic(int quadA, int quadB, int quadC)
	{
		setEquation(quadA, quadB, quadC);
		calcRoots();
	}

	public void setEquation(int quadA, int quadB, int quadC)
	{
		a = quadA;
		b = quadB;
		c = quadC;

 	}

	public void calcRoots( )
	{
		double d = Math.sqrt(Math.pow(b,2)-4*a*c);
		rootOne = (-b+d)/(2*a);
		rootTwo = (-b-d)/(2*a);
	}

    public void print()
    {
		System.out.println("Root 1 == " + rootOne);
		System.out.println("Root 2 == " + rootTwo);

    }
    
    //complete either print or the toString()

	public String toString()
	{
		return "";
	}
}