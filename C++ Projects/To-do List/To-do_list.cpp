#include <iostream>
#include <fstream>
#include <vector>
#include<windows.h>
using std::cin;
using std::cout;
using std::endl;
using std::string;
std::vector<string> list;

void assign()
{
    int num = 0;
    string line;
    std::ifstream read("To do list.txt");
    while (getline(read, line))
    {
        list.push_back(line);
    }
}

int count()
{
  int count = list.size();
  return count;
}

void upload()
{
    std::ofstream write("To do list.txt");
    for(string value:list)
    {
        write << value << endl;
    }
}

void view()
{
    int i = 0;
    for (string word:list)
    {
        i++;
        cout<<i<<". "<<word<<endl;
    }
}

void remove()
{
    int response;
    cout<< "Which of your current to-do's would you like to remove?"<< endl;
    view();
    cout<<">>";
    cin >> response;
    response--;
    cout<< "Removing..."<<endl;
    Sleep(3000);
    cout << "The to-do '"<< list[response]<< "' has been removed."<<endl;
    Sleep(1000);
    list.erase(next(list.begin(), response));
    cout<< "Your current to-do's are: "<<endl;
    view();
}

void todolist(int response)
{
    if(response == 1)
    {
        string entry;
        cout<<"New To-do"<<endl;
        cout<<">> ";
        getline(cin, entry);
        list.push_back(entry);
        upload();
        cout<<"To-do has been added!"<<endl;
        for (string val:list)
        {
            cout<<val<<endl;
        }
    }
    else if(response == 2)
    {
        remove();
    }
    else if(response == 3)
    {
        cout<< "Your to-do's are: "<< endl;
        view();
    }
}
int main()
{
    int response;
    assign();
    do
    {
    cout<< "*************************"<<endl;
    cout<< "What would you like to do?"<< endl;
    cout<< "1. Add a new to-do"<<endl;
    cout<< "2. Remove a to-do" <<endl;
    cout<< "3. View to-do list" <<endl;
    cout<< "4. Exit Menu " <<endl;
    cout<< ">> ";
    cin >> response;
    cin.ignore(1,'\n');
    todolist(response);
    } while(response != 4);
    upload();
}
    