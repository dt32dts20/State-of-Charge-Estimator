from LUT import LUT

###################################################################################################
# BATTERY CLASS LUT DATA
###################################################################################################

x_vals = [0,20,40,60,80,100]
y_vals = [500,5000,8000,10000,8000,15000]
points = zip(x_vals,y_vals)
C1_lut = LUT(points)

x_vals = [0,20,40,60,80,100]
y_vals = [5000,100000,80000,90000,220000,280000]
points = zip(x_vals,y_vals)
C2_lut = LUT(points)

points = ((100.17478103363105, 7.991429534779783  ),
(95.15576604903906, 3.19043997145792    ),
(90.018818953823, 3.304137817471826     ),
(79.89296720013174, 3.745011016929219   ),
(70.20308787667312, 3.4374387403846924  ),
(60.22026017203662, 3.2370952944774203  ),
(49.94636598160448, 3.464490986505247   ),
(40.1140899075519, 3.9049721244246456   ),
(29.98698355693911, 4.132171785683475   ),
(24.99682430154239, 4.245673600928406   ),
(20.007292344606427, 4.466012185272604  ),
(15.017133089209707, 4.57951400051752   ),
(9.88081329245442, 4.800048615630708    ),
(4.890654037057672, 4.913550430875624   ),
(0.0, 5.0   ))
R0_lut = LUT(points)

x_vals = [0,20,40,60,80,100]
y_vals = [1.0,0.8,0.4,0.2,0.1,0.05]
y_vals[:] = [x / 1000 for x in y_vals]
points = zip(x_vals,y_vals)
R1_lut = LUT(points)

x_vals = [0,20,40,60,80,100]
y_vals = [1.0,0.8,0.4,0.2,0.1,0.05]
y_vals[:] = [x / 1000 for x in y_vals]
points = zip(x_vals,y_vals)
R2_lut = LUT(points)

points = ((0.0,0.0),
(4.6360153300 ,3.102851711),
(6.0153256699 ,3.149239544),
(7.854406130  ,3.204752852),
(10.0         ,3.222243346),
(11.9923371   ,3.228326996),
(13.98467433  ,3.234410646),
(15.9770114   ,3.243536122),
(17.9693486   ,3.253422053),
(19.96168582  ,3.265589354),
(21.95402299  ,3.273193916),
(23.94636015  ,3.280038023),
(25.93869732  ,3.286882129),
(27.93103447  ,3.292965779),
(29.92337165  ,3.29904943 ),
(31.91570880  ,3.302851711),
(33.90804598  ,3.306653992),
(35.90038314  ,3.308174905),
(37.89272031  ,3.308174905),
(40.03831418  ,3.308935361),
(42.03065134  ,3.308935361),
(43.8697318   ,3.308935361),
(45.86206897  ,3.308935361),
(48.00766284  ,3.308935361),
(50.0         ,3.309695817),
(51.83908046  ,3.309695817),
(53.98467433  ,3.310456274),
(55.97701149  ,3.31121673 ),
(57.96934866  ,3.31121673 ),
(59.96168582  ,3.31121673 ),
(61.95402299  ,3.312737643),
(63.94636015  ,3.312737643),
(65.93869732  ,3.314258555),
(67.93103448  ,3.31730038 ),
(69.92337165  ,3.322623574),
(71.91570881  ,3.330988593),
(73.90804598  ,3.339353612),
(75.74712644  ,3.343155894),
(77.89272031  ,3.343155894),
(79.88505746  ,3.343155894),
(81.87739464  ,3.343155894),
(83.8697318   ,3.343155894),
(86.01532567  ,3.342395437),
(88.00766284  ,3.343155894),
(89.8467433   ,3.342395437),
(91.992337165 ,3.34391635 ),
(93.831417625 ,3.34391635 ),
(95.977011494 ,3.344676806),
(97.969348659 ,3.366730038),
(98.429118774 ,3.397148289),
(100          ,3.5))
OCVCharge_lut = LUT(points)

points = ((0                  ,0),
(5.4022988505747378 ,3.1013307984790872),
(5.8620689655172526 ,3.1279467680608364),
(7.8544061302682167 ,3.1819391634980985),
(10.000000000000014 ,3.1963878326996196),
(11.839080459770145 ,3.2032319391634978),
(13.984674329501942 ,3.2070342205323192),
(15.977011494252892 ,3.2176806083650189),
(17.969348659003842 ,3.2252851711026613),
(19.961685823754806 ,3.23212927756654  ),
(21.800766283524922 ,3.238212927756654 ),
(23.94636015325672  ,3.2450570342205323),
(26.091954022988517 ,3.2503802281368821),
(27.931034482758633 ,3.2541825095057035),
(29.923371647509597 ,3.2595057034220529),
(32.068965517241395 ,3.2655893536121674),
(33.908045977011511 ,3.2716730038022814),
(36.053639846743309 ,3.2792775665399239),
(38.045977011494273 ,3.2868821292775663),
(40.038314176245237 ,3.2899239543726235),
(42.030651340996172 ,3.2906844106463877),
(44.022988505747136 ,3.2906844106463877),
(45.862068965517253 ,3.2906844106463877),
(47.701149425287369 ,3.2899239543726235),
(50.000000000000014 ,3.2906844106463877),
(51.992337164750964 ,3.2922053231939161),
(53.83141762452108  ,3.2922053231939161),
(55.977011494252878 ,3.2922053231939161),
(57.969348659003842 ,3.2922053231939161),
(59.961685823754792 ,3.2929657794676803),
(61.954022988505756 ,3.2929657794676803),
(63.946360153256705 ,3.2944866920152092),
(65.938697318007669 ,3.2960076045627376),
(68.084291187739467 ,3.2967680608365018),
(69.923371647509583 ,3.3013307984790874),
(71.915708812260533 ,3.3104562737642587),
(73.9080459770115   ,3.3256653992395435),
(75.900383141762461 ,3.3309885931558934),
(77.892720306513411 ,3.3317490494296575),
(80.038314176245223 ,3.3317490494296575),
(81.877394636015325 ,3.3325095057034222),
(83.869731800766289 ,3.3332699619771864),
(85.862068965517238 ,3.3340304182509506),
(87.8544061302682   ,3.3347908745247148),
(90.0                 ,3.3347908745247148),
(91.99233716475095  ,3.3347908745247148),
(93.83141762452108  ,3.3363117870722432),
(95.82375478927203  ,3.3385931558935362),
(97.969348659003828 ,3.367490494296578 ),
(98.429118773946357 ,3.3986692015209128),
(100.0 ,3.5))
OCVDischarge_lut = LUT(points)

