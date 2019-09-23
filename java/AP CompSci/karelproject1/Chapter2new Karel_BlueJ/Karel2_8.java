import kareltherobot.*;
public class Karel2_8 implements Directions
{
    public static void main (String [] args)
    {
    // create and exercise robots here.
    UrRobot bob = new UrRobot(4,3,East,0);
    bob.move();
    bob.move();
    bob.turnLeft();
    bob.turnLeft();
    bob.turnLeft();
    bob.move();
    bob.pickBeeper();
    bob.move();
    bob.pickBeeper();
    bob.turnLeft();
    bob.turnLeft();
    bob.move();
    bob.move();
    bob.move();
    bob.pickBeeper();
    bob.move();
    bob.pickBeeper();
    bob.turnLeft();
    bob.turnLeft();
    bob.move();
    bob.move();
    bob.turnLeft();
    bob.move();
    bob.putBeeper();
    bob.move();
    bob.putBeeper();
    bob.turnLeft();
    bob.turnLeft();
    bob.move();
    bob.move();
    bob.move();
    bob.putBeeper();
    bob.move();
    bob.putBeeper();
    bob.turnLeft();
    bob.move();
    bob.move();
    bob.turnLeft();
    bob.move();
    bob.move();
    bob.turnLeft();
    bob.turnOff();
    

        
    }

    static
    { 
        World.readWorld("fig2_8.kwld");
        World.setVisible(true);
        World.setDelay(30);
        World.showSpeedControl(true);
    }

}