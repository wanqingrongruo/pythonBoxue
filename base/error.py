
# 异常类
# Exception AttributeError IndexError KeyError NameError SyntaxError TypeError ValueError ZeroDivisionError 自定义

try:
    #3/0
    fn()
except ZeroDivisionError:
    print("Divide by zero")
except NameError:
    print("Invide name")
except:
    print("Default handler")
else:
    print("else的场景???")
finally:
    print("公共处理")  # 总会执行
