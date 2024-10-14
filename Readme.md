Repository to create and store jit-compiled libtorch modules.

Package versions of `torch` and other related packages are in `requirements.txt` which you can install via `pip install -r requirements.txt`

Modules can be generated with scripts contained in `scripts` directory.
For example
```
cd scripts
python3.8 ./jit-squeezenet1_1.py
```
They will be placed by default in `jit-compiled-models`