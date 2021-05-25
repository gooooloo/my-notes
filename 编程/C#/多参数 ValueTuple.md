# 主题

已知 `ValueTuple` 的定义最多支持8个参数：`ValueTuple<T1, T2, T3, T4, T5, T6, T7, TRest>`。那么当实际使用时超过8个的时候，是怎么样的呢？比如如下代码：

``` C#
using System;

namespace ConsoleApp6
{
    class Program
    {
        static (int a1, int a2, int a3, int a4, int a5, int a6, int a7, int a8, int a9) Foo9()
        {
            return (3, 3, 3, 3, 3, 3, 3, 3, 3);
        }

        static void Main(string[] args)
        {
            var x = Foo9();
            Console.WriteLine(x.a9);
        }
    }
}
```



# 答案

在 [SharpLab](https://sharplab.io/) 上可以看到，是套娃式的展开

``` C#
namespace ConsoleApp6
{
    internal class Program
    {
        [return: TupleElementNames(new string[] {
            "a1",
            "a2",
            "a3",
            "a4",
            "a5",
            "a6",
            "a7",
            "a8",
            "a9",
            null,
            null
        })]
        private static ValueTuple<int, int, int, int, int, int, int, ValueTuple<int, int>> Foo9()
        {
            return new ValueTuple<int, int, int, int, int, int, int, ValueTuple<int, int>>(3, 3, 3, 3, 3, 3, 3, new ValueTuple<int, int>(3, 3));
        }

        private static void Main(string[] args)
        {
            Console.WriteLine(Foo9().Rest.Item2);
        }
    }
}
```



