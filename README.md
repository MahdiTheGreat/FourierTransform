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

# Fourier transform

Sound is a kind of continuous mechanical wave that is created by the vibration of air particles. When this wave reaches our eardrum, it vibrates and we hear the sound. If we consider one of the particles of the environment (for example, an air molecule near the ear) and draw its displacement relative to its equilibrium point at different times, the sound waveform that we hear is created.

Digital audio is also made by sampling this continuous wave at short intervals. For example, the sounds that we work with in this project have a sampling rate of 44100 Hz (that is, sampling at an interval of 1/44100 S).
In this exercise, we want to calculate and check the Fourier series of several audio signals. For this purpose, we use four audio files from wave4 to wave1 and open them with Scipy.io.wavfile read function, and draw their graph in the time domain (note that for the horizontal axis, each 44100 sample is equal to one second. We can also plot the first few samples [for example, the initial 500 samples] to see the signals better.)
We know that the Fourier series coefficients of continuous-time signals are obtained from the following equation:

![image](https://github.com/MahdiTheGreat/FourierTransform/assets/47212121/a4784cb3-731b-4dfb-8253-c6a02b725f3f)

By expanding on the above equation, we can calculate the real part (b_k) and the imaginary part (c_k) of each coefficient separately like below:

![image](https://github.com/MahdiTheGreat/FourierTransform/assets/47212121/5c46621a-ebe4-44fe-99ab-897e05777b88)

For each of the four given signals, we calculate their Fourier series coefficients (b_k) and (c_k) for k=0 till k = 10 manually and draw the graph of |a_k|s. Below we plot both the waves and their |a_k|s.

wave1:

![wave1](https://github.com/MahdiTheGreat/SignalProcessing/assets/47212121/9c26f726-bbc8-4629-9c5c-45bc9985433a)

wave1 |a_k|s:

![wave1ak](https://github.com/MahdiTheGreat/SignalProcessing/assets/47212121/c2f06f9c-115a-4a03-99d1-b84adf56e5c2)

wave2:

![wave2](https://github.com/MahdiTheGreat/SignalProcessing/assets/47212121/ad8aad7a-beb1-4c75-bae6-2add60444ba9)

wave2 |a_k|s:

![wave2ak](https://github.com/MahdiTheGreat/SignalProcessing/assets/47212121/8df1fb3c-2698-44ce-a016-002fe1200119)

wave3:

![wave3](https://github.com/MahdiTheGreat/SignalProcessing/assets/47212121/1c46bc1c-6be1-4304-95fa-9594b9c4adab)

wave3 |a_k|s:

![wave3ak](https://github.com/MahdiTheGreat/SignalProcessing/assets/47212121/33ee9444-b585-479b-a2e8-afdf4a63c3e6)

wave4:

![wave4](https://github.com/MahdiTheGreat/SignalProcessing/assets/47212121/3268fce5-fe70-45bb-8eaa-eca2607e3a20)

wave4 |a_k|s:

![wave4ak](https://github.com/MahdiTheGreat/SignalProcessing/assets/47212121/0095c1c9-38c8-4f4e-ac28-4cd43de76c78)

as can be seen, by the plots, the sound file wave1.wav has the most complete sound, which we can understand both by listening to it and by looking at the graph of |a_k| coefficients, which shows us fourier series signals contribute to the consturction to wave1 more than the other files and have more effect in the construction of wave1, as seen by the coefficients.










