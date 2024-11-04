**1. 我们准备的单元测试类（MyGreeterTest）是否存在问题?**<br/>
* 是

**2.test_greeting 测试方法有如下问题**
* self.assertTrue(len(self._my_greeter.greeting())>0) 的入参中错误的使用了len方法。对于assertTrue断言方法，实际用于验证给定的表达式是否为True，而len方法的结果是数字
* 需要测试的方法MyGreeter -> greeting()运行后的返回结果是字符串，应该使用assertEqual断言方法更为合适
* 一共3种结果，并且运行期间，是动态时间作为输出结果的判断依据，需要有3个测试用例才能满足不同情况