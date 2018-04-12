"""
ELG5376 DSP Project 2018

Step1: TDOA Implementation
"""

###################  main library imports #####################################
import numpy as np
import matplotlib.pyplot as plt
from scipy import io
import scipy.io.wavfile

# Refer to https://github.com/xiongyihui/tdoa/blob/master/gcc_phat.py
def gcc_phat(sig, refsig, fs=1, max_tau=None, interp=16):
    """TDOA Algorithm: Generalized Cross Correlation - Phase Thansform method """
    n = sig.shape[0] + refsig.shape[0]
    # n = np.int(np.power(2, np.ceil(np.log2(n))))   # make n is power of 2

    SIG1 = np.fft.rfft(sig, n=n)
    SIG2 = np.fft.rfft(refsig, n=n)
    R = SIG1 * np.conj(SIG2)

    cc = np.fft.irfft(R/np.abs(R), n=(interp * n))
    max_shift = int(interp * n/2)
    # if max_tau:
    #     max_shift = np.minimum(int(interp * fs * max_tau), max_shift)

    cc = np.concatenate((cc[-max_shift:], cc[:max_shift+1]))

    # detect peaks from cc
    shift = np.argmax(np.abs(cc))
    shift = shift - max_shift
    tau = shift / float(interp * fs)
    print("Tau: ", tau)

    return tau, cc


if __name__ == '__main__':
    fs1, m1_read = io.wavfile.read('mixture1.wav')
    fs3, m3_read = io.wavfile.read('mixture3.wav')
    y_m1 = np.float64(m1_read)
    y_m3 = np.float64(m3_read)

    sound_speed = 340
    distance = 0.25
    max_tau = 2 * distance / sound_speed

    # Step 1: TDOA
    cc = np.correlate(y_m1[fs1*2:], y_m3[fs1*2:], "full") # also we can use gcc_phat method
    plt.plot(cc)
    plt.title('Correlation')
    plt.show()
    # from the figure, we can get 3 peaks around shift at -23, -4, 23, then we can get 3 taus
    tau1 = -23 #/ float(fs)  # gama*cos(theta1)
    tau2 = -4 #/ float(fs)
    tau3 = 23 #/ float(fs)

















