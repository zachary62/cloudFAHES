#
#  Zezhou Huang
#  zhuang333@wisc.edu
#
import sys
import os
import pandas as pd
from io import StringIO

class sus_disguised:
    def __init__(self, attr_name, value, score, frequency, tool_name):
        self.attr_name = attr_name
        self.value = str(value)
        self.score = score
        self.frequency = frequency
        self.tool_name = tool_name
    def __str__(self):
        return str(self.__dict__)
    def __eq__(self, other):
        return self.attr_name == other.attr_name and self.value == other.value

import patterns
import DV_Detector
import RandDMVD
import OD

def check_d_quotation(str):
    if "," in str:
        return "\""+str+"\""
    return str

def main2(file1,column):

    #check input csv
    try:
        io1 = StringIO(file1.file.read().decode("utf-8"))
        T = pd.read_csv(io1, dtype=str, keep_default_na=False)
    except OSError as e:
        result = "Error reading csv!"
        return result

    #histogram
    #res = {col:T[col].value_counts() for col in T.columns}
    #print(T['a'].value_counts().get(1))
    sus_dis_values = []

    sus_dis_values = patterns.find_all_patterns(T, sus_dis_values,column)
    sus_dis_values = DV_Detector.check_non_conforming_patterns(T, sus_dis_values,column)
    sus_dis_values = RandDMVD.find_disguised_values(T, sus_dis_values,column)
    sus_dis_values = OD.detect_outliers(T, sus_dis_values,column)
    result = ""
    result += "<p>Attribute Name,DMV,Frequency,Detecting Tool</p>"
    for sus_dis in sus_dis_values:
        result += "<p>" + check_d_quotation(sus_dis.attr_name)+","+check_d_quotation(sus_dis.value)+","+str(sus_dis.frequency)+","+sus_dis.tool_name + "</p>"
    return result
