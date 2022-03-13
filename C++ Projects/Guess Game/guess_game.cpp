#include <iostream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <array>
#include <fstream>
#include <vector>
using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::array;
std::vector<int> guesses;

void scores(std::vector<int> guesses)
{
    std::ofstream write("Scores.txt", std::ios::app);
	write<<"Guesses: {";
	for (int guess:guesses)
	{
		write << " " << guess << " ";
	}
	write<<"} \n";
}

void best_score(int tries)
{
    std::ifstream read("BestScore.txt");
    int current;
    read >> current;

    if (!read.is_open())
    {
        cout<<"Error Reading File!"<<endl;
        return;
    }

    std::ofstream writeup("BestScore.txt");
    if(tries < current)
    {
        writeup << tries;
    }
    else
    {
        writeup << current;
    }

    if (!writeup.is_open())
    {
        cout<<"Error Writing to File!"<<endl;
        return;
    }
}

void tracker(std::vector<int> guesses, int tries)
{
    int counter = 0;
    for (int j = 0; j < tries; j++)
    {
        counter++;  
        cout << "Guess " << counter << ": " << guesses[j] << endl;
    }
    cout << "********************" << endl;
}
 
void guess_game()
{
    int random = rand() % 251;
    //We want a random number but we want that number to be in the range of 0 to 250.
    //That's why we find the mod of that number to base 251. 251 can never be an answer because that will give us 0.
    cout << "Guess the number: \n";
    int guess;
    int tries = 0;
    int i = 0;
    while (tries < 10)
    {
        tries++;
        cout << ">> ";
        cin >> guess;
        guesses.push_back(guess);
        if (guess == random)
        {
            cout << "You win!\n";
            break;
        }
        else if (guess < random && tries < 10)
        {
            cout << "You are too low...\n";
        }
        else if (guess > random && tries < 10)
        {
            cout << "You are too high...\n";
        }
        else
        {
            cout << "You lost!\n";
            cout << "The answer was " << random << endl;
        }
        i++;
    }
    scores(guesses);
    best_score(tries);
    char r;
    cout << "Would you like to see your guesses?(y/n)\n>>";
    cin >> r;
    char response = (char)tolower(r);
    switch (response)
    {
    case 'y':
        tracker(guesses, tries);
        break;

    default:
        break;
    }
}

int main()
{
    srand(time(NULL));
    int choice;
    do
    {
        cout << "O. Quit\n"
             << "1. Play Game\n";
        cout << ">> ";
        cin >> choice;
        switch (choice)
        {
        case 0:
            cout << "Quiting Game...\n";
            break;
        case 1:
			guesses.clear();
            guess_game();
            break;
        default:
            cout << "Invalid input!";
            break;
        }
    } while (choice != 0);

}