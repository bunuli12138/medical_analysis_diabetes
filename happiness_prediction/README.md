## 简介
对于天池“挖掘幸福度”比赛的操作仓库  

## 目录
[Data](Data)： 数据集  
[Operate](Operate)： 操作文件  
[Result](Result)： 结果文件夹（可提交）  

## 数据集

| 表格 | 描述 |  
| --- | --- |  
| index | 每个变量对应的问卷题目，以及变量取值的含义 |  
| survey | 数据源的原版问卷 |   
| *_complete | 变量完整版数据 |   
| *_abbr | 变量精简版数据 |  

提交格式：
| id | happiness |  
| --- | --- |  

分数公式：$score = \frac{1}{n}\sum_{1}^{n}(y_i-y^*)^2$


## 命名规则
X/Y/train/test_Class_Description 或 Class_Description   
含义：     
- X：特征数据集，Y：标签，train：训练集，test：测试集  
- Class： 变量名称， Description：变量作用或来源简介  
- 逐步改变的变量，则后加 _Feature， 表示当前改变的来源特征  
- 以 _ 开头的变量表示不可变     
- 方法内的变量描述为简写首字母   
