# Fourier-Analysis

A very basic Machine-Learning Algorithm, involving the Monte-Carlo-Method to find the Fourier-Series Approximation of a given Signal.

The Following Image shows the result of the approximation of a sine wave (red). The Longer the runtime of the algorithm, the better the approximation.
The Label of the Blue Line shows the Error associated with the output, which is connected to the area difference between the two lines. The algorithm aims to reduce this area by randomly varying the parameters of a Fourier-Series. 
If the Result is minimizing the Area, it will be accepted, otherwise it will be discarded. This idea is called "Monte-Carlo-Method" and has wide applications in Science. The runtime associated with these kinds of algorithms can be huge.
Even though approximating the sine wave with a Fourier-Series is a trivial example, the algorithm can be applied to any given signal.
![WhatsApp Bild 2024-10-29 um 14 25 17_3c9f5b7f](https://github.com/user-attachments/assets/42cd4e5b-5d3c-487d-9833-5a359f3a3aa7)
