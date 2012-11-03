from _Details.Mock import Mock
from _Details.ExpectationGrouping import OrderedExpectationGroup, UnorderedExpectationGroup, AtomicExpectationGroup, OptionalExpectationGroup, AlternativeExpectationGroup, RepeatedExpectationGroup
from _Details.ExpectationHandler import ExpectationHandler

class Engine:
    def __init__( self ):
        self.__handler = ExpectationHandler( OrderedExpectationGroup() )

    def create( self, name ):
        return Mock( name, self.__handler )

    def tearDown( self ):
        self.__handler.tearDown()

    @property
    def unordered( self ):
        return self.__handler.pushGroup( UnorderedExpectationGroup() )

    @property
    def ordered( self ):
        return self.__handler.pushGroup( OrderedExpectationGroup() )

    @property
    def atomic( self ):
        return self.__handler.pushGroup( AtomicExpectationGroup() )

    @property
    def optional( self ):
        return self.__handler.pushGroup( OptionalExpectationGroup() )

    @property
    def alternative( self ):
        return self.__handler.pushGroup( AlternativeExpectationGroup() )

    @property
    def repeated( self ):
        return self.__handler.pushGroup( RepeatedExpectationGroup() )
