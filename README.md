# SweepFlaw demo

## Prerequisites
### System requirement
- git
- make
- clang
- g++
### Python requirement
- `python >= 3.5`
- `setuptools`
- `torch >= 1.0` will be installed during installation process.

## Install
```
# If 'position-learning' and 'position_learning' directory exists at project root,
# erase them before install.
make install
```
## Run Sample Scenario
```
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
python3 app.py [Source File] [Input Testcase Directory] [Output Testcase Directory]
```