# Signal Processing

At first, we are gonna use the Matplotlib and NumPy library to plot some continuous and discrete signals. These signals can be seen below:

![image](https://github.com/MahdiTheGreat/SignalProcessing/assets/47212121/f750baf6-d86c-4664-a2f4-87a7612631ce)

We plot these signals in signalsPlot.py. The plots of these functions are also uploaded to the repository.

Sound is a kind of continuous mechanical wave that is created by the vibration of air particles. When this wave reaches our eardrum, it vibrates and we hear the sound. If we consider one of the particles of the environment (for example, an air molecule near the ear) and draw its displacement relative to its equilibrium point at different times, the sound waveform that we hear is created.

Digital audio is also made by sampling this continuous wave at short intervals. For example, the sounds that we work with in this project have a sampling rate of 44100 Hz (that is, sampling at an interval of 1/44100 S).
In this exercise, we want to calculate and check the Fourier series of several audio signals. For this purpose, we use four audio files from wave4 to wave1 and open them with Scipy.io.wavfile read function, and draw their graph in the time domain (note that for the horizontal axis, each 44100 sample is equal to one second. We can also plot the first few samples [for example, the initial 500 samples] to see the signals better.)
We know that the Fourier series coefficients of continuous-time signals are obtained from the following equation:

![image](https://github.com/MahdiTheGreat/FourierTransform/assets/47212121/a4784cb3-731b-4dfb-8253-c6a02b725f3f)

By expanding on the above equation, we can calculate the real part (b_k) and the imaginary part (c_k) of each coefficient separately like below:

![image](https://github.com/MahdiTheGreat/FourierTransform/assets/47212121/5c46621a-ebe4-44fe-99ab-897e05777b88)

For each of the four given signals, we calculate their Fourier series coefficients (b_k) and (c_k) for k=0 till k = 10 manually and draw the graph of |a_k|s For example, the output of one of the signals can be seen below:

![image](https://github.com/MahdiTheGreat/FourierTransform/assets/47212121/8da13957-b249-414f-8b25-ff2077f77ebb)






