import numpy as np
import logging
import streamlit as st

def reader(mtx:list) -> np.ndarray:
    """ Take input from user sparse numbers from string, while parsing line of string 
        will be row for matrix (numpy array) and return numerical numpy array """
    arr = []
    for row in mtx:
        row = row.strip()
        if len(row) <= 0:
            logging.warning("value not entered properly")
            break
        
        int_row = []
        for val in row.split(' '):
            val = val.strip()
            if len(val) <= 0:
                continue
            try:
                val = int(val)
                int_row.append(val)
            except:
                logging.warning("Invalid literal for int while reading")
                raise ValueError("Invalid literal for int while reading")
        arr.append(int_row)

    try:
        arr = np.matrix(arr)
    except:
        logging.warning("Invalid user input, can't convert to matrix")
        raise ValueError("Invalid user input, can't convert to matrix")
    return arr