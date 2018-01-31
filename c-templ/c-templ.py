#!/usr/bin/python

import sys
import os.path
from string import Template

def fileExists(filename):
	return os.path.isfile(filename + '.h') or os.path.isfile(filename + '.c')

def generateHFile(filename):
	includeGuard = filename.replace('-', "_")
	headerContent = Template("""#ifndef $guard
#define $guard

#ifdef __cplusplus
extern \"C\" {
#endif

/**
 * @file $name.h
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

#ifdef __cplusplus
}
#endif

#endif /* $guard */
""")
	headerContent = headerContent.substitute(
		guard='_%s_H_' % includeGuard,
		name='%s.h' % fileName)
	headerFile = open('%s.h' % fileName, 'w+')
	headerFile.write(headerContent)
	headerFile.close()

def generateCFile(filename):
	cContent = Template("""/**
 * @file $name
 *
 * Description
 *
 */

/*======= Includes ==========================================================*/

#include "$header"

/*======= Local Macro Definitions ===========================================*/
/*======= Type Definitions ==================================================*/
/*======= Local function prototypes =========================================*/
/*======= Local variable declarations =======================================*/
/*======= Global function implementations ===================================*/
/*======= Local function implementations ====================================*/

""")
	cContent = cContent.substitute(
		header='%s.h' % fileName,
		name='%s.c' % fileName)
	headerFile = open('%s.c' % fileName, 'w+')
	headerFile.write(cContent)
	headerFile.close()

if len(sys.argv) < 2:
	print('Usage: python c-templ.py file1 file2')
	exit(0)

for fileName in sys.argv[1:]:
	if fileExists(fileName):
		print('Files for %s exists, skipping.' % fileName)
	generateHFile(fileName)
	generateCFile(fileName)
