# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 19:34:26 2026

@author: wellz
"""

import pandas as pd

astronomy_data = pd.DataFrame({
    "Celestial Object": ["Mars", "Venus", "Jupiter", "Saturn", "Moon"],
    "Brightness (Magnitude)": [-2.0, -4.6, -1.8, 0.2, -12.7],
    "Observation Date": pd.date_range(start="2024-01-01", periods=5),
})
