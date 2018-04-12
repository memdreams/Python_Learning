"""
ELG5376 DSP Project 2018

Post-filter logmmse implementation
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import io
import scipy.io.wavfile
from scipy.special import *

# Refer to https://github.com/braindead/logmmse
def logmmse(x, Srate, noise_frames=6, Slen=0, eta=0.15):
    if Slen == 0:
        Slen = int(np.floor(0.02 * Srate))


    if Slen % 2 == 1:
        Slen = Slen + 1

    PERC = 50
    len1 = (Slen * PERC) // 100
    len2 = int(Slen - len1)

    win = np.hanning(Slen)
    win = win * len2 / np.sum(win) 
    nFFT = 2 * Slen

    noise_mean = np.zeros(nFFT) 
    for j in range(0, Slen*noise_frames, Slen):
        noise_mean = noise_mean + np.absolute(np.fft.fft(win * x[j:j + Slen], nFFT, axis=0))
        noise_mu = noise_mean / noise_frames
        noise_mu2 = noise_mu ** 2

    x_old = np.zeros(len1)
    Xk_prev = np.zeros(Slen * 2)  # size160    ## size640
    Nframes = int(np.floor(len(x) / len2) - np.floor(Slen / len2))
    xfinal = np.zeros(Nframes * len2)
    aa = 0.98
    mu = 0.98
    ksi_min = 10 ** (-25 / 10)

    k = 0

    #for k in range(0, Nframes*len2, len2):
    for n in range(0, Nframes-1, 1): 
        insign = win * x[k:k + Slen] 

        spec = np.fft.fft(insign, nFFT, axis=0)
        sig = np.absolute(spec)
        sig2 = sig ** 2

        gammak = np.minimum(sig2 / noise_mu2, 40)

        #if Xk_prev.all() == 0:
        if n == 0:
            ksi = aa + (1 - aa) * np.maximum(gammak - 1, 0)
        else:
            ksi = aa * Xk_prev / noise_mu2 + (1 - aa) * np.maximum(gammak - 1, 0)
            ksi = np.maximum(ksi_min, ksi)

        log_sigma_k = gammak * ksi/(1 + ksi) - np.log(1 + ksi)
        vad_decision = np.sum(log_sigma_k)/Slen
        if (vad_decision < eta):
            noise_mu2 = mu * noise_mu2 + (1 - mu) * sig2

        A = ksi / (1 + ksi)
        vk = A * gammak
        ei_vk = 0.5 * expn(1, vk)
        hw = A * np.exp(ei_vk)

        sig = sig * hw
        Xk_prev = sig ** 2
        xi_w = np.fft.ifft(hw * spec, nFFT, axis=0)
        xi_w = np.real(xi_w)

        xfinal[k:k + len2] = x_old + xi_w[0:len1]
        x_old = xi_w[len1:Slen]

        k = k + len2

    return xfinal, {'noise_mu2': noise_mu2, 'Xk_prev': Xk_prev, 'x_old': x_old}



if __name__ == "__main__":
    fs, beamformerResult = io.wavfile.read('mvdr_output.wav')
    samplesNum = 12 * fs
    data = np.float64(beamformerResult[:samplesNum])

    plt.subplot(211)
    plt.plot(data)
    plt.title('mvdr')

    # plt.show()

    chunk_size = 60 * fs
    noise_frames = 10
    window_len = 0
    noise_threshold = 0.3

    samples_read = 0
    while (samples_read < samplesNum):
        frames = samplesNum - samples_read if samples_read + chunk_size > samplesNum else chunk_size
        samples_read += frames

        out = logmmse(data, fs, noise_frames, window_len, noise_threshold)

        scaled = np.int16(out[0] / np.max(np.abs(out[0])) * 32767)
        io.wavfile.write('final_output.wav', 16000, scaled)

    plt.subplot(212)
    plt.plot(scaled)
    plt.title('logmmse')

    plt.show()

