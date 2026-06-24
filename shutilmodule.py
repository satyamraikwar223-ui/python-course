import shutil 

shutil.copy("clutter.py", "clutter_copy.py")
#outputs: clutter_copy.py 


shutil.copytree("clutterfolder", "clutterfolder_copy")
#outputs: clutterfolder_copy 

shutil.move("clutterfolder/clutter.py", "clutter.py")
#outputs: clutter.py came out of clutterfolder and moved to the current directory

shutil.rmtree("clutterfolder_copy")
#outputs: clutterfolder_copy deleted

shutil.rm("clutter_copy.py")
#outputs: clutter_copy.py deleted

