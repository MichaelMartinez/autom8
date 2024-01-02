# create a script that will walk a directory and print out the duplicate files in that directory
# the script should take a single argument which is the directory to search
# the script should print out the duplicate files in the following format:
# <full path to file1>: <full path to file2>

import os
import sys
import hashlib
import tkinter as tk
from tkinter import filedialog

def hashfile(path, blocksize=65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def findDup(parentFolder):
    # Dups in format {hash:[names]}
    dups = {}
    for dirName, subdirs, fileList in os.walk(parentFolder):
        print('Scanning %s...' % dirName)
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            # Calculate hash
            file_hash = hashfile(path)
            # Add or append the file path
            if file_hash in dups:
                dups[file_hash].append(path)
            else:
                dups[file_hash] = [path]
    return dups

def printResults(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        result_str = 'Duplicates Found:\n\nThe following files are identical. The name could differ, but the content is identical\n\n'
        for result in results:
            for subresult in result:
                result_str += subresult + '\n'
            result_str += '___________________\n'
        result_text.config(state='normal')
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, result_str)
        result_text.config(state='disabled')
    else:
        result_text.config(state='normal')
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, 'No duplicate files found.')
        result_text.config(state='disabled')

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        dir_entry.delete(0, tk.END)
        dir_entry.insert(0, directory)
        run_scan()

def run_scan():
    directory = dir_entry.get()
    if os.path.exists(directory):
        dups = findDup(directory)
        printResults(dups)
    else:
        result_text.config(state='normal')
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, 'Please enter a valid directory path.')
        result_text.config(state='disabled')

root = tk.Tk()
root.title('Duplicate File Finder')

dir_label = tk.Label(root, text='Directory:')
dir_label.grid(row=0, column=0, padx=5, pady=5)

dir_entry = tk.Entry(root, width=50)
dir_entry.grid(row=0, column=1, padx=5, pady=5)

dir_button = tk.Button(root, text='Select', command=select_directory)
dir_button.grid(row=0, column=2, padx=5, pady=5)

result_text = tk.Text(root, width=80, height=20, state='disabled') 
scan_button = tk.Button(root, text='Scan', command=run_scan)
scan_button.grid(row=2, column=1, padx=5, pady=5)


    