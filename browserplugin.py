#!/usr/bin/env python

import os
from nose.plugins import Plugin


class BrowserOutput(Plugin):
    name = "browserplugin"
    score = 200

    def setOutputStream(self, stream):
        self.stream = stream
        return None

    def describeTest(self, test):
        browser = os.getenv("SL_BROWSER")
        b_version = os.getenv("SL_BROWSER_VERSION")
        if b_version.strip() == "":
            specific = browser
        else:
            specific = '-'.join([browser, b_version.strip()])
        names = str(test).split()
        func_name = names[0]
        class_module = names[1].strip("()").split('.')
        if len(class_module) < 4:
            return ' '.join(class_module)
        test_name = class_module[2] + ".py:" + class_module[3] + "." + func_name
        return ' '.join([test_name, specific])

    def addSuccess(self, test):
        out = "\n" + self.describeTest(test) + " SUCCESS"
        self.stream.writeln(out)

    def formatFailure(self, test, err):
        out = "\n" + self.describeTest(test) + " FAILURE"
        self.stream.writeln(out)
        return err

    def formatError(self, test, err):
        out = "\n" + self.describeTest(test) + " EXCEPTION"
        self.stream.writeln(out)
        return err
