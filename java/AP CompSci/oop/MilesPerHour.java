//Name - Connor Gannaway
//Date - 9/19
//Class -AP1
//Lab  - OOP
import java.util.Scanner; 
import static java.lang.System.*;
import static java.lang.Math.*;

//fix print float, going past tenths place

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
	}

	public void setNums(int dist, int hrs, int mins)
	{
		distance = dist;
		hours = hrs;
		minutes = mins;
	}

	public void calcMPH()
	{
		mph = (double)distance/(hours + ((double)minutes/60));
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