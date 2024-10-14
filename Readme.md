Repository to create and store jit-compiled libtorch modules.

`jit-compiled-models` directory contains generated modules. They can be regenerated with scripts contained in `scripts` directory.
For example
```
cd scripts
python3.8 ./jit-squeezenet1_1.py
```