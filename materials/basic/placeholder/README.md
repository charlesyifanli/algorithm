## Placeholder

Using the .format() method:

```
name = "Alice"
age = 30
formatted_string = "My name is {}, and I am {} years old.".format(name, age)
```

Using % formatting:

```
name = "Bob"
age = 25
formatted_string = "My name is %s, and I am %d years old." % (name, age)
```

Using f-strings:

```
name = "Charlie"
age = 20
formatted_string = f"My name is {name}, and I am {age} years old."
```

Formatting numbers:

```
value = 3.14159
formatted_float = "{:.2f}".format(value)  # 保留两位小数
formatted_int = "{:03d}".format(7)  # 整数填充成3位，不足时在前面补0
```

Controlling alignment and padding:

```
number = 42
formatted_left = "{:<10}".format(number)  # 左对齐填充空格
formatted_right = "{:>10}".format(number)  # 右对齐填充空格
formatted_center = "{:^10}".format(number)  # 居中填充空格
```

Time formatting:

```
import datetime
now = datetime.datetime.now()
formatted_date = "{:%Y-%m-%d %H:%M:%S}".format(now)  # 格式化当前时间
print(formatted_date)
```

Handle Parameters
```
demo = 1
demo2 = 2

str_ = 'test:{1:!<20.3f}\n{0:?>20.2f}'.format(demo, demo2)

print(str_)
```