# Signal Processing

At first, we are gonna use the Matplotlib and NumPy library to plot some continuous and discrete signals. These signals can be seen below:

![image](https://github.com/MahdiTheGreat/SignalProcessing/assets/47212121/f750baf6-d86c-4664-a2f4-87a7612631ce)

We plot these signals in signalsPlot.py. The plots of these functions can be seen below:

x1(t):

![x1(t)](https://github.com/MahdiTheGreat/SignalProcessing/assets/47212121/903b1b03-eb16-406e-bce1-64bd4b7eebdc)

x2(t):

![x2(t)](https://github.com/MahdiTheGreat/SignalProcessing/assets/47212121/e8f18126-0fe3-4e50-9263-ef6b8c858905)

x3(t):

![x3(t)](https://github.com/MahdiTheGreat/SignalProcessing/assets/47212121/4118772b-8e7e-4bba-8d01-5e92950d01f8)

x1[n]:

![x1 n](https://github.com/MahdiTheGreat/SignalProcessing/assets/47212121/4d698e9b-2db3-4a57-8bc7-60c657c2e8fe)

x2[n]:

![x2 n](https://github.com/MahdiTheGreat/SignalProcessing/assets/47212121/7487dc4d-201a-45c9-bd49-83018e55da85)

x3[n]:

![x3 n](https://github.com/MahdiTheGreat/SignalProcessing/assets/47212121/4360af03-7fc4-4582-85f0-eb7bd5fc7a25)

# Convolution
Next, we are gonna program a function that calculates the convolution of two inputted  functions and plots it. For testing, we use the two sets of functions below as input:

![image](https://github.com/MahdiTheGreat/SignalProcessing/assets/47212121/d1b8fcc7-88a9-4cf9-9f3a-eeb682f513b7)

The outputs can be seen below:

a)

![aConvolution](https://github.com/MahdiTheGreat/SignalProcessing/assets/47212121/d479d5ed-170b-4f5a-8651-7e4bf568f7f0)

b)

![bConvolution](https://github.com/MahdiTheGreat/SignalProcessing/assets/47212121/83491b0c-4b38-450f-ab10-80b836c58c4f)




Sound is a kind of continuous mechanical wave that is created by the vibration of air particles. When this wave reaches our eardrum, it vibrates and we hear the sound. If we consider one of the particles of the environment (for example, an air molecule near the ear) and draw its displacement relative to its equilibrium point at different times, the sound waveform that we hear is created.

Digital audio is also made by sampling this continuous wave at short intervals. For example, the sounds that we work with in this project have a sampling rate of 44100 Hz (that is, sampling at an interval of 1/44100 S).
In this exercise, we want to calculate and check the Fourier series of several audio signals. For this purpose, we use four audio files from wave4 to wave1 and open them with Scipy.io.wavfile read function, and draw their graph in the time domain (note that for the horizontal axis, each 44100 sample is equal to one second. We can also plot the first few samples [for example, the initial 500 samples] to see the signals better.)
We know that the Fourier series coefficients of continuous-time signals are obtained from the following equation:

![image](https://github.com/MahdiTheGreat/FourierTransform/assets/47212121/a4784cb3-731b-4dfb-8253-c6a02b725f3f)

By expanding on the above equation, we can calculate the real part (b_k) and the imaginary part (c_k) of each coefficient separately like below:

![image](https://github.com/MahdiTheGreat/FourierTransform/assets/47212121/5c46621a-ebe4-44fe-99ab-897e05777b88)

For each of the four given signals, we calculate their Fourier series coefficients (b_k) and (c_k) for k=0 till k = 10 manually and draw the graph of |a_k|s For example, the output of one of the signals can be seen below:

![image](https://github.com/MahdiTheGreat/FourierTransform/assets/47212121/8da13957-b249-414f-8b25-ff2077f77ebb)






