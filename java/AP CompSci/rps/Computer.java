
//Computer class 

public class Computer
{
	//instance / member variables
   private String choice;
   
	public Computer()
	{
		//call random set Choice
		randomSetChoice();	
	}
	
	public String getChoice()
	{
		return choice;
	}
	
	public void randomSetChoice()
	{
		//use Math.random()
		//use switch case
		int randint =  (int) (Math.random() * 3);
		if(randint == 0){
			choice = "rock";
		}
		else if(randint == 1){
			choice = "paper";
		}
		else if(randint == 2){
			choice = "scissors";
		}
	}	
		
	/*
	 didIWin(Player p) will return the following values
	 	0 - both players have the same choice
	 	1 - the computer had the higher ranking choice
	 	-1 - the player had the higher ranking choice
	 */	
	public int didIWin(Player p)
	{
		String pChoice = p.getChoice();

		if(choice == "rock" && pChoice == "paper"){
			return -1;
		}
		else if(choice == "rock" && pChoice == "scissors"){
			return 1;
		}
		else if(choice == "paper" && pChoice == "rock"){
			return 1;
		}
		else if(choice == "paper" && pChoice == "scissors"){
			return -1;
		}
		else if(choice == "scissors" && pChoice == "rock"){
			return -1;
		}
		else if(choice == "scissors" && pChoice == "paper"){
			return 1;
		}
		else{
			return 0;
		}
	}
	
	public String toString()
	{
		return "Computer Chose: " + choice;
	}		   
}