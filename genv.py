
DIR_INPUT = "kaggle-data/"
DIR_OUTPUT = "kaggle-data/subset/"

import os
if not os.path.exists(DIR_OUTPUT):
    os.makedirs(DIR_OUTPUT)

# FILES
FILE_TRAIN_UNBALANCED = 'train.csv'
FILE_EVALTEST = 'test.csv'

# COLUMN NAMES
COL_NAME = ['datetime', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
       'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
       'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'amount',
       'fraud']

# COLUMN TYPES
COL_TYPE = ['float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'categorical']

# COL SELECT
LABEL = 'fraud'
DATECOL = 'datetime'

# Fraud features X_fraud

X_fraud = COL_NAME[:]
y_fraud = LABEL
X_fraud.remove(LABEL)
X_fraud.remove(DATECOL)

OUTLIER_COLUMNS = ["outlier_autoenc", "outlier_pca", "outlier_zscore"]
X_fraud_outlier = X_fraud + OUTLIER_COLUMNS
COL_NAME_OUTLIER = COL_NAME  + OUTLIER_COLUMNS
COL_TYPE_OUTLIER = COL_TYPE + ["real", "real", "real"]

OUTLIER_ENSEMBLE_COLUMNS = ["ensemble_outlier"]
X_fraud_ensemble_outlier = X_fraud + OUTLIER_ENSEMBLE_COLUMNS
COL_NAME_OUTLIER = COL_NAME_OUTLIER  + OUTLIER_ENSEMBLE_COLUMNS
COL_TYPE_OUTLIER = COL_TYPE_OUTLIER + ["real"]

# Outliers ignore
OUTLIER_IGNORE = []

# Outliers 

X_autoenc = [x for x in X_fraud if x not in OUTLIER_IGNORE]
X_pca     = [x for x in X_fraud if x not in OUTLIER_IGNORE]
K_COMPONENTS = len(X_pca) - 3
X_zscore  = [x for x in X_fraud if x not in OUTLIER_IGNORE]

# Label hypothesis name
LABEL_HYPOTHESIS_NAME = "True"
LABEL_TRUE_HYPOTHESIS_NAME = True

# graph output
IMAGE_OUTPUT = "image/"
IMAGE_FORMAT = "png"
IMAGE_HEIGT = int(1080/2)
IMAGE_WIDTH = int(1920/2)

# evaluation:

TOP_N = 100


# warnings with traceback

import traceback
import warnings
import sys

def warn_with_traceback(message, category, filename, lineno, file=None, line=None):
    traceback.print_stack()
    log = file if hasattr(file,'write') else sys.stderr
    log.write(warnings.formatwarning(message, category, filename, lineno, line))


# date converter timestamp_to_day
import datetime
timestamp_to_day = lambda x : datetime.datetime.fromtimestamp(x/1000).strftime('%Y-%m-%d') + " (str)"
