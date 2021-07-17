

//Player Runner 

public class PlayerRunner
{
	public static void main(String[] args)
	{
		Player s = new Player("Michael Jackson", "rock");

		System.out.println(s.getChoice());			//outs rock
		System.out.println(s.getName());					//outs Michael Jackson
		System.out.println(s);								//outs Michael Jackson rock
		
		s.setChoice("paper");
		System.out.println(s);								//outs Michael Jackson paper	
		
		//instantiate a new Player named jb named Jim Bob that chose scissors
		//print out Jim Bob	
		Player jb = new Player("Jim Bob", "scissors");
		System.out.println(jb);
	}
}





