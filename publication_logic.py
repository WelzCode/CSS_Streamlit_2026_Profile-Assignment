# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 19:36:58 2026

@author: wellz
"""

def filter_by_keyword(df, keyword):
    return df[
        df.apply(
            lambda row: keyword.lower() in row.astype(str).str.lower().values,
            axis=1
        )
    ]
