# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     custom_cell_magics: kql
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: everything
#     language: python
#     name: python3
# ---

# %%
import numpy as np
n = 1000
x1 = np.sum(np.arange(n+1))
x2 = n * (n + 1) / 2
x1 == x2

# %% [markdown]
# some more changes again for testing
