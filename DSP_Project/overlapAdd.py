"""
ELG5376 DSP Project 2018
Author: Jie Meng

overlap-add implementation
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import io
import scipy.io.wavfile
from scipy import fftpack



def main():
    rate1, m1_read = io.wavfile.read('mixture1.wav') #rate1 is actually fs
    fs, m2_read = io.wavfile.read('mixture2.wav')
    rate3, m3_read = io.wavfile.read('mixture3.wav')
    y_m = np.zeros([3, m1_read.shape[0]])
    y_m[0] = np.float64(m1_read)
    y_m[1] = np.float64(m2_read)
    y_m[2] = np.float64(m3_read)


    # Step 1: TDOA
    # cc = np.correlate(y_m1[rate1*2:], y_m3[rate1*2:], "full") # also we can use gcc_phat method
    # from the figure, we can get 3 peaks around shift at -23, -4, 23, then we can get 3 taus
    tau1 = -23 #/ float(fs)  # gama*cos(theta1)
    tau2 = -4 #/ float(fs)
    tau3 = 23 #/ float(fs)


    # Step 2: Beam-forming
    # Y(w) overlap-add; frame width is 40ms*fs=640 or 1s*fs=16000, 75% overlap
    test_data = y_m[:, rate1*2:]
    frameWidth = 512
    n = frameWidth
    # n = np.int(np.power(2, np.ceil(np.log2(frameWidth))))
    overlap = n - frameWidth
    frameNum = test_data.shape[1]//frameWidth

    ############  H Calculate    ############
    H = np.zeros([3, n//2], dtype=complex)
    for k in range(0, n // 2):
        # Steering Vector
        w = 2*np.pi*k/n
        D_s = np.array([1, np.exp(-1j * w * tau2 / 2), np.exp(-1j * w * tau2)])
        D_n1 = np.array([1, np.exp(-1j * w * tau1 / 2), np.exp(-1j * w * tau1)])  # noise vector
        D_n2 = np.array([1, np.exp(-1j * w * tau3 / 2), np.exp(-1j * w * tau3)])  # noise vector

        # Gamma Inverse Matrix Calculate
        alpha_psn = 0.9
        D_n1 = np.mat(D_n1).T
        D_n2 = np.mat(D_n2).T
        Gamma_pswn = (1 - alpha_psn) * np.eye(3) + alpha_psn * (D_n1 * D_n1.conj().T + D_n2 * D_n2.conj().T)  # Eq. 30
        Gamma_inv = Gamma_pswn.I

        # System function H
        D_s = np.mat(D_s).T
        numerator = Gamma_inv * D_s
        denominator = D_s.conj().T * numerator
        H[:, k] = (numerator / denominator).getA1()  # calculate the system function of MVDR

    # Overlap-add
    output = np.zeros(test_data.shape[1], dtype=complex)
    for i in range(frameNum):
        ola_len = frameWidth
        frameData = test_data[:, i * frameWidth: (i + 1) * frameWidth]
        window = np.kaiser(ola_len, 6)
        for freqbin in range(frameData.shape[0]):
            frameData[freqbin] = frameData[freqbin] * window

        output_freq = fftpack.fft(frameData, n)

        # shift = winlen - overlap

        z_freq = np.zeros(H.shape[1], dtype=complex)
        for jj in range(H.shape[0]):
            z_freq += H[jj].conj().T * output_freq[jj, : H.shape[1]]
        z_inverse = z_freq[:: -1]
        z_freq = np.concatenate((z_freq, z_inverse.conj()))

        z = fftpack.ifft(z_freq)
        output[i * frameWidth: (i + 1) * frameWidth] = z


    output = output.real


    scaled = np.int16(output / np.max(np.abs(output)) * 32767)
    io.wavfile.write('tau2_beamformer.wav', 16000, scaled)




    # Step 3: poster-filter log








if __name__ == '__main__':
    main()

