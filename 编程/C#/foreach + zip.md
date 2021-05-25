# 问题

希望对两个数组配对遍历



# 解决

            foreach(var xx in mylist1.Zip(mylist2, (x,y) => new { Elem1 = x, Elem2 = y}))
            {
                Console.WriteLine(xx.Elem1);
                Console.WriteLine(xx.Elem2);
            }

