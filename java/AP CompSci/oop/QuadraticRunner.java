//Name - Connor Gannaway
//Date - 9/19
//Class -AP1
//Lab  - OOP

import java.util.Scanner; 
import static java.lang.System.*;
import static java.lang.Math.*;

public class QuadraticRunner
{
	public static void main( String[] args )
	{
		//add test cases 
		Scanner keyboard = new Scanner(System.in);
		System.out.print("Input variable A :: ");
		int varA = keyboard.nextInt();
		System.out.print("Input variable B :: ");
		int varB = keyboard.nextInt();
		System.out.print("Input variable C :: ");
		int varC = keyboard.nextInt();


		Quadratic quad1 = new Quadratic(varA,varB,varC);
		quad1.print();
	}
}