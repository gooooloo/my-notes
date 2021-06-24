# 时间

2020-12-25



# 链接

[Configure schedules to run pipelines - Azure Pipelines | Microsoft Docs](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/scheduled-triggers?view=azure-devops&tabs=yaml#supported-cron-syntax)



# 基本内容

```
mm HH DD MM DW
 \  \  \  \  \__ Days of week // 0 - 6 (从周日开始), 英文名全名或前3个字母
  \  \  \  \____ Months       // 1 - 12, 英文名全名或前3个字母
   \  \  \______ Days         // 1 - 31
    \  \________ Hours        // 0 - 23
     \__________ Minutes      // 0 - 59
```

| Format          | Example          | Description                                                  |
| :-------------- | :--------------- | :----------------------------------------------------------- |
| Wildcard        | `*`              | Matches all values for this field                            |
| Single value    | `5`              | Specifies a single value for this field                      |
| Comma delimited | `3,5,6`          | Specifies multiple values for this field. Multiple formats can be combined, like `1,3-6` |
| Ranges          | `1-3`            | The inclusive range of values for this field                 |
| Intervals       | `*/4` or `1-5/2` | Intervals to match for this field, such as every 4th value or the range 1-5 with a step interval of 2 |