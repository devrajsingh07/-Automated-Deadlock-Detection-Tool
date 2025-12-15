Automated Deadlock Detection Tool
Project Overview

The Automated Deadlock Detection Tool is a Python-based project designed to automatically detect potential deadlocks in system processes by analyzing process dependencies and resource allocation. Deadlocks occur when a set of processes are each waiting for resources held by others, forming a cycle that prevents any of them from proceeding. This tool uses Resource Allocation Graphs (RAG) and Depth-First Search (DFS) to identify such cycles and notify the user about potential deadlocks. It provides an easy-to-use command-line interface and is useful for students, developers, and researchers studying operating systems and process synchronization.

Features

Detects deadlocks in systems with multiple processes and resources.

Accepts user input for the number of processes, resources, allocation matrix, and request matrix.

Implements cycle detection using DFS to find circular wait conditions.

Displays clear output showing whether a deadlock exists and which processes are involved.

Lightweight, requires only Python (no external libraries needed).

How It Works

The tool constructs a Resource Allocation Graph where nodes represent processes and resources, and edges represent allocations and requests. It then performs a DFS traversal to detect cycles in the graph. If a cycle is found, it indicates a deadlock. Users provide input via the command line, and the tool outputs the deadlock status along with the involved processes.

Installation & Usage

Clone or download the repository.

Ensure Python 3 is installed on your system.

Open a terminal or command prompt in the project folder.

Run the program using:

python src.py


Follow the prompts to enter the number of processes, resources, allocation matrix, and request matrix.

The tool will output whether a deadlock exists and the processes involved.

Sample Input/Output

Input:

Number of Processes: 3  
Number of Resources: 3  
Allocation Matrix:  
0 1 0  
2 0 0  
3 0 3  
Request Matrix:  
0 0 1  
2 0 0  
0 0 0  


Output:

Deadlock detected!  
Processes involved: P0, P1

Future Enhancements

Create a graphical interface to visualize the Resource Allocation Graph and detected cycles.

Implement deadlock resolution suggestions, such as process termination or resource preemption.

Add support for dynamic resource allocation and real-time deadlock detection.

Technologies Used

Python 3: Core programming language for implementing the detection logic.

DFS Algorithm: Used to traverse the graph and detect cycles.

Command-line Interface: Simple user interaction for input and output.