# Creating Coco-toolkit-GUI Executable File 

## 1 - Run GUI from terminal

### Git Clone
```bash
git clone https://github.com/kadircosar/Coco-toolkit-GUI.git
```

### Install requirenments
Please make sure you are in Coco-toolkit-GUI directory. Then run in terminal:

```bash
pip install -r requirenments.txt
```
### Run GUI 
Run this command in GUI.py directory.

```bash
python GUI.py
```
## 2 - Run GUI with Executable File

### Git Clone
```bash
git clone https://github.com/kadircosar/Coco-toolkit-GUI.git
```

### Install requirenments
Please make sure you are in Coco-toolkit-GUI directory. Then run in terminal:

```bash
pip install -r requirenments.txt
```

### Install pyinstaller

To create executable file we need to install pyinstaller.

```bash
pip install pyinstaller
```

### Build Executable File

####  For Windows
```bash
pyinstaller.exe --onefile --icon=coco.ico GUI.py
```

####  For Linux 
```bash
pyinstaller --onefile --icon=coco.ico GUI.py
```

### Run Program 
After building  executable file, go Coco-toolkit-GUI/dist directory and run GUI.
