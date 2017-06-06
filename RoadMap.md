This project is done (see README.rst). No more changes will be made.


Functional improvements
=======================

- Allow other arguments checking than simple constants
- Derive a class from unittest.TestCase that provides a mock factory and auto-tearDowns the created mocks
- Decide if passing a mock to another mock's contructor is a good way to link them <- No! It's deinitely not intuitive. Let's create an explicit factory for mocks.

Technical improvements
======================

- Allow positional arguments (*args) to be passed by name (**kwds)
- Check that expected properties do not allow call and that expected method calls require call
- Be thread safe



mock2 = mock.expect.foo.and_returnMock()  # foo returns the mock2.object
