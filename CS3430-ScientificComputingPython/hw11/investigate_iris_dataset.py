#!/usr/bin/python

##########################################################
# Programmatic investigation of the features
# of the sklearn iris dataset.
# go to https://scikit-learn.org/stable/install.html
# to install scikit-learn
# bugs to vladimir dot kulyukin at usu dot edu
##########################################################

import sys
import numpy as np
# the iris dataset is loaded with load_iris from sklearn
from sklearn.datasets import load_iris

"""
- load_iris() returns the iris dataset object with the following fields (actually,
these fields are standard for all sklearn datasets):

- iris_data.feature_names: the names of the attributes (aka, features)
- iris_data.data: the actual examples (aka data items)
- iris_data.target: the vector with the ground truth number classification of each example
- iris_data.target_names: the names of the targets corresponding to each numerical value in
                      iris_data.target.
"""
iris_data = load_iris()

# These are feature numbers and their names in the IRIS dataset.
# 0 - 'sepal length (cm)'
# 1 - 'sepal width  (cm)'
# 2 - 'petal length (cm)'
# 3 - 'petal width  (cm)'


def get_iris_feat_names(iris_data):
    """
    returns features names of the iris dataset iris_data
    """
    return iris_data.feature_names


def get_iris_examples(iris_data):
    """ 
    get all examples from the iris dataset iris_data
    """
    return iris_data.data


"""
The IRIS dataset's targets are as follows:
array([0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2
2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
2 2])
0 - setosa
1 - versicolor
2 - virginica
"""


def get_iris_target(iris_data):
    """
    returns iris dataset's targets.
    """
    return iris_data.target

# The target names for the IRIS dataser are array(['setosa' 'versicolor' 'virginica']).


def get_iris_target_names(iris_data):
    """
    returns iris dataset's target names.
    """
    return iris_data.target_names


"""
BOOLEAN INDEXING

Consider this target array for the iris data set:

>>> iris_data.target
array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])

The first fifty values in this array are 0, the second fifty are 1, and
the third fifty are 2.

The boolean indexing allows us to create an array of boolean values 
iris_data.target==t returns a boolean array B where B[i] == True if and
only if iris_data.target[i] == t.

Let's create a boolean index bool_inx_0 where bool_inx_0[i] == True
if and only if iris_data.target[i] == 0. In other words, this
boolean index contains indexing information for all setosas.

>>> bool_inx_0 = iris_data.target==0
>>> bool_inx_0
array([ True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False])

Let's create a boolean index bool_inx_1 where bool_inx_1[i] == True
if and only if iris_data.target[i] == 1. This boolean index
contains indexing information for versicolors.

>>> bool_inx_1 = iris_data.target==1
>>> bool_inx_1
array([False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False])

Let's create a boolean index bool_inx_2 where bool_inx_2[i] == True
if and only if iris_data.target[i] == 2. This boolean index
contains indexing information for all virginicas.

>>> bool_inx_2 = iris_data.target==2
>>> bool_inx_2
array([False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True])

How do we use boolean indices? 

You can use the boolean indices directly as you typically use numeric
array indices. For example, a[0], a[1]. You can use boolean indices
w/ numpy arrays similary to retrieve the elements for which the
corresponding cells in a boolean index are True.

>>> import numpy as np
>>> a = np.array([1, 2, 3, 4, 5])
>>> bool_inx = np.array([True, False, True, False, True])
>>> a[bool_inx]
array([1, 3, 5])

Here's how we can use bool_inx_0 to retrieve all setosas.
>>> iris_data.data[bool_inx_0]
array([[5.1, 3.5, 1.4, 0.2],
       ...,
       [5. , 3.3, 1.4, 0.2]])

Here's how we can use bool_inx_1 to retrieve all versicolors.
>>> iris_data.data[bool_inx_1]
array([[7. , 3.2, 4.7, 1.4],
       ...,
       [5.7, 2.8, 4.1, 1.3]])

Here's how we can use bool_inx_2 to retrieve all virginicas.
>>> iris_data.data[bool_inx_2]
array([[6.3, 3.3, 6. , 2.5],
       ...,
       [5.9, 3. , 5.1, 1.8]])
"""

"""
We can write a function that takes the iris_data set and
returns all examples classified setosas, verscicolors, or virginicas.
"""


def get_iris_examples_classified_as(iris_data, target_name):
    """
    takes the iris dataset (iris_data) and returns all examples whose 
    target=target_name.
    """
    assert target_name in get_iris_target_names(iris_data)
    # 1. get the names of targets
    target_names = iris_data.target_names
    # 2. get the examples
    examples = iris_data.data
    # 3. get the numerical values of targets
    target = iris_data.target
    try:
        # find the index of target_name in list of target names
        # t is 0, 1, or 2: 0 -- for setosa, 1 -- for versicolor,
        # 2 -- for virginica.
        t = target_names.tolist().index(target_name)
        assert t == 0 or t == 1 or t == 2
        # get me all target items classified as t, where
        target_examples = examples[target==t]
        return target_examples
    except Exception as e:
        print(e)


