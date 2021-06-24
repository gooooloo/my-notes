# 问题

`Foreach` 的时候希望带上 `index`

# 解决

``` C#
            foreach(var xx in mylist.Select((x,i) => new { Value = x, Index = i }))
            {
                Console.WriteLine(xx.Value);
                Console.WriteLine(xx.Index);
            }
```

