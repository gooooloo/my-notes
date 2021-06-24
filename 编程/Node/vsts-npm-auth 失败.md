# 时间

2021-02-04



# 问题

``` console
> vsts-npm-auth -config .npmrc
 
vsts-npm-auth v0.41.0.0
-----------------------
The input is not a valid Base-64 string as it contains a non-base 64 character, more than two padding characters, or an illegal character among the padding characters.
```



# 答案

加上 -F 就好了

`vsts-npm-auth -config .npmrc -F`

[.npmrc - vsts-npm-auth exists with code 1, the input is not a valid Base-64 string - Stack Overflow](https://stackoverflow.com/questions/63148661/vsts-npm-auth-exists-with-code-1-the-input-is-not-a-valid-base-64-string)

