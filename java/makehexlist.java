import java.util.ArrayList;
import java.util.Collections;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class makehexlist {

    public static String[] people = { "Aidan McGaha", "Asa McNeil", "Blais Cameron", "Braxton Lazarus",
            "Braxton Algood", "Burke Edwards", "Casey Cutts", "Chris Hoffmann", "Connor Gannaway", "Ethan Brobston",
            "Ethan Morrell", "Gabe Cisco", "Jack Parker", "Jackson Dodd", "Jim Williams", "John WIlliams",
            "Kyra Kendall", "Lucie Pitt", "Luke Palumbo", "Moana Mancuso", "Nathan Linn", "Pierre Bugrat",
            "Rowane Sylvester", "Spencer DeCuir", "TJ Fantine", "Vasili Ekimogloy", "Walker Xoc" };

    public static ArrayList<String> hexlist = new ArrayList<String>();

    public static void main(String[] args) {
        for (String person : people) {
            String hexstring = "";
            char[] characters = person.toCharArray();
            for (char character : characters) {
                hexstring = hexstring + Integer.toHexString(character);
            }
            hexlist.add(hexstring);
        }
        
        Collections.shuffle(hexlist);
        System.out.println(hexlist);

        writeToFile(hexlist, "output.txt");

    }

    public static void writeToFile(ArrayList<String> hexlist, String filename) {
            File f = new File(filename);
            FileWriter write;
            try {
                write = new FileWriter(filename);
                for(String hex : hexlist){
                    write.write(hex + "\n");
                }
                write.close();
    
            } catch (IOException e) {
                e.printStackTrace();
            }
            
        }
    
}