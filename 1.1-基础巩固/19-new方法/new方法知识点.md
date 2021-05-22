1. 当你创建一个对象，那么这个对象会自动执行 init()方法，而这个对象是由 new()方法来创建的
2. 构造方法包含创建和初始化，但是 python 中有两种，首先 new 然后 init 这是两个独立的

#### 创建对象后会调用

```
def __init__(self):
    pass
```

#### 删除时候会调用

```
def __del__(self):
    pass
```

#### 当调用 print 打印对象 return 一个结果的时候

```
def __str__(self):
    return "对象描述信息"
```

#### 对类实力化的时候

```
def __new__(cls):
    pass
``·
```
