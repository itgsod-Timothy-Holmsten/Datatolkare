#encoding: utf-8

from nose.tools import assert_equal
from nose.tools import assert_is_instance
from nose.tools import assert_raises
from StringIO import StringIO

import sys
##sys.path.append('..')

from lib.parser import main


def test_main_prints_the_day_of_the_biggest_variation():
    saved_stdout = sys.stdout
    out = StringIO()
    sys.stdout = out
    main('test/test.dat')
    output = out.getvalue().strip()
    assert_equal(output, "Day 2 had the biggest variation (26.0 degrees)")
    sys.stdout = saved_stdout


