
import re
from utils import readJson
from torch import IntTensor

glyphList = [ v for v in readJson('./data/glyphs.json') ]
glyphList.sort( key=lambda x: len(x), reverse=True);

glyphSearchRe =  '|'.join(glyphList)

#  escape chars like ", ; ) ( ] [ ? *" for regex
glyphSearchRe = re.sub(r"[(){}\[\]\/\\.*?+-]", r"\\\g<0>", glyphSearchRe)

glyphSearchRe = re.compile( '(%s)' % glyphSearchRe)


def encodeStr( word ):
    glyphs = filter( None, glyphSearchRe.split( word ) )
    out = [ glyphList.index( g ) for g in  glyphs ]
    return out, len( out )

def encodeStrList( items ):
    txt, l = list( zip( *[ encodeStr(i) for i in items ] ) )
    return IntTensor( sum(txt, []) ), IntTensor( l )
encode = encodeStrList



def decodeStr( strEnc ):
    glyphs = [ glyphList[ g ] for g in strEnc ]
    return ''.join( glyphs )

def decodeStrList( items ):
    return list( zip( *[ decodeStr(i) for i in items ] ) )
decode = decodeStrList
