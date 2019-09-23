import kareltherobot.*;
public class Karel2_9 implements Directions
{
	public static void main (String [] args)
	{
	// create and exercise robots here.
	UrRobot bob = new UrRobot(3,5,North,0);
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
	bob.turnLeft();
	bob.turnLeft();
	bob.turnLeft();
	bob.turnOff();
	
	

		
	}

	static
	{ 
		World.readWorld("fig2_9.kwld");
		World.setVisible(true);
		World.setDelay(30);
		World.showSpeedControl(true);
	}

}