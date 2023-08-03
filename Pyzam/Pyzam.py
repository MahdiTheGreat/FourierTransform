import scipy.io.wavfile as wavRead
import numpy as np
import copy

def slicer(lastStop,message,step):
    lastStop[0]+=step
    return message[lastStop[0]-step:lastStop[0]]


def similarity(song_spec, clip_spec, points_per_slice=6):
    song_flat = song_spec.flatten()
    clip_flat = clip_spec.flatten()

    sim_window_size = points_per_slice - 1
    score = 0
    for anchor in range(clip_flat.shape[0] - points_per_slice):
        anchor_y = anchor % points_per_slice
        sim_window = clip_flat[anchor: anchor + sim_window_size]
        for song_anchor in range(anchor_y, song_flat.shape[0] - points_per_slice - 1, points_per_slice):
            if clip_flat[anchor] == song_flat[song_anchor]:
                if np.count_nonzero((song_flat[song_anchor:song_anchor + sim_window_size] - sim_window) == 0) >= 4:
                    score += 1

    score /= song_flat.shape[0]
    return score

def max(row):
    print()
    max=copy.deepcopy(row[0])
    for i in range(len(row)):
        if max[1]<row[i][1]:
            max=copy.deepcopy(row[i])
    return max[0]

def noisePrintProducer(wav,fs):
    lastStop = [0]
    #print("the lenght of wave is ")
    #print(len(wav))
    #print()
    fourierMatrix = []
    windowSize = 6
    windowFreq = 5000
    windowStep = windowFreq / (windowSize - 1)
    windowLength = 2048


    while (lastStop[0] < len(wav)):
        if lastStop[0] + windowLength < len(wav):
            sample = slicer(lastStop, wav, windowLength)
        else:
            sample = slicer(lastStop, wav, len(wav) - lastStop[0])
        signal = np.array(sample, dtype=float)
        fourier = np.fft.fft(signal)
        n = signal.size
        freq = np.fft.fftfreq(n,d=1/fs)

        fourierMatrix.append(np.stack((np.abs(freq),np.abs(fourier)), axis=-1))

    noisePrint = [[[] for j in range(len(fourierMatrix))] for i in range(windowSize-1)]

    print()

    for i in range(len(fourierMatrix)):
        for j in range(len(fourierMatrix[i])):
            for k in range(windowSize - 1):
                if (100 if k == 0 else k * windowStep) <= fourierMatrix[i][j][0] < (k + 1) * windowStep:
                    noisePrint[k][i].append(fourierMatrix[i][j])
    print()

    for i in range(len(noisePrint)):
        for j in range(len(noisePrint[i])):
                if(len(noisePrint[i][j])>0):
                 noisePrint[i][j] = max(noisePrint[i][j])
                else:noisePrint[i][j]=0



    return noisePrint

def matrixPrinter(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

def similarityFinder(clipNumber):
    score=[]
    wav = wavRead.read("clip/"+str(clipNumber)+".wav")
    fs = copy.deepcopy(wav[0])
    wav = wav[1]
    noisePrint2 = np.asarray(noisePrintProducer(wav, fs))
    #print("noisePrint2 is")
    #matrixPrinter(noisePrint2)
    for i in range(1,5):
        wav = wavRead.read("data/"+str(i)+".wav")
        fs = copy.deepcopy(wav[0])
        wav = wav[1]
        noisePrint1 = np.asarray(noisePrintProducer(wav, fs))
        # print("noisePrint1 is")
        # matrixPrinter(noisePrint1)
        score.append(similarity(noisePrint1,noisePrint2))

    print("the scores are")
    print(score)

    maxScore=np.argmax(np.asarray(score))
    print("the clip is similar to song number")
    print(maxScore+1)


clipNumber=input("enter the number of the clip")
similarityFinder(clipNumber)











