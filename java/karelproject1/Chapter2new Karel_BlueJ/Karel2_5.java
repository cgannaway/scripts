import kareltherobot.*;
public class Karel2_5 implements Directions
{
	public static void main (String [] args)
	{
	// create and exercise robots here.
	UrRobot bob = new UrRobot(3, 4, West, 0);
	bob.turnLeft();
	bob.turnLeft();
	bob.turnLeft();
	bob.move();
	bob.move();
	bob.turnLeft();
	bob.move();
	bob.move();
	bob.turnLeft();
	bob.move();
	bob.move();
	bob.turnLeft();
	bob.move();
	bob.pickBeeper();
	
	bob.turnLeft();
	bob.turnLeft();
	bob.move();
	bob.turnLeft();
	bob.turnLeft();
	bob.turnLeft();
	bob.move();
	bob.move();	
	bob.turnLeft();
	bob.turnLeft();
	bob.turnLeft();
	bob.move();
	bob.move();	
	bob.turnLeft();
	bob.turnLeft();
	bob.turnLeft();
	bob.move();
	bob.move();	
	bob.turnLeft();
	bob.turnLeft();
	bob.turnLeft();
	bob.putBeeper();
	bob.turnOff();
	
	}

	static
	{ 
		World.readWorld("fig2_5.kwld");
		World.setVisible(true);
		World.setDelay(30);
		World.showSpeedControl(true);
	}

}