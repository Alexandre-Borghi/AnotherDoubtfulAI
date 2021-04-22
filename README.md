# Simple perceptron visualization

This project shows a perceptron classifying two categories of objects, here blue and red dots. You can add dots by left/right clicking on the upper left frame to see the AI adjusting the decision boundary in real-time.

I recommend the latest version of Python to run this program. You also need the tkinter library.

I created the code for the AI from scratch, starting from a Matrix class to store weights and biases and do the math, and then a NeuralNetwork class, with which you can create an arbitrary sized, fully-connected neural network.

This project allowed me to test the code I created on a very simple case, though one could theoretically use it on more complex problems, but it's not really optimized.

Screenshot:
![Screenshot of the perceptron visualization](/doc/screenshot.png)