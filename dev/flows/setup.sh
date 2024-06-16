#!/bin/bash

# Initialize conda for bash
eval "$(conda shell.bash hook)"

conda activate azureml_py310_sdkv2
pip install promptflow promptflow-tools
