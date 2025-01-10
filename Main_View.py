import os
import sys
import csv
import shutil
import time
import pandas as pd
from tkinter import *
import time
from time import sleep
from sklearn.preprocessing import StandardScaler
import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import glob
from tkinter import *
from plyer import notification
from Audio_Preprocessing import *
from CNN import *
from Train_the_Model import *
from Compare_the_Results import *
from Metrics import *
from tkinter import Tk, Label, Button
from tkinter import messagebox
import warnings
warnings.filterwarnings("ignore")
def Dataset():
    print ("\t\t\t |--------- ****** Develop a deep learning-based speech enhancement model ****** --------|")
    time.sleep(1)
    print('===========================================================================')
    print ("\t\t\t ****** LOAD THE DIVERSE DATASET OF SPEECH RECORDINGS ******")
    print('===========================================================================')
    def load_wav_file():
        notification.notify(
            message='LOAD THE DIVERSE DATASET OF SPEECH RECORDINGS',
            app_name='My Python App',
            app_icon=None,
        )
        file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
        if file_path:
            audio = AudioSegment.from_wav(file_path)
            audio.export("Input_speech.wav", format="wav")
            display_waveform(audio)
            directory_path = 'recordings'
            audio_file_extensions = ['*.mp3', '*.wav', '*.flac']
            audio_files = []
            for extension in audio_file_extensions:
                audio_files.extend(glob.glob(os.path.join(directory_path, extension)))
            file_count = len(audio_files)
            output_file = 'file_count.txt'
            with open(output_file, 'w') as file:
                file.write(str(file_count))
            messagebox.showinfo('LOAD THE DIVERSE DATASET','SPEECH RECORDINGS Loaded successfully!')
            print('\nSPEECH RECORDINGS Loaded successfully!\n')
            print('\nNext Click PREPROCESSING button...\n')
    def display_waveform(audio):
        plt.clf()
        plt.plot(audio.get_array_of_samples())
        plt.title("Waveform")
        canvas.draw()
    root = tk.Tk()
    root.title("LOAD THE DIVERSE DATASET OF SPEECH RECORDINGS")
    load_button = tk.Button(root, text="Load .wav File", command=load_wav_file)
    load_button.pack(pady=20)
    fig, ax = plt.subplots(figsize=(6, 4))
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(padx=20, pady=20)
    root.mainloop()
def WavPreprocessing():
    time.sleep(1)
    print ("\t\t\t ****** PREPROCESSING ******")
    notification.notify(
            message='PREPROCESSING',
            app_name='My Python App',
            app_icon=None,
        )
    time.sleep(1)
    Preprocessing();
    time.sleep(1)
    messagebox.showinfo('PREPROCESSING','PREPROCESSING successfully completed!')
    print('\nPREPROCESSING is successfully completed!\n')
    print('\nNext Click NEURAL NETWORK LAYERS button...\n')
def CNN():
    time.sleep(1)
    print ("\t\t\t ****** CONVOLUTIONAL NEURAL NETWORK ******")
    notification.notify(
            message='CONVOLUTIONAL NEURAL NETWORK',
            app_name='My Python App',
            app_icon=None,
        )
    time.sleep(1)
    NeuralNetworkLayers();
    time.sleep(1)
    messagebox.showinfo('CONVOLUTIONAL NEURAL NETWORK','CNN process is Completed!')
    print('\nCNN is successfully completed!\n')
    print('\nNext Click TRAIN THE MODEL button...\n')
def Train():
    time.sleep(1)
    print ("\t\t\t ****** TRAIN THE MODEL ******")
    notification.notify(
            message='TRAIN THE MODEL',
            app_name='My Python App',
            app_icon=None,
        )
    time.sleep(1)
    Traning();
    time.sleep(1)
    messagebox.showinfo('TRAIN THE MODEL','TRAIN THE MODEL process is Completed!')
    print('\nTRAIN THE MODEL is successfully completed!\n')
    print('\nNext Click SPEECH ENHANCEMENT button...\n')
def speechenhancement():
    time.sleep(1)
    print ("\t\t\t ****** SPEECH ENHANCEMENT ******")
    notification.notify(
            message='SPEECH ENHANCEMENT',
            app_name='My Python App',
            app_icon=None,
        )
    time.sleep(1)
    speech_enhancement();
    time.sleep(1)
    messagebox.showinfo('SPEECH ENHANCEMENT','SPEECH ENHANCEMENT process is Completed!')
    print('\nSPEECH ENHANCEMENT process is successfully completed!\n')
    print('\nNext Click PERFORMANCE METRICS button...\n')
def Performancemetrics():
    time.sleep(1)
    print ("\t\t\t ****** PERFORMANCE METRICS ******")
    print('\nGraph generation process is starting\n')
    notification.notify(
            message='PERFORMANCE METRICS',
            app_name='My Python App',
            app_icon=None,
        )
    time.sleep(1)
    PerformanceMetrics();
    print('\nGraph is Generated Successfully...!')
    print('==========================================================================================')
    print("\n\n+++++++++++++++++++++++++++++++++++++++ END ++++++++++++++++++++++++++++++++++++")
def main_screen():
    window = Tk()
    window.title("DEVELOP A DEEP LEARNING_BASED SPEECH ENHANCEMENT MODEL")
    window_width = 800
    window_height = 550
    window.geometry(f"{window_width}x{window_height}")
    window.configure(bg="lightseagreen")
    label_bg_color = "deepskyblue"
    button_bg_color = "purple"
    button_fg_color = "white"
    Label(window, text="Develop a deep learning-based speech enhancement model", bg=label_bg_color, fg="white", width="500", height="2", font=('Georgia', 12)).pack()
    Label(text = "",bg="lightseagreen", fg="White").pack(pady=10)    
    b1 = Button(text="START", height="2", width="25", bg=button_bg_color, fg=button_fg_color, font=('Times New Roman', 12), command=Dataset)
    b1.pack(pady=10)
    b2 = Button(text="PREPROCESSING", height="2", width="25", bg=button_bg_color, fg=button_fg_color, font=('Times New Roman', 12), command=WavPreprocessing)
    b2.pack(pady=10)
    b3 = Button(text="NEURAL NETWORK LAYERS", height="2", width="25", bg=button_bg_color, fg=button_fg_color, font=('Times New Roman', 12), command=CNN)
    b3.pack(pady=10)
    b4 = Button(text="TRAIN THE MODEL", height="2", width="25", bg=button_bg_color, fg=button_fg_color, font=('Times New Roman', 12), command=Train)
    b4.pack(pady=10)
    b5 = Button(text="SPEECH ENHANCEMENT", height="2", width="25", bg=button_bg_color, fg=button_fg_color, font=('Times New Roman', 12), command=speechenhancement)
    b5.pack(pady=10)
    b6 = Button(text="PERFORMANCE\nMETRICS", height="2", width="25", bg=button_bg_color, fg=button_fg_color, font=('Times New Roman', 12), command=Performancemetrics)
    b6.pack(pady=10)
    window.mainloop()
main_screen()
