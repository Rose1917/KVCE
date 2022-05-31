# Kernel Variable Code Exactor(KVCE) 

#### ������快速跳转

- ������[最新进展(点我老师)](#531)
- ������[任务描述](#1-任务描述)
- ������[最终产物](#2-最终产物)

#### 1. 任务描述

* 主线任务：编写一个脚本，该脚本能够：
  1. 根据任一内核源代码（任务以内核`5.15.9`为例），得到所有的内核配置项。
  2. 对于任意一个配置项，能够定位到它所对应和影响的文件、文件中的代码片段
* 支线任务：
  1. 根据任一内核源代码的补丁，能够定位到当前的补丁对哪一个配置项有影响

#### 2. 最终产物

最终的项目交付，是以一个`Repo`的形式，最终的`Repo`中应该包含如下的内容：

* 任务描述中的脚本文件

* 示例内核源代码（以内核`5.15.9`为例）

* 输出的Json文件：

  ```json
  config_name:{
      release_time: XXXX-XX-XX
      file_name1:{
          func_name1: 
     {
      start_line,
      end_line
     }
          func_name2:
     {
      start_line,
      end_line
     }  
          ....
          func_nameN: 
     {
      start_line,
      end_line
     }
      } 
  
      ...
  
      file_nameN:{
          func_name1:    
     {
      start_line,
      end_line
     }
          func_name2: 
     {
      start_line,
      end_line
     }
          ....
          func_nameN:    
     {
      start_line,
      end_line
     }
      }  
  }   
  ```

  

* 针对git 补丁的json :

  ```json
  config_name:{
      git_id1:{
          op_status:XXX  // create, update, del 
          op_time: XXXX-XX-XX
          file_name1:{
              func_name1: {add:xx,del:xx}
              func_name2: {add:xx,del:xx}
              ....
              func_nameN: {add:xx,del:xx}
          }  
             
          ....
          
          file_nameN:{
              func_name1: {add:xx,del:xx}
              func_name2: {add:xx,del:xx}
              ....
              func_nameN: {add:xx,del:xx}
          }     
      }
  
      ...
  
      git_id2:{
          op_status:XXX  // add, update, del 
          op_time: XXXX-XX-XX
          file_name1:{
              func_name1: {add:xx,del:xx}
              func_name2: {add:xx,del:xx}
              ....
              func_nameN: {add:xx,del:xx}
          }  
             
          ....
          
          file_nameN:{
              func_name1: {add:xx,del:xx}
              func_name2: {add:xx,del:xx}
              ....
              func_nameN: {add:xx,del:xx}
          }     
      } 
  }
  ```

  

### Appendix A: Diary

---

#### **5.30**

**工作进展**

今天主要是明确了任务目的做了一些准备的工作。

* 明确了任务和最终的提交物：
* 基础的工作：
  * 新建了一个`Repo`，后续代码和日记（每日工作进展）会在上面更新。网站网址为：[我的Github该项目主页](https://github.com/Rose1917/KVCE)
  * 能够提取出内核中所有配置变量的代码

* 思路方面：
  * 一个思路是暴力搜，对于每一个配置变量，直接暴力在源码中搜索出现的宏定义。但是这种方法比较暴力，更加依赖于指定的规则，而且感觉效率不会太高。
  * 另外一个思路，由于这些变量应该是都当作宏来处理，应该是在编译的预处理阶段来处理。能否在编译的预处理阶段，对变量和代码进行提取。

**明天计划**

对第一个思路先手动测试一下，看看效果。第二个思路在网上再查查资料。另外是，想到Github上看看有没有好的代码静态分析工具，或者甚至是内核代码的静态分析工具。



---

#### 5.31

**工作进展**

今天主要是根据侯老师的意见，修改了系统的版本（已经上传至`Github`)，**修改**了本文档的**《任务描述》**和**《最终提交物》**部分。以及根据变量名溯源到对应的子模块的`KgConfig`文件，从而定位到具体的子文件夹。具体的内容描述如下：

* 根据老师的意见修改的内容如下：
  * 将系统版本从之前我自己用的`5.15.9`修改至`5.17.6`, 系统文件来自于[微软镜像站](https://mirrors.edge.kernel.org/pub/linux/kernel/v5.x/)。
  * 修改了最终[最终交付文件](# 2.-最终提交物)

* 生成`5.17.6`版本内核的变量列表，详见项目根目录下的`config_list_5_17_6.txt`，作为一个中间文件，方便以后使用。

* 暴力搜索和优化

  * 配置项的文件定位：今天试图尝试第一种方法，即直接在源代码中进行检索对应的配置项。大致步骤如下：

    ```bash
    make clean # 清除二进制文件，防止grep对二进制文件进行检索
    grep -r CONFIG_XXX linux5.17.6 # 直接在内核源码中进行检索
    ```

    因为内核代码特别多，所以如果一个一个这么检索，速度会非常的慢。

    由于我之前在做内核分类的时候，给大家做过一个内核的树状图，所以可以定位到每一个配置变量的层级结构，可以利用这个层级信息，只在部分子文件夹中进行检索。下面是一个例子。

  * 实例：

    直接对变量`CONFIG_MEMTEST`进行搜索

    ```bash
    grep -r "CONFIG_MEMTEST" .
    ```

    结果如下：

    ```bash
    ./arch/arm/configs/mps2_defconfig:CONFIG_MEMTEST=y
    ./arch/arm64/configs/defconfig:CONFIG_MEMTEST=y
    ./arch/riscv/configs/defconfig:CONFIG_MEMTEST=y
    ./arch/riscv/configs/rv32_defconfig:CONFIG_MEMTEST=y
    ./mm/Makefile:obj-$(CONFIG_MEMTEST)		+= memtest.o
    ./include/linux/memblock.h:#ifdef CONFIG_MEMTEST
    ```

    其中主要出现了三类结果：一种是`defconfig`文件，关于`defconfig`文件的描述可以参照[这篇文章](https://stackoverflow.com/questions/41885015/what-exactly-does-linux-kernels-make-defconfig-do)。第二种是`Makefile`，主要是将对应的`.c`文件加入编译。第三种是对应的头文件，是否启用该接口。这个和我们之前预测的差不多，果然是在一个宏定义中得到使用。

    

**明天计划**

**第一种方法的尝试明天再深入尝试一下**，看能否有更加结构化的方法，而不是盲目搜索。针对该课题给出较好的解决方案。这种方法简单粗暴，利用`KgConfig`的定位信息也可以在效率上得到不错的提升；但是这种方案的缺点非常明显，即不能对代码进行一些结构化的建模和处理。**明天准备学习`.config`文件中的配置变量是如何被使用起来的**，顺着这个线索看能否有更好的方案。如果真的如老师所讲，作为宏被使用，那么它的处理一定是在编译的预处理阶段，顺着这个线索找下去，看能否有更好的办法...