"""
We can know test the verasity of get_iris_examples_classified_as() with np.array_equal.
Since we know that the first 50 elements in iris_data.data are setosas, this
statement must be true, if get_iris_examples_classified_as() does its job:

>>> np.array_equal(iris_data.data[:50], get_iris_examples_classified_as(iris_data, 'setosa'))
True

Since we know that the second 50 elements in iris_data.data are versicolors, this
statement must be true, if get_iris_examples_classified_as() does its job:

>>> np.array_equal(iris_data.data[50:100], get_iris_examples_classified_as(iris_data, 'versicolor'))
True

Since we know that the third 50 elements in iris_data.data are virginicas, this statement
must true, if get_iris_examples_classified_as() does its job:

>>> np.array_equal(iris_data.data[100:], get_iris_examples_classified_as(iris_data, 'virginica'))
True
"""        

"""        
So, we know the target numbers:
0 - setosa
1 - versicolor
2 - virginica

We know the feature (attribute) numbers:
0 - sepal length (cm); SepLen
1 - sepal width  (cm); SepWid
2 - petal length (cm); PetLen
3 - petal width  (cm); PetWid

Let's work on the problem of getting all feature/attribute values for
a specific target. How would we get all sepal lengths of
setosas? How would we get all petal lengths of versicolors?

Let's write the function get_feat_vals_for_iris_target() that uses boolean 
indexing to answer such questions for us. Remember that 
the feat nums are:

0 - sepal length (cm)
1 - sepal width  (cm)
2 - petal length (cm)
3 - petal width  (cm)

The targets are:
0 - setosa
1 - versicolor
2 - virginica
"""


def get_feat_vals_for_iris_target(iris_data, fnum=0, tnum=0):
    """
    returns from the iris dataset iris_data a numpy array of the feature values 
    of the feature whose number is fnum (0, 1, 2, 3) for the examples whose 
    target is tnum (0, 1, 2).
    """
    assert fnum in set([0, 1, 2, 3])
    assert tnum in set([0, 1, 2])
    examples = iris_data.data
    target = iris_data.target
    feature_vals = examples[target==tnum,fnum]
    return feature_vals


"""
0 - sepal length (cm)
1 - sepal width  (cm)
2 - petal length (cm)
3 - petal width  (cm)

0 - setosa
1 - versicolor
2 - virginica
A couple of examples of get_feat_vals_for_iris_target()

1) Let's get all sepal lengths of setosas, versicolors, and virginicas:
>>> get_feat_vals_for_iris_target(iris_data, fnum=0, tnum=0)
>>> get_feat_vals_for_iris_target(iris_data, fnum=0, tnum=1)
>>> get_feat_vals_for_iris_target(iris_data, fnum=0, tnum=2)

Let's run a few unit tests to make sure that get_feat_vals_for_iris_target() returns
the right stuff:

>>> np.array_equal(iris_data.data[:,0][:50], get_feat_vals_for_iris_target(iris_data, fnum=0, tnum=0))
True
>>> np.array_equal(iris_data.data[:,0][50:100], get_feat_vals_for_iris_target(iris_data, fnum=0, tnum=1))
True
>>> np.array_equal(iris_data.data[:,0][100:], get_feat_vals_for_iris_target(iris_data, fnum=0, tnum=2))
True

2) Let's get all sepal widths of setosas, versicolors, and virginicas:
>>> get_feat_vals_for_iris_target(iris_data, fnum=1, tnum=0)
>>> get_feat_vals_for_iris_target(iris_data, fnum=1, tnum=1)
>>> get_feat_vals_for_iris_target(iris_data, fnum=1, tnum=2)

Let's make sure that the right stuff is returned:

>>> np.array_equal(iris_data.data[:,1][:50], get_feat_vals_for_iris_target(iris_data, fnum=1, tnum=0))
True
>>> np.array_equal(iris_data.data[:,1][50:100], get_feat_vals_for_iris_target(iris_data, fnum=1, tnum=1))
True
>>> np.array_equal(iris_data.data[:,1][100:], get_feat_vals_for_iris_target(iris_data, fnum=1, tnum=2))
True
"""


def get_vals_for_iris_feat(iris_data, fnum=0):
    """
    get all values for the feature whose number is fnum.
    """
    return iris_data.data[:,fnum]

# 0 - sepal length (cm)
# 1 - sepal width  (cm)
# 2 - petal length (cm)
# 3 - petal width  (cm)


def get_sorted_feat_vals_for_iris_feats(iris_data):
    """
    returns a dictionary where the names of iris dataset's features
    are mapped to their sorted values.
    """
    feat_vals = {}
    feat_vals['SepLen'] = sorted(get_vals_for_iris_feat(iris_data, fnum=0))
    feat_vals['SepWid'] = sorted(get_vals_for_iris_feat(iris_data, fnum=1))
    feat_vals['PetLen'] = sorted(get_vals_for_iris_feat(iris_data, fnum=2))
    feat_vals['PetWid'] = sorted(get_vals_for_iris_feat(iris_data, fnum=3))
    return feat_vals


if __name__ == '__main__':
    pass
