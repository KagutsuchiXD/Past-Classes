####################################
# module: iris_bin_id3.py
# Connor Osborne
# A01880782
# The three choices that gave me the best results was versicolor, verginica, setosa
#####################################

from bin_id3 import bin_id3
from bin_id3 import PLUS, MINUS
import numpy as np
import random
from investigate_iris_dataset import get_iris_examples_classified_as
from investigate_iris_dataset import iris_data
from disc_iris import disc_train_test_bin_split_for_flower


# def train_dt(train_examples, target_attrib, avt, dbg):
#     """
#     Trains a binary ID3 tree on train_examples.
#     """
#     return bin_id3.fit(train_examples, target_attrib, attribs, avt, dbg)


def test_dt(dt, test_examples, target_attrib):
    """
    Tests a binary ID3 tree dt on test_examples.
    """
    return sum([predict_dt(dt, tex) == tex[target_attrib] for tex in test_examples])/len(test_examples)


def predict_dt(dt, ex):
    """
    Use binary ID3 tree dt to classify example ex.
    """
    return bin_id3.predict(dt, ex)


def test_multi_dt(setosa_dt, versicolor_dt, virginica_dt, test_examples, target_attrib):
    """
    Given three binary ID3 trees for setosa, versicolor, and virginica to 
    classify test_examples with bin_id3_iris_classify().
    """
    acc = 0.0
    for te in test_examples:
        pv = bin_id3_iris_classify(setosa_dt, versicolor_dt, virginica_dt, te)
        tv = bin_id3.get_example_attrib_val(te, target_attrib)
        if pv == tv:
            acc += 1
        # print('pv = {}; tv = {}'.format(pv, tv))
    return acc/len(test_examples)


def train_test_bin_id3_dt(iris_data, target_attrib, flower_class, n, train_size, dbg):
    """
    Train a binary ID3 decision tree for IRIS data for flower_class for n runs and
    a given training size train_size.
    """
    assert flower_class in set(['setosa', 'versicolor', 'virginica'])
    total_acc = 0.0
    train_bin_csv = flower_class + '_train_bin.csv'
    test_bin_csv = flower_class + '_test_bin.csv'
    print('Testing bin id3 trees for {}'.format(flower_class))
    for i in range(n):
        # 1. generate train and test csv files for flower_class.
        disc_train_test_bin_split_for_flower(iris_data, flower_class, train_size)
        # 2. get the train examples for flower_class
        train_bin_examples, colnames = bin_id3.parse_csv_file_into_examples(train_bin_csv)
        attribs = set(colnames[1:])        
        avt = bin_id3.construct_attrib_values_from_examples(train_bin_examples, colnames[1:])
        # 3. fit a bin id3 tree to the train examples
        dt = bin_id3.fit(train_bin_examples, target_attrib, attribs, avt, dbg)
        # 4. display the dt if need be
        # bin_id3.display_id3_node(dt, '')
        # 5. get the test examples
        test_bin_examples, colnames = bin_id3.parse_csv_file_into_examples(test_bin_csv)
        # 6. run the decision tree on the test examples
        run_acc = test_dt(dt, test_bin_examples, target_attrib)
        # 7. update the total accuracy
        total_acc += run_acc
        print('run {}) acc = {}'.format(i, run_acc))
    total_acc /= n    
    print('avrg acc = {}\n'.format(total_acc))
    return total_acc


def train_test_bin_id3_multi_dt(iris_data, target_attrib, n, train_size, dbg):
    """
    Train three decision trees (setosa, versicolor, virginica) on IRIS.
    """
    total_acc = 0.0
    setosa_train_bin_csv = 'setosa_train_bin.csv'
    setosa_test_bin_csv  = 'setosa_test_bin.csv'
    versicolor_train_bin_csv = 'versicolor_train_bin.csv'
    versicolor_test_bin_csv  = 'versicolor_test_bin.csv'
    virginica_train_bin_csv = 'virginica_train_bin.csv'
    virginica_test_bin_csv  = 'virginica_test_bin.csv'
    setosa_dt, versicolor_dt, virginica_dt = None, None, None
    print('Testing multi bin id3 tree classification for iris dataset')
    for i in range(n):
        # Setosa
        # 1. generate train and test csv files for setosa.
        disc_train_test_bin_split_for_flower(iris_data, 'setosa', train_size)
        # 2. get the train examples for setosa
        train_examples, colnames = bin_id3.parse_csv_file_into_examples(setosa_train_bin_csv)
        attribs = set(colnames[1:])        
        avt = bin_id3.construct_attrib_values_from_examples(train_examples, colnames[1:])
        # 3. fit a bin id3 tree to the train examples
        setosa_dt = bin_id3.fit(train_examples, target_attrib, attribs, avt, dbg)
        # 4. display the dt if need be
        # bin_id3.display_id3_node(dt, '')
        
        # 1. generate train and test csv files for versicolor.
        disc_train_test_bin_split_for_flower(iris_data, 'versicolor', train_size)
        # 2. get the train examples for versicolor
        train_examples, colnames = bin_id3.parse_csv_file_into_examples(versicolor_train_bin_csv)
        attribs = set(colnames[1:])        
        avt = bin_id3.construct_attrib_values_from_examples(train_examples, colnames[1:])
        # 3. fit a bin id3 tree to the train examples
        versicolor_dt = bin_id3.fit(train_examples, target_attrib, attribs, avt, dbg)
        # 4. display the dt if need be
        # bin_id3.display_id3_node(dt, '')

        # 1. generate train and test csv files for virginica.
        disc_train_test_bin_split_for_flower(iris_data, 'virginica', train_size)
        # 2. get the train examples for virginica
        train_examples, colnames = bin_id3.parse_csv_file_into_examples(virginica_train_bin_csv)
        attribs = set(colnames[1:])
        avt = bin_id3.construct_attrib_values_from_examples(train_examples, colnames[1:])
        # 3. fit a bin id3 tree to the train examples
        virginica_dt = bin_id3.fit(train_examples, target_attrib, attribs, avt, dbg)
        # 4. display the dt if need be
        # bin_id3.display_id3_node(dt, '')
        
        # 5. get real test examples
        test_examples, colnames = bin_id3.parse_csv_file_into_examples('iris_test_data.csv')
        # 6. run the decision tree on the test examples
        run_acc = test_multi_dt(setosa_dt, versicolor_dt, virginica_dt, test_examples, target_attrib)
        # 7. update the total accuracy
        total_acc += run_acc
        print('run {}) average acc = {}'.format(i, run_acc))
        
    total_acc /= n    
    print('avrg acc = {}\n'.format(total_acc))
    return total_acc


def bin_id3_iris_classify(setosa_dt, versi_dt, virg_dt, example):
    """
    Classify example with three binary ID3 decision trees: setosa_dt, versi_dt, virg_dt. 
    Returns 'unknown' if all three decision trees return MINUS.
    """
    if bin_id3.predict(versi_dt, example) == PLUS:
        return 'versicolor'
    if bin_id3.predict(virg_dt, example) == PLUS:
        return 'virginica'
    if bin_id3.predict(setosa_dt, example) == PLUS:
        return 'setosa'

    return 'unknown'


if __name__ == '__main__':
    train_test_bin_id3_multi_dt(iris_data, 'Class', 10, 0.8, False)
    train_test_bin_id3_multi_dt(iris_data, 'Class', 10, 0.7, False)
    train_test_bin_id3_multi_dt(iris_data, 'Class', 10, 0.6, False)
    pass        
