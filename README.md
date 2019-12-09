# SweepFlaw demo

## Prerequisites
### System package requirement
- `git`
- `make`
- `clang`
- `g++`
- `python >= 3.5`
### Python package requirement
- `setuptools`
- `torch >= 1.0` This will be installed during installation process.

## Install
Make sure you have installed all the requirements before installing.
```
# If 'position-learning' and 'position_learning' directory exists at project root,
# erase them before install.

make install
```
## Run Sample Scenario
```
# run for very small size code.
make fasttest

# run for little bigger code than above one.
make demo
```
## Custom Scenario
### Testcase Directory Structure
You can see the example at `demodata/TC_1204B/input` and `demodata/TC_1204B/output`.
It should be strictly followed.
```
$ tree demodata/TC_1204B/input
demodata/TC_1204B/input
├── 1
├── 10
├── 11
├── 12
├── 13
├── 14
├── 2
├── 3
├── 4
├── 5
├── 6
├── 7
├── 8
└── 9

0 directories, 14 files
```
```
$ tree demodata/TC_1204B/output
demodata/TC_1204B/output
├── 1
├── 10
├── 11
├── 12
├── 13
├── 14
├── 2
├── 3
├── 4
├── 5
├── 6
├── 7
├── 8
└── 9

0 directories, 14 files
```
As you can see, the corresponding output of the input file `input/1` is `output/1`. You can configure related setting at `src/setting.py`'s `TESTCASE_STARTNUM`, `TESTCASE_PREFIX`, and `TESTCASE_POSTFIX`.
### Run Custom Scenario
```
python3 app.py [Source File] [Input Testcase Directory] [Output Testcase Directory] [Result Output Json Filename]
```
If you turn on the `JSONFILE_OUT` flag in `setting.py`, you should put the argument `Result Output Json Filename`. If `JSONFILE_OUT` flag turn off, the argument `Result Output Json Filename` will be ignored.
