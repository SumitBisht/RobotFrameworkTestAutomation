#!/usr/bin/env python

import os
import sys

class ExampleRemoteLibrary:
  def strings_should_be_equal(self, str1, str2):
    print "Comparing '%s' to '%s'" % (str1, str2)
    if str1 != str2:
      raise AssertionError("Given strings are not equal")
    else:
      return "Given strings are equal"


if __name__ == '__main__':
  from robotremoteserver import RobotRemoteServer
  RobotRemoteServer(ExampleRemoteLibrary(), *sys.argv[1:])
