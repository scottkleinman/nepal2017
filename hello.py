# Import the Python os module
import os

# Configure the directory and file paths
path = "C:/Users/Scott/Documents/dhnepal2017"
filename = 'hello.txt'

# If the folder does not exist, make it
if not os.path.isdir(path):
    os.mkdir(path)
# Make the file path
filepath = os.path.join(path, filename)
# Write the file
iacer = open(filepath, 'w')
iacer.write('Hello world')

# Provide some feedback
print("Created file called "+filename+" in "+path+".")