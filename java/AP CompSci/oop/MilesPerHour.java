//Name - Connor Gannaway
//Date - 9/19
//Class -AP1
//Lab  - OOP
import java.util.Scanner; 
import static java.lang.System.*;
import static java.lang.Math.*;

public class MilesPerHour
{
	private int distance, hours, minutes;
	private double totalHrs;
	private double mph;

	public MilesPerHour()
	{
		setNums(0,0,0);
		mph=0.0;
	}

	public MilesPerHour(int dist, int hrs, int mins)
	{
		setNums(dist,hrs,mins);
		calcTotHrs();

	}

	public void setNums(int dist, int hrs, int mins)
	{
		distance = dist;
		hours = hrs;
		minutes = mins;
	}
	public void calcTotHrs()
	{
		int hrsInMin = hours * 60;
		double totalmin = hrsInMin + minutes;
		totalHrs = totalmin/60;
		
	}

	public void calcMPH()
	{
		mph = distance/totalHrs;
	}

	public void print()
	{
		System.out.println(distance + " miles driven in " + hours + " hours and " + minutes + " minutes going " + mph + "mph");
	}
	
	//create a print or toString or both
	
	public String toString()
	{
		return "";
	}
}