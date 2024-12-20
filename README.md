# A simple Translator from C++ to Python

## Environment setup

```bash
git clone --recursive https://github.com/yuan-yao21/cppParse.git
cd cppParse
conda create -n parse python=3.13.0
conda activate parse
pip install -r requirments.txt
```

If other libraries are missing, follow the prompts to install them.

## Run code

Modify the `file_symbol` variable(which can be: 1, 2, 3, 4, err1, err2, err3, err4, err5, err6, err7_1, err7_2) in `main.py` to handle different files:

```bash
python main.py
```

You will find the results in the `./result/result_{file_symbol}` folder.
