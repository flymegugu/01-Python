class ShortInputException(Exception):
    def __init__(self, length, atleast):
        self.length = length
        self.atleast = atleast


def main():
    try:
        s = input('请输入--->:')
        if len(s) < 3:
            # 当小于3，那么久传递给ShortInputException自定义异常类，产生一个异常对象，并传入参数（用于将信息给result）
            raise ShortInputException(len(s), 3)
        #
    except ShortInputException as result:
        print('ShortInputException:输入的长度是%d,长度至少是%d' %
              (result.length, result.atleast))


main()
