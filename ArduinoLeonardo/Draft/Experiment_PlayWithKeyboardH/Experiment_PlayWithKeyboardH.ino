#include "Keyboard.h"
#include "Mouse.h"
// If you want your action to be resticted by the two first digit.
int between_min= 0;//1900000000; 
int between_max= 2000000000;

#define KEY_LEFT_CTRL     0x80
#define KEY_LEFT_SHIFT    0x81
#define KEY_LEFT_ALT      0x82
#define KEY_LEFT_GUI      0x83
#define KEY_RIGHT_CTRL    0x84
#define KEY_RIGHT_SHIFT   0x85
#define KEY_RIGHT_ALT     0x86
#define KEY_RIGHT_GUI     0x87
#define KEY_UP_ARROW      0xDA
#define KEY_DOWN_ARROW    0xD9
#define KEY_LEFT_ARROW    0xD8
#define KEY_RIGHT_ARROW   0xD7
#define KEY_BACKSPACE     0xB2
#define KEY_TAB           0xB3
#define KEY_RETURN        0xB0
#define KEY_MENU          0xED 
#define KEY_ESC           0xB1
#define KEY_INSERT        0xD1
#define KEY_DELETE        0xD4
#define KEY_PAGE_UP       0xD3
#define KEY_PAGE_DOWN     0xD6
#define KEY_HOME          0xD2
#define KEY_END           0xD5
#define KEY_CAPS_LOCK     0xC1
#define KEY_PRINT_SCREEN  0xCE 
#define KEY_SCROLL_LOCK   0xCF
#define KEY_PAUSE         0xD0
#define KEY_NUM_LOCK      0xDB
#define KEY_KP_SLASH      0xDC
#define KEY_KP_ASTERISK   0xDD
#define KEY_KP_MINUS      0xDE
#define KEY_KP_PLUS       0xDF
#define KEY_KP_ENTER      0xE0
#define KEY_KP_1          0xE1
#define KEY_KP_2          0xE2
#define KEY_KP_3          0xE3
#define KEY_KP_4          0xE4
#define KEY_KP_5          0xE5
#define KEY_KP_6          0xE6
#define KEY_KP_7          0xE7
#define KEY_KP_8          0xE8
#define KEY_KP_9          0xE9
#define KEY_KP_0          0xEA
#define KEY_KP_DOT        0xEB
#define KEY_F1            0xC2
#define KEY_F2            0xC3
#define KEY_F3            0xC4
#define KEY_F4            0xC5
#define KEY_F5            0xC6
#define KEY_F6            0xC7
#define KEY_F7            0xC8
#define KEY_F8            0xC9
#define KEY_F9            0xCA
#define KEY_F10           0xCB
#define KEY_F11           0xCC
#define KEY_F12           0xCD
#define KEY_F13           0xF0
#define KEY_F14           0xF1
#define KEY_F15           0xF2
#define KEY_F16           0xF3
#define KEY_F17           0xF4
#define KEY_F18           0xF5
#define KEY_F19           0xF6
#define KEY_F20           0xF7
#define KEY_F21           0xF8
#define KEY_F22           0xF9
#define KEY_F23           0xFA
#define KEY_F24           0xFB




