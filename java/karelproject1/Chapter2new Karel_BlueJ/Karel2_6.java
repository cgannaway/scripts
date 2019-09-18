import kareltherobot.*;
public class Karel2_6 implements Directions
{
	public static void main (String [] args)
	{
	// create and exercise robots here.
		UrRobot bob = new UrRobot(1,2,East,1);
		bob.move();
		bob.turnLeft();
		bob.move();
		bob.move();
		bob.turnLeft();
		bob.turnLeft();
		bob.turnLeft();
		bob.move();
		bob.turnLeft();
		bob.move();
		bob.move();
		bob.turnLeft();
		bob.turnLeft();
		bob.turnLeft();
		bob.move();
		bob.putBeeper();
		bob.move();
		bob.turnLeft();
		bob.turnLeft();
		bob.turnLeft();
		bob.move();
		bob.move();
		bob.turnLeft();
		bob.move();
		bob.turnLeft();
		bob.turnLeft();
		bob.turnLeft();
		bob.move();
		bob.move();
		bob.turnLeft();
		bob.move();
		bob.turnOff();

	}

	static
	{
		World.readWorld("fig2_6.kwld");
		World.setVisible(true);
		World.setDelay(30);
		World.showSpeedControl(true);
	}

}