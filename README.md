# TUI Bank Client
This project had been created by a TUI method which is command method means bank clerk when start he/she will see a list of command with keywords and in the last line “Type Your Command:> “ will appear and clerk must type an valuable keyword, the good point in here is that program created in way that doesn’t crash and give clerk errors by typing wrong keywords, on other hand clerk doesn’t worry about errors in the whole program, even if the internet connection has problems, at the program launch! This it a big point and advantage.

<p>
The other advantage is that the program or client is colorful, and the clerk won’t be tired during the performance! 

  
<p>
  The client doesn’t care about the way you type it means if you type “exit” or “eXiT” client see them in same way and understand that you want to exit! (not a case sensitive)

  
## This client has some main commands, this client can do things as follow
* Client gives a list of bank accounts: he/she can see who has been opened account in bank, how many account this person has and what’s each account status and in the last how much money has list and all of the data sort at the first (The advantage point is if too many data were on server client doesn’t stop to load all the data and save it then show then, actually it show the data whenever it received and clerk doesn’t has to wait for loading all the data together, it won’t be sensed!)
* Client shows account logs: the client shows the accounts logs, debits and credit in color, in a console shell and after showing the logs in the shell the turtle shell with launch and shows the logs in a chart which has been coded by turtle library in python and that’s colorful too.
* Client Opens/Closes/Blocks an account: client can open an account with filing a form and it also can close or block an account by entering an account number. 
* Opening an account and add it to account owner: the client can also open an account for a person who has an account or some account in the current time which is deferent from opening an account for a new person which hasn’t ever opened an account in bank 
* Retrieving a blocked or closed account number in a sorted way 
* Retrieving a person all information and accounts in a sorted way 
* Creating a new clerk account: clerk who logged in at first can also open an account for other employees by giving system a username and password. 
* Can transfers money (fund transfer): clerk can transfer money by cash or by account to account. 
* Showing a transferred money logs for every account numbers 
* Clerk can easily exit by typing exit
  
### Installation
1. Packages You Need to Run This
   ```sh
   pip install requests
   ```
    ```sh
   pip install pip._vendor.colorama
   ```
    ```sh
   pip install turtle
   ```
