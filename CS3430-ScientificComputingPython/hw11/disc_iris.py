#!/usr/bin/python

##########################################################
# module: disc_iris.py
# description: discretization  of scikit learn iris dataset.
# each feature's interval is mapped into four sub-intervals
# and each sub-interval is assigned a discrete symbol.
# read and  run investigate_iris_dataset.py to study
# the programmatic structure if the iris dataset.
#
# bugs to vladimir dot kulyukin at usu dot edu
##########################################################

import sys
import numpy as np
from investigate_iris_dataset import get_sorted_feat_vals_for_iris_feats
from investigate_iris_dataset import get_iris_examples_classified_as
from investigate_iris_dataset import iris_data
from bin_id3 import PLUS, MINUS
import random


def disc_iris_feat_vals_into_ranges(iris_data):
    """
    Returns a dictionary that discretizes iris feature values into
    symbolic ranges. This discretization is arbitrary. Many other (actually,
    infinitely many) discretizations can be found.
    """
    fv = get_sorted_feat_vals_for_iris_feats(iris_data)
    fv2 = {}

    # SepLen is discretized into SLR0, SLR1, SLR2, SLR3, SLR4.
    fv2['SLR0'] = fv['SepLen'][0:30]
    fv2['SLR1'] = fv['SepLen'][30:60]
    fv2['SLR2'] = fv['SepLen'][60:90]
    fv2['SLR3'] = fv['SepLen'][90:120]
    fv2['SLR4'] = fv['SepLen'][120:150]

    # SepWid is discretized into SWR0, SWR1, SWR2, SWR3, SWR4.
    fv2['SWR0'] = fv['SepWid'][0:30]
    fv2['SWR1'] = fv['SepWid'][30:60]
    fv2['SWR2'] = fv['SepWid'][60:90]
    fv2['SWR3'] = fv['SepWid'][90:120]
    fv2['SWR4'] = fv['SepWid'][120:150]

    # PetLen is discretized into PLR0, PLR1, PLR2, PLR3, PLR4.
    fv2['PLR0'] = fv['PetLen'][0:30]
    fv2['PLR1'] = fv['PetLen'][30:60]
    fv2['PLR2'] = fv['PetLen'][60:90]
    fv2['PLR3'] = fv['PetLen'][90:120]
    fv2['PLR4'] = fv['PetLen'][120:150]

    # PetWid is discretized into PWR0, PWR1, PWR2, PWR3, PWR4.
    fv2['PWR0'] = fv['PetWid'][0:30]
    fv2['PWR1'] = fv['PetWid'][30:60]
    fv2['PWR2'] = fv['PetWid'][60:90]
    fv2['PWR3'] = fv['PetWid'][90:120]
    fv2['PWR4'] = fv['PetWid'][120:150]

    return fv2


def disc_seplen(sepl):
    """
    Maps a sepal length sepl to SepLen0, SepLen1, SepLen2, SepLen3, or SepLen4.
    """
    seplen = {'SepLen0': [4.3, 5.02], 
              'SepLen1': [5.02, 5.739999999999999], 
              'SepLen2': [5.74, 6.46], 
              'SepLen3': [6.46, 7.18], 
              'SepLen4': [7.18, 7.909999999999999]}
    for k, v in seplen.items():
        if v[0] <= sepl < v[1]:
            return k


def disc_sepwid(sepw):
    """
    Maps a sepal width sepw to SepWid0, SepWid1, SepWid2, SepWid3, or SepWid4.
    """
    sepwid = {'SepWid0': [2.0, 2.48], 
              'SepWid1': [2.48, 2.96], 
              'SepWid2': [2.96, 3.44], 
              'SepWid3': [3.4400000000000004, 3.9200000000000004], 
              'SepWid4': [3.9200000000000004, 4.41]}
    for k, v in sepwid.items():
        if v[0] <= sepw < v[1]:
            return k


def disc_petlen(petl):
    """
    Maps a petal length petlen to PetLen0, PetLen1, PetLen2, PetLen3, or PetLen4.
    """
    petlen = {'PetLen0': [1.0, 2.18], 
              'PetLen1': [2.18, 3.3600000000000003], 
              'PetLen2': [3.3600000000000003, 4.540000000000001], 
              'PetLen3': [4.540000000000001, 5.720000000000001], 
              'PetLen4': [5.720000000000001, 6.91]}
    for k, v in petlen.items():
        if v[0] <= petl < v[1]:
            return k


