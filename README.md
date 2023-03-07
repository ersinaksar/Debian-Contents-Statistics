# Debian-Contents-Statistics
## Thought Process
For the solution of this task, I first read about the task assigned to me. Then I dissected this task. These are the parts that make up the actual logic of the task for me and fulfill the functionality of the task. I prefer to break them down and examine them to solve problems. The parts that perform the functionality of the task are actually just simple tasks. These things work like reading a file, downloading a file, or saving a file. The part that created the main logic of the task was to find the packages from the Contents file that performed the actual operation of the task and how many files there were for these packages.

After determining these parts, I directly examine the file where the actual logic of the task will work and think about what kind of logic and structure I should establish here. After establishing the algorithm here, I concentrate on the errors and exceptions that may occur. After solving these stages, I start to implement other parts of the code that will fulfill the functionality of the task. At this point, it is much easier to implement the other parts into the code because I have already proven that the code works well and solidly in the kernel, and all the added parts are placed around this kernel.

Of course, dividing the code into functions, classes or more advanced structures varies according to the project made and desired, but at this point I did not do this. Because I want my way of thinking to be more clear. If you look closely at the python script, you can see the part in the center of the program that I read and break down the task at first and that does the main function of the program. I'm leaving this code that way so that it can seem easier.

## Time Spent Working
Normally in work, I spend most of my time understanding the problem, breaking it down into the right pieces and writing the functional code. But the article I wrote for this task also took me a while. So I took a total of two and a half to three hours to complete this task.


## Debian-Contents-Statistics
This is a command line tool written in Python that takes the architecture (amd64, arm64, mips etc.) as an argument and downloads the compressed Contents file associated with it from a Debian mirror. The program then parses the file and outputs the statistics of the top 10 packages that have the most files associated with them.

The code uses the argparse library to parse the command line arguments, urllib library to download the Contents file, gzip library to handle the compression of the file, and the csv library to parse the file.

The program begins by defining the command line argument for the architecture using the argparse library. It then constructs the url for the Contents file based on the architecture provided and uses the urllib library to download the file. The downloaded file is then decompressed using the gzip library and the contents are written to a text file.

The program then opens the contents.txt file and uses the csv library to parse the file, line by line. For each line, the program checks if there are multiple packages associated with the file by checking for the presence of a ',' in the second column of the line. If there are multiple packages, the program splits the package names by ',' and increments the file count for each package in the dictionary. If there is only one package, the program increments the file count for that package in the dictionary.

After the file has been completely parsed, the program sorts the dictionary by file count in descending order and prints out the top 10 packages with the most files associated with them. The package names are also modified to only show the package name and not the full path.

To use the program, simply run the command "python package_statistics.py [architecture]" where architecture is the desired architecture for which you want to download the Contents file and get the statistics.



## Pseudo Code

* #### 1-Define the command line argument for the architecture.

* #### 2- Download the compressed Contents file for the given architecture from a Debian mirror.

* #### 3- Decompress and parse the contents file.

* #### 4- Create an empty dictionary to store the package name and number of files associated with it.

* #### 5- Read the contents file line by line, ignoring any lines that do not conform to the specified format.

* #### 6- For each line, check if there are multiple packages listed. If so, split the package names and add them to the dictionary.

* #### 7- If there is only one package listed, add it to the dictionary.

* #### 8- Sort the dictionary by the number of files in descending order.

* #### 9- Print out the top 10 packages and the number of files associated with them in the format "package_name number_of_files".
