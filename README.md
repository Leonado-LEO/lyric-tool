# 双语歌词时序调整

## 起因与适用症
- 我曾经买过一个廉价多功能MP3播放器（~~能在学校看小说摸鱼那种~~），然而带有翻译的歌词不能正确显示，**同一句的英文和中文翻译不能同时出现**。所以我编写了这个批量处理程序来调整歌词。  

- 本工具**本质上**是识别每一句对应的英文和中文翻译，并**按需调整时序码**。具体如下：  

----

如果你打开一个普通的`.lrc歌词文件`，你就会发现：

每一句的**英文**和**中文翻译**的**时序一致**，并且它们**被分开了**，例如：

`[00:00.000]` 作曲 : Alphonso Henderson/Ed Sheeran/Jason Epperson/Andreas Carlsson/Steve Mac/Julia Michaels/Jacob Schulze/Tracy Marrow/George Clinton Jr/Benjamin Levin  <---**歌曲信息**  
`[00:00.004]`作词 : Alphonso Henderson/Ed Sheeran/Jason Epperson/Andreas Carlsson/Steve Mac/Julia Michaels/Jacob Schulze/Tracy Marrow/George Clinton Jr/Benjamin Levin  <---**歌曲信息**  

`[00:00.51]`I will always remember the day you kissed my lips    <---**第1句原文**  
`[00:05.64]`Light as a feather    <---**第2句原文**  
`[00:08.06]`And it went just like this    <---**第3句原文**  

*此处省略n行...*

`[by:Cepohalm]`  
`[00:00.51]`我永远不会忘记你我相吻的那天    <---**第1句翻译**  
`[00:05.64]`那吻很轻 很柔    <---**第2句翻译**  
`[00:08.06]`爱意油然而生    <---**第3句翻译**  

*此处省略n行...*

在普通的播放软件里，会**自动识别双语**，并同时显示。  

但是在这种类似的**廉价MP3**中，**显然没有**这方面的识别，只是**单纯的按照时序显示歌词**，就会导致中文的翻译不显示。    

本工具的原理就是**将中文翻译的时序**调整至**下一句英文歌词的时序**，并将它们**连接起来**，例如：  

`[00:00.000]` 作曲 : Alphonso Henderson/Ed Sheeran/Jason Epperson/Andreas Carlsson/Steve Mac/Julia Michaels/Jacob Schulze/Tracy Marrow/George Clinton Jr/Benjamin Levin  <---**歌曲信息不变**  
`[00:00.004]`作词 : Alphonso Henderson/Ed Sheeran/Jason Epperson/Andreas Carlsson/Steve Mac/Julia Michaels/Jacob Schulze/Tracy Marrow/George Clinton Jr/Benjamin Levin  <---**歌曲信息不变**  

`[00:00.51]`I will always remember the day you kissed my lips   <---**第1句原文**  
`[00:05.64]`我永远不会忘记你我相吻的那天    <---**第1句翻译，且时序推后**  

`[00:05.64]`Light as a feather    <---**第2句原文**  
`[00:08.06]`那吻很轻 很柔    <---**第2句翻译，且时序推后**  

*此处省略n行...*

这样，MP3会将中文翻译认为是**下一句歌词**，从而显示在第二行，变相实现了**同时显示英文和中文翻译**。 

----


## 程序优点

1. 自动识别歌词部分，不改变开头的歌曲信息部分，不修改没有中文翻译的歌词。
2. 修改过的歌词文件格式统一。
3. 支持批量处理。


## 使用方法

1. 到**release**中下载最新版本的工具。
2. 双击运行，按提示进行操作。

**注意：**使用前务必**备份原文件**！后续会加入文件保护机制。（见To Do List）



## To Do List
> 优先级从上至下


- [ ] 询问用户是否保留原文件或直接覆盖
- [ ] 判断文件是否为双语歌词文件，非指定格式不做修改
- [ ] debug模式
