--------------Automated Deadlock Detection Tool-----------------

The Automated Deadlock Detection Tool is a C++ based project designed to automatically identify potential deadlocks in system processes by analyzing process dependencies and resource allocation. 
Deadlocks occur when a set of processes are each waiting for resources held by the others, resulting in a cycle that prevents any of them from proceeding. 
This tool helps users understand and visualize such situations by detecting circular wait conditions using Resource Allocation Graphs (RAG) and Depth-First Search (DFS) algorithms. 
It is particularly useful for operating system students, developers, and anyone interested in process synchronization and resource management.

--------Features-----------

* Detects deadlocks in systems with multiple processes and resources.

* Uses a simple command-line interface for inputting process and resource data.

* Implements cycle detection via DFS to identify circular wait conditions.

* Provides clear output indicating whether a deadlock exists and which processes are involved.

* Lightweight and runs on any standard C++ compiler with no external dependencies.

-------How It Works------------

The tool works by constructing a Resource Allocation Graph where nodes represent processes and resources, and edges represent allocation and requests. 
Using Depth-First Search, it traverses the graph to detect cycles. If a cycle is found, it indicates a deadlock scenario. 
Users input the number of processes and resources, along with the allocation and request details, and the program outputs the deadlock status.

Installation & Usage

Clone or download the repository to your local system.

Open a terminal or command prompt in the project folder.

Compile the Python program using a compiler like python:
cd deadlock_detection 

Future Enhancements

Develop a graphical interface to visualize the Resource Allocation Graph and cycles.

Extend the tool to suggest deadlock resolution strategies such as process termination or resource preemption.

Add support for dynamic process and resource allocation at runtime.

Technologies Used

Python: Core programming language for implementing the detection logic.

DFS Algorithm: Used to traverse the graph and detect cycles.

Command-line Interface: Simple interaction for user input and output.