void pressAllKeys(){
   int action =0;
    for (int ascii=0;ascii<255;ascii++) {
      action=3000+ascii;
      Serial.println(String(action));
      Keyboard.print("Start Simulating all keys");
      Keyboard.print(ascii);
      integerToActions(action);
      delay(1);
      action=4000+ascii;
      Serial.println(String(action));
      integerToActions(action);
      Keyboard.print('\n');
      delay(20);
    }
 

}
void integerToActions(int integer){
        Serial.println("INTEGER:"+String(integer));
    // START BY 1900000000
    //if(between_min <= integer && integer < between_max)
    {
      int fourDigit = integer%9999;
                  
        Serial.println("INTEGER:"+String(integer));
        Serial.println("FOUR DIGIT:"+String(fourDigit));
      if(integer>=6000){
        //1980307070  // Move of 30 Pixel
        //6001 =-1999 pixel 9999 +1999 pixel
          int x = ((integer/1000)%9999)-8000;
          int y = fourDigit-8000;
          Mouse.move(x, y);
      }
      else if(fourDigit>=4000){
      //4042 = press key number 42 as byte on the computer
        int value = fourDigit-4000;
        Keyboard.release(value);
        Serial.println("RELEASE:"+String(value));
      }else if(fourDigit>=3000){
      //3042 = press key number 42 as byte on the computer
        int value = fourDigit-3000;
        Serial.println("PRESS:"+String(value));
        Keyboard.press(value);
      }
    }
    switch(integer){
      case 1300: Mouse.press(MOUSE_LEFT); break;
      case 2300: Mouse.release(MOUSE_LEFT); break;
      case 1301: Mouse.press(MOUSE_MIDDLE); break;
      case 2301: Mouse.release(MOUSE_MIDDLE); break;
      case 1302: Mouse.press(MOUSE_RIGHT); break;
      case 2303: Mouse.release(MOUSE_RIGHT); break;
      case 1501: Mouse.move(0,0,1); break; // WHEEL UP
      case 2501: Mouse.move(0,0,-1); break;// WHEEL DOWN
      case 1502: Mouse.move(0,0,2); break;// WHEEL UP
      case 2502: Mouse.move(0,0,-2); break;// WHEEL DOWN
      case 1503: Mouse.move(0,0,3); break;// WHEEL UP
      case 2504: Mouse.move(0,0,-3); break;// WHEEL DOWN
      case 1511: Mouse.move(1,0); break; //MOVE RIGHT?
      case 2511: Mouse.move(-1,0); break;//MOVE LEFT?
      case 1522: Mouse.move(10,0); break;
      case 2522: Mouse.move(-10,0); break;
      case 1533: Mouse.move(100,0); break;
      case 2534: Mouse.move(-100,0); break;
      case 1611: Mouse.move(0,1); break;//MOVE UP?
      case 2611: Mouse.move(0,-1); break; //MOVE DOWN?
      case 1622: Mouse.move(0,10); break;
      case 2622: Mouse.move(0,-10); break;
      case 1633: Mouse.move(0,100); break;
      case 2634: Mouse.move(0,-100); break;
      //SOURCE/ https://github.com/arduino-libraries/Keyboard/blob/master/src/Keyboard.h#L35
      case 1400: Keyboard.releaseAll(); break;
      case 1401: Keyboard.end(); Keyboard.begin(KeyboardLayout_de_DE); Serial.println("KeyboardLayout_de_DE") ; break;
      case 1402: Keyboard.end(); Keyboard.begin(KeyboardLayout_en_US); Serial.println("KeyboardLayout_en_US") ; break;
      case 1403: Keyboard.end(); Keyboard.begin(KeyboardLayout_es_ES); Serial.println("KeyboardLayout_es_ES") ; break;
      case 1404: Keyboard.end(); Keyboard.begin(KeyboardLayout_fr_FR); Serial.println("KeyboardLayout_fr_FR") ; break;
      case 1405: Keyboard.end(); Keyboard.begin(KeyboardLayout_it_IT); Serial.println("KeyboardLayout_it_IT") ; break;
      case 1406: Keyboard.end(); Keyboard.begin(KeyboardLayout_pt_PT); Serial.println("KeyboardLayout_pt_PT") ; break;
      case 1407: Keyboard.end(); Keyboard.begin(KeyboardLayout_sv_SE); Serial.println("KeyboardLayout_sv_SE") ; break;
      case 1408: Keyboard.end(); Keyboard.begin(KeyboardLayout_da_DK); Serial.println("KeyboardLayout_da_DK") ; break;
      case 1409: Keyboard.end(); Keyboard.begin(KeyboardLayout_hu_HU); Serial.println("KeyboardLayout_hu_HU") ; break;

        case 1000: Keyboard.releaseAll();break;
        //Key	Decimal	Hexadecimal	Press	Release
        case 1008: Keyboard.press(KEY_BACKSPACE); break;  //Backspace	8	0x08	1008	2008
        case 1009: Keyboard.press(KEY_TAB); break;  //Tab	9	0x09	1009	2009
        case 1012: Keyboard.press(' '); break;  //Clear	12	0x0C	1012	2012
        case 1013: Keyboard.press(KEY_RETURN); break;  //Enter	13	0x0D	1013	2013  ///KEY_KP_ENTER
        case 1016: Keyboard.press(KEY_LEFT_SHIFT); break;  //Shift	16	0x10	1016	2016
        case 1017: Keyboard.press(KEY_LEFT_CTRL); break;  //Ctrl	17	0x11	1017	2017
        case 1018: Keyboard.press(KEY_LEFT_ALT); break;  //Alt	18	0x12	1018	2018
        case 1019: Keyboard.press(KEY_PAUSE); break;  //Pause	19	0x13	1019	2019
        case 1020: Keyboard.press(KEY_CAPS_LOCK); break;  //CapsLock	20	0x14	1020	2020
        case 1027: Keyboard.press(KEY_ESC); break;  //Escape	27	0x1B	1027	2027
        case 1032: Keyboard.press(' '); break;  //Space	32	0x20	1032	2032
        case 1033: Keyboard.press(KEY_PAGE_UP); break;  //PageUp	33	0x21	1033	2033
        case 1034: Keyboard.press(KEY_PAGE_DOWN); break;  //PageDown	34	0x22	1034	2034
        case 1035: Keyboard.press(KEY_END); break;  //End	35	0x23	1035	2035
        case 1036: Keyboard.press(KEY_HOME); break;  //Home	36	0x24	1036	2036
        case 1037: Keyboard.press(KEY_LEFT_ARROW); break;  //LeftArrow	37	0x25	1037	2037
        case 1038: Keyboard.press(KEY_UP_ARROW); break;  //UpArrow	38	0x26	1038	2038
        case 1039: Keyboard.press(KEY_RIGHT_ARROW); break;  //RightArrow	39	0x27	1039	2039
        case 1040: Keyboard.press(KEY_DOWN_ARROW); break;  //DownArrow	40	0x28	1040	2040
        case 1041: Keyboard.press(' '); break;  //Select	41	0x29	1041	2041
        case 1042: Keyboard.press(KEY_PRINT_SCREEN); break;  //Print	42	0x2A	1042	2042
        case 1043: Keyboard.press(' '); break;  //Execute	43	0x2B	1043	2043
        case 1044: Keyboard.press(KEY_PRINT_SCREEN); break;  //PrintScreen	44	0x2C	1044	2044              
        case 1045: Keyboard.press(KEY_INSERT); break;  //Insert	45	0x2D	1045	2045
        case 1046: Keyboard.press(KEY_DELETE); break;  //Delete	46	0x2E	1046	2046
        case 1048: Keyboard.press('0'); break;  //0	48	0x30	1048	2048
        case 1049: Keyboard.press('1'); break;  //1	49	0x31	1049	2049
        case 1050: Keyboard.press('2'); break;  //2	50	0x32	1050	2050
        case 1051: Keyboard.press('3'); break;  //3	51	0x33	1051	2051
        case 1052: Keyboard.press('4'); break;  //4	52	0x34	1052	2052
        case 1053: Keyboard.press('5'); break;  //5	53	0x35	1053	2053
        case 1054: Keyboard.press('6'); break;  //6	54	0x36	1054	2054
        case 1055: Keyboard.press('7'); break;  //7	55	0x37	1055	2055
        case 1056: Keyboard.press('8'); break;  //8	56	0x38	1056	2056
        case 1057: Keyboard.press('9'); break;  //9	57	0x39	1057	2057
        case 1065: Keyboard.press('A'); break;  //A	65	0x41	1065	2065
        case 1066: Keyboard.press('B'); break;  //B	66	0x42	1066	2066
        case 1067: Keyboard.press('C'); break;  //C	67	0x43	1067	2067
        case 1068: Keyboard.press('D'); break;  //D	68	0x44	1068	2068
        case 1069: Keyboard.press('E'); break;  //E	69	0x45	1069	2069
        case 1070: Keyboard.press('F'); break;  //F	70	0x46	1070	2070
        case 1071: Keyboard.press('G'); break;  //G	71	0x47	1071	2071
        case 1072: Keyboard.press('H'); break;  //H	72	0x48	1072	2072
        case 1073: Keyboard.press('I'); break;  //I	73	0x49	1073	2073
        case 1074: Keyboard.press('J'); break;  //J	74	0x4A	1074	2074
        case 1075: Keyboard.press('K'); break;  //K	75	0x4B	1075	2075
        case 1076: Keyboard.press('L'); break;  //L	76	0x4C	1076	2076
        case 1077: Keyboard.press('M'); break;  //M	77	0x4D	1077	2077
        case 1078: Keyboard.press('N'); break;  //N	78	0x4E	1078	2078
        case 1079: Keyboard.press('O'); break;  //O	79	0x4F	1079	2079
        case 1080: Keyboard.press('P'); break;  //P	80	0x50	1080	2080
        case 1081: Keyboard.press('Q'); break;  //Q	81	0x51	1081	2081
        case 1082: Keyboard.press('R'); break;  //R	82	0x52	1082	2082
        case 1083: Keyboard.press('S'); break;  //S	83	0x53	1083	2083
        case 1084: Keyboard.press('T'); break;  //T	84	0x54	1084	2084
        case 1085: Keyboard.press('U'); break;  //U	85	0x55	1085	2085
        case 1086: Keyboard.press('V'); break;  //V	86	0x56	1086	2086
        case 1087: Keyboard.press('W'); break;  //W	87	0x57	1087	2087
        case 1088: Keyboard.press('X'); break;  //X	88	0x58	1088	2088
        case 1089: Keyboard.press('Y'); break;  //Y	89	0x59	1089	2089
        case 1090: Keyboard.press('Z'); break;  //Z	90	0x5A	1090	2090
        case 1091: Keyboard.press(KEY_BACKSPACE); break;  //LeftWindows	91	0x5B	1091	2091
        case 1092: Keyboard.press(' '); break;  //RightWindows	92	0x5C	1092	2092
        case 1093: Keyboard.press(KEY_MENU   ); break;  //Applications	93	0x5D	1093	2093
        case 1095: Keyboard.press(' '); break;  //Sleep	95	0x5F	1095	2095
        case 1096: Keyboard.press(KEY_KP_0); break;  //Numpad0	96	0x60	1096	2096
        case 1097: Keyboard.press(KEY_KP_1); break;  //Numpad1	97	0x61	1097	2097
        case 1098: Keyboard.press(KEY_KP_2); break;  //Numpad2	98	0x62	1098	2098
        case 1099: Keyboard.press(KEY_KP_3); break;  //Numpad3	99	0x63	1099	2099
        case 1100: Keyboard.press(KEY_KP_4); break;  //Numpad4	100	0x64	1100	2100
        case 1101: Keyboard.press(KEY_KP_5); break;  //Numpad5	101	0x65	1101	2101
        case 1102: Keyboard.press(KEY_KP_6); break;  //Numpad6	102	0x66	1102	2102
        case 1103: Keyboard.press(KEY_KP_7); break;  //Numpad7	103	0x67	1103	2103
        case 1104: Keyboard.press(KEY_KP_8); break;  //Numpad8	104	0x68	1104	2104
        case 1105: Keyboard.press(KEY_KP_9); break;  //Numpad9	105	0x69	1105	2105
        case 1106: Keyboard.press(KEY_KP_ASTERISK); break;  //Multiply	106	0x6A	1106	2106
        case 1107: Keyboard.press(KEY_KP_PLUS); break;  //Add	107	0x6B	1107	2107
        case 1108: Keyboard.press(' '); break;  //Separator	108	0x6C	1108	2108
        case 1109: Keyboard.press(KEY_KP_MINUS); break;  //Subtract	109	0x6D	1109	2109
        case 1110: Keyboard.press(KEY_KP_DOT); break;  //Decimal	110	0x6E	1110	2110
        case 1111: Keyboard.press(KEY_KP_SLASH); break;  //Divide	111	0x6F	1111	2111
        case 1112: Keyboard.press( KEY_F1); break;  //F1	112	0x70	1112	2112
        case 1113: Keyboard.press( KEY_F2); break;  //F2	113	0x71	1113	2113
        case 1114: Keyboard.press( KEY_F3); break;  //F3	114	0x72	1114	2114
        case 1115: Keyboard.press( KEY_F4); break;  //F4	115	0x73	1115	2115
        case 1116: Keyboard.press( KEY_F5); break;  //F5	116	0x74	1116	2116
        case 1117: Keyboard.press( KEY_F6); break;  //F6	117	0x75	1117	2117
        case 1118: Keyboard.press( KEY_F7); break;  //F7	118	0x76	1118	2118
        case 1119: Keyboard.press( KEY_F8); break;  //F8	119	0x77	1119	2119
        case 1120: Keyboard.press( KEY_F9); break;  //F9	120	0x78	1120	2120
        case 1121: Keyboard.press(KEY_F10); break;  //F10	121	0x79	1121	2121
        case 1122: Keyboard.press(KEY_F11); break;  //F11	122	0x7A	1122	2122
        case 1123: Keyboard.press(KEY_F12); break;  //F12	123	0x7B	1123	2123
        case 1124: Keyboard.press(KEY_F13); break;  //F13	124	0x7C	1124	2124
        case 1125: Keyboard.press(KEY_F14); break;  //F14	125	0x7D	1125	2125
        case 1126: Keyboard.press(KEY_F15); break;  //F15	126	0x7E	1126	2126
        case 1127: Keyboard.press(KEY_F16); break;  //F16	127	0x7F	1127	2127
        case 1128: Keyboard.press(KEY_F17); break;  //F17	128	0x80	1128	2128
        case 1129: Keyboard.press(KEY_F18); break;  //F18	129	0x81	1129	2129
        case 1130: Keyboard.press(KEY_F19); break;  //F19	130	0x82	1130	2130
        case 1131: Keyboard.press(KEY_F20); break;  //F20	131	0x83	1131	2131
        case 1132: Keyboard.press(KEY_F21); break;  //F21	132	0x84	1132	2132
        case 1133: Keyboard.press(KEY_F22); break;  //F22	133	0x85	1133	2133
        case 1134: Keyboard.press(KEY_F23); break;  //F23	134	0x86	1134	2134
        case 1135: Keyboard.press(KEY_F24); break;  //F24	135	0x87	1135	2135
        case 1144: Keyboard.press(KEY_NUM_LOCK); break;  //NumLock	144	0x90	1144	2144
        case 1145: Keyboard.press(KEY_SCROLL_LOCK            ); break;  //ScrollLock	145	0x91	1145	2145
        case 1160: Keyboard.press(KEY_LEFT_SHIFT            ); break;  //LeftShift	160	0xA0	1160	2160
        case 1161: Keyboard.press(KEY_RIGHT_SHIFT            ); break;  //RightShift	161	0xA1	1161	2161
        case 1162: Keyboard.press(KEY_LEFT_CTRL            ); break;  //LeftControl	162	0xA2	1162	2162
        case 1163: Keyboard.press(KEY_RIGHT_CTRL); break;  //RightControl	163	0xA3	1163	2163
        case 1164: Keyboard.press(KEY_LEFT_ALT); break;  //LeftAlt	164	0xA4	1164	2164
        case 1165: Keyboard.press(KEY_RIGHT_ALT); break;  //RightAlt	165	0xA5	1165	2165
        case 1166: Keyboard.press(' '); break;  //BrowserBack	166	0xA6	1166	2166
        case 1167: Keyboard.press(' '); break;  //BrowserForward	167	0xA7	1167	2177
        case 1168: Keyboard.press(' '); break;  //BrowserRefresh	168	0xA8	1168	2168
        case 1169: Keyboard.press(' '); break;  //BrowserStop	169	0xA9	1169	2169
        case 1170: Keyboard.press(' '); break;  //BrowserSearch	170	0xAA	1170	2170
        case 1171: Keyboard.press(' '); break;  //BrowserFavorites	171	0xAB	1171	2171
        case 1172: Keyboard.press(' '); break;  //BrowserHome	172	0xAC	1172	2172
        case 1173: Keyboard.press(' '); break;  //VolumeMute	173	0xAD	1173	2173
        case 1174: Keyboard.press(' '); break;  //VolumeDown	174	0xAE	1174	2174
        case 1175: Keyboard.press(' '); break;  //VolumeUp	175	0xAF	1175	2175
        case 1176: Keyboard.press(' '); break;  //MediaNextTrack	176	0xB0	1176	2176
        case 1177: Keyboard.press(' '); break;  //MediaPreviousTrack	177	0xB1	1177	2177
        case 1178: Keyboard.press(' '); break;  //MediaStop	178	0xB2	1178	2178
        case 1179: Keyboard.press(' '); break;  //MediaPlay	179	0xB3	1179	2179
        case 1180: Keyboard.press(' '); break;  //LaunchMail	180	0xB4	1180	2180
        case 1181: Keyboard.press(' '); break;  //LaunchMediaSelect	181	0xB5	1181	2181
        case 1182: Keyboard.press(' '); break;  //LaunchApp1	182	0xB6	1182	2182
        case 1183: Keyboard.press(' '); break;  //LaunchApp2	183	0xB7	1183	2183
        case 1186: Keyboard.press(' '); break;  //OEM1	186	0xBA	1186	2186
        case 1187: Keyboard.press(' '); break;  //OEMPlus	187	0xBB	1187	2187
        case 1188: Keyboard.press(' '); break;  //OEMComma	188	0xBC	1188	2188
        case 1189: Keyboard.press(' '); break;  //OEMMinus	189	0xBD	1189	2189
        case 1190: Keyboard.press(' '); break;  //OEMPeriod	190	0xBE	1190	2190
        case 1191: Keyboard.press(' '); break;  //OEM2	191	0xBF	1191	2191
        case 1192: Keyboard.press(' '); break;  //OEM3	192	0xC0	1192	2192
        case 1219: Keyboard.press(' '); break;  //OEM4	219	0xDB	1219	2219
        case 1220: Keyboard.press(' '); break;  //OEM5	220	0xDC	1220	2220
        case 1221: Keyboard.press(' '); break;  //OEM6	221	0xDD	1221	2221
        case 1222: Keyboard.press(' '); break;  //OEM7	222	0xDE	1222	2222
        case 1223: Keyboard.press(' '); break;  //OEM8	223	0xDF	1223	2223
        case 1226: Keyboard.press(' '); break;  //OEM102	226	0xE2	1226	2226
        case 1229: Keyboard.press(' '); break;  //ProcessKey	229	0xE5	1229	2229
        case 1231: Keyboard.press(' '); break;  //Packet	231	0xE7	1231	2231
        case 1246: Keyboard.press(' '); break;  //Attn	246	0xF6	1246	2246
        case 1247: Keyboard.press(' '); break;  //CrSel	247	0xF7	1247	2247
        case 1248: Keyboard.press(' '); break;  //ExSel	248	0xF8	1248	2248
        case 1249: Keyboard.press(' '); break;  //EraseEOF	249	0xF9	1249	2249
        case 1250: Keyboard.press(' '); break;  //Play	250	0xFA	1250	2250
        case 1251: Keyboard.press(' '); break;  //Zoom	251	0xFB	1251	2251
        case 1253: Keyboard.press(' '); break;  //PA1	253	0xFD	1253	2253


        case 2000: Keyboard.releaseAll();break;
        case 2008: Keyboard.release(KEY_BACKSPACE); break;  //Backspace	8	0x08	1008	2008
        case 2009: Keyboard.release(KEY_TAB); break;  //Tab	9	0x09	1009	2009
        case 2012: Keyboard.release(' '); break;  //Clear	12	0x0C	1012	2012
        case 2013: Keyboard.release(KEY_RETURN); break;  //Enter	13	0x0D	1013	2013  ///KEY_KP_ENTER
        case 2016: Keyboard.release(KEY_LEFT_SHIFT); break;  //Shift	16	0x10	1016	2016
        case 2017: Keyboard.release(KEY_LEFT_CTRL); break;  //Ctrl	17	0x11	1017	2017
        case 2018: Keyboard.release(KEY_LEFT_ALT); break;  //Alt	18	0x12	1018	2018
        case 2019: Keyboard.release(KEY_PAUSE); break;  //Pause	19	0x13	1019	2019
        case 2020: Keyboard.release(KEY_CAPS_LOCK); break;  //CapsLock	20	0x14	1020	2020
        case 2027: Keyboard.release(KEY_ESC); break;  //Escape	27	0x1B	1027	2027
        case 2032: Keyboard.release(' '); break;  //Space	32	0x20	1032	2032
        case 2033: Keyboard.release(KEY_PAGE_UP); break;  //PageUp	33	0x21	1033	2033
        case 2034: Keyboard.release(KEY_PAGE_DOWN); break;  //PageDown	34	0x22	1034	2034
        case 2035: Keyboard.release(KEY_END); break;  //End	35	0x23	1035	2035
        case 2036: Keyboard.release(KEY_HOME); break;  //Home	36	0x24	1036	2036
        case 2037: Keyboard.release(KEY_LEFT_ARROW); break;  //LeftArrow	37	0x25	1037	2037
        case 2038: Keyboard.release(KEY_UP_ARROW); break;  //UpArrow	38	0x26	1038	2038
        case 2039: Keyboard.release(KEY_RIGHT_ARROW); break;  //RightArrow	39	0x27	1039	2039
        case 2040: Keyboard.release(KEY_DOWN_ARROW); break;  //DownArrow	40	0x28	1040	2040
        case 2041: Keyboard.release(' '); break;  //Select	41	0x29	1041	2041
        case 2042: Keyboard.release(KEY_PRINT_SCREEN); break;  //Print	42	0x2A	1042	2042
        case 2043: Keyboard.release(' '); break;  //Execute	43	0x2B	1043	2043
        case 2044: Keyboard.release(KEY_PRINT_SCREEN); break;  //PrintScreen	44	0x2C	1044	2044              
        case 2045: Keyboard.release(KEY_INSERT); break;  //Insert	45	0x2D	1045	2045
        case 2046: Keyboard.release(KEY_DELETE); break;  //Delete	46	0x2E	1046	2046
        case 2048: Keyboard.release('0'); break;  //0	48	0x30	1048	2048
        case 2049: Keyboard.release('1'); break;  //1	49	0x31	1049	2049
        case 2050: Keyboard.release('2'); break;  //2	50	0x32	1050	2050
        case 2051: Keyboard.release('3'); break;  //3	51	0x33	1051	2051
        case 2052: Keyboard.release('4'); break;  //4	52	0x34	1052	2052
        case 2053: Keyboard.release('5'); break;  //5	53	0x35	1053	2053
        case 2054: Keyboard.release('6'); break;  //6	54	0x36	1054	2054
        case 2055: Keyboard.release('7'); break;  //7	55	0x37	1055	2055
        case 2056: Keyboard.release('8'); break;  //8	56	0x38	1056	2056
        case 2057: Keyboard.release('9'); break;  //9	57	0x39	1057	2057
        case 2065: Keyboard.release('A'); break;  //A	65	0x41	1065	2065
        case 2066: Keyboard.release('B'); break;  //B	66	0x42	1066	2066
        case 2067: Keyboard.release('C'); break;  //C	67	0x43	1067	2067
        case 2068: Keyboard.release('D'); break;  //D	68	0x44	1068	2068
        case 2069: Keyboard.release('E'); break;  //E	69	0x45	1069	2069
        case 2070: Keyboard.release('F'); break;  //F	70	0x46	1070	2070
        case 2071: Keyboard.release('G'); break;  //G	71	0x47	1071	2071
        case 2072: Keyboard.release('H'); break;  //H	72	0x48	1072	2072
        case 2073: Keyboard.release('I'); break;  //I	73	0x49	1073	2073
        case 2074: Keyboard.release('J'); break;  //J	74	0x4A	1074	2074
        case 2075: Keyboard.release('K'); break;  //K	75	0x4B	1075	2075
        case 2076: Keyboard.release('L'); break;  //L	76	0x4C	1076	2076
        case 2077: Keyboard.release('M'); break;  //M	77	0x4D	1077	2077
        case 2078: Keyboard.release('N'); break;  //N	78	0x4E	1078	2078
        case 2079: Keyboard.release('O'); break;  //O	79	0x4F	1079	2079
        case 2080: Keyboard.release('P'); break;  //P	80	0x50	1080	2080
        case 2081: Keyboard.release('Q'); break;  //Q	81	0x51	1081	2081
        case 2082: Keyboard.release('R'); break;  //R	82	0x52	1082	2082
        case 2083: Keyboard.release('S'); break;  //S	83	0x53	1083	2083
        case 2084: Keyboard.release('T'); break;  //T	84	0x54	1084	2084
        case 2085: Keyboard.release('U'); break;  //U	85	0x55	1085	2085
        case 2086: Keyboard.release('V'); break;  //V	86	0x56	1086	2086
        case 2087: Keyboard.release('W'); break;  //W	87	0x57	1087	2087
        case 2088: Keyboard.release('X'); break;  //X	88	0x58	1088	2088
        case 2089: Keyboard.release('Y'); break;  //Y	89	0x59	1089	2089
        case 2090: Keyboard.release('Z'); break;  //Z	90	0x5A	1090	2090
        case 2091: Keyboard.release(KEY_BACKSPACE); break;  //LeftWindows	91	0x5B	1091	2091
        case 2092: Keyboard.release(' '); break;  //RightWindows	92	0x5C	1092	2092
        case 2093: Keyboard.release(KEY_MENU   ); break;  //Applications	93	0x5D	1093	2093
        case 2095: Keyboard.release(' '); break;  //Sleep	95	0x5F	1095	2095
        case 2096: Keyboard.release(KEY_KP_0); break;  //Numpad0	96	0x60	1096	2096
        case 2097: Keyboard.release(KEY_KP_1); break;  //Numpad1	97	0x61	1097	2097
        case 2098: Keyboard.release(KEY_KP_2); break;  //Numpad2	98	0x62	1098	2098
        case 2099: Keyboard.release(KEY_KP_3); break;  //Numpad3	99	0x63	1099	2099
        case 2100: Keyboard.release(KEY_KP_4); break;  //Numpad4	100	0x64	1100	2100
        case 2101: Keyboard.release(KEY_KP_5); break;  //Numpad5	101	0x65	1101	2101
        case 2102: Keyboard.release(KEY_KP_6); break;  //Numpad6	102	0x66	1102	2102
        case 2103: Keyboard.release(KEY_KP_7); break;  //Numpad7	103	0x67	1103	2103
        case 2104: Keyboard.release(KEY_KP_8); break;  //Numpad8	104	0x68	1104	2104
        case 2105: Keyboard.release(KEY_KP_9); break;  //Numpad9	105	0x69	1105	2105
        case 2106: Keyboard.release(KEY_KP_ASTERISK); break;  //Multiply	106	0x6A	1106	2106
        case 2107: Keyboard.release(KEY_KP_PLUS); break;  //Add	107	0x6B	1107	2107
        case 2108: Keyboard.release(' '); break;  //Separator	108	0x6C	1108	2108
        case 2109: Keyboard.release(KEY_KP_MINUS); break;  //Subtract	109	0x6D	1109	2109
        case 2110: Keyboard.release(KEY_KP_DOT); break;  //Decimal	110	0x6E	1110	2110
        case 2111: Keyboard.release(KEY_KP_SLASH); break;  //Divide	111	0x6F	1111	2111
        case 2112: Keyboard.release( KEY_F1); break;  //F1	112	0x70	1112	2112
        case 2113: Keyboard.release( KEY_F2); break;  //F2	113	0x71	1113	2113
        case 2114: Keyboard.release( KEY_F3); break;  //F3	114	0x72	1114	2114
        case 2115: Keyboard.release( KEY_F4); break;  //F4	115	0x73	1115	2115
        case 2116: Keyboard.release( KEY_F5); break;  //F5	116	0x74	1116	2116
        case 2117: Keyboard.release( KEY_F6); break;  //F6	117	0x75	1117	2117
        case 2118: Keyboard.release( KEY_F7); break;  //F7	118	0x76	1118	2118
        case 2119: Keyboard.release( KEY_F8); break;  //F8	119	0x77	1119	2119
        case 2120: Keyboard.release( KEY_F9); break;  //F9	120	0x78	1120	2120
        case 2121: Keyboard.release(KEY_F10); break;  //F10	121	0x79	1121	2121
        case 2122: Keyboard.release(KEY_F11); break;  //F11	122	0x7A	1122	2122
        case 2123: Keyboard.release(KEY_F12); break;  //F12	123	0x7B	1123	2123
        case 2124: Keyboard.release(KEY_F13); break;  //F13	124	0x7C	1124	2124
        case 2125: Keyboard.release(KEY_F14); break;  //F14	125	0x7D	1125	2125
        case 2126: Keyboard.release(KEY_F15); break;  //F15	126	0x7E	1126	2126
        case 2127: Keyboard.release(KEY_F16); break;  //F16	127	0x7F	1127	2127
        case 2128: Keyboard.release(KEY_F17); break;  //F17	128	0x80	1128	2128
        case 2129: Keyboard.release(KEY_F18); break;  //F18	129	0x81	1129	2129
        case 2130: Keyboard.release(KEY_F19); break;  //F19	130	0x82	1130	2130
        case 2131: Keyboard.release(KEY_F20); break;  //F20	131	0x83	1131	2131
        case 2132: Keyboard.release(KEY_F21); break;  //F21	132	0x84	1132	2132
        case 2133: Keyboard.release(KEY_F22); break;  //F22	133	0x85	1133	2133
        case 2134: Keyboard.release(KEY_F23); break;  //F23	134	0x86	1134	2134
        case 2135: Keyboard.release(KEY_F24); break;  //F24	135	0x87	1135	2135
        case 2144: Keyboard.release(KEY_NUM_LOCK); break;  //NumLock	144	0x90	1144	2144
        case 2145: Keyboard.release(KEY_SCROLL_LOCK            ); break;  //ScrollLock	145	0x91	1145	2145
        case 2160: Keyboard.release(KEY_LEFT_SHIFT            ); break;  //LeftShift	160	0xA0	1160	2160
        case 2161: Keyboard.release(KEY_RIGHT_SHIFT            ); break;  //RightShift	161	0xA1	1161	2161
        case 2162: Keyboard.release(KEY_LEFT_CTRL            ); break;  //LeftControl	162	0xA2	1162	2162
        case 2163: Keyboard.release(KEY_RIGHT_CTRL); break;  //RightControl	163	0xA3	1163	2163
        case 2164: Keyboard.release(KEY_LEFT_ALT); break;  //LeftAlt	164	0xA4	1164	2164
        case 2165: Keyboard.release(KEY_RIGHT_ALT); break;  //RightAlt	165	0xA5	1165	2165
        case 2166: Keyboard.release(' '); break;  //BrowserBack	166	0xA6	1166	2166
        case 2167: Keyboard.release(' '); break;  //BrowserForward	167	0xA7	1167	2177
        case 2168: Keyboard.release(' '); break;  //BrowserRefresh	168	0xA8	1168	2168
        case 2169: Keyboard.release(' '); break;  //BrowserStop	169	0xA9	1169	2169
        case 2170: Keyboard.release(' '); break;  //BrowserSearch	170	0xAA	1170	2170
        case 2171: Keyboard.release(' '); break;  //BrowserFavorites	171	0xAB	1171	2171
        case 2172: Keyboard.release(' '); break;  //BrowserHome	172	0xAC	1172	2172
        case 2173: Keyboard.release(' '); break;  //VolumeMute	173	0xAD	1173	2173
        case 2174: Keyboard.release(' '); break;  //VolumeDown	174	0xAE	1174	2174
        case 2175: Keyboard.release(' '); break;  //VolumeUp	175	0xAF	1175	2175
        case 2176: Keyboard.release(' '); break;  //MediaNextTrack	176	0xB0	1176	2176
        case 2177: Keyboard.release(' '); break;  //MediaPreviousTrack	177	0xB1	1177	2177
        case 2178: Keyboard.release(' '); break;  //MediaStop	178	0xB2	1178	2178
        case 2179: Keyboard.release(' '); break;  //MediaPlay	179	0xB3	1179	2179
        case 2180: Keyboard.release(' '); break;  //LaunchMail	180	0xB4	1180	2180
        case 2181: Keyboard.release(' '); break;  //LaunchMediaSelect	181	0xB5	1181	2181
        case 2182: Keyboard.release(' '); break;  //LaunchApp1	182	0xB6	1182	2182
        case 2183: Keyboard.release(' '); break;  //LaunchApp2	183	0xB7	1183	2183
        case 2186: Keyboard.release(' '); break;  //OEM1	186	0xBA	1186	2186
        case 2187: Keyboard.release(' '); break;  //OEMPlus	187	0xBB	1187	2187
        case 2188: Keyboard.release(' '); break;  //OEMComma	188	0xBC	1188	2188
        case 2189: Keyboard.release(' '); break;  //OEMMinus	189	0xBD	1189	2189
        case 2190: Keyboard.release(' '); break;  //OEMPeriod	190	0xBE	1190	2190
        case 2191: Keyboard.release(' '); break;  //OEM2	191	0xBF	1191	2191
        case 2192: Keyboard.release(' '); break;  //OEM3	192	0xC0	1192	2192
        case 2219: Keyboard.release(' '); break;  //OEM4	219	0xDB	1219	2219
        case 2220: Keyboard.release(' '); break;  //OEM5	220	0xDC	1220	2220
        case 2221: Keyboard.release(' '); break;  //OEM6	221	0xDD	1221	2221
        case 2222: Keyboard.release(' '); break;  //OEM7	222	0xDE	1222	2222
        case 2223: Keyboard.release(' '); break;  //OEM8	223	0xDF	1223	2223
        case 2226: Keyboard.release(' '); break;  //OEM102	226	0xE2	1226	2226
        case 2229: Keyboard.release(' '); break;  //ProcessKey	229	0xE5	1229	2229
        case 2231: Keyboard.release(' '); break;  //Packet	231	0xE7	1231	2231
        case 2246: Keyboard.release(' '); break;  //Attn	246	0xF6	1246	2246
        case 2247: Keyboard.release(' '); break;  //CrSel	247	0xF7	1247	2247
        case 2248: Keyboard.release(' '); break;  //ExSel	248	0xF8	1248	2248
        case 2249: Keyboard.release(' '); break;  //EraseEOF	249	0xF9	1249	2249
        case 2250: Keyboard.release(' '); break;  //Play	250	0xFA	1250	2250
        case 2251: Keyboard.release(' '); break;  //Zoom	251	0xFB	1251	2251
        case 2253: Keyboard.release(' '); break;  //PA1	253	0xFD	1253	2253

        case 42: pressAllKeys();break; 
    }

}



void setup() {
  Serial.begin(9600);
  Keyboard.begin(KeyboardLayout_fr_FR);
  Mouse.begin();
  delay(2000);
}


int8_t index;
void loop() {

 
    delay(1000);


}
