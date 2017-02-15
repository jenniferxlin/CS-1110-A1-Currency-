#a1test.py
#Jennifer Lin (jl3263)
#September 18, 2016
#Some of these test cases were suggested by Nancy Shen (nws37).
"""Unit test for module a1

When run as a script, this module invokes several procedures that 
test the various functions in the module a1."""
import cornelltest
import a1

def testA( ):
    """Returns:'Module name is working correctly' if functions before_space
    and after_space test cases work.""" 
    #First before_space test case
    result = a1.before_space('500 Yuan')
    cornelltest.assert_equals('500', result)
    
    #First after_space test case
    result = a1.after_space('500 Yuan')
    cornelltest.assert_equals('Yuan', result)
     
    #Second before_space test case
    result = a1.before_space(' 19.2 pesos')
    cornelltest.assert_equals('19.2', result)
    
    #Second after_space test case
    result = a1.after_space(' 19.2 pesos')
    cornelltest.assert_equals('pesos', result)
    
    #Third before_space test case
    result = a1.before_space('0.73 Pounds ')
    cornelltest.assert_equals('0.73', result)
    
    #Third after_space test case
    result = a1.after_space('0.73 Pounds ')
    cornelltest.assert_equals('Pounds', result)
    
    #Fourth before_space test case
    result = a1.before_space(' 0.08 YEN ')
    cornelltest.assert_equals('0.08', result)
    
    #Fourth after_space test case
    result = a1.after_space('0.08 YEN')
    cornelltest.assert_equals('YEN', result)
    print 'Module name is working correctly'
    
    
def testB( ):
    """Returns:'Module name is working correctly' if functions get_from,
    get_to, and has_error test cases work."""
    #First get_from test case
    result = a1.get_from('{ "from":"3 United States Dollars", "to": '+ 
                         '"20.041308 Chinese Yuan", "success" : true, ' + 
                         '"error" : "" }')
    cornelltest.assert_equals('3 United States Dollars', result)
    
    #First get_to test case
    result = a1.get_to('{ "from":"3 United States Dollars", "to":"20.041308 ' + 
                       'Chinese Yuan", "success" : true, "error" : "" }')
    cornelltest.assert_equals('20.041308 Chinese Yuan', result)
    
    #Second get_from test case
    result = a1.get_from('{ "from":"30 Liberian Dollars", "to":' +
                         '"0.32876712328767 United States Dollars", ' + 
                         '"success" : true, "error" : "" }')
    cornelltest.assert_equals('30 Liberian Dollars', result)
    
    #Second get_to test case
    result = a1.get_to('{ "from":"30 Liberian Dollars", "to":' +
                       '"0.32876712328767 United States Dollars", "success" ' + 
                       ': true, "error" : "" }')
    cornelltest.assert_equals('0.32876712328767 United States Dollars', result)
    
    #First has_error test case
    result = a1.has_error('{ "from":"", "to":"", "success" : false, "error" ' + 
                          ': "Exchange currency code is invalid." }')
    cornelltest.assert_equals(True, result)
    
    #Second has_error test case
    result = a1.has_error('{ "from":"", "to":"", "success" : false, "error" ' + 
                          ': "Currency amount is invalid." }')
    cornelltest.assert_equals(True,result)
    
    #Third has_error test case
    result = a1.has_error('{ "from":"", "to":"", "success" : false, "error" ' + 
                          ': "Source currency code is invalid." }')
    cornelltest.assert_equals(True, result)
    
    print 'Module name is working correctly'


def testC():
    """Returns:'Module name is working correctly' if function currency_response
    test cases work."""
    #First test case
    result = a1.currency_response('USD','EUR', 2.5)
    cornelltest.assert_equals('{ "from" : "2.5 United States Dollars", "to" ' +
                              ': "2.24075 Euros", "success" : true, "error" ' +
                              ': "" }', result)
    
    #Second test case
    result = a1.currency_response('BBD','USD', 3000)
    cornelltest.assert_equals('{ "from" : "3000 Barbadian Dollars", "to" : ' +
                              '"1500 United States Dollars", "success" : ' +
                              'true, "error" : "" }',result)
    

def testD():
    """Returns:'Module name is working correctly' if functions iscurrency and
    exchange test cases work."""
    #First is_currency test case
    result = a1.iscurrency('USD')
    cornelltest.assert_equals(True, result)
    
    #Second is_currency test case suggested by Consultant Nancy Shen (nws37)
    result = a1.iscurrency('hi')
    cornelltest.assert_equals(False,result)
    #End Nancy's suggestion
    
    #Third is_currency test case
    result = a1.iscurrency('usd')
    cornelltest.assert_equals(False,result)
    
    #First exchange test case
    result = a1.exchange('USD','EUR', 2.5)
    cornelltest.assert_equals(2.24075,result)
    
    #Second test case
    result = a1.exchange('BBD','USD', 3000)
    cornelltest.assert_equals(1500,result)
    
testA()
testB()
testC()
testD()
print "Module a1 passed all tests"