# Generated from cpp.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,75,613,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,
        71,2,72,7,72,2,73,7,73,2,74,7,74,2,75,7,75,1,0,1,0,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,5,2,168,8,2,10,2,12,2,171,9,2,
        1,2,1,2,1,2,1,2,1,2,5,2,178,8,2,10,2,12,2,181,9,2,1,2,3,2,184,8,
        2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,247,8,
        4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,291,8,5,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,304,8,6,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,3,7,315,8,7,1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,
        1,10,1,11,1,11,1,11,1,12,1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,14,
        1,15,1,15,1,15,1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,18,1,19,1,19,
        1,20,1,20,1,21,1,21,1,22,1,22,1,23,1,23,1,23,1,24,1,24,1,25,1,25,
        1,26,1,26,1,27,1,27,1,28,1,28,1,29,1,29,1,30,1,30,1,30,1,31,1,31,
        1,31,1,32,1,32,1,33,1,33,1,34,1,34,1,35,1,35,1,35,1,36,1,36,1,37,
        1,37,1,38,1,38,1,39,1,39,1,40,1,40,1,41,1,41,1,42,1,42,1,43,1,43,
        1,44,1,44,1,45,1,45,1,46,1,46,1,46,1,47,1,47,1,47,1,47,1,47,1,48,
        1,48,1,48,1,48,1,48,1,48,1,49,1,49,1,49,1,49,1,50,1,50,1,50,1,50,
        1,50,1,50,1,50,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,52,1,52,1,52,
        1,52,1,52,1,52,1,52,1,52,1,52,1,52,1,52,1,52,1,52,1,53,1,53,1,53,
        1,53,1,54,1,54,1,54,1,54,1,54,1,54,1,54,1,55,1,55,1,55,1,55,1,55,
        1,56,1,56,1,56,1,56,1,56,1,56,1,56,1,57,1,57,1,57,1,57,1,57,1,57,
        1,58,1,58,1,58,1,58,1,58,1,59,1,59,1,59,1,59,1,59,1,60,1,60,1,60,
        1,60,1,60,1,60,1,60,1,61,1,61,1,61,1,61,1,61,1,61,1,62,1,62,1,62,
        1,62,1,62,1,62,1,63,1,63,1,63,1,63,1,64,1,64,1,64,1,64,1,64,1,64,
        1,65,1,65,1,65,1,65,1,65,1,65,1,65,1,65,1,65,1,65,1,66,1,66,1,66,
        1,66,1,66,1,66,1,66,1,66,1,67,1,67,1,67,1,67,1,68,1,68,1,68,1,68,
        1,68,1,69,1,69,1,69,1,69,1,69,1,70,3,70,553,8,70,1,70,4,70,556,8,
        70,11,70,12,70,557,1,70,1,70,4,70,562,8,70,11,70,12,70,563,3,70,
        566,8,70,1,71,1,71,5,71,570,8,71,10,71,12,71,573,9,71,1,72,4,72,
        576,8,72,11,72,12,72,577,1,72,1,72,1,73,1,73,1,73,1,73,5,73,586,
        8,73,10,73,12,73,589,9,73,1,73,1,73,1,74,1,74,1,74,1,74,5,74,597,
        8,74,10,74,12,74,600,9,74,1,74,1,74,1,74,1,74,1,74,1,75,4,75,608,
        8,75,11,75,12,75,609,1,75,1,75,1,598,0,76,1,1,3,2,5,3,7,4,9,0,11,
        5,13,6,15,7,17,8,19,9,21,10,23,11,25,12,27,13,29,14,31,15,33,16,
        35,17,37,18,39,19,41,20,43,21,45,22,47,23,49,24,51,25,53,26,55,27,
        57,28,59,29,61,30,63,31,65,32,67,33,69,34,71,35,73,36,75,37,77,38,
        79,39,81,40,83,41,85,42,87,43,89,44,91,45,93,46,95,47,97,48,99,49,
        101,50,103,51,105,52,107,53,109,54,111,55,113,56,115,57,117,58,119,
        59,121,60,123,61,125,62,127,63,129,64,131,65,133,66,135,67,137,68,
        139,69,141,70,143,71,145,72,147,73,149,74,151,75,1,0,7,4,0,10,10,
        13,13,34,34,92,92,4,0,10,10,13,13,39,39,92,92,1,0,48,57,3,0,48,57,
        65,90,97,122,4,0,48,57,65,90,95,95,97,122,3,0,9,10,13,13,32,32,2,
        0,10,10,13,13,643,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,
        0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,
        0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,
        0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,
        0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,
        0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,
        0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,
        0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,
        0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,0,0,0,0,89,1,0,0,
        0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,0,0,0,0,97,1,0,0,0,0,99,1,0,0,
        0,0,101,1,0,0,0,0,103,1,0,0,0,0,105,1,0,0,0,0,107,1,0,0,0,0,109,
        1,0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,0,115,1,0,0,0,0,117,1,0,0,0,
        0,119,1,0,0,0,0,121,1,0,0,0,0,123,1,0,0,0,0,125,1,0,0,0,0,127,1,
        0,0,0,0,129,1,0,0,0,0,131,1,0,0,0,0,133,1,0,0,0,0,135,1,0,0,0,0,
        137,1,0,0,0,0,139,1,0,0,0,0,141,1,0,0,0,0,143,1,0,0,0,0,145,1,0,
        0,0,0,147,1,0,0,0,0,149,1,0,0,0,0,151,1,0,0,0,1,153,1,0,0,0,3,155,
        1,0,0,0,5,183,1,0,0,0,7,185,1,0,0,0,9,246,1,0,0,0,11,290,1,0,0,0,
        13,303,1,0,0,0,15,314,1,0,0,0,17,316,1,0,0,0,19,319,1,0,0,0,21,322,
        1,0,0,0,23,325,1,0,0,0,25,328,1,0,0,0,27,331,1,0,0,0,29,334,1,0,
        0,0,31,337,1,0,0,0,33,340,1,0,0,0,35,342,1,0,0,0,37,345,1,0,0,0,
        39,348,1,0,0,0,41,350,1,0,0,0,43,352,1,0,0,0,45,354,1,0,0,0,47,356,
        1,0,0,0,49,359,1,0,0,0,51,361,1,0,0,0,53,363,1,0,0,0,55,365,1,0,
        0,0,57,367,1,0,0,0,59,369,1,0,0,0,61,371,1,0,0,0,63,374,1,0,0,0,
        65,377,1,0,0,0,67,379,1,0,0,0,69,381,1,0,0,0,71,383,1,0,0,0,73,386,
        1,0,0,0,75,388,1,0,0,0,77,390,1,0,0,0,79,392,1,0,0,0,81,394,1,0,
        0,0,83,396,1,0,0,0,85,398,1,0,0,0,87,400,1,0,0,0,89,402,1,0,0,0,
        91,404,1,0,0,0,93,406,1,0,0,0,95,409,1,0,0,0,97,414,1,0,0,0,99,420,
        1,0,0,0,101,424,1,0,0,0,103,431,1,0,0,0,105,438,1,0,0,0,107,451,
        1,0,0,0,109,455,1,0,0,0,111,462,1,0,0,0,113,467,1,0,0,0,115,474,
        1,0,0,0,117,480,1,0,0,0,119,485,1,0,0,0,121,490,1,0,0,0,123,497,
        1,0,0,0,125,503,1,0,0,0,127,509,1,0,0,0,129,513,1,0,0,0,131,519,
        1,0,0,0,133,529,1,0,0,0,135,537,1,0,0,0,137,541,1,0,0,0,139,546,
        1,0,0,0,141,552,1,0,0,0,143,567,1,0,0,0,145,575,1,0,0,0,147,581,
        1,0,0,0,149,592,1,0,0,0,151,607,1,0,0,0,153,154,5,35,0,0,154,2,1,
        0,0,0,155,156,5,105,0,0,156,157,5,110,0,0,157,158,5,99,0,0,158,159,
        5,108,0,0,159,160,5,117,0,0,160,161,5,100,0,0,161,162,5,101,0,0,
        162,4,1,0,0,0,163,169,5,34,0,0,164,168,8,0,0,0,165,166,5,92,0,0,
        166,168,9,0,0,0,167,164,1,0,0,0,167,165,1,0,0,0,168,171,1,0,0,0,
        169,167,1,0,0,0,169,170,1,0,0,0,170,172,1,0,0,0,171,169,1,0,0,0,
        172,184,5,34,0,0,173,179,5,39,0,0,174,178,8,1,0,0,175,176,5,92,0,
        0,176,178,9,0,0,0,177,174,1,0,0,0,177,175,1,0,0,0,178,181,1,0,0,
        0,179,177,1,0,0,0,179,180,1,0,0,0,180,182,1,0,0,0,181,179,1,0,0,
        0,182,184,5,39,0,0,183,163,1,0,0,0,183,173,1,0,0,0,184,6,1,0,0,0,
        185,186,5,60,0,0,186,187,3,9,4,0,187,188,5,62,0,0,188,8,1,0,0,0,
        189,190,5,105,0,0,190,191,5,111,0,0,191,192,5,115,0,0,192,193,5,
        116,0,0,193,194,5,114,0,0,194,195,5,101,0,0,195,196,5,97,0,0,196,
        247,5,109,0,0,197,198,5,118,0,0,198,199,5,101,0,0,199,200,5,99,0,
        0,200,201,5,116,0,0,201,202,5,111,0,0,202,247,5,114,0,0,203,204,
        5,115,0,0,204,205,5,116,0,0,205,206,5,114,0,0,206,207,5,105,0,0,
        207,208,5,110,0,0,208,247,5,103,0,0,209,210,5,102,0,0,210,211,5,
        115,0,0,211,212,5,116,0,0,212,213,5,114,0,0,213,214,5,101,0,0,214,
        215,5,97,0,0,215,247,5,109,0,0,216,217,5,97,0,0,217,218,5,108,0,
        0,218,219,5,103,0,0,219,220,5,111,0,0,220,221,5,114,0,0,221,222,
        5,105,0,0,222,223,5,116,0,0,223,224,5,104,0,0,224,247,5,109,0,0,
        225,226,5,115,0,0,226,227,5,115,0,0,227,228,5,116,0,0,228,229,5,
        114,0,0,229,230,5,101,0,0,230,231,5,97,0,0,231,247,5,109,0,0,232,
        233,5,115,0,0,233,234,5,116,0,0,234,235,5,97,0,0,235,236,5,99,0,
        0,236,247,5,107,0,0,237,238,5,99,0,0,238,239,5,99,0,0,239,240,5,
        116,0,0,240,241,5,121,0,0,241,242,5,112,0,0,242,247,5,101,0,0,243,
        244,5,109,0,0,244,245,5,97,0,0,245,247,5,112,0,0,246,189,1,0,0,0,
        246,197,1,0,0,0,246,203,1,0,0,0,246,209,1,0,0,0,246,216,1,0,0,0,
        246,225,1,0,0,0,246,232,1,0,0,0,246,237,1,0,0,0,246,243,1,0,0,0,
        247,10,1,0,0,0,248,249,5,115,0,0,249,250,5,105,0,0,250,251,5,122,
        0,0,251,291,5,101,0,0,252,253,5,98,0,0,253,254,5,101,0,0,254,255,
        5,103,0,0,255,256,5,105,0,0,256,291,5,110,0,0,257,258,5,101,0,0,
        258,259,5,110,0,0,259,291,5,100,0,0,260,261,5,112,0,0,261,262,5,
        117,0,0,262,263,5,115,0,0,263,264,5,104,0,0,264,265,5,95,0,0,265,
        266,5,98,0,0,266,267,5,97,0,0,267,268,5,99,0,0,268,291,5,107,0,0,
        269,270,5,108,0,0,270,271,5,101,0,0,271,272,5,110,0,0,272,273,5,
        103,0,0,273,274,5,116,0,0,274,291,5,104,0,0,275,276,5,112,0,0,276,
        277,5,117,0,0,277,278,5,115,0,0,278,291,5,104,0,0,279,280,5,101,
        0,0,280,281,5,109,0,0,281,282,5,112,0,0,282,283,5,116,0,0,283,291,
        5,121,0,0,284,285,5,116,0,0,285,286,5,111,0,0,286,291,5,112,0,0,
        287,288,5,112,0,0,288,289,5,111,0,0,289,291,5,112,0,0,290,248,1,
        0,0,0,290,252,1,0,0,0,290,257,1,0,0,0,290,260,1,0,0,0,290,269,1,
        0,0,0,290,275,1,0,0,0,290,279,1,0,0,0,290,284,1,0,0,0,290,287,1,
        0,0,0,291,12,1,0,0,0,292,293,5,115,0,0,293,294,5,116,0,0,294,295,
        5,111,0,0,295,304,5,105,0,0,296,297,5,105,0,0,297,298,5,115,0,0,
        298,299,5,100,0,0,299,300,5,105,0,0,300,301,5,103,0,0,301,302,5,
        105,0,0,302,304,5,116,0,0,303,292,1,0,0,0,303,296,1,0,0,0,304,14,
        1,0,0,0,305,306,5,116,0,0,306,307,5,114,0,0,307,308,5,117,0,0,308,
        315,5,101,0,0,309,310,5,102,0,0,310,311,5,97,0,0,311,312,5,108,0,
        0,312,313,5,115,0,0,313,315,5,101,0,0,314,305,1,0,0,0,314,309,1,
        0,0,0,315,16,1,0,0,0,316,317,5,60,0,0,317,318,5,60,0,0,318,18,1,
        0,0,0,319,320,5,62,0,0,320,321,5,62,0,0,321,20,1,0,0,0,322,323,5,
        61,0,0,323,324,5,61,0,0,324,22,1,0,0,0,325,326,5,43,0,0,326,327,
        5,61,0,0,327,24,1,0,0,0,328,329,5,45,0,0,329,330,5,61,0,0,330,26,
        1,0,0,0,331,332,5,33,0,0,332,333,5,61,0,0,333,28,1,0,0,0,334,335,
        5,60,0,0,335,336,5,61,0,0,336,30,1,0,0,0,337,338,5,62,0,0,338,339,
        5,61,0,0,339,32,1,0,0,0,340,341,5,33,0,0,341,34,1,0,0,0,342,343,
        5,38,0,0,343,344,5,38,0,0,344,36,1,0,0,0,345,346,5,124,0,0,346,347,
        5,124,0,0,347,38,1,0,0,0,348,349,5,63,0,0,349,40,1,0,0,0,350,351,
        5,59,0,0,351,42,1,0,0,0,352,353,5,44,0,0,353,44,1,0,0,0,354,355,
        5,46,0,0,355,46,1,0,0,0,356,357,5,45,0,0,357,358,5,62,0,0,358,48,
        1,0,0,0,359,360,5,40,0,0,360,50,1,0,0,0,361,362,5,41,0,0,362,52,
        1,0,0,0,363,364,5,123,0,0,364,54,1,0,0,0,365,366,5,125,0,0,366,56,
        1,0,0,0,367,368,5,91,0,0,368,58,1,0,0,0,369,370,5,93,0,0,370,60,
        1,0,0,0,371,372,5,43,0,0,372,373,5,43,0,0,373,62,1,0,0,0,374,375,
        5,45,0,0,375,376,5,45,0,0,376,64,1,0,0,0,377,378,5,124,0,0,378,66,
        1,0,0,0,379,380,5,94,0,0,380,68,1,0,0,0,381,382,5,126,0,0,382,70,
        1,0,0,0,383,384,5,58,0,0,384,385,5,58,0,0,385,72,1,0,0,0,386,387,
        5,38,0,0,387,74,1,0,0,0,388,389,5,43,0,0,389,76,1,0,0,0,390,391,
        5,45,0,0,391,78,1,0,0,0,392,393,5,42,0,0,393,80,1,0,0,0,394,395,
        5,47,0,0,395,82,1,0,0,0,396,397,5,37,0,0,397,84,1,0,0,0,398,399,
        5,61,0,0,399,86,1,0,0,0,400,401,5,60,0,0,401,88,1,0,0,0,402,403,
        5,62,0,0,403,90,1,0,0,0,404,405,5,58,0,0,405,92,1,0,0,0,406,407,
        5,105,0,0,407,408,5,102,0,0,408,94,1,0,0,0,409,410,5,101,0,0,410,
        411,5,108,0,0,411,412,5,115,0,0,412,413,5,101,0,0,413,96,1,0,0,0,
        414,415,5,119,0,0,415,416,5,104,0,0,416,417,5,105,0,0,417,418,5,
        108,0,0,418,419,5,101,0,0,419,98,1,0,0,0,420,421,5,102,0,0,421,422,
        5,111,0,0,422,423,5,114,0,0,423,100,1,0,0,0,424,425,5,114,0,0,425,
        426,5,101,0,0,426,427,5,116,0,0,427,428,5,117,0,0,428,429,5,114,
        0,0,429,430,5,110,0,0,430,102,1,0,0,0,431,432,5,115,0,0,432,433,
        5,105,0,0,433,434,5,122,0,0,434,435,5,101,0,0,435,436,5,95,0,0,436,
        437,5,116,0,0,437,104,1,0,0,0,438,439,5,115,0,0,439,440,5,116,0,
        0,440,441,5,114,0,0,441,442,5,105,0,0,442,443,5,110,0,0,443,444,
        5,103,0,0,444,445,5,115,0,0,445,446,5,116,0,0,446,447,5,114,0,0,
        447,448,5,101,0,0,448,449,5,97,0,0,449,450,5,109,0,0,450,106,1,0,
        0,0,451,452,5,105,0,0,452,453,5,110,0,0,453,454,5,116,0,0,454,108,
        1,0,0,0,455,456,5,115,0,0,456,457,5,116,0,0,457,458,5,114,0,0,458,
        459,5,105,0,0,459,460,5,110,0,0,460,461,5,103,0,0,461,110,1,0,0,
        0,462,463,5,98,0,0,463,464,5,111,0,0,464,465,5,111,0,0,465,466,5,
        108,0,0,466,112,1,0,0,0,467,468,5,100,0,0,468,469,5,111,0,0,469,
        470,5,117,0,0,470,471,5,98,0,0,471,472,5,108,0,0,472,473,5,101,0,
        0,473,114,1,0,0,0,474,475,5,102,0,0,475,476,5,108,0,0,476,477,5,
        111,0,0,477,478,5,97,0,0,478,479,5,116,0,0,479,116,1,0,0,0,480,481,
        5,118,0,0,481,482,5,111,0,0,482,483,5,105,0,0,483,484,5,100,0,0,
        484,118,1,0,0,0,485,486,5,99,0,0,486,487,5,104,0,0,487,488,5,97,
        0,0,488,489,5,114,0,0,489,120,1,0,0,0,490,491,5,118,0,0,491,492,
        5,101,0,0,492,493,5,99,0,0,493,494,5,116,0,0,494,495,5,111,0,0,495,
        496,5,114,0,0,496,122,1,0,0,0,497,498,5,115,0,0,498,499,5,116,0,
        0,499,500,5,97,0,0,500,501,5,99,0,0,501,502,5,107,0,0,502,124,1,
        0,0,0,503,504,5,99,0,0,504,505,5,111,0,0,505,506,5,110,0,0,506,507,
        5,115,0,0,507,508,5,116,0,0,508,126,1,0,0,0,509,510,5,115,0,0,510,
        511,5,116,0,0,511,512,5,100,0,0,512,128,1,0,0,0,513,514,5,117,0,
        0,514,515,5,115,0,0,515,516,5,105,0,0,516,517,5,110,0,0,517,518,
        5,103,0,0,518,130,1,0,0,0,519,520,5,110,0,0,520,521,5,97,0,0,521,
        522,5,109,0,0,522,523,5,101,0,0,523,524,5,115,0,0,524,525,5,112,
        0,0,525,526,5,97,0,0,526,527,5,99,0,0,527,528,5,101,0,0,528,132,
        1,0,0,0,529,530,5,103,0,0,530,531,5,101,0,0,531,532,5,116,0,0,532,
        533,5,108,0,0,533,534,5,105,0,0,534,535,5,110,0,0,535,536,5,101,
        0,0,536,134,1,0,0,0,537,538,5,99,0,0,538,539,5,105,0,0,539,540,5,
        110,0,0,540,136,1,0,0,0,541,542,5,99,0,0,542,543,5,111,0,0,543,544,
        5,117,0,0,544,545,5,116,0,0,545,138,1,0,0,0,546,547,5,101,0,0,547,
        548,5,110,0,0,548,549,5,100,0,0,549,550,5,108,0,0,550,140,1,0,0,
        0,551,553,5,45,0,0,552,551,1,0,0,0,552,553,1,0,0,0,553,555,1,0,0,
        0,554,556,7,2,0,0,555,554,1,0,0,0,556,557,1,0,0,0,557,555,1,0,0,
        0,557,558,1,0,0,0,558,565,1,0,0,0,559,561,5,46,0,0,560,562,7,2,0,
        0,561,560,1,0,0,0,562,563,1,0,0,0,563,561,1,0,0,0,563,564,1,0,0,
        0,564,566,1,0,0,0,565,559,1,0,0,0,565,566,1,0,0,0,566,142,1,0,0,
        0,567,571,7,3,0,0,568,570,7,4,0,0,569,568,1,0,0,0,570,573,1,0,0,
        0,571,569,1,0,0,0,571,572,1,0,0,0,572,144,1,0,0,0,573,571,1,0,0,
        0,574,576,7,5,0,0,575,574,1,0,0,0,576,577,1,0,0,0,577,575,1,0,0,
        0,577,578,1,0,0,0,578,579,1,0,0,0,579,580,6,72,0,0,580,146,1,0,0,
        0,581,582,5,47,0,0,582,583,5,47,0,0,583,587,1,0,0,0,584,586,8,6,
        0,0,585,584,1,0,0,0,586,589,1,0,0,0,587,585,1,0,0,0,587,588,1,0,
        0,0,588,590,1,0,0,0,589,587,1,0,0,0,590,591,6,73,0,0,591,148,1,0,
        0,0,592,593,5,47,0,0,593,594,5,42,0,0,594,598,1,0,0,0,595,597,9,
        0,0,0,596,595,1,0,0,0,597,600,1,0,0,0,598,599,1,0,0,0,598,596,1,
        0,0,0,599,601,1,0,0,0,600,598,1,0,0,0,601,602,5,42,0,0,602,603,5,
        47,0,0,603,604,1,0,0,0,604,605,6,74,0,0,605,150,1,0,0,0,606,608,
        7,6,0,0,607,606,1,0,0,0,608,609,1,0,0,0,609,607,1,0,0,0,609,610,
        1,0,0,0,610,611,1,0,0,0,611,612,6,75,0,0,612,152,1,0,0,0,19,0,167,
        169,177,179,183,246,290,303,314,552,557,563,565,571,577,587,598,
        609,1,6,0,0
    ]

class cppLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    HASH = 1
    INCLUDE = 2
    StringLiteral = 3
    IncludeFileName = 4
    BACK_FUNCTION = 5
    FRONT_FUNCTION = 6
    BooleanLiteral = 7
    LEFT_SHIFT = 8
    RIGHT_SHIFT = 9
    EQUAL = 10
    PLUS_EQUAL = 11
    MINUS_EQUAL = 12
    NOT_EQUAL = 13
    LESS_EQUAL = 14
    GREATER_EQUAL = 15
    NOT = 16
    AND_OP = 17
    OR_OP = 18
    QUESTION = 19
    SEMICOLON = 20
    COMMA = 21
    DOT = 22
    ARROW = 23
    LPAREN = 24
    RPAREN = 25
    LBRACE = 26
    RBRACE = 27
    LBRACK = 28
    RBRACK = 29
    INCREMENT = 30
    DECREMENT = 31
    BITWISE_OR = 32
    BITWISE_XOR = 33
    BITWISE_NOT = 34
    DOUBLE_COLON = 35
    AMPERSAND = 36
    PLUS = 37
    MINUS = 38
    STAR = 39
    DIV = 40
    MOD = 41
    ASSIGN = 42
    LESS = 43
    GREATER = 44
    COLON = 45
    IF = 46
    ELSE = 47
    WHILE = 48
    FOR = 49
    RETURN = 50
    SIZE_T = 51
    STRING_STREAM = 52
    INT = 53
    STRING = 54
    BOOL = 55
    DOUBLE = 56
    FLOAT = 57
    VOID = 58
    CHAR = 59
    VECTOR = 60
    STACK = 61
    CONST = 62
    STD = 63
    USING = 64
    NAMESPACE = 65
    GET = 66
    CIN = 67
    COUT = 68
    ENDL = 69
    NUMBER = 70
    ID = 71
    WS = 72
    COMMENT = 73
    MULTILINE_COMMENT = 74
    NEWLINE = 75

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'#'", "'include'", "'<<'", "'>>'", "'=='", "'+='", "'-='", 
            "'!='", "'<='", "'>='", "'!'", "'&&'", "'||'", "'?'", "';'", 
            "','", "'.'", "'->'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
            "'++'", "'--'", "'|'", "'^'", "'~'", "'::'", "'&'", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'='", "'<'", "'>'", "':'", "'if'", "'else'", 
            "'while'", "'for'", "'return'", "'size_t'", "'stringstream'", 
            "'int'", "'string'", "'bool'", "'double'", "'float'", "'void'", 
            "'char'", "'vector'", "'stack'", "'const'", "'std'", "'using'", 
            "'namespace'", "'getline'", "'cin'", "'cout'", "'endl'" ]

    symbolicNames = [ "<INVALID>",
            "HASH", "INCLUDE", "StringLiteral", "IncludeFileName", "BACK_FUNCTION", 
            "FRONT_FUNCTION", "BooleanLiteral", "LEFT_SHIFT", "RIGHT_SHIFT", 
            "EQUAL", "PLUS_EQUAL", "MINUS_EQUAL", "NOT_EQUAL", "LESS_EQUAL", 
            "GREATER_EQUAL", "NOT", "AND_OP", "OR_OP", "QUESTION", "SEMICOLON", 
            "COMMA", "DOT", "ARROW", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
            "LBRACK", "RBRACK", "INCREMENT", "DECREMENT", "BITWISE_OR", 
            "BITWISE_XOR", "BITWISE_NOT", "DOUBLE_COLON", "AMPERSAND", "PLUS", 
            "MINUS", "STAR", "DIV", "MOD", "ASSIGN", "LESS", "GREATER", 
            "COLON", "IF", "ELSE", "WHILE", "FOR", "RETURN", "SIZE_T", "STRING_STREAM", 
            "INT", "STRING", "BOOL", "DOUBLE", "FLOAT", "VOID", "CHAR", 
            "VECTOR", "STACK", "CONST", "STD", "USING", "NAMESPACE", "GET", 
            "CIN", "COUT", "ENDL", "NUMBER", "ID", "WS", "COMMENT", "MULTILINE_COMMENT", 
            "NEWLINE" ]

    ruleNames = [ "HASH", "INCLUDE", "StringLiteral", "IncludeFileName", 
                  "LIBRARY_FILE", "BACK_FUNCTION", "FRONT_FUNCTION", "BooleanLiteral", 
                  "LEFT_SHIFT", "RIGHT_SHIFT", "EQUAL", "PLUS_EQUAL", "MINUS_EQUAL", 
                  "NOT_EQUAL", "LESS_EQUAL", "GREATER_EQUAL", "NOT", "AND_OP", 
                  "OR_OP", "QUESTION", "SEMICOLON", "COMMA", "DOT", "ARROW", 
                  "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
                  "INCREMENT", "DECREMENT", "BITWISE_OR", "BITWISE_XOR", 
                  "BITWISE_NOT", "DOUBLE_COLON", "AMPERSAND", "PLUS", "MINUS", 
                  "STAR", "DIV", "MOD", "ASSIGN", "LESS", "GREATER", "COLON", 
                  "IF", "ELSE", "WHILE", "FOR", "RETURN", "SIZE_T", "STRING_STREAM", 
                  "INT", "STRING", "BOOL", "DOUBLE", "FLOAT", "VOID", "CHAR", 
                  "VECTOR", "STACK", "CONST", "STD", "USING", "NAMESPACE", 
                  "GET", "CIN", "COUT", "ENDL", "NUMBER", "ID", "WS", "COMMENT", 
                  "MULTILINE_COMMENT", "NEWLINE" ]

    grammarFileName = "cpp.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

