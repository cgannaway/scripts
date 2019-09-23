import kareltherobot.*;
public class Karel2_7 implements Directions
{
    public static void main (String [] args)
    {
    // create and exercise robots here.
    UrRobot bob = new UrRobot(5,7,East,0);
    bob.turnLeft();
    bob.turnLeft();
    bob.move();
    bob.move();
    bob.pickBeeper();
    bob.turnLeft();
    bob.turnLeft();
    bob.turnLeft();
    bob.move();
    bob.turnLeft();
    bob.move();
    bob.pickBeeper();
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
    bob.turnLeft();
    bob.move();
    bob.move();
    bob.move();
    bob.move();
    bob.turnOff();
    

        
    }

    static
    { 
        World.readWorld("fig2_7.kwld");
        World.setVisible(true);
        World.setDelay(30);
        World.showSpeedControl(true);
    }

}