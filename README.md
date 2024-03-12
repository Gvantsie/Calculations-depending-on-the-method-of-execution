Trapezoid, Rectangle, and Square Area Calculation depending on the method of execution
==============================
This Python script provides functionality to calculate the areas of trapezoids, rectangles, and squares using different methods, including sequential execution, threads, processes, and a hybrid approach.

*Classes:

-Trapezoid-   
Represents a trapezoid shape.   
Attributes:
a: The smaller base of the trapezoid.  
b: The larger base of the trapezoid.   
h: The height of the trapezoid.   
Methods:  
area(): Computes and returns the area of the trapezoid.  
Comparison methods (__lt__, __eq__, __ge__) to compare trapezoids based on their areas.    

-Rectangle-   
Inherits from the Trapezoid class.  
Represents a rectangle shape.  
Attributes:  
a: The height of the rectangle.  
h: The width of the rectangle.  
Method:  
__str__(): String representation of the rectangle.  

-Square-   
Inherits from the Rectangle class.  
Represents a square shape.  
Attribute:
a: The side length of the square.  
Method:  
__str__(): String representation of the square.

*Functions
trapezoid_area(arr): Calculates the areas of trapezoids in the given array.  
rectangle_area(arr): Calculates the areas of rectangles in the given array.  
square_area(arr): Calculates the areas of squares in the given array.  
regular(arr): Computes areas sequentially without using threads or processes.  
threads(arr): Computes areas using threads.  
multiprocess(arr): Computes areas using processes.  
hybrid(arr): Computes areas using a hybrid approach combining processes and threads.

*Execution  
Random arrays of trapezoids, rectangles, and squares are generated.
The script measures the time taken to compute the areas using different methods:  
Sequential execution (regular()).  
Execution with threads (threads()).  
Execution with processes (multiprocess()).  
Hybrid execution (hybrid()), combining processes and threads.  

*Usage   
Ensure you have Python installed.  
revise requirements.txt file to install the required packages.

*Run the script.  
python trapezoid.py  
Check the output for the time taken for each method of area calculation.

*Note  
You can adjust the number of shapes generated and their dimensions by modifying the parameters passed to the random.randint() function calls.  
The script provides placeholders for printing parameters within the area calculation functions. Uncomment these lines if you want to see the parameters printed during execution.  
You can also adjust the number of threads and processes used in the hybrid approach by modifying the values of the THREADS and PROCESSES constants.

To see the time difference, under different running and size conditions, you can open time_statistics.txt file.

>Gvantsa



