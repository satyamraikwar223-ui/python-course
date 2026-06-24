import os 

files = os.listdir("clutteredfolder")
i = 1
for file in files:
    if file.endswith(".png"):
        os.rename(f"clutteredfolder/{file}", f"clutteredfolder/image{i}.png")
        i += 1

        