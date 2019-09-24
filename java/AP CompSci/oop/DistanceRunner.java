//Name - Connor Gannaway
//Date - 9/19
//Class -AP1
//Lab  - OOP

import java.util.Scanner; 
import static java.lang.System.*;
import static java.lang.Math.*;

public class DistanceRunner
{
	public static void main( String[] args )
	{
		//add test cases	
		Scanner keyboard = new Scanner(System.in);
		System.out.print("X1 :: ");
		int x1 = keyboard.nextInt();
		System.out.print("Y1 :: ");
		int y1 = keyboard.nextInt();
		System.out.print("X2 :: ");
		int x2 = keyboard.nextInt();
		System.out.print("Y2 :: ");
		int y2 = keyboard.nextInt();

		Distance dist1 = new Distance(x1,y1,x2,y2);
		dist1.print();


	}
}