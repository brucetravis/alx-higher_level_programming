#!/usr/bin/python3
import hidden_4

module_attributes = dir(hidden_4)


for attribute in sorted(module_attributes):
if not attribute.startswith("__"):
print(attribute)