def disc_petwid(petw):
    """
    Maps a petal width petw to PetWid0, PetWid1, PetWid2, PetWid3, or PetWid4.
    """
    petwid = {'PetWid0': [0.1, 0.58], 
              'PetWid1': [0.58, 1.06], 
              'PetWid2': [1.06, 1.54], 
              'PetWid3': [1.54, 2.02], 
              'PetWid4': [2.02, 2.51]}
    for k, v in petwid.items():
        if v[0] <= petw < v[1]:
            return k


def disc_iris_example(example, named_target):
    """
    Maps an iris example example into a 5-tuple of discretized symbols.
    """
    assert named_target in set(['setosa', 'versicolor', 'virginica'])
    sepl, sepw, petl, petw = example
    # ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
    return (disc_seplen(sepl), disc_sepwid(sepw), disc_petlen(petl), disc_petwid(petw), named_target)


def disc_iris(iris_data, csv_file):
    """
    Converts scikit-learn IRIS dataset and converts it into a CSV file of symbolic attributes.
    """
    setosa = get_iris_examples_classified_as(iris_data, 'setosa') 
    versicolor = get_iris_examples_classified_as(iris_data, 'versicolor')
    virginica = get_iris_examples_classified_as(iris_data, 'virginica')
    flower_counter = 0
    with open(csv_file, 'w') as outf:
        outf.write('Number,\t SepLen,\t SepWid,\t PetLen,\t PetWid,\t Class\n')        
        for ex in setosa:
            d = disc_iris_example(ex, 'setosa')
            outf.write('{},\t {},\t {},\t {},\t {},\t {}\n'.format(flower_counter, d[0], d[1], d[2], d[3], d[4]))
            flower_counter += 1
        for ex in versicolor:
            d = disc_iris_example(ex, 'versicolor')
            outf.write('{},\t {},\t {},\t {},\t {},\t {}\n'.format(flower_counter, d[0], d[1], d[2], d[3], d[4])) 
            flower_counter += 1
        for ex in virginica:
            d = disc_iris_example(ex, 'virginica')
            outf.write('{},\t {},\t {},\t {},\t {},\t {}\n'.format(flower_counter, d[0], d[1], d[2], d[3], d[4]))
            flower_counter += 1


def train_test_split_iris(iris_data, train_size):
    """
    Splits iris_data into training and testing dataset; 
    train_size specifies the percentage of the data allocated for training.
    """
    assert 0.0 < train_size < 1.0
    setosa = get_iris_examples_classified_as(iris_data, 'setosa')
    versicolor = get_iris_examples_classified_as(iris_data, 'versicolor')
    virginica = get_iris_examples_classified_as(iris_data, 'virginica')
    random.shuffle(setosa)
    random.shuffle(versicolor)
    random.shuffle(virginica)
    train_index = int(50*train_size)
    train_setosa, test_setosa = setosa[:train_index], setosa[train_index:]
    train_versicolor, test_versicolor = versicolor[:train_index], versicolor[train_index:]
    train_virginica, test_virginica = virginica[:train_index], virginica[train_index:]
    return train_setosa, train_versicolor, train_virginica, test_setosa, test_versicolor, test_virginica


