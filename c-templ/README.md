# C File template
Two sublime text snippets for creating template for c- and header files.

## *.h layout
```c
#ifndef _TEST_H_
#define _TEST_H_
/**
 * @file test.h
 *
 * Description
 *
 */

/*======= Includes ==========================================================*/

#include <stdint.h>

/*======= Public macro definitions ==========================================*/
/*======= Type Definitions and declarations =================================*/
/*======= Public variable declarations ======================================*/
/*======= Public function declarations ======================================*/

/**
 * @brief [brief description]
 * @details [long description]
 * 
 * @param in [description]
 * @return [description]
 */
uint8_t a_function(uint8_t in);

#endif /* _TEST_H_ */

```

## *.c layout
```c
/**
 * @file test.c
 *
 * Description
 *
 */

/*======= Includes ==========================================================*/
/*======= Local Macro Definitions ===========================================*/
/*======= Type Definitions ==================================================*/
/*======= Local function prototypes =========================================*/
/*======= Local variable declarations =======================================*/
/*======= Global function implementations ===================================*/
/*======= Local function implementations ====================================*/

```



