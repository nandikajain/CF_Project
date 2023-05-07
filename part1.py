import codecs
import pandas as pd
import numpy as np


NUM_USERS = 943
NUM_ITEMS = 1682


def init_data_matrices():
    """
    Reads and initializes data matrices
    """
    COLUMNS = ["user-id", "item-id", "rating", "timestamp"]

    doc_data = codecs.open(f"ml-100k/u.data", "rU", "UTF-8")
    base_df = pd.read_csv(doc_data, sep="\t", encoding="utf-8", names=COLUMNS)
    base_df["user-id"] -= 1
    base_df["item-id"] -= 1

    data_mat = np.zeros((NUM_USERS, NUM_ITEMS)) - 1
    for i in range(len(base_df)):
        data_mat[base_df["user-id"][i]][base_df["item-id"][i]] = base_df["rating"][i]

    print("data matrix initialized!")
    return data_mat


R = init_data_matrices()


# =======================
# STEP 1
# =======================


# Preference
P = (R > 0).astype(int)

# Weight
W = np.sum(P, axis=1)

# Create user, item, weight, preference columns
with open("wals_input", "w") as fp:
    fp.write(f"%%MatrixMarket matrix coordinate real general\n")
    fp.write(f"{NUM_USERS} {NUM_ITEMS} {P.sum()}\n")
    for u in range(R.shape[0]):
        for i in range(R.shape[1]):
            fp.write(f"{u} {i} {W[u]} {P[u][i]}\n")


"""
wals --training=wals_input --lambda=0.065 --minval=1 --maxval=5 --max_iter=6 --quiet=1
"""