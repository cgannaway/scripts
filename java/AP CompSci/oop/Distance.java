//Name - Connor Gannaway
//Date - 9/19
//Class -AP1
//Lab  - OOP

import java.util.Scanner; 
import static java.lang.System.*;
import static java.lang.Math.*;

public class Distance
{
	private int xOne,yOne,xTwo,yTwo;
	private double distance;

	public Distance()
	{
		distance = getDistance();
	}

	public Distance(int x1, int y1, int x2, int y2)
	{
		setCoordinates(x1, y1, x2, y2);
		calcDistance();
	}

	public void setCoordinates(int x1, int y1, int x2, int y2)
	{
		xOne = x1;
		xTwo = x2;
		yOne = y1;
		yTwo = y2;
	}

	public void calcDistance()
	{
		double part1 = (xTwo-xOne)*(xTwo-xOne);
		double part2 = (yTwo-yOne)*(yTwo-yOne);
		double part3 = part1 + part2;
		distance = Math.sqrt(part3);
	}
	
	public double getDistance()
	{
		return 0.0;
	}
	
	public void print()
	{
		System.out.println("distance == "+ distance);
	}
	
	//complete print or the toString

	public String toString()
	{
		return "";
	}
}