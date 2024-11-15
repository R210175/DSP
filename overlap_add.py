import numpy as np
import matplotlib.pyplot as plt

def overlap_add_convolution(signal, kernel, segment_length):
    """
    Perform convolution using the overlap-add method.

    Parameters:
    - signal: Input signal array
    - kernel: Convolution kernel array
    - segment_length: Length of each segment for processing

    Returns:
    - Convolved signal
    """
    kernel_length = len(kernel)
    output_length = len(signal) + kernel_length - 1
    num_segments = (len(signal) + segment_length - 1) // segment_length
    convolved_signal = np.zeros(output_length)
    
    for i in range(num_segments):
        start = i * segment_length
        end = min(start + segment_length, len(signal))
        segment = signal[start:end]
        segment_result = np.convolve(segment, kernel)
        convolved_signal[start:start + len(segment_result)] += segment_result
    
    return convolved_signal
if __name__ == "__main__":
    # Define a signal and kernel
    signal = np.sin(np.linspace(0, 4 * np.pi, 500))  
    kernel = np.array([0.25, 0.5, 0.25]) 
    segment_length = 128
    convolved_signal = overlap_add_convolution(signal, kernel, segment_length)
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(signal, label='Original Signal')
    plt.title('Original Signal')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(convolved_signal, label='Convolved Signal', color='orange')
    plt.title('Convolved Signal (Overlap-Add)')
    plt.legend()

    plt.tight_layout()
    plt.show()

