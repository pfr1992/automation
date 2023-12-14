#!/bin/bash

python app.py

for i in {1..100000}
    do
        if [ $? -gt 10 ]; then
            python app.py
    done