def disc_bin_train_test_iris(train_setosa, train_versicolor, train_virginica,
                             test_setosa, test_versicolor, test_virginica,
                             flower_class):
    assert flower_class in set(['setosa', 'versicolor', 'virginica'])
    # generate binary (PLUS/MINUS) train data
    with open(flower_class + '_train_bin.csv', 'w') as outf:
        outf.write('Number,\t SepLen,\t SepWid,\t PetLen,\t PetWid,\t Class\n')        
        flower_counter = 0
        for f in train_setosa:
            d = disc_iris_example(f, 'setosa')
            if flower_class == 'setosa':
                outf.write('{},\t {},\t {},\t {},\t {},\t {}\n'.format(flower_counter, d[0], d[1], d[2], d[3], PLUS))
            else:
                outf.write('{},\t {},\t {},\t {},\t {},\t {}\n'.format(flower_counter, d[0], d[1], d[2], d[3], MINUS))
            flower_counter += 1
        for f in train_versicolor:
            d = disc_iris_example(f, 'versicolor')
            if flower_class == 'versicolor':
                outf.write('{},\t {},\t {},\t {},\t {},\t {}\n'.format(flower_counter, d[0], d[1], d[2], d[3], PLUS))
            else:
                outf.write('{},\t {},\t {},\t {},\t {},\t {}\n'.format(flower_counter, d[0], d[1], d[2], d[3], MINUS))
            flower_counter += 1
        for f in train_virginica:
            d = disc_iris_example(f, 'virginica')
            if flower_class == 'virginica':
                outf.write('{},\t {},\t {},\t {},\t {},\t {}\n'.format(flower_counter, d[0], d[1], d[2], d[3], PLUS))
            else:
                outf.write('{},\t {},\t {},\t {},\t {},\t {}\n'.format(flower_counter, d[0], d[1], d[2], d[3], MINUS))
            flower_counter += 1

    # generate binary (PLUS/MINUS) test data
    with open(flower_class + '_test_bin.csv', 'w') as outf:
        outf.write('Number,\t SepLen,\t SepWid,\t PetLen,\t PetWid,\t Class\n')        

        flower_counter = 0
        for f in test_setosa:
            d = disc_iris_example(f, 'setosa')
            if flower_class == 'setosa':
                outf.write('{},\t {},\t {},\t {},\t {},\t {}\n'.format(flower_counter, d[0], d[1], d[2], d[3], PLUS))
            else:
                outf.write('{},\t {},\t {},\t {},\t {},\t {}\n'.format(flower_counter, d[0], d[1], d[2], d[3], MINUS))
            flower_counter += 1
            
        for f in test_versicolor:
            d = disc_iris_example(f, 'versicolor')
            if flower_class == 'versicolor':
                outf.write('{},\t {},\t {},\t {},\t {},\t {}\n'.format(flower_counter, d[0], d[1], d[2], d[3], PLUS))
            else:
                outf.write('{},\t {},\t {},\t {},\t {},\t {}\n'.format(flower_counter, d[0], d[1], d[2], d[3], MINUS))
            flower_counter += 1
        
        for f in test_virginica:
            d = disc_iris_example(f, 'virginica')
            if flower_class == 'virginica':
                outf.write('{},\t {},\t {},\t {},\t {},\t {}\n'.format(flower_counter, d[0], d[1], d[2], d[3], PLUS))
            else:
                outf.write('{},\t {},\t {},\t {},\t {},\t {}\n'.format(flower_counter, d[0], d[1], d[2], d[3], MINUS))
            flower_counter += 1

    # save the real test data
    with open('iris_test_data.csv', 'w') as outf:
        outf.write('Number,\t SepLen,\t SepWid,\t PetLen,\t PetWid,\t Class\n')        
        flower_counter = 0
        for f in test_setosa:
            d = disc_iris_example(f, 'setosa')
            outf.write('{},\t {},\t {},\t {},\t {},\t {}\n'.format(flower_counter, d[0], d[1], d[2], d[3], 'setosa'))
            flower_counter += 1
        for f in test_versicolor:
            d = disc_iris_example(f, 'versicolor')
            outf.write('{},\t {},\t {},\t {},\t {},\t {}\n'.format(flower_counter, d[0], d[1], d[2], d[3], 'versicolor'))
            flower_counter += 1
        for f in test_virginica:
            d = disc_iris_example(f, 'virginica')
            outf.write('{},\t {},\t {},\t {},\t {},\t {}\n'.format(flower_counter, d[0], d[1], d[2], d[3], 'virginica'))
            flower_counter += 1


def disc_train_test_bin_split_for_flower(iris_data, flower_class, train_size):
    """
    Discretizes IRIS data for a specific flower for binary ID3 algorithm and splits
    the data into training and testing datasets.
    """
    tr_set, tr_versi, tr_virg, test_set, test_versi, test_virg = train_test_split_iris(iris_data, train_size)
    disc_bin_train_test_iris(tr_set, tr_versi, tr_virg, test_set, test_versi, test_virg, flower_class)    


if __name__ == '__main__':
    disc_iris(iris_data, 'iris_data.csv')    
    pass
