# Kernel Variable Code Exactor(KVCE) 

#### 🔗快速跳转

- 🚀[最新进展](#602)
- 🎉[任务描述](#1-任务描述)
- 🎈[最终产物](#2-最终产物)

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
  * 修改了最终[最终交付文件](#2-最终产物)

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



#### 6.01

**工作进展**

今天主要是对暴力搜索的方法进行了进一步的探索，尝试在大规模变量上尝试。不过正如昨天写的一样，变量在内核中出现的情况远比我们之前预想的要复杂的多。可能出现在我们预想的`ifdef`中，但是也可能出现在`Makefile`和其他的一些文本文件中。所以今天准备先将退一步，将所有的变量都在内核中搜索一遍，输出出现的文件和对应的行号，以及对应的代码。所以今天的工作主要是：

* 写了一个`extractor.py`的代码。该脚本读入之前的中间文件（配置变量列表），对每一个变量都到内核的所有源代码中进行搜索，如果有匹配，则输出对应的行号和文件名。

* 因为这个过程比较耗时，所以这里只粘贴出来部分的输出：

  ```
  CONFIG_CC_IS_GCC
      file:/home/march1917/projects/kernel_src/linux-5.17.6/Makefile :680
      ifdef CONFIG_CC_IS_GCC
  
      file:/home/march1917/projects/kernel_src/linux-5.17.6/Makefile :754
      ifdef CONFIG_CC_IS_GCC
  
      file:/home/march1917/projects/kernel_src/linux-5.17.6/Makefile :961
      ifdef CONFIG_CC_IS_GCC
  
      file:/home/march1917/projects/kernel_src/linux-5.17.6/Makefile :965
      ifdef CONFIG_CC_IS_GCC
  
      file:/home/march1917/projects/kernel_src/linux-5.17.6/Makefile :987
      ifdef CONFIG_CC_IS_GCC
  
      file:/home/march1917/projects/kernel_src/linux-5.17.6/scripts/Makefile.kcsan :15
      ifdef CONFIG_CC_IS_GCC
  
      file:/home/march1917/projects/kernel_src/linux-5.17.6/scripts/Makefile.debug :20
      ifdef CONFIG_CC_IS_GCC
  
      file:/home/march1917/projects/kernel_src/linux-5.17.6/scripts/dummy-tools/gcc :52
      # To set CONFIG_CC_IS_GCC=y
  
      file:/home/march1917/projects/kernel_src/linux-5.17.6/lib/Makefile :111
      ifdef CONFIG_CC_IS_GCC
  
      file:/home/march1917/projects/kernel_src/linux-5.17.6/lib/mpi/longlong.h :655
      #if defined(__mips_isa_rev) && __mips_isa_rev >= 6 && defined(CONFIG_CC_IS_GCC)
  
      file:/home/march1917/projects/kernel_src/linux-5.17.6/arch/x86/Makefile :14
      ifdef CONFIG_CC_IS_GCC
  
      file:/home/march1917/projects/kernel_src/linux-5.17.6/arch/arm/Makefile :35
      ifeq ($(CONFIG_CC_IS_GCC),y)
  
      file:/home/march1917/projects/kernel_src/linux-5.17.6/arch/riscv/include/asm/ftrace.h :19
      #if defined(CONFIG_CC_IS_GCC) || CONFIG_CLANG_VERSION >= 130000
  
      file:/home/march1917/projects/kernel_src/linux-5.17.6/kernel/gcov/Makefile :4
      obj-$(CONFIG_CC_IS_GCC) += gcc_base.o gcc_4_7.o
  
      file:/home/march1917/projects/kernel_src/linux-5.17.6/kernel/bpf/Makefile :4
      cflags-nogcse-$(CONFIG_X86)$(CONFIG_CC_IS_GCC) := -fno-gcse
  
      file:/home/march1917/projects/kernel_src/linux-5.17.6/drivers/gpu/drm/amd/display/dc/dcn303/Makefile :18
      ifdef CONFIG_CC_IS_GCC
  
      file:/home/march1917/projects/kernel_src/linux-5.17.6/drivers/gpu/drm/amd/display/dc/calcs/Makefile :35
      ifdef CONFIG_CC_IS_GCC
  
      file:/home/march1917/projects/kernel_src/linux-5.17.6/drivers/gpu/drm/amd/display/dc/dcn302/Makefile :22
      ifdef CONFIG_CC_IS_GCC
  
      file:/home/march1917/projects/kernel_src/linux-5.17.6/drivers/gpu/drm/amd/display/dc/dcn201/Makefile :16
      ifdef CONFIG_CC_IS_GCC
  
      file:/home/march1917/projects/kernel_src/linux-5.17.6/drivers/gpu/drm/amd/display/dc/dcn20/Makefile :19
      ifdef CONFIG_CC_IS_GCC
  
      file:/home/march1917/projects/kernel_src/linux-5.17.6/drivers/gpu/drm/amd/display/dc/dcn21/Makefile :15
      ifdef CONFIG_CC_IS_GCC
  
      file:/home/march1917/projects/kernel_src/linux-5.17.6/drivers/gpu/drm/amd/display/dc/dml/Makefile :35
      ifdef CONFIG_CC_IS_GCC
  
      file:/home/march1917/projects/kernel_src/linux-5.17.6/drivers/gpu/drm/amd/display/dc/dcn30/Makefile :43
      ifdef CONFIG_CC_IS_GCC
  
      file:/home/march1917/projects/kernel_src/linux-5.17.6/drivers/gpu/drm/amd/display/dc/dcn31/Makefile :25
      ifdef CONFIG_CC_IS_GCC
  
      file:/home/march1917/projects/kernel_src/linux-5.17.6/crypto/Makefile :111
      aegis128-cflags-$(CONFIG_CC_IS_GCC) += -ffixed-q16 -ffixed-q17 -ffixed-q18 \
  
      file:/home/march1917/projects/kernel_src/linux-5.17.6/crypto/aegis128-neon-inner.c :70
      #ifndef CONFIG_CC_IS_GCC
  
      file:/home/march1917/projects/kernel_src/linux-5.17.6/crypto/aegis128-neon-inner.c :122
      	    !IS_ENABLED(CONFIG_CC_IS_GCC) ||
  
  
  ```

  

* 一些初步的结论：和之前想象的不同，实际上大部分的（这里这个大部分有待考证，是指符合直觉上的大部分）内核配置项，是通过影响`Makefile`进而影响内核的构建的，而不是之前想象的主要通过头文件中的条件宏(#ifdef)这种来影响构建的。

**明天的计划**

因为这个工作非常耗时，所以这部分所有的输出还没有整理出来，我也没有`push`上去。一晚上的时间应该是差不多了。等到明天出了结果以后，再好好看看，看能否有一些新的思路。但是我目前仍然是对这种通过暴力检索的方法所最终产生的结果质量不是特别看好的。

不管怎么样，这个方法总归是比较简单。等到端午节的时候，可以好好看看源码中的`Makefile`，了解一下`make bzImages`和`make modules`命令执行以后，发生了什么！

#### **6.02**

**工作进展**

这几天的工作主要集中在搜索工作的进一步细化。

* 目前的主要思路就是：

  - [x] 从Kgconfig文件中提取出变量，变量列表`var_with_config.txt`

  - [x] 对每一个变量进行搜索，生成`res.txt`文件
  - [ ] 对搜索的结果根据不同的文件，例如`Makefile`、`.c`和`.h`分别进行解析
    - [ ] Makefile
    - [ ] .c
    - [ ] .h
  - [ ] 生成最终的`Json`文件

上周的主要工作主要集中在对每一个变量进行搜索，之前我说用自己写的`py`脚本，效率非常低，搜索的时间是按天计数的。后来采用的是基于`rust`重写的一个`grep`命令的`bash`脚本（详见`extractor.sh`)，速度才上来（现在大约需要两个小时完成一次搜索）。这里虽然生成的是`txt`文件，但是为了后面的处理，其实输出是有讲究的，是有一定的格式的。详情参照`res.txt`.



除此以外，我还在`stackoverflow`和`reddit`上发布了讨论帖，详见[Stack-Overflow](https://stackoverflow.com/questions/72469384/linux-kernel-config-file-variable-and-its-corresponding-source-code?noredirect=1#comment128020772_72469384)和[reddit](https://www.reddit.com/r/linuxquestions/comments/v4pgn0/linux_kernel_config_file_variable_and_its/). 似乎没有太好的方案，只能进行检索，对于不同的文件类型，分别处理。如果老师，有什么好的思路，也可以启发一下我哈。

**明天的计划**

正如我上面所写，下一步准备对搜索的结果转化成为结构化的`json`数据，方便后续的整理，例如统计文件的类型、源代码的解析等等。

#### **6.06**
**工作进展**
今天主要工作体现在`Coding`,今天完成了从之前的文本到`json`的转换。这个转换是非常有意义的，因为无结构的数据很难处理。后面我们的工作就在`python`下完成就好。具体地：
* 完成了`process.py`中的`block_to_json`函数，这个函数的作用是把`res`文件转化为`json`格式。
* 具体的`json`格式请参阅`data.json`数据文件，大概是这样：
```
    the transfered json pattern
    {
        "config_name:" "XXXX"
        "search_res": [
            {
                "file_path": "./linux-5.17.6/arch/XXXX",
                "hits":
                    [
                        {
                            "line_no" : XXX,
                            "content" : XXX
                        },
                        {
                            "line_no" : XXX,
                            "content" : XXX
                        }


                    ]

            },
            {
                "file_path": "./linux-5.17.6/...",
                "hits": 
                    [
                        {
                            "line_no" : XXX,
                            "content" : XXXX,

                        }

                        {
                            "line_no" : XXX,
                            "content" : XXXX,

                        }

                    ]

            }
        ]
'''
```
**明日计划**
对不同的文件类型进行匹配，开始按照文件进行处理。
