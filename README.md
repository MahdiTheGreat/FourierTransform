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

Next, we open the bonus audio file and with the help of the function we wrote and obtain its Fourier series coefficients and draw them in a graph below(the periodicity of this signal is approximately 229.34 milliseconds).

Bonus:

![bonus](https://github.com/MahdiTheGreat/SignalProcessing/assets/47212121/ed0ef527-c85d-49e5-807a-c25b95ae2291)

bonus |a_k|s:

![bonusAk](https://github.com/MahdiTheGreat/SignalProcessing/assets/47212121/713979b9-1403-41dc-9ba0-aaef2897db48)

If we pay close attention, the 5 dominant frequencies in this signal are rational coefficients of each other, and for this reason, the sound of this signal is more pleasant than the previous ones. Also there is a more pleasant shape to the progression of these frequencies. The five dominant frequencies are in the form of e^-jwk for k from 5 to 10, and with w=2pi/(10114×(1/44100)).

# Pyzam

Most likely, you are familiar with music recognition systems (such as Shazam). It is interesting to know that music recognition in these systems is done with the help of Fourier transform. In this part, we want to implement such a system ourselves!

We know that by using the Fourier transform, we can move the signals from the time domain to the frequency domain. By doing this, the constituent frequencies of a signal (which could not be identified in the time domain) are determined. For example, consider the following audio signal in the time domain. Suppose we want to obtain the constituent components of this signal.

![image](https://github.com/MahdiTheGreat/SignalProcessing/assets/47212121/4ecf9182-8b32-4d35-b82f-15813f04cf4f)

As you can see, the above diagram gives complete information about signal changes in the time domain. For example, we notice that this sound is silent between 2 and 3 seconds. But this chart does not give us any information about the frequencies in other times. The following graph is obtained by calculating and plotting the Fourier transform using the fft function in numpy.

![image](https://github.com/MahdiTheGreat/SignalProcessing/assets/47212121/7c152e80-28c4-4f3b-8511-455ed14c192c)

As you can see the output is similar to what we have implemented in the Fourier transform section, however in this section we use numpy for it's better performance. This chart gives us complete information about the range of frequencies in the signal. For example, we notice that frequencies around 750 and 1250 Hz make up our signal. But the chart above does not give us any information about when each of these frequencies were present.

To obtain this information, we need a graph that gives us a state between the time and frequency domains. Suppose we break the given signal into shorter seperate time windows (for example, 100 milliseconds), and for each time window we calculate its Fourier transform independently. Putting this instantaneous transformation together, we get a frequency versus time graph. We arrive at what is called the spectrogram or spectrogram of the signal. For example, for the mentioned signal, its spectrogram is as follows (brighter points mean that the Fourier transform value is larger at that point).

![image](https://github.com/MahdiTheGreat/SignalProcessing/assets/47212121/5300940d-eb56-4b97-a9db-a1a89488d129)

Now, it is clear from this graph that in the first 2 seconds the frequencies of about 666 and 1200 Hz and in the last 2 seconds the frequencies of about 666 and 1333 Hz formed our signal. Results that could not be obtained from any of the graphs of the time and frequency domains.

To build a music recognition system, we need to compare the spectrogram of the signals. In this section, we have two sets of audio files at our disposal. The data collection contains the original version of some music and the audio input by the user should be compared with all the members of this collection. The clip collection contains several examples of user inputs that you can use to test your code. To compare the signals, we follow the steps below for each of the signals:

1. Break the signal into 2048 sample windows (about 50 ms) and take the Fourier transform from each time window separately using numpy. We store this Fourier transform in the form of a matrix, each column of which is the Fourier transform output for a It is a time window.
2. Keep the data about frequency around 100 to 5000 Hz and remove the rest (you can use fftfreq to get the frequency corresponding to each fft output element).
3. Divide the frequencies of each time window into 6 baskets with equal sizes and consider the frequency that has the maximum value in each basket as the index frequency of that basket. To better understand this process, consider the following figure as an example. In this diagram, the frequency of the index of each basket in each time window is marked with a dot.

![image](https://github.com/MahdiTheGreat/SignalProcessing/assets/47212121/fd08c466-9193-4b74-b65c-e26047e8831c)

After going through the above steps for each signal, we have a matrix with 6 rows, each row represents the index frequency in one of the baskets and each column represents the 6 index frequencies of each time window, which we call signals noiseprint.

Now, to identify an input music, it is enough to compare its noiseprint with the noiseprint of the music we calculated earlier in our database (data set). For this, we use the similarity function. By receiving the noiseprint of the signal in the database in the first input and the noiseprint of the signal given by the user in the second input, this function returns their similarity in the form of a number. Finally, any signal from the database that is more similar to the user's input is selected as the detected music.












