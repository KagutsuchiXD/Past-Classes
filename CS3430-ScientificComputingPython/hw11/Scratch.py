import csv
import math
import copy

##################################################
# module: bin_id3.py
# description: Binary ID3 decision tree learning
# Connor Osborne
# A01880782
# bugs to vladimir dot kulyukin at usu dot edu
###################################################

# Positive and Negative Constant labels; don't change
# these.
PLUS = 'Yes'
MINUS = 'No'


class id3_node(object):

    def __init__(self, lbl):
        self.__label = lbl
        self.__children = {}

    def set_label(self, lbl):
        self.__label = lbl

    def add_child(self, attrib_val, node):
        self.__children[attrib_val] = node

    def get_label(self):
        return self.__label

    def get_children(self):
        return self.__children

    def get_child(self, attrib_val):
        assert attrib_val in self.__children
        return self.__children[attrib_val]


class bin_id3(object):

    @staticmethod
    def get_attrib_values(a, kvt):
        """
        Looks up values of attribute a in key-value table.
        """
        return kvt[a]

    @staticmethod
    def get_example_attrib_val(example, attrib):
        """
        Get the value of attribute attrib in example.
        """
        assert attrib in example
        print(example)
        print(attrib)
        return example[attrib]

    @staticmethod
    def parse_csv_file_into_examples(csv_fp):
        """
        Takes a csv file specified by the path csv_fp and
        converts it into an array of examples, each of which
        is a dictionary of key-value pairs where keys are
        column names and the values are column attributes.
        """
        examples = []
        with open(csv_fp) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            key_names = None
            for row in csv_reader:
                if len(row) == 0:
                    continue
                if line_count == 0:
                    key_names = row
                    for i in range(len(key_names)):
                        # strip whitespace on both ends.
                        row[i] = row[i].strip()
                        line_count += 1
                else:
                    ex = {}
                    for i, k in enumerate(key_names):
                        # strip white spaces on both ends.
                        ex[k] = row[i].strip()
                    examples.append(ex)
            return examples, key_names

    @staticmethod
    def construct_attrib_values_from_examples(examples, attributes):
        """
        Constructs a dictionary from a list of examples where each attribute
        is mapped to a list of all its possible values in examples.
        """
        avt = {}
        for a in attributes:
            if not a in avt:
                avt[a] = set()
            for ex in examples:
                if a in ex:
                    if not ex[a] in avt[a]:
                        avt[a].add(ex[a])
                else:
                    avt[a].add(None)
        return avt

    @staticmethod
    def find_examples_given_attrib_val(examples, attrib, val):
        """
        Finds all examples in such that attrib = val.
        """
        rslt = []
        # print('Looking for examples where {}={}'.format(attrib, val))
        for ex in examples:
            if attrib in ex:
                if ex[attrib] == val:
                    rslt.append(ex)
        return rslt

    @staticmethod
    def find_most_common_attrib_val(examples, attrib, avt):
        """
        Finds the most common value of attribute attrib in examples.
        """
        attrib_vals = bin_id3.get_attrib_values(attrib, avt)
        val_counts = {}
        for av in attrib_vals:
            SV = bin_id3.find_examples_given_attrib_val(examples, attrib, av)
            val_counts[av] = len(SV)
        max_cnt = 0
        max_val = None
        # print('val_counts = {}'.format(val_counts))
        for val, cnt in val_counts.items():
            if cnt > max_cnt:
                max_cnt = cnt
                max_val = val
        assert max_val is not None
        return max_val, max_cnt

    @staticmethod
    def get_non_target_attributes(target_attrib, attribs):
        """
        Returns a comma separated string of all attributes in the list attribs that
        that are not equal to target_attrib;
        - target_attrib is a string.
        - attribs is a list of strings.
        """
        return ', '.join([a for a in attribs if a != target_attrib])

    @staticmethod
    def display_info_gains(gains):
        """
        Displays a dictionary of information gains in the format attribute: gain.
        """
        print('Information gains are as follows:')
        for attrib, gain in gains.items():
            print('\t{}: {}'.format(attrib, gain))

    @staticmethod
    def display_id3_node(node, tabs):
        """
        Displays the subtree rooted at a node.
        """
        print(tabs + '{}'.format(node.get_label()))
        children = node.get_children()
        for v, n in children.items():
            print(tabs + '\t{}'.format(v))
            bin_id3.display_id3_node(n, tabs + '\t\t')

    # HW10
    @staticmethod
    def proportion(examples, attrib, val):
        """
        Computes the proportion of examples whose attribute attrib has the value val.
        """
        denom = len(examples)
        if denom == 0:
            return 0
        attrib_in_examples = bin_id3.find_examples_given_attrib_val(examples, attrib, val)
        numer = len(attrib_in_examples)
        propor = numer / denom
        return propor

    # HW10
    @staticmethod
    def entropy(examples, attrib, avt):
        """
        Computes entropy of examples with respect of attribute attrib.
        avt is the attribute value table computed by construct_attrib_values_from_examples().
        """
        values = avt[attrib]
        return sum(bin_id3.entropy_sections(examples, attrib, pi) for pi in values)

    @staticmethod
    def entropy_sections(examples, attrib, p):
        propor = bin_id3.proportion(examples, attrib, p)
        if propor == 0:
            return 0
        else:
            return -propor * math.log(propor, 2)

    # HW10
    @staticmethod
    def gain(examples, target_attrib, attrib, avt):
        """
        Computes gain of the attribute attrib in examples.
        """
        Hs = bin_id3.entropy(examples, target_attrib, avt)
        values = avt[attrib]
        for v in values:
            cp = bin_id3.proportion(examples, attrib, v)
            exv = bin_id3.find_examples_given_attrib_val(examples, attrib, v)
            hsv = bin_id3.entropy(exv, target_attrib, avt)
            Hs -= (cp * hsv)
        return Hs

    # HW10
    @staticmethod
    def find_best_attribute(examples, target_attrib, attribs, avt):
        """
        Finds the attribute in attribs with the highest information gain.
        This method returns three values: best attribute, its gain, and
        a dictionary that maps each attribute to its gain.
        """
        # print('attribs')
        # print(attribs)
        # print('target_attrib')
        # print(target_attrib)
        gains = {}

        for a in attribs:
            if a == target_attrib:
                continue
            else:
                gains[a] = bin_id3.gain(examples, target_attrib, a, avt)
        bg = -1.0
        ba = None
        for a, g in gains.items():
            if g > bg:
                bg = g
                ba = a
        assert ba is not None
        return ba, bg, gains

    # HW10
    @staticmethod
    def fit(examples, target_attrib, attribs, avt, dbg):
        """
        Returns a decision tree from examples given target_attribute target_attrib,
        attributes attribs, and attribute-value table.
        - examples is a list of examples;
        - target_attrib is a string (e.g., 'PlayTennis')
        - attribs is a list of attributes (strings)
        - avt is a dictionary constructed by construct_attrib_values_from_examples()
        - dbg is a debug flag True/False. When it is true, then things should
          be printed out as the algorithm computes the decision tree. For example,
          in my implementation I have things like
          if len(SV) == len(examples):
            ## if all examples are positive, then return the root node whose label is PLUS.
            if dbg == True:
                print('All examples positive...')
                print('Setting label of root to {}'.format(PLUS))
            root.set_label(PLUS)
            return root
        """
        global PLUS
        global MINUS
        # 1
        root = id3_node('root')
        # 2
        psv = bin_id3.find_examples_given_attrib_val(examples, target_attrib, PLUS)
        # 3
        if len(psv) == len(examples):
            root.set_label(PLUS)
            return root
        # 4
        nsv = bin_id3.find_examples_given_attrib_val(examples, target_attrib, MINUS)
        # 5
        if len(nsv) == len(examples):
            root.set_label(MINUS)
            return root
        # 6
        if len(attribs) == 0:
            most_common = bin_id3.find_most_common_attrib_val(examples, target_attrib, avt)
            root.set_label(most_common)
            return root
        # 7
        best_attrib, best_gain, table = bin_id3.find_best_attribute(examples, target_attrib, attribs, avt)
        root.set_label(best_attrib)
        values = avt[best_attrib]
        for bav in values:
            new_examples = bin_id3.find_examples_given_attrib_val(examples, best_attrib, bav)
            if len(new_examples) == 0:
                label = bin_id3.find_most_common_attrib_val(examples, target_attrib, avt)
                child = id3_node(label)
                root.add_child(bav, child)
            else:
                attribs_copy = copy.copy(attribs)
                attribs_copy.remove(best_attrib)
                child = bin_id3.fit(new_examples, target_attrib, attribs_copy, avt, dbg)
                root.add_child(bav, child)
        return root

    # HW10
    @staticmethod
    def predict(root, example):
        print('example')
        print(example)
        """
        Classifies an example given a decision tree whose root is root.
        """
        global PLUS
        global MINUS
        if root.get_label() == PLUS:
            return PLUS
        if root.get_label() == MINUS:
            return MINUS
        rat = root.get_label()
        # print('rat')
        # print(rat)
        rav = bin_id3.get_example_attrib_val(example, rat)
        # print('Curent Tree:')
        # bin_id3.display_id3_node(root, '')
        # print('RAV:')
        # print(rav)
        ch = root.get_child(rav)
        return bin_id3.predict(ch, example)