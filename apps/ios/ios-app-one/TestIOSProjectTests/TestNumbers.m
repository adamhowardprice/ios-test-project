#import <XCTest/XCTest.h>

@interface TestNumbers : XCTestCase

@end

@implementation TestNumbers

- (void)setUp
{
    
}

- (void)tearDown
{
    
}

- (void)testOne
{
    NSAssert(1==1, @"1 is one");
}

- (void)testTwo
{
    NSAssert(2==2, @"2 is two");
}

- (void)testThree
{
    NSAssert(3==3, @"3 is three");
}

- (void)testFour
{
    NSAssert(4==4, @"4 is four");
}

- (void)testFive
{
    NSAssert(5==5, @"5 is five");
}

- (void)testSix
{
    NSAssert(6==6, @"6 is six");
}

- (void)testSeven
{
    NSAssert(7==7, @"7 is seven");
}

- (void)testEight
{
    NSAssert(8==8, @"8 is eight");
}

- (void)testNine
{
    NSAssert(9==9, @"9 is nine");
}

- (void)testTen
{
    NSAssert(10==10, @"10 is ten");
}

@end
