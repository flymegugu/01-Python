# 此方式用于发布一个包，让大家都可以用
from distutils.core import setup
setup(name="BG", version="1.0", description="BG modules",
      author="BG", py_modules=["TestMsg.recvmsg"])
