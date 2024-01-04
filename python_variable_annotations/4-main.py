#!/usr/bin/env python3

a = __import__('4-define_variables').a
pi = __import__('4-define_variables').pi
i_understand_annotations = __import__('4-define_variables').i_understand_annotations
school = __import__('4-define_variables').school

print("a is a {} with a value of {}".format(a, type(a)))
print("pi is a {} with a value of {}".format(pi, type(pi)))
print("i_understand_annotations is a {} with a value of {}".format(i_understand_annotations, type(i_understand_annotations)))
print("school is a {} with a value of {}".format(school, type(school)))
