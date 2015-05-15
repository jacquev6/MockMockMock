# coding: utf8

# Copyright 2013-2015 Vincent Jacques <vincent@vincent-jacques.net>

import inspect
import unittest

from .expectation_grouping import OrderedExpectationGroup, UnorderedExpectationGroup, AtomicExpectationGroup, OptionalExpectationGroup, AlternativeExpectationGroup, RepeatedExpectationGroup
from .expectation_handling import ExpectationHandler
from .mock import Mock

# @todo When an arguments validator fails, include description of failure in exception (see PyGithub's replay mode: comparers have to log by themselves to make it practical)


class TestCase(unittest.TestCase):
    """
    TestCase()

    A convenience base class for test cases needing a single mock :class:`.Engine`.
    It inherits from :class:`unittest.TestCase` and sets-up and tears-down one for you.
    """

    @property
    def mocks(self):
        """
        The mock :class:`.Engine`.
        """
        return self.__mocks

    def setUp(self):
        """
        Do not forget to call the base version if you override it.
        """
        super(TestCase, self).setUp()
        self.__mocks = Engine()

    def tearDown(self):
        """
        Do not forget to call the base version if you override it.
        """
        self.__mocks.tearDown()
        super(TestCase, self).tearDown()


class MockException(Exception):
    """
    @todoc
    """


class Engine:
    """
    @todoc
    """
    def __init__(self):
        self.__handler = ExpectationHandler(OrderedExpectationGroup())
        self.__replaced = []

    def create(self, name):
        """
        @todoc
        """
        return Mock(name, self.__handler)

    def replace(self, name):  # @todo Add optional param to pass the mock in (to allow replacing several things by same mock)
        """
        @todoc
        """
        # @todo Put that in a Replacer class.
        container, attribute = self.__findByName(name)
        self.__replaced.append((container, attribute, getattr(container, attribute)))
        m = self.create(name)
        setattr(container, attribute, m.object)
        return m

    @staticmethod
    def __findByName(name):
        names = name.split(".")
        attribute = names[-1]
        current = inspect.currentframe()
        try:
            frame = current.f_back.f_back
            symbols = dict(frame.f_globals)
            symbols.update(frame.f_locals)
            container = symbols[names[0]]
        finally:
            del current
        for name in names[1:-1]:
            container = getattr(container, name)
        return container, attribute

    def tearDown(self):
        """
        @todoc
        """
        for container, attribute, value in self.__replaced:
            setattr(container, attribute, value)
        self.__handler.tearDown()

    @property
    def unordered(self):
        """
        @todoc with link to user guide (Expectations grouping)
        """
        return self.__handler.pushGroup(UnorderedExpectationGroup())

    @property
    def ordered(self):
        """
        @todoc with link to user guide (Expectations grouping)
        """
        return self.__handler.pushGroup(OrderedExpectationGroup())

    @property
    def atomic(self):
        """
        @todoc with link to user guide (Expectations grouping)
        """
        return self.__handler.pushGroup(AtomicExpectationGroup())

    @property
    def optional(self):
        """
        @todoc with link to user guide (Expectations grouping)
        """
        return self.__handler.pushGroup(OptionalExpectationGroup())

    @property
    def alternative(self):
        """
        @todoc with link to user guide (Expectations grouping)
        """
        return self.__handler.pushGroup(AlternativeExpectationGroup())

    @property
    def repeated(self):
        """
        @todoc with link to user guide (Expectations grouping)
        """
        return self.__handler.pushGroup(RepeatedExpectationGroup())

    @property
    def records(self):
        """
        @todoc with link to user guide (Recording)
        """
        return self.__handler.getRecordedCalls()
