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

Modify the `file_symbol` variable in `main.py` to handle different files:

```bash
python main.py
```

You will find the results in the `./result/result_{file_symbol}` folder.
