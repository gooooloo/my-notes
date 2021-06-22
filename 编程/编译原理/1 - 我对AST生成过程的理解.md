# 主题

我复习 Alex Aiken Compiler 课程中相关部分后，对于 从 token 生成 AST 部分的理解。



# Alex Aiken 课程中有什么？

- Context Free Grammars
- Derivations
- Ambiguity
- Error Handling
- Abstract Syntax Tree
- Recursive Descent Parsing
- Left Recursion
- Predictive Parsing
- First Set
- Follow Set
- LL(1) Parsing Table
- Bottom-Up Parsing
- Shift Reduce
- Handles
- Viable Prefixes
- Valid Items
- SLR parsing



# 我的理解



## 语法树和抽象语法树的区别

抽象语法树会把很多显然的东西合为一体。比如如果只有一个字节点之类的。



## 规则的定义

production



比如如果`T`有两个可能的展开：

`T=int*int`

`T=int*double`



如果你想，T 还能变成：

`T=int*E`

`E=int｜double`



# 规则的好坏

如果有歧义，就不好。比如允许这两个规则同时存在

`if A then B`

`If A then B else C`

那么就会导致这个有问题：`“If a then if b then c else d"` ---- `else d` 究竟算是那个 `if` 的呢？



解决办法

重新定义规则。比如规定`else`只能跟在最近的一个`if`

`T1: if a then T1 else B`

`T2: if a then T1｜T2`



## 怎样用规则去匹配代码？

### 办法 1：搜索每一个规则

遍历每一套可能的规则组合，依次套在代码身上。第一套成功的规则就是结果。一套规则失败了，就再看下一套。其实这就是回溯算法。



### 优化 1:

如果两套规则拥有相同的头部规则，那么就可以复用检测结果。这个体现在 ast 里就是相同的父节点。



### 优化 2:

回溯的时候，如果两个规则拥有相同的前缀，则可以复用检测结果。比如 规则 1 是  `= int*int+E`，规则 2 是 `=int*int+F` 。那么当规则 1 最终失败后，继续尝试规则 2 时， 由于 `int*int+` 这部分和规则 1 是一样的，则不用重新检查，直接复用之前的结果就可以了。这个在课程里，演化成了 left factor。



### 优化 3:

回溯的时候，同一子套规则 + 同一套字符串 ，可能会被重复检测很多遍。比如，有可能第一次匹配 T = int*int+E｜F 的时候，检测出当接下来的代码是 int*int+double* 的时候，可以匹配 T=int*int+E ，但是不匹配 T=int*int+F ，那么当下一个次遇到 T 的检测的时候，而且代码也是 int*int+double* 的时候，就可以直接采用 int*int+E ，抛弃 int*int+F 。这就是 LL(K) 算法。



### 总结

优化 1 和优化 2，本质上都是空间换时间。而且还可以在匹配开始前就算好存起来，这是因为规则也是事先定好的。



再先算的时候，有一个特殊情况，会导致麻烦：epsilon。这时候就需要 follow 集的计算。其余情况就只是 first 集的情况。



### 注意 1:

需要把规则应用到代码结尾。这意味着，要把结束符纳入规则。一个反面例子是，规则是： T11=int。T2=int+int。如果没有把结尾符号纳入规则，那么可能会发现 T1 可以。



### 注意 2:

其实是会死循环的。比如 T=Ta｜b 这种。解决办法是该描述，去掉“首递归”



## 正则表达式

仔细想想这个其实就是正则表达式。

那么就可以用 dfa 来求解。但如果从一开始为起点来构造 dfa，则图太大了。这是因为 production 太多了。所以有一个巧的办法，从每个 production 开始，而不是从字符串开始来构造 dfa。每当匹配完一个 production 时，就化简一下代码，再从头开始。由于每次都会简化至少一个 token，所以会结束。



### 优化 1:

有时既可以进入新的 production，也可以感觉下个 token 继续匹配本 production。这时候新 production 的 follow set 可以帮助剪枝：如果下个 token 不属于新 production 的 followset，则肯定不需要尝试那个新 production。

