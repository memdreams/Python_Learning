"""
ELG5376 DSP Project 2018

MVDR Beamformer implementation

Refer to: "Performance study of the MVDR beamformer as a function of the source incidence angle."
"""

import numpy as np
from scipy import fftpack
from scipy import io
import scipy.io.wavfile


# Steering Vector
def steeringV(axisShape, tau, M=3):
    y_axis = axisShape[1]//2
    D = np.zeros([M, y_axis], dtype=complex)
    D[0, :] = 1
    for k in range(y_axis):
        w = 2*np.pi*k/(axisShape[1]-1)
        D[1, k] = np.exp(-1j * w * tau / 2)
        D[2, k] = np.exp(-1j * w * tau)
    return D

def gammaInv(D_n1, D_n2, M=3, alpha_psn=0.95):
    D_n1 = np.mat(D_n1).T
    D_n2 = np.mat(D_n2).T
    Gamma_w1 = D_n1 * D_n1.conj().T
    Gamma_w2 = D_n2 * D_n2.conj().T
    I_m = np.eye(M)
    Gamma_pswn = (1-alpha_psn)*I_m + alpha_psn*(Gamma_w1+Gamma_w2) # Eq. 30
    Gamma_inv = np.linalg.inv(Gamma_pswn)
    return Gamma_inv


def mvdr(D, D_n1, D_n2):
    h = np.zeros(D.shape, dtype=complex)
    for freqPin in range(h.shape[1]):   # h(w) = (Gamma_inv(w)*D(w))/(D_H(w)*Gamma_inv(w)*D(w)
        gamma_inv = gammaInv(D_n1[:, freqPin], D_n2[:, freqPin])
        d_s = np.mat(D[:, freqPin]).T
        numerator = gamma_inv * d_s
        denominator = d_s.conj().T * numerator
        # denominator_mod = np.sqrt(denominator.real ** 2 + denominator.imag ** 2)
        h_freqpin = (numerator / denominator).getA1()
        h[:, freqPin] = h_freqpin

    return h




if __name__ == '__main__':
    fs1, m1_read = io.wavfile.read('mixture1.wav')
    fs, m2_read = io.wavfile.read('mixture2.wav')
    fs3, m3_read = io.wavfile.read('mixture3.wav')
    y_m = np.zeros([3, m1_read.shape[0]])
    y_m[0] = np.float64(m1_read)
    y_m[1] = np.float64(m2_read)
    y_m[2] = np.float64(m3_read)

    # From Step 1: TDOA, we can get 3 taus
    tau1 = -23 #/ float(fs)  # gama*cos(theta1)
    tau2 = -4 #/ float(fs)
    tau3 = 23 #/ float(fs)


    # Step 2: Beam-forming
    frameWidth = y_m.shape[1]
    n = frameWidth
    n = np.int(np.power(2, np.ceil(np.log2(n))))
    y_freq = fftpack.fft(y_m, n)


    # Steering Vector
    D_s = steeringV(y_freq.shape, tau2)  # source vector
    D_n1 = steeringV(y_freq.shape, tau1)  # noise vector
    D_n2 = steeringV(y_freq.shape, tau3)  # noise vector

    H = mvdr(D_s, D_n1, D_n2)  # calculate the system function of MVDR

    # output = np.zeros(test_data.shape[1], dtype=complex)
    z_freq = np.zeros(H.shape[1], dtype=complex)
    for i in range(H.shape[0]):
        z_freq += H[i].conj() * y_freq[i, :H.shape[1]]

    # plt.plot(z_freq / np.max(np.abs(z_freq)))
    # plt.show()

    z_inverse = z_freq[: : -1]
    # z_f = np.concatenate((z_freq, z_inverse.conj()))
    z_freq = np.concatenate((z_freq, np.zeros(H.shape[1])))
    z_inverse = np.concatenate((np.zeros(H.shape[1]-64000), z_inverse))
    z_inverse = np.concatenate((z_inverse, np.zeros(64000)))
    z_f = z_freq + z_inverse.conj()


    z = fftpack.ifft(z_f)
    z = z.real

    scaled = np.int16(z / np.max(np.abs(z)) * 32767)
    io.wavfile.write('mvdr_output.wav', 16000, scaled)