points = ((0.0,0.0),
(0.13651877133105828, -0.0003673183339408198    ),
(0.9556313993174079, -0.00032979555319924447    ),
(1.9795221843003432, -0.000300044180832146      ),
(3.822525597269628, -0.00025607099859725855     ),
(5.460750853242324, -0.00022633288047980385     ),
(6.689419795221845, -0.000201763919723428       ),
(8.532423208191126, -0.00017073572130731085     ),
(10.580204778156997, -0.00014359543612003933    ),
(13.242320819112628, -0.00012164639870991967    ),
(16.109215017064848, -0.00009840728100113768    ),
(20, -0.00008036824723593668                    ),
(24.09556313993174, -0.00006103913317207329     ),
(27.576791808873722, -0.000028751781039795918   ),
(28.191126279863475, -0.0000028750676518992215  ),
(29.010238907849825, 0.000008757745452135591    ),
(30.443686006825935, 0.000054034262235329186    ),
(32.901023890784984, 0.00007598771772866338     ),
(35.972696245733786, 0.00008757193191733764     ),
(38.02047781569966, 0.00010306173166771591      ),
(40.68259385665528, 0.00011724377878657343      ),
(44.36860068259386, 0.0001249312435799728       ),
(49.07849829351536, 0.00013259661795729917      ),
(54.40273037542662, 0.0001402487380849818       ),
(57.474402730375424, 0.0001427714636005169      ),
(61.97952218430033, 0.00014655776091542682      ),
(64.64163822525597, 0.000142616830688006        ),
(66.27986348122866, 0.00012186951191225681      ),
(66.89419795221843, 0.00010114428355258067      ),
(67.71331058020479, 0.00007523664358218183      ),
(68.32764505119454, 0.00006098390713189081      ),
(69.96587030716722, 0.000040236588356141665     ),
(73.4470989761092, 0.000037572484177739445      ),
(77.33788395904435, 0.00004137203574229318      ),
(81.63822525597269, 0.00004386825275854068      ),
(87.16723549488054, 0.0000528104531848857       ),
(90.23890784982936, 0.0000605111722279289       ),
(95.56313993174061, 0.00007204678750124256      ),
(97.81569965870307, 0.00008235417564089818      ),
(99.86348122866892, 0.00009654947700939946      ),
(100, 0.00009654947700939946                    ))
tempcorr_lut = LUT(points)

points = (( 0, 65664),
( 1, 65572),
( 2, 65476),
( 3, 65376),
( 4, 65274),
( 5, 65168),
( 6, 65059),
( 7, 64947),
( 8, 64833),
( 9, 64715),
(10, 64596),
(11, 64473),
(12, 64348),
(13, 64221),
(14, 64092),
(15, 63960),
(16, 63827),
(17, 63691),
(18, 63554),
(19, 63415),
(20, 63275),
(21, 63133),
(22, 62990),
(23, 62846),
(24, 62700),
(25, 62554),
(26, 62407),
(27, 62259),
(28, 62110),
(29, 61960),
(30, 61811),
(31, 61660),
(32, 61510),
(33, 61359),
(34, 61209),
(35, 61058),
(36, 60908),
(37, 60758),
(38, 60608),
(39, 60459),
(40, 60310),
(41, 60162),
(42, 60015),
(43, 59869),
(44, 59724),
(45, 59580),
(46, 59437),
(47, 59296),
(48, 59156),
(49, 59018),
(50, 58882),
(51, 58747),
(52, 58614),
(53, 58483),
(54, 58355),
(55, 58228),
(56, 58104),
(57, 57982),
(58, 57863),
(59, 57747),
(60, 57633),
(61, 57522),
(62, 57415),
(63, 57310),
(64, 57208),
(65, 57110),
(66, 57015),
(67, 56924),
(68, 56837),
(69, 56753),
(70, 56673),
(71, 56597),
(72, 56525),
(73, 56457),
(74, 56393),
(75, 56334),
(76, 56280),
(77, 56229),
(78, 56184),
(79, 56144),
(80, 56108),
(81, 56078),
(82, 56052),
(83, 56032),
(84, 56017),
(85, 56008),
(86, 56005),
(87, 55996),
(88, 55993),
(89, 55984),
(90, 55981),
(91, 55971),
(92, 55968),
(93, 55959),
(94, 55956),
(95, 55947),
(96, 55944),
(97, 55935),
(98, 55932),
(99, 55930))
Capacity_lut = LUT(points)

#C1_lut[self.SOC]
#C2_lut[self.SOC]
#R0_lut[self.SOC]
#R1_lut[self.SOC]
#R2_lut[self.SOC]
#OCVCharge_lut[self.SOCVoc]
#OCVDischarge_lut[self.SOCVoc]
#tempcorr_lut[self.SOCVoc] 
#Capacity_lut[abs(self.I)]