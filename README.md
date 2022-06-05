# Kernel Variable Code Exactor(KVCE) 

#### í ½í´å¿«éè·³è½¬

- í ½íº[ææ°è¿å±(ç¹æèå¸)](#602)
- í ¼í½[ä»»å¡æè¿°](#1-ä»»å¡æè¿°)
- í ¼í½­[æç»äº§ç©](#2-æç»äº§ç©)

#### 1. ä»»å¡æè¿°

* ä¸»çº¿ä»»å¡ï¼ç¼åä¸ä¸ªèæ¬ï¼è¯¥èæ¬è½å¤ï¼
  1. æ ¹æ®ä»»ä¸åæ ¸æºä»£ç ï¼ä»»å¡ä»¥åæ ¸`5.15.9`ä¸ºä¾ï¼ï¼å¾å°ææçåæ ¸éç½®é¡¹ã
  2. å¯¹äºä»»æä¸ä¸ªéç½®é¡¹ï¼è½å¤å®ä½å°å®æå¯¹åºåå½±åçæä»¶ãæä»¶ä¸­çä»£ç çæ®µ
* æ¯çº¿ä»»å¡ï¼
  1. æ ¹æ®ä»»ä¸åæ ¸æºä»£ç çè¡¥ä¸ï¼è½å¤å®ä½å°å½åçè¡¥ä¸å¯¹åªä¸ä¸ªéç½®é¡¹æå½±å

#### 2. æç»äº§ç©

æç»çé¡¹ç®äº¤ä»ï¼æ¯ä»¥ä¸ä¸ª`Repo`çå½¢å¼ï¼æç»ç`Repo`ä¸­åºè¯¥åå«å¦ä¸çåå®¹ï¼

* ä»»å¡æè¿°ä¸­çèæ¬æä»¶

* ç¤ºä¾åæ ¸æºä»£ç ï¼ä»¥åæ ¸`5.15.9`ä¸ºä¾ï¼

* è¾åºçJsonæä»¶ï¼

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

  

* éå¯¹git è¡¥ä¸çjson :

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

**å·¥ä½è¿å±**

ä»å¤©ä¸»è¦æ¯æç¡®äºä»»å¡ç®çåäºä¸äºåå¤çå·¥ä½ã

* æç¡®äºä»»å¡åæç»çæäº¤ç©ï¼
* åºç¡çå·¥ä½ï¼
  * æ°å»ºäºä¸ä¸ª`Repo`ï¼åç»­ä»£ç åæ¥è®°ï¼æ¯æ¥å·¥ä½è¿å±ï¼ä¼å¨ä¸é¢æ´æ°ãç½ç«ç½åä¸ºï¼[æçGithubè¯¥é¡¹ç®ä¸»é¡µ](https://github.com/Rose1917/KVCE)
  * è½å¤æååºåæ ¸ä¸­ææéç½®åéçä»£ç 

* æè·¯æ¹é¢ï¼
  * ä¸ä¸ªæè·¯æ¯æ´åæï¼å¯¹äºæ¯ä¸ä¸ªéç½®åéï¼ç´æ¥æ´åå¨æºç ä¸­æç´¢åºç°çå®å®ä¹ãä½æ¯è¿ç§æ¹æ³æ¯è¾æ´åï¼æ´å ä¾èµäºæå®çè§åï¼èä¸æè§æçä¸ä¼å¤ªé«ã
  * å¦å¤ä¸ä¸ªæè·¯ï¼ç±äºè¿äºåéåºè¯¥æ¯é½å½ä½å®æ¥å¤çï¼åºè¯¥æ¯å¨ç¼è¯çé¢å¤çé¶æ®µæ¥å¤çãè½å¦å¨ç¼è¯çé¢å¤çé¶æ®µï¼å¯¹åéåä»£ç è¿è¡æåã

**æå¤©è®¡å**

å¯¹ç¬¬ä¸ä¸ªæè·¯åæå¨æµè¯ä¸ä¸ï¼ççææãç¬¬äºä¸ªæè·¯å¨ç½ä¸åæ¥æ¥èµæãå¦å¤æ¯ï¼æ³å°Githubä¸ççææ²¡æå¥½çä»£ç éæåæå·¥å·ï¼æèçè³æ¯åæ ¸ä»£ç çéæåæå·¥å·ã



---

#### 5.31

**å·¥ä½è¿å±**

ä»å¤©ä¸»è¦æ¯æ ¹æ®ä¾¯èå¸çæè§ï¼ä¿®æ¹äºç³»ç»ççæ¬ï¼å·²ç»ä¸ä¼ è³`Github`)ï¼**ä¿®æ¹**äºæ¬ææ¡£ç**ãä»»å¡æè¿°ã**å**ãæç»æäº¤ç©ã**é¨åãä»¥åæ ¹æ®åéåæº¯æºå°å¯¹åºçå­æ¨¡åç`KgConfig`æä»¶ï¼ä»èå®ä½å°å·ä½çå­æä»¶å¤¹ãå·ä½çåå®¹æè¿°å¦ä¸ï¼

* æ ¹æ®èå¸çæè§ä¿®æ¹çåå®¹å¦ä¸ï¼

  * å°ç³»ç»çæ¬ä»ä¹åæèªå·±ç¨ç`5.15.9`ä¿®æ¹è³`5.17.6`, ç³»ç»æä»¶æ¥èªäº[å¾®è½¯éåç«](https://mirrors.edge.kernel.org/pub/linux/kernel/v5.x/)ã
  * ä¿®æ¹äºæç»[æç»äº¤ä»æä»¶](#2-æç»äº§ç©)

* çæ`5.17.6`çæ¬åæ ¸çåéåè¡¨ï¼è¯¦è§é¡¹ç®æ ¹ç®å½ä¸ç`config_list_5_17_6.txt`ï¼ä½ä¸ºä¸ä¸ªä¸­é´æä»¶ï¼æ¹ä¾¿ä»¥åä½¿ç¨ã

* æ´åæç´¢åä¼å

  * éç½®é¡¹çæä»¶å®ä½ï¼ä»å¤©è¯å¾å°è¯ç¬¬ä¸ç§æ¹æ³ï¼å³ç´æ¥å¨æºä»£ç ä¸­è¿è¡æ£ç´¢å¯¹åºçéç½®é¡¹ãå¤§è´æ­¥éª¤å¦ä¸ï¼

    ```bash
    make clean # æ¸é¤äºè¿å¶æä»¶ï¼é²æ­¢grepå¯¹äºè¿å¶æä»¶è¿è¡æ£ç´¢
    grep -r CONFIG_XXX linux5.17.6 # ç´æ¥å¨åæ ¸æºç ä¸­è¿è¡æ£ç´¢
    ```

    å ä¸ºåæ ¸ä»£ç ç¹å«å¤ï¼æä»¥å¦æä¸ä¸ªä¸ä¸ªè¿ä¹æ£ç´¢ï¼éåº¦ä¼éå¸¸çæ¢ã

    ç±äºæä¹åå¨ååæ ¸åç±»çæ¶åï¼ç»å¤§å®¶åè¿ä¸ä¸ªåæ ¸çæ ç¶å¾ï¼æä»¥å¯ä»¥å®ä½å°æ¯ä¸ä¸ªéç½®åéçå±çº§ç»æï¼å¯ä»¥å©ç¨è¿ä¸ªå±çº§ä¿¡æ¯ï¼åªå¨é¨åå­æä»¶å¤¹ä¸­è¿è¡æ£ç´¢ãä¸é¢æ¯ä¸ä¸ªä¾å­ã

  * å®ä¾ï¼

    ç´æ¥å¯¹åé`CONFIG_MEMTEST`è¿è¡æç´¢

    ```bash
    grep -r "CONFIG_MEMTEST" .
    ```

    ç»æå¦ä¸ï¼

    ```bash
    ./arch/arm/configs/mps2_defconfig:CONFIG_MEMTEST=y
    ./arch/arm64/configs/defconfig:CONFIG_MEMTEST=y
    ./arch/riscv/configs/defconfig:CONFIG_MEMTEST=y
    ./arch/riscv/configs/rv32_defconfig:CONFIG_MEMTEST=y
    ./mm/Makefile:obj-$(CONFIG_MEMTEST)		+= memtest.o
    ./include/linux/memblock.h:#ifdef CONFIG_MEMTEST
    ```

    å¶ä¸­ä¸»è¦åºç°äºä¸ç±»ç»æï¼ä¸ç§æ¯`defconfig`æä»¶ï¼å³äº`defconfig`æä»¶çæè¿°å¯ä»¥åç§[è¿ç¯æç« ](https://stackoverflow.com/questions/41885015/what-exactly-does-linux-kernels-make-defconfig-do)ãç¬¬äºç§æ¯`Makefile`ï¼ä¸»è¦æ¯å°å¯¹åºç`.c`æä»¶å å¥ç¼è¯ãç¬¬ä¸ç§æ¯å¯¹åºçå¤´æä»¶ï¼æ¯å¦å¯ç¨è¯¥æ¥å£ãè¿ä¸ªåæä»¬ä¹åé¢æµçå·®ä¸å¤ï¼æç¶æ¯å¨ä¸ä¸ªå®å®ä¹ä¸­å¾å°ä½¿ç¨ã

    

**æå¤©è®¡å**

**ç¬¬ä¸ç§æ¹æ³çå°è¯æå¤©åæ·±å¥å°è¯ä¸ä¸**ï¼çè½å¦ææ´å ç»æåçæ¹æ³ï¼èä¸æ¯ç²ç®æç´¢ãéå¯¹è¯¥è¯¾é¢ç»åºè¾å¥½çè§£å³æ¹æ¡ãè¿ç§æ¹æ³ç®åç²æ´ï¼å©ç¨`KgConfig`çå®ä½ä¿¡æ¯ä¹å¯ä»¥å¨æçä¸å¾å°ä¸éçæåï¼ä½æ¯è¿ç§æ¹æ¡çç¼ºç¹éå¸¸ææ¾ï¼å³ä¸è½å¯¹ä»£ç è¿è¡ä¸äºç»æåçå»ºæ¨¡åå¤çã**æå¤©åå¤å­¦ä¹ `.config`æä»¶ä¸­çéç½®åéæ¯å¦ä½è¢«ä½¿ç¨èµ·æ¥ç**ï¼é¡ºçè¿ä¸ªçº¿ç´¢çè½å¦ææ´å¥½çæ¹æ¡ãå¦æççå¦èå¸æè®²ï¼ä½ä¸ºå®è¢«ä½¿ç¨ï¼é£ä¹å®çå¤çä¸å®æ¯å¨ç¼è¯çé¢å¤çé¶æ®µï¼é¡ºçè¿ä¸ªçº¿ç´¢æ¾ä¸å»ï¼çè½å¦ææ´å¥½çåæ³...



#### 6.01

**å·¥ä½è¿å±**

ä»å¤©ä¸»è¦æ¯å¯¹æ´åæç´¢çæ¹æ³è¿è¡äºè¿ä¸æ­¥çæ¢ç´¢ï¼å°è¯å¨å¤§è§æ¨¡åéä¸å°è¯ãä¸è¿æ­£å¦æ¨å¤©åçä¸æ ·ï¼åéå¨åæ ¸ä¸­åºç°çæåµè¿æ¯æä»¬ä¹åé¢æ³çè¦å¤æçå¤ãå¯è½åºç°å¨æä»¬é¢æ³ç`ifdef`ä¸­ï¼ä½æ¯ä¹å¯è½åºç°å¨`Makefile`åå¶ä»çä¸äºææ¬æä»¶ä¸­ãæä»¥ä»å¤©åå¤åå°éä¸æ­¥ï¼å°ææçåéé½å¨åæ ¸ä¸­æç´¢ä¸éï¼è¾åºåºç°çæä»¶åå¯¹åºçè¡å·ï¼ä»¥åå¯¹åºçä»£ç ãæä»¥ä»å¤©çå·¥ä½ä¸»è¦æ¯ï¼

* åäºä¸ä¸ª`extractor.py`çä»£ç ãè¯¥èæ¬è¯»å¥ä¹åçä¸­é´æä»¶ï¼éç½®åéåè¡¨ï¼ï¼å¯¹æ¯ä¸ä¸ªåéé½å°åæ ¸çæææºä»£ç ä¸­è¿è¡æç´¢ï¼å¦ææå¹éï¼åè¾åºå¯¹åºçè¡å·åæä»¶åã

* å ä¸ºè¿ä¸ªè¿ç¨æ¯è¾èæ¶ï¼æä»¥è¿éåªç²è´´åºæ¥é¨åçè¾åºï¼

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

  

* ä¸äºåæ­¥çç»è®ºï¼åä¹åæ³è±¡çä¸åï¼å®éä¸å¤§é¨åçï¼è¿éè¿ä¸ªå¤§é¨åæå¾èè¯ï¼æ¯æç¬¦åç´è§ä¸çå¤§é¨åï¼åæ ¸éç½®é¡¹ï¼æ¯éè¿å½±å`Makefile`è¿èå½±ååæ ¸çæå»ºçï¼èä¸æ¯ä¹åæ³è±¡çä¸»è¦éè¿å¤´æä»¶ä¸­çæ¡ä»¶å®(#ifdef)è¿ç§æ¥å½±åæå»ºçã

**æå¤©çè®¡å**

å ä¸ºè¿ä¸ªå·¥ä½éå¸¸èæ¶ï¼æä»¥è¿é¨åææçè¾åºè¿æ²¡ææ´çåºæ¥ï¼æä¹æ²¡æ`push`ä¸å»ãä¸æä¸çæ¶é´åºè¯¥æ¯å·®ä¸å¤äºãç­å°æå¤©åºäºç»æä»¥åï¼åå¥½å¥½ççï¼çè½å¦æä¸äºæ°çæè·¯ãä½æ¯æç®åä»ç¶æ¯å¯¹è¿ç§éè¿æ´åæ£ç´¢çæ¹æ³ææç»äº§ççç»æè´¨éä¸æ¯ç¹å«çå¥½çã

ä¸ç®¡æä¹æ ·ï¼è¿ä¸ªæ¹æ³æ»å½æ¯æ¯è¾ç®åãç­å°ç«¯åèçæ¶åï¼å¯ä»¥å¥½å¥½ççæºç ä¸­ç`Makefile`ï¼äºè§£ä¸ä¸`make bzImages`å`make modules`å½ä»¤æ§è¡ä»¥åï¼åçäºä»ä¹ï¼

#### **6.02**

**å·¥ä½è¿å±**

è¿å å¤©çå·¥ä½ä¸»è¦éä¸­å¨æç´¢å·¥ä½çè¿ä¸æ­¥ç»åã

* ç®åçä¸»è¦æè·¯å°±æ¯ï¼

  - [x] ä»Kgconfigæä»¶ä¸­æååºåéï¼åéåè¡¨`var_with_config.txt`

  - [x] å¯¹æ¯ä¸ä¸ªåéè¿è¡æç´¢ï¼çæ`res.txt`æä»¶
  - [ ] å¯¹æç´¢çç»ææ ¹æ®ä¸åçæä»¶ï¼ä¾å¦`Makefile`ã`.c`å`.h`åå«è¿è¡è§£æ
    - [ ] Makefile
    - [ ] .c
    - [ ] .h
  - [ ] çææç»ç`Json`æä»¶

ä¸å¨çä¸»è¦å·¥ä½ä¸»è¦éä¸­å¨å¯¹æ¯ä¸ä¸ªåéè¿è¡æç´¢ï¼ä¹åæè¯´ç¨èªå·±åç`py`èæ¬ï¼æçéå¸¸ä½ï¼æç´¢çæ¶é´æ¯æå¤©è®¡æ°çãåæ¥éç¨çæ¯åºäº`rust`éåçä¸ä¸ª`grep`å½ä»¤ç`bash`èæ¬ï¼è¯¦è§`extractor.sh`)ï¼éåº¦æä¸æ¥ï¼ç°å¨å¤§çº¦éè¦ä¸¤ä¸ªå°æ¶å®æä¸æ¬¡æç´¢ï¼ãè¿éè½ç¶çæçæ¯`txt`æä»¶ï¼ä½æ¯ä¸ºäºåé¢çå¤çï¼å¶å®è¾åºæ¯æè®²ç©¶çï¼æ¯æä¸å®çæ ¼å¼çãè¯¦æåç§`res.txt`.



é¤æ­¤ä»¥å¤ï¼æè¿å¨`stackoverflow`å`reddit`ä¸åå¸äºè®¨è®ºå¸ï¼è¯¦è§[Stack-Overflow](https://stackoverflow.com/questions/72469384/linux-kernel-config-file-variable-and-its-corresponding-source-code?noredirect=1#comment128020772_72469384)å[reddit](https://www.reddit.com/r/linuxquestions/comments/v4pgn0/linux_kernel_config_file_variable_and_its/). ä¼¼ä¹æ²¡æå¤ªå¥½çæ¹æ¡ï¼åªè½è¿è¡æ£ç´¢ï¼å¯¹äºä¸åçæä»¶ç±»åï¼åå«å¤çãå¦æèå¸ï¼æä»ä¹å¥½çæè·¯ï¼ä¹å¯ä»¥å¯åä¸ä¸æåã

**æå¤©çè®¡å**

æ­£å¦æä¸é¢æåï¼ä¸ä¸æ­¥åå¤å¯¹æç´¢çç»æè½¬åæä¸ºç»æåç`json`æ°æ®ï¼æ¹ä¾¿åç»­çæ´çï¼ä¾å¦ç»è®¡æä»¶çç±»åãæºä»£ç çè§£æç­ç­ã
