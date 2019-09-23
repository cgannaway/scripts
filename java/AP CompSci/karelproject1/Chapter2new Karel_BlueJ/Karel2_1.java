
/**
 * Karel2_1.java 
 *
 * @author - Jane Doe
 * @author - Period n
 * @author - Id nnnnnnn
 *
 * @author - I received help from ...
 *
 */

import kareltherobot.*;
import java.awt.Color;

public class Karel2_1 implements Directions
{
    public static void main(String[] args)
    {
        UrRobot bob = new UrRobot(2, 7, West, 0);
        bob.move();
        bob.turnLeft();
        bob.move();
        bob.turnLeft();
        bob.turnLeft();
        bob.turnLeft();
        bob.move();
        bob.turnLeft();
        bob.turnLeft();
        bob.turnLeft();
        bob.move();
        bob.pickBeeper();
        bob.turnOff();

    }

    static
    {
        World.setVisible(true);
        World.readWorld("fig2_1.kwld");
        World.showSpeedControl(true);
    }
}