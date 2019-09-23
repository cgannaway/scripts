
//Name - Connor Gannaway
//Date - 9/19
//Class -AP1
//Lab  - OOP

import java.util.Scanner; 
import static java.lang.System.*;
import static java.lang.Math.*;

public class MPHRunner
{
	public static void main( String[] args )
	{
		Scanner keyboard = new Scanner(in);

		out.print("\nEnter the distance :: ");
		int dist = keyboard.nextInt();

		out.print("\nEnter the hours :: ");
		int hrs = keyboard.nextInt();

		out.print("\nEnter the minutes :: ");
		int mins = keyboard.nextInt();

		MilesPerHour mph1 = new MilesPerHour(dist, hrs, mins);
		mph1.calcMPH();
		mph1.print();
		
		//add more test cases
		
		
		
	}
}