# EP12: Andes flight disaster (Uruguayan Air Force Flight 571, 1972), ~21 min. Entries: (cut, text, pause, prompt)
PLANE = "a white and red twin-turboprop Fairchild FH-227D airliner of the Uruguayan Air Force"
FUS = "the broken white fuselage of a twin-turboprop airliner without wings or tail, half buried in deep snow on a glacier high in the Andes"
SURV = "young Uruguayan men of 1972 in layers of sweaters, rugby jerseys and blankets, with sunburned bearded faces"
NANDO = "a tall thin Uruguayan young man of 1972 with dark curly hair, a beard and a determined gaze, wrapped in layers of sweaters"
CANE = "a slim Uruguayan medical student of 1972 with short dark hair, a beard and intense eyes, wearing layered sweaters"
MTN = "towering snow-covered peaks of the high Andes under a deep blue sky, endless ridges in every direction"
INSIDE = "the cramped dark interior of a broken airliner fuselage packed with seats, luggage and blankets, lit by thin light from the windows"

CHAPTERS = [
    (1, "雪の中の機体"),
    (4, "旅立ち"),
    (7, "墜落"),
    (10, "最初の夜"),
    (13, "捜索打ち切り"),
    (16, "究極の選択"),
    (19, "雪崩"),
    (23, "山を越える"),
    (27, "最後の旅へ"),
    (30, "10日間の行進"),
    (34, "川の向こうの男"),
    (38, "救出"),
    (42, "その後"),
]

LINES = [
    # ch1 雪の中の機体
    (1, '1972年12月。南米アンデス山脈の、標高3600メートルを超える雪の谷。', 's', MTN + ', a tiny white object far below in a vast snowy valley, silent'),
    (1, 'そこに、翼を失った1機の飛行機が、雪に埋もれていた。', 'l', FUS + ', seen from a distance, lonely, harsh sunlight'),
    (1, '機体の中では、やせ細った若者たちが、身を寄せ合って生きていた。', 'l', INSIDE + ', thin exhausted young men huddled together under blankets, silent'),
    (1, '雪の白さと、空の青さ以外、何もない世界だった。', 'l', MTN + ', blinding white snow and deep blue sky, nothing else, silent'),
    (1, '墜落から、すでに2か月以上がたっていた。', 'c', 'a handmade calendar of scratched marks on the inside wall of an airliner fuselage, many lines, close-up, no readable text'),
    (2, 'そのころ、2人の若者が、雪の山を越えて、ひたすら歩き続けていた。', 'x', 'two small figures walking across a vast snowfield in the high Andes, long shadows, epic scale'),
    (2, '地図も、登山の道具も、ほとんど持っていなかった。', 'l', 'close-up of worn rugby boots wrapped in cloth sinking into deep snow, a makeshift sleeping bag on a back'),
    (2, '足元は、雪に濡れたラグビーシューズ。体は、何枚も重ねたセーターで包んでいた。', 'l', 'close-up of wet rugby boots and layered sweaters on a young man walking in snow'),
    (2, '目指したのは、山の向こうにあるはずの、人の住む世界だった。', 'c', NANDO + ' standing on a snowy ridge looking out over endless peaks, wind blowing, determined'),
    (3, '1972年10月13日。45人を乗せた飛行機が、アンデスの山中に墜落した。', 's', PLANE + ' flying low between snowy mountain peaks in turbulent clouds, ominous, 1972'),
    (3, '救助が来ない雪山で、生き残った人々は、72日間を耐え抜くことになる。', 'l', SURV + ' standing in front of the broken fuselage on the snow, looking at the sky, hopeful and afraid'),
    (3, 'そこで彼らが下した決断は、のちに世界中を驚かせた。', 'l', 'a group of young men sitting in a circle inside a dark fuselage, heads bowed, solemn decision, candle light'),
    (3, 'その多くは、まだ20歳前後の若者たちだった。', 'l', 'young Uruguayan men of 1972 laughing together in a team photo pose, faded edges, memory'),
    (3, 'これは、アンデスの雪山で、実際に起きた記録である。', 'c', 'a dark archive desk with a case file, an old photograph of snowy mountains clipped to it, single desk lamp, no readable text'),
    # ch2 旅立ち
    (4, '南米の国、ウルグアイ。首都モンテビデオに、オールド・クリスチャンズというラグビーチームがあった。', 's', 'young Uruguayan rugby players of 1972 in striped jerseys practicing on a green field in Montevideo, sunny, cheerful'),
    (4, 'メンバーの多くは、カトリック系の学校で育った仲間たちだった。', 'l', 'a group of smiling young men in school uniforms in front of a Catholic school building in Montevideo, 1960s, friendship'),
    (4, '1972年の10月、彼らはチリで試合をするため、飛行機をチャーターした。', 'l', 'young men with bags laughing at a small airport terminal of 1972, excited for a trip'),
    (4, '南米の小さな国で、彼らは、ラグビーを通じて固い絆で結ばれていた。', 'l', 'young rugby players embracing after a match on a green field, 1970s, joy'),
    (4, 'チリへの遠征は、仲間たちとの楽しい旅になるはずだった。', 'l', 'young men singing on a bus to the airport in 1972, cheerful, sunny'),
    (4, '乗り込んだのは、ウルグアイ空軍の双発プロペラ機だった。', 'c', PLANE + ' parked on an airport apron, passengers climbing the stairs, 1972, bright day'),
    (5, '乗客は40人。選手のほかに、家族や友人も一緒だった。', 's', 'passengers of 1972 including young men, a middle-aged woman and a young woman taking seats in a small airliner cabin, cheerful'),
    (5, 'その中には、ナンド・パラードという青年と、その母と妹もいた。', 'l', NANDO + ' sitting next to his mother and younger sister in an airliner cabin, smiling, warm family moment'),
    (5, 'ナンドの家族にとっても、それは久しぶりの家族旅行だった。', 'l', 'a middle-aged Uruguayan woman and her daughter smiling at an airport in 1972, warm'),
    (5, '乗員5人を合わせて、45人が、アンデスの向こうの、チリのサンティアゴを目指した。', 'c', 'an illustrated old-style map of South America showing a route from Uruguay across Argentina over the Andes to Chile, no readable text'),
    (6, 'だが、出発の日、アンデスの上空は、天候が悪かった。', 's', MTN + ' covered by dark storm clouds, wind blowing snow off the ridges'),
    (6, '飛行機は、アルゼンチンのメンドーサで、一晩、足止めされた。', 'l', 'a small airport in Mendoza, Argentina at night in 1972, an airliner parked under lights, quiet'),
    (6, '目の前にそびえるアンデス山脈は、6000メートルを超える峰が連なる、世界でも有数の険しい山々である。', 'l', MTN + ', seen from an airplane window, huge and threatening'),
    (6, '操縦していたのは、空軍のベテラン操縦士と、副操縦士の2人。山越えの飛行には、慣れているはずだった。', 'l', 'two Uruguayan Air Force pilots of 1972 in the cockpit before takeoff, confident'),
    (6, '翌日の午後、天候が少し回復したのを見て、機体は再び飛び立った。', 'c', PLANE + ' taking off from a runway toward distant snowy mountains in the afternoon'),
    # ch3 墜落
    (7, '1972年10月13日、午後。飛行機は、雲に包まれたアンデスの山々の上を飛んでいた。', 's', PLANE + ' flying inside thick white clouds above hidden mountain peaks, eerie'),
    (7, '機内では、若者たちが冗談を言い合い、ボールを投げ合っていた。', 'l', 'young men laughing and tossing a rugby ball in the aisle of a small airliner cabin, 1972, cheerful'),
    (7, '突然、機体が大きく揺れた。窓の外に、すぐそばまで迫った岩山が見えた。', 'l', 'the view through an airliner window of a jagged snowy rock face terrifyingly close, passengers screaming'),
    (7, '機体は、激しい乱気流に巻き込まれ、何度も大きく落ちた。', 'l', 'passengers gripping their seats as an airliner cabin shakes violently, bags falling, fear'),
    (7, '操縦士は、山の位置を読み違えていた。すでに山を越えたと考え、高度を下げていたのである。', 'c', 'the cockpit of a 1972 turboprop airliner, two pilots pulling hard on the controls, a mountain wall filling the windshield'),
    (8, '午後3時34分。機体は山の尾根に激突した。', 'x', PLANE + ' clipping a snowy mountain ridge, a wing breaking off, snow exploding, dramatic, not gory'),
    (8, '翼と後ろの部分がちぎれ飛び、残った胴体は、雪の斜面を滑り落ちていった。', 'l', 'the broken fuselage of an airliner sliding at high speed down a steep snow slope, snow spraying, dramatic'),
    (8, 'その衝撃で、何人かの乗客が、座席ごと外へ投げ出された。', 'l', 'an empty seat row at the torn end of a fuselage open to swirling snow, dramatic, no people'),
    (8, 'そして、深い雪の中に突っ込み、ようやく止まった。', 'c', FUS + ', just after the crash, snow settling around it, silence'),
    (9, 'この墜落で、多くの人が命を落とした。', 's', 'scattered luggage and broken seats lying in the snow around a crashed fuselage, solemn, no bodies'),
    (9, 'ナンド・パラードの母も、その中にいた。', 'l', 'a woman\'s scarf lying on the snow next to a broken airliner seat, solemn, symbolic'),
    (9, 'ナンド自身も、頭を強く打ち、意識を失っていた。', 'l', NANDO + ' lying unconscious under a blanket inside a dark fuselage, friends watching over him, worried'),
    (9, 'ナンドの妹も、重いけがを負っていた。', 'l', 'a young woman lying under a blanket inside a dark fuselage, her brother holding her hand, sorrow'),
    (9, '生き残った人々は、雪と静けさに包まれた谷で、ぼう然と立ち尽くした。', 'c', SURV + ' standing in shock beside the crashed fuselage in a silent white valley surrounded by peaks'),
    # ch4 最初の夜
    (10, 'その夜、気温は、マイナス30度近くまで下がった。', 's', 'the crashed fuselage on a glacier at night under a sky full of stars, frost everywhere, freezing'),
    (10, '壊れた機体の後ろには、大きな穴が開いていた。', 'l', 'the torn open rear end of an airliner fuselage with a gaping hole, snow blowing in at night'),
    (10, '生存者たちは、荷物や座席を積み上げて、風と雪をふさいだ。', 'l', SURV + ' stacking suitcases and seats to block a hole at the end of a fuselage at night, desperate teamwork'),
    (10, '標高3600メートルを超える場所では、空気も薄く、少し動くだけで息が切れた。', 'l', SURV + ' gasping for breath in thin air, leaning on the fuselage, exhausted'),
    (10, '夜の闇の中で、仲間のうめき声と、風の音だけが聞こえていた。', 'l', 'the dark interior of a fuselage at night, only shapes visible, wind howling outside'),
    (10, 'それでも、体を寄せ合わなければ、凍えてしまうほどの寒さだった。', 'c', INSIDE + ', at night, young men pressed together for warmth, breath steaming, shivering'),
    (11, '乗客の中にいた医学生のロベルト・カネッサたちが、けが人の手当てに走り回った。', 's', CANE + ' bandaging the leg of an injured young man with torn cloth inside a dark fuselage, focused'),
    (11, 'だが、薬も道具も、ほとんどなかった。', 'l', 'a small first aid kit almost empty on a seat inside a fuselage, a few bandages, dim light'),
    (11, '脚を骨折した者、頭にけがをした者。痛みに苦しむ声が、一晩中、機体の中に響いた。', 'l', 'injured young men lying under blankets in a dark fuselage at night, pain, dim light'),
    (11, '最初の夜を越えられずに、さらに何人かが亡くなった。', 'c', 'the first light of dawn falling on the snowy fuselage, silence, grief, mountains in the background'),
    (12, '残ったのは、30人ほどだった。', 's', SURV + ' gathered outside the fuselage in the morning sun, counting each other, exhausted'),
    (12, '持っていた食料は、わずかなチョコレートやお菓子、それにワインだけだった。', 'l', 'a few chocolate bars, small candies and wine bottles laid out on a seat cushion in the snow, close-up'),
    (12, 'リーダー役の若者が、それを少しずつ、全員に分けた。', 'l', 'a young man carefully breaking a small piece of chocolate into tiny portions for others, serious faces'),
    (12, '1日に口にできるのは、チョコレートのひとかけらと、キャップ1杯のワインだけ。', 'l', 'a tiny square of chocolate and a bottle cap filled with wine in a thin hand, close-up'),
    (12, '彼らは、ラグビーチームの主将を中心に、全員で力を合わせることを誓った。', 'l', 'a young team captain speaking to others gathered in the fuselage, rallying them, determined'),
    (12, '救助隊は、すぐに来てくれる。誰もが、そう信じていた。', 'c', SURV + ' looking up at an empty blue sky above the peaks, waiting for planes, hopeful'),
    # ch5 捜索打ち切り
    (13, '上空を、飛行機が通り過ぎることもあった。', 's', 'a small search plane flying high above the Andes, tiny in the sky, young men waving from the snow far below'),
    (13, '彼らは、口紅で機体の屋根に十字を書き、必死に手を振った。', 'l', 'young men drawing a large red cross on the roof of a white fuselage with lipstick, waving at the sky'),
    (13, '近くを飛ぶ飛行機を見て、救助が来たと思ったこともあった。だが、機体はそのまま飛び去っていった。', 'l', 'young men waving desperately as a small plane disappears behind mountain peaks, despair'),
    (13, 'しかし、白い機体は、雪の中でほとんど見えなかった。', 'c', 'a vast snowy valley seen from high above, the white fuselage almost invisible against the snow'),
    (14, '墜落から10日ほどたったころ、彼らは、壊れた機体からラジオを見つけ出し、ニュースを聞いた。', 's', 'a group of young men gathered around a small transistor radio inside a dark fuselage, listening intently'),
    (14, 'そこで流れたのは、信じられない知らせだった。', 'l', 'close-up of a transistor radio with a makeshift wire antenna, young faces frozen in shock in the background'),
    (14, 'ウルグアイ政府は、生存者はいないと判断していた。', 'l', 'officials of 1972 in a government office reading a report, shaking heads, no readable text'),
    (14, '捜索は、打ち切られた。', 'c', 'young men crying and holding each other inside a dark fuselage, despair, dim light'),
    (15, '誰もが、言葉を失った。', 's', SURV + ' sitting in silence in the snow, heads in their hands, vast mountains around them'),
    (15, 'だが、ナンドは、静かにこう言った。', 'l', 'close-up of ' + NANDO + ' with burning eyes, sunburned face, quiet determination'),
    (15, 'それは、誰もが心のどこかで恐れていた言葉だった。', 'l', 'young men looking at each other in silence inside a dark fuselage, fear'),
    (15, '助けが来ないなら、自分たちの足で、ここを出るしかない。', 'c', NANDO + ' looking toward the high western peaks from the snowy valley, wind blowing, resolve'),
    # ch6 究極の選択
    (16, '食料は、もう、ほとんど残っていなかった。', 's', 'an empty chocolate wrapper blowing across the snow next to the fuselage, desolate'),
    (16, '雪の上には、草一本生えていない。動物もいない。', 'l', MTN + ', completely barren white landscape, no life anywhere, silent'),
    (16, '彼らは、機体の革や布を口にしようとしたが、とても食べ物にはならなかった。', 'l', 'a young man chewing on a strip of leather from a seat, hunger, despair'),
    (16, 'このままでは、全員が、飢えて死んでしまう。', 'c', 'thin exhausted young men lying under blankets inside a dark fuselage, weak, hollow cheeks'),
    (17, '彼らは、長い話し合いを重ねた。', 's', 'a group of young men sitting in a circle inside a dark fuselage, talking seriously, candle light, solemn'),
    (17, 'そして、生き延びるために、亡くなった仲間の体を、食べ物にするという決断をした。', 'l', 'a young man kneeling in the snow with his head bowed and hands clasped in prayer, solemn, symbolic, no bodies'),
    (17, '彼らは、自分が死んだら、自分の体を使ってほしいと、互いに約束し合ったという。', 'l', 'young men holding hands in a circle in the snow, eyes closed, a solemn pact'),
    (17, 'それは、生き残った者たちが、生きて帰るために選んだ、ぎりぎりの決断だった。', 'l', 'young men standing in silence in the snow at dusk, heads bowed, solemn'),
    (17, 'それは、信仰を持つ彼らにとって、あまりにも重い選択だった。', 'c', 'a small wooden rosary hanging inside a dark fuselage, faint light, symbolic'),
    (18, '最後まで、食べることを拒んだ者もいた。', 's', 'a young man sitting alone in the corner of a fuselage, refusing food, turning his face away'),
    (18, 'それでも、生きて家族のもとへ帰るために、多くの者は、その決断を受け入れた。', 'l', 'young men looking at an old family photograph inside a fuselage, tears in their eyes, no readable text'),
    (18, 'この決断が、のちに世界中から、さまざまな目で見られることになる。', 'l', 'the fuselage in the snow under heavy clouds, quiet, weight of a decision'),
    (18, 'この選択がなければ、誰一人、生き残ることはできなかったとされる。', 'c', 'the fuselage in the snow at dusk, a faint light glowing inside, quiet'),
    # ch7 雪崩
    (19, '1972年10月29日の夜。生存者たちは、機体の中で眠っていた。', 's', INSIDE + ', at night, young men sleeping huddled together under blankets, calm'),
    (19, 'そのとき、山の上から、ごう音が響いた。', 'x', 'a massive avalanche crashing down a steep mountain slope at night under moonlight, snow cloud billowing'),
    (19, '雪崩だった。', 'l', 'a wall of snow slamming into a small white fuselage in a valley at night, dramatic, not gory'),
    (19, 'その日は、ナンドの妹が亡くなってから、まだ1週間ほどしかたっていなかった。', 'l', 'close-up of ' + NANDO + ' sleeping restlessly inside a dark fuselage, grief'),
    (19, '大量の雪が、機体の中にまで流れ込み、眠っていた人々を埋めた。', 'c', 'snow pouring through a broken opening into a dark fuselage, blankets and seats buried, chaos, not gory'),
    (20, '生き残った者たちは、素手で必死に雪をかき分けた。', 's', 'young men digging frantically through snow with their bare hands inside a dark fuselage, desperate'),
    (20, 'だが、この雪崩で、8人が命を落とした。', 'l', 'a quiet snow-filled fuselage interior at dawn, light seeping in, grief, no bodies'),
    (20, '雪崩のあとも、雪は、何日も降り続いた。', 'l', 'heavy snowfall burying the fuselage in a storm, only a small dark opening visible'),
    (20, '残った19人は、雪に閉じ込められた機体の中で、3日間を過ごした。', 'c', 'young men trapped inside a snow-filled fuselage in near darkness, exhausted, breath steaming'),
    (21, 'その後も、寒さとけがで、仲間は少しずつ減っていった。', 's', 'a row of simple wooden crosses made of seat parts standing in the snow near the fuselage, solemn'),
    (21, '高い山の上では、太陽の光が雪に反射し、目を焼いた。', 'l', 'a young man shading his eyes from blinding sunlight reflecting off a snowfield, squinting in pain'),
    (21, '11月、12月と時がたつにつれて、生存者は、さらに少なくなっていった。', 'l', 'the fuselage under grey skies, a few figures moving slowly outside, weary'),
    (21, '雪目と呼ばれる症状で、目が焼けるように痛み、何も見えなくなることもあった。', 'l', 'a young man covering his eyes in pain in bright snow, a friend guiding him'),
    (21, '彼らは、サングラスの代わりに、窓のプラスチックを切って使った。', 'c', 'close-up of hands cutting a piece of tinted plastic from an airliner window to make sunglasses'),
    (22, '一方で、彼らは知恵を出し合い、生き延びる工夫を重ねていった。', 's', SURV + ' working together outside the fuselage in the sun, organizing, busy'),
    (22, '金属の板に雪を乗せ、太陽の熱で溶かして、飲み水を作った。', 'l', 'snow melting on a shiny sheet of aluminum in bright sunlight, water dripping into a bottle, close-up'),
    (22, '座席のカバーをはがして、毛布の代わりにした。', 'l', 'young men stripping fabric covers from airliner seats to use as blankets, inside a fuselage'),
    (22, 'いとこ同士の3人は、肉を切り分ける係を引き受け、食べ物を管理した。', 'l', 'three young men organizing supplies inside the fuselage, serious, cooperative'),
    (22, 'ラグビーで鍛えたチームワークが、極限の中で、彼らをひとつにしていた。', 'l', 'young men pulling each other up a snowy slope, teamwork, determined'),
    (22, 'それぞれが役割を持ち、ひとつのチームとして、生きることを続けた。', 'c', SURV + ' sitting together in front of the fuselage at sunset, tired but united, rugby spirit'),
    # ch8 山を越える
    (23, '彼らが知っていたのは、自分たちがチリの近くにいるということだけだった。', 's', 'the broken cockpit instruments of an airliner, a faded map, a young man studying it, no readable text'),
    (23, '操縦士は、墜落の前に、チリの上空にいると無線で伝えていた。', 'l', 'a crackling old aircraft radio in a broken cockpit, wires hanging, dim light'),
    (23, 'ラジオから流れるチリの放送も、彼らが西の近くにいることを示していた。', 'l', 'a young man holding a small radio to his ear in the snow, listening carefully'),
    (23, 'だから、西に向かえば、チリの緑の谷に出られるはずだと考えた。', 'c', MTN + ', the setting sun in the west beyond the peaks, golden light, hope'),
    (24, 'しかし、実際には、機体はアルゼンチン側の、山の奥深くにあった。', 's', 'an illustrated map of the Andes border between Argentina and Chile with a small crash marker deep in the mountains, no readable text'),
    (24, '西には、標高4000メートルを超える険しい峰が、立ちはだかっていた。', 'l', MTN + ', a huge sheer mountain wall rising above a small snowy valley, intimidating'),
    (24, '実際には、人が住む場所までは、70キロ以上も離れていた。', 'l', 'an illustrated map with a long route over mountains to a distant valley, no readable text'),
    (24, '彼らの持つ情報は、すべて間違っていたのである。', 'l', 'close-up of a broken altimeter in a crashed cockpit, frost on the glass'),
    (24, '何度か、数人で偵察に出たが、薄い空気と寒さに、すぐに力尽きた。', 'c', 'three young men struggling up a steep snow slope, gasping for air, exhausted, high altitude'),
    (25, 'ある偵察で、彼らは、ちぎれ飛んだ機体の後ろの部分を見つけた。', 's', 'the torn tail section of an airliner lying in the snow far down a valley, three young men approaching it'),
    (25, 'そこには、スーツケースや、わずかな食べ物、たばこが残されていた。', 'l', 'open suitcases with clothes, a few food tins and cigarette packs lying in the snow, close-up'),
    (25, '機体のバッテリーもあった。彼らは、無線を直そうと試みた。', 'l', 'young men trying to connect wires to an aircraft battery in the snow, concentration'),
    (25, '後ろの部分には、小さな暖房器具もあり、彼らはひと晩だけ、暖かく眠ることができた。', 'l', 'three young men sleeping among scattered suitcases inside a torn tail section of an airliner, relief'),
    (25, 'だが、無線は、最後まで動かなかった。', 'c', 'a young man throwing a dead radio receiver down onto the snow in frustration, mountains around'),
    (26, '12月に入ると、山の雪が少しずつ解け始めた。', 's', MTN + ', early summer, snow melting on rocks, water trickling, brighter light'),
    (26, '昼間の気温が上がり、歩いて山を越えるなら、今しかなかった。', 'l', SURV + ' looking up at the western peaks in warmer sunlight, making a decision'),
    (26, '残された仲間の中には、もう歩けないほど弱った者もいた。', 'l', 'a very weak young man lying inside the fuselage, friends caring for him'),
    (26, '彼らは、最も体力の残っている者たちを選んだ。', 'c', 'three young men standing in front of the others outside the fuselage, chosen, serious faces'),
    # ch9 最後の旅へ
    (27, '選ばれたのは、ナンド・パラード、ロベルト・カネッサ、そして、アントニオ・ビジンティンの3人だった。', 's', NANDO + ' and ' + CANE + ' and a third young man standing together with packs, ready to leave'),
    (27, '仲間たちは、機体の断熱材を縫い合わせて、寝袋を作った。', 'l', 'young men sewing together silver aircraft insulation into a large sleeping bag with needle and thread, close-up'),
    (27, '食べ物は、何日分も袋に詰めて、持っていくことになった。', 'l', 'bundles of supplies packed in socks and bags inside a fuselage, preparation'),
    (27, 'それは、夜の寒さから身を守るための、命綱だった。', 'c', 'a handmade silver sleeping bag rolled up beside the fuselage, symbolic'),
    (28, 'ナンドは、母と妹をこの山で失っていた。', 's', 'close-up of ' + NANDO + ' looking down at the snow, grief in his eyes, quiet'),
    (28, 'それでも、父のもとへ帰る。その思いが、彼を支えていた。', 'l', 'a memory of an older Uruguayan man smiling at a young man, faded edges, warm, nostalgic'),
    (28, 'カネッサもまた、医学生として、仲間たちの命を背負っていた。', 'l', 'close-up of ' + CANE + ' looking at the weak friends in the fuselage, heavy responsibility'),
    (28, '出発の前、ナンドは、仲間に言ったという。もし食べ物がなくなったら、ためらわずに自分を使ってくれ、と。', 'c', NANDO + ' speaking quietly to friends inside the fuselage, serious, candle light'),
    (29, '1972年12月12日。3人は、西の山に向かって歩き出した。', 'x', 'three small figures leaving the fuselage and walking up a vast snow slope toward huge peaks at dawn'),
    (29, '機体に残った仲間たちは、その背中が見えなくなるまで、見送り続けた。', 'l', SURV + ' standing beside the fuselage watching three tiny figures disappear up the mountain'),
    (29, '彼らは、出発の前に、仲間ひとりひとりと抱き合った。', 'l', 'young men embracing one by one beside the fuselage at dawn, tearful farewell'),
    (29, 'これが、最後の望みだった。', 'c', 'the fuselage alone in the vast snowy valley, tiny footprints leading away up the mountain'),
    # ch10 10日間の行進
    (30, '山の斜面は、想像以上に急だった。', 's', 'three young men climbing a very steep snow slope on hands and knees, gasping, high altitude'),
    (30, '一歩進むたびに、ひざまで雪に沈み、息が切れた。', 'l', 'close-up of legs sinking knee-deep into snow, a hand gripping a rock, exhaustion'),
    (30, '足を滑らせれば、数百メートル下まで落ちてしまう。命がけの登山だった。', 'l', 'a young man clinging to a rocky ridge above a sheer drop, snow blowing, danger'),
    (30, '昼は、照りつける太陽と、雪の照り返し。夜は、マイナス30度近い寒さ。', 'l', 'two young men walking under blazing sun on a snowfield, then shivering at night, contrast'),
    (30, '夜は、手作りの寝袋に3人でくるまり、寒さに耐えた。', 'c', 'three young men huddled inside a silver handmade sleeping bag on a snowy ledge at night under stars'),
    (31, '3日目、ついに山の頂上にたどり着いた。', 's', NANDO + ' reaching a snowy summit and standing up, the wind blowing, vast view'),
    (31, 'だが、そこから見えたのは、緑の谷ではなかった。', 'l', MTN + ', seen from a summit, endless snowy peaks stretching to the horizon in every direction, overwhelming'),
    (31, '頂上の標高は、4600メートルを超えていたとされる。', 'l', 'a snowy summit ridge with two tiny figures, thin clouds below, extreme altitude'),
    (31, 'ナンドは、そのとき、ここで死ぬのだと思ったと、のちに語っている。', 'l', 'close-up of ' + NANDO + ' with tears freezing on his cheeks on a summit, wind blowing'),
    (31, 'どこまでも続く、雪の山々だった。', 'c', 'close-up of ' + NANDO + ' staring at endless mountains, shock and despair, then resolve'),
    (32, 'それでもナンドは、遠くに、雪のない、低い山並みを見つけた。', 's', 'far away on the horizon, low brown mountains without snow, faint, seen between peaks'),
    (32, '食料が足りないと考えた3人は、ビジンティンを機体に戻らせ、2人で進むことにした。', 'l', 'a young man walking back down the slope alone while two others watch, sad farewell'),
    (32, 'ナンドは言った。たとえ死ぬとしても、助けを求めて歩きながら死にたい、と。', 'l', 'close-up of ' + NANDO + ' speaking to ' + CANE + ' on a ridge, wind, resolve'),
    (32, 'ナンドとカネッサは、再び、歩き出した。', 'c', 'two small figures descending a long snowfield toward distant valleys, determination'),
    (33, '何日も、雪と岩の斜面を下り続けた。', 's', NANDO + ' and ' + CANE + ' walking down a rocky valley with melting snow, exhausted'),
    (33, 'やがて、雪が消え、小さな川の流れが現れた。', 'l', 'a small stream flowing between rocks where the snow ends, first green moss, hope'),
    (33, 'そして、草が生え、牛の足跡が見つかった。', 'l', 'cow hoofprints in muddy grass beside a mountain stream, close-up, sign of life'),
    (33, 'カネッサの体は弱っていたが、ナンドが励まし、2人は支え合って進んだ。', 'l', NANDO + ' helping ' + CANE + ' over rocks in a valley, supporting him, exhausted'),
    (33, '2人の体は、もう限界に近かった。それでも、足を止めることはなかった。', 'l', 'two exhausted figures walking side by side down a long valley at sunset, unbroken'),
    (33, '人が住む場所が、近づいていた。', 'c', 'a green mountain valley in Chile with grass and bushes, a river below, warm light'),
    # ch11 川の向こうの男
    (34, '1972年12月20日。歩き始めて、9日目の夕方。', 's', 'a mountain river valley at dusk, two exhausted bearded young men resting on rocks'),
    (34, '川の向こう岸に、馬に乗った男の姿が見えた。', 'l', 'a Chilean horseman in a poncho and hat on the far bank of a rushing river at dusk'),
    (34, '2人は、とうとう幻を見たのではないかと思ったという。', 'l', 'two exhausted young men staring across a river at a distant figure on horseback, disbelief'),
    (34, '2人は、必死に叫んだ。だが、川の音で、声は届かなかった。', 'c', 'two ragged young men shouting and waving their arms across a loud rushing river'),
    (35, '翌朝、男は、再び川辺に現れた。', 's', 'a Chilean horseman returning to the river bank in the morning light, cautious'),
    (35, 'チリの牧童、セルヒオ・カタラン。', 'l', 'portrait of a Chilean cattle herder of 1972 in his forties with a weathered face, a hat and a poncho, kind eyes'),
    (35, '男は、2人の様子を見て、何かが起きたと気づいた。', 'l', 'a Chilean horseman looking carefully across the river at two ragged young men, concerned'),
    (35, '男は、紙と鉛筆を石に結びつけ、川の向こうに投げてよこした。', 'c', 'a stone wrapped with paper and a pencil flying across a river, close-up'),
    (36, 'ナンドは、震える手で書いた。', 's', 'close-up of trembling thin hands writing on a scrap of paper with a pencil on a rock, no readable text'),
    (36, '私は、山に墜ちた飛行機から来た。10日間、歩き続けてきた。', 'l', NANDO + ' writing a note on his knee beside the river, tears in his eyes, no readable text'),
    (36, '私たちは、何も食べるものがない。助けてほしい。', 'l', 'a thin hand writing on paper, close-up, emotional, no readable text'),
    (36, '飛行機には、まだ14人の仲間がいる。', 'c', 'a folded note tied to a stone, held in a thin hand, close-up, no readable text'),
    (37, 'ナンドは、そのメモを石に結び、川の向こうへ投げ返した。', 's', 'a stone with a note tied to it flying back across a rushing river toward the horseman'),
    (37, '男はメモを読むと、うなずき、2人にパンを投げてよこした。', 'l', 'a Chilean horseman reading a note and throwing bread across the river, two young men reaching out'),
    (37, '2人は、そのパンをかみしめながら、声を上げて泣いた。', 'l', 'two ragged young men eating bread on a river bank and crying with relief'),
    (37, 'そして、助けを呼ぶために、馬を走らせた。', 'c', 'a Chilean horseman galloping away along a mountain trail, dust flying, urgent, hopeful'),
    # ch12 救出
    (38, '知らせは、すぐにチリ中に広がった。', 's', 'a busy radio newsroom in Chile in 1972, people shouting with excitement, no readable text'),
    (38, '死んだと思われていた人々が、生きていた。', 'l', 'families in Montevideo of 1972 gathered around a radio, crying and embracing with joy'),
    (38, '12月21日、ナンドとカネッサは、近くの村で保護された。', 'l', 'two thin young men sitting by a fire in a rustic Chilean farmhouse, wrapped in blankets, villagers around'),
    (38, 'ナンドとカネッサは、すぐに、残された仲間たちの居場所を伝えた。', 'l', NANDO + ' speaking urgently to Chilean soldiers and pointing at the mountains'),
    (38, '12月22日。チリ空軍のヘリコプターが、山へ向かった。', 'c', 'two military helicopters of 1972 flying over the high Andes toward a snowy valley'),
    (39, '道案内をしたのは、ナンド自身だった。', 's', NANDO + ' sitting in a helicopter cockpit pointing down at the mountains, guiding the pilot'),
    (39, '機体のそばで待つ仲間たちの耳に、ヘリコプターの音が聞こえてきた。', 'l', SURV + ' outside the fuselage looking up, hearing a sound, faces lighting up'),
    (39, 'ヘリコプターは、強い風の中、何度も山の間をすり抜けながら飛んだ。', 'l', 'a helicopter flying through narrow snowy mountain passes in strong wind, dangerous'),
    (39, '彼らは、雪の上で抱き合い、叫び、泣いた。', 'c', 'young men jumping and embracing in the snow beside the fuselage, waving at a helicopter, overwhelming joy'),
    (40, 'その日、天候が悪くなり、半分の人だけが、ヘリコプターで運ばれた。', 's', 'a helicopter landing on the snow near the fuselage in gusting wind, young men being helped aboard'),
    (40, '残りの8人は、救助隊とともに、もう一晩、山で過ごした。', 'l', 'rescuers and survivors sitting together around a small light beside the fuselage at night, hopeful'),
    (40, '救助隊の隊員たちも、彼らが生き抜いた現場の厳しさに、言葉を失ったという。', 'l', 'Chilean rescuers looking around the snowy crash site in awe, mountains towering above'),
    (40, '12月23日。最後の生存者が、山から救い出された。', 'c', 'a helicopter lifting off from the snowy valley at sunrise, the fuselage left behind, emotional'),
    (41, '墜落から72日。生き残ったのは、16人だった。', 'x', 'sixteen thin bearded young men in blankets standing together in a Chilean mountain village, sunlight, emotional'),
    (41, '彼らの体重は、多くの者が、大きく減っていた。', 'l', 'thin young men being examined by doctors in a small hospital of 1972, gentle care'),
    (41, '彼らを見た人々は、その姿に、言葉を失った。', 'l', 'villagers and soldiers in Chile staring at thin bearded young men in blankets, emotional'),
    (41, '病院の前には、家族たちが、泣きながら駆けつけた。', 'c', 'families running to embrace thin young men in front of a hospital in Chile, 1972, tears of joy'),
    # ch13 その後
    (42, 'やがて、生存者たちが生き延びた方法が、明らかになった。', 's', 'a crowded press conference of 1972 with reporters, camera flashes and microphones, no readable text'),
    (42, '世間には、驚きと、さまざまな声が広がった。', 'l', 'newspapers piled on a table in 1972, people reading with shocked faces, no readable text'),
    (42, '生存者たちは、記者会見で、包み隠さずに語った。', 'l', 'young men sitting at a table speaking into microphones at a press conference, serious, honest'),
    (42, 'その事実は、多くの人に、大きな衝撃を与えた。', 'l', 'people of 1972 on a street reading newspapers, shocked faces, no readable text'),
    (42, '亡くなった仲間の家族の多くも、その決断を受け入れ、彼らを支えたという。', 'c', 'an older woman embracing a thin young man warmly, forgiveness, emotional, soft light'),
    (43, '墜落現場には、亡くなった人々を弔う、十字架が立てられた。', 's', 'a simple iron cross standing on a pile of stones in a snowy valley in the Andes, memorial, solemn'),
    (43, '今も、毎年のように、多くの人がこの場所を訪れている。', 'l', 'hikers with mules walking up a mountain valley toward a memorial cross in the Andes, summer, respectful'),
    (43, '生存者の多くは、その後、医師や実業家などとして、それぞれの人生を歩んだ。', 'l', 'a middle-aged doctor in a white coat in a modern hospital, warm, dignified'),
    (43, '彼らは、亡くなった仲間たちのことを、決して忘れなかった。', 'l', 'old men placing flowers at a memorial cross in the Andes, quiet, solemn'),
    (43, 'カネッサは、心臓の病気の子どもを診る医師になった。ナンドは、講演を通して、この体験を世界に語り続けた。', 'c', 'an older man speaking on a stage to a large audience, warm lighting, inspiring, no readable text'),
    (44, '72日間の極限の中で、彼らを支えたものは、何だったのか。', 's', MTN + ', at sunset, golden light on the peaks, reflective mood'),
    (44, 'それは、あきらめない意志と、仲間を信じる心だったのかもしれない。', 'l', 'many hands of young men stacked on top of each other in a rugby huddle, close-up, unity'),
    (44, '極限の寒さと飢え、そして、仲間を失う悲しみ。', 'l', 'a lone young man sitting in the snow at dusk looking at the mountains, grief and strength'),
    (44, '1人ひとりの力だけでは、決して生き延びることはできなかった。', 'l', 'young men in a circle with arms around each other in the snow, unity'),
    (44, '誰かが倒れれば、誰かが支える。それは、彼らがラグビーで学んできたことでもあった。', 'c', 'young rugby players helping a fallen teammate up on a green field, warm sunlight, memory'),
    (45, 'アンデスの雪山は、今も、あの日と同じように、静かにそびえている。', 's', MTN + ', calm and silent under a clear blue sky, majestic'),
    (45, '生きて帰るために、限界を超えた人々。その記録を、忘れてはならない。', 'l', 'two small figures standing on a snowy ridge at sunrise, looking toward a distant green valley, hope'),
    (45, '亡くなった29人の命も、また、この物語の一部である。', 'c', 'a memorial cross with flowers in a snowy Andes valley at dusk, solemn, peaceful'),
    (45, 'このチャンネルでは、実際に起きた極限のサバイバルを記録している。', 's', 'a dark archive room with shelves of case files, one file open under a single desk lamp'),
    (45, '次の記録を見逃さないよう、チャンネル登録をお願いしたい。', 'x', 'the case file closing, the desk lamp switching off, darkness'),
]

# ---- 以下、パイプライン用の設定 ----
SCENE = "the Andes mountains between Argentina and Chile / Uruguay, 1972"
STYLE = ("Japanese gekiga manga illustration style (hand-drawn comic art, NOT photorealistic), bold black ink linework with cross-hatching, "
         "painted full colors, cold blue-white snow, harsh high-altitude sunlight and deep shadows, warm candle light inside the fuselage, "
         "accurate 1972 period details, ONE single full-frame illustration showing one continuous scene (absolutely NO comic panels, "
         "NO split screen, NO inset frames, NO borders), dramatic high contrast cinematic lighting, serious documentary mood, "
         "not gory (no blood, no wounds, no corpses, no body parts), no speech bubbles, no text, no letters, no captions, no logos")
# 本編20分以上にするため少しゆっくり読む
TTS_SPEED = 0.91

READINGS = {"ナンド": "ナンド", "ビジンティン": "ビジンティン", "牧童": "ぼくどう"}
STAMPS = {}
for _c, _t, _p, _i in LINES:
    for _k, _v in [("1972年12月。", "1972年12月"), ("1972年10月13日。", "1972年10月13日"), ("1972年10月13日、午後。", "1972年10月13日"),
                   ("午後3時34分。", "15:34"), ("1972年10月29日の夜。", "1972年10月29日"), ("1972年12月12日。", "1972年12月12日"),
                   ("1972年12月20日。", "1972年12月20日"), ("12月22日。", "1972年12月22日"), ("墜落から72日。", "72日目")]:
        if _t.startswith(_k):
            STAMPS[_t] = _v
THUMB = {"image": 2, "big": "アンデス", "red": "七十二日", "top": "雪山に墜ちた45人", "sub": "救助打ち切り…生き延びるための究極の選択"}
SHORT = {"sel": [10, 11, 35, 36, 37, 67, 69, 71], "stamp": {"10": "1972年10月13日", "67": "墜落から10日"},
         "h1": "【実話】アンデスの奇跡", "h2": "雪山に墜ちた45人", "e1": "彼らが下した決断は――", "e2": "▶ 続きは本編で（固定コメント）",
         "title": "【実話】雪山に墜落、救助は打ち切られた…アンデスの72日間 #shorts",
         "desc": "1972年、45人を乗せた飛行機がアンデス山脈に墜落した。生き残った若者たちに、ラジオが伝えた絶望の知らせとは。\n#実話 #アンデスの奇跡 #サバイバル #shorts"}
META = {"title": "【実話】アンデスの奇跡…雪山に墜ちた45人、救助打ち切りから72日間を生き延びた若者たち",
        "description": ("ウルグアイ空軍571便遭難事故（1972年）の実話。ラグビーチームの若者たちを乗せた飛行機が、アンデス山脈の標高3600m超の雪山に墜落した。\n"
                        "マイナス30度の夜、捜索打ち切りの知らせ、生き延びるための究極の決断、そして雪崩。仲間を救うため、2人の若者が10日間かけて雪山を越えた。72日間の記録を約20分で描く。\n\n"
                        "▼チャプター\n{CHAPTERS}\n\n"
                        "※映像はすべて実話をもとにした再現イラストです。実在の人物の外見とは異なります。\n"
                        "※出来事の詳細には諸説あります。本動画は記録・資料をもとに構成しています。\n"
                        "※亡くなられた29人の方々のご冥福をお祈りいたします。\n\n"
                        "▼前回：【実話】小野田寛郎…終戦を信じず29年、ルバング島のジャングルで戦い続けた最後の日本兵\nhttps://youtu.be/-Cm1sISXWWc\n\n"
                        "▼参考資料\n・ピアズ・ポール・リード『生存者』\n・ナンド・パラード『アンデスの奇蹟』\n・ウルグアイ空軍571便遭難事故に関する各種資料・報道\n\n"
                        "ナレーション：VOICEVOX:青山龍星\n\n"
                        "クライシス・ファイル〜極限サバイバル劇画〜\n実際に起きた極限のサバイバルを、劇画で記録するチャンネルです。\n"
                        "チャンネル登録：https://www.youtube.com/@CrisisFiles_Survival\n\n"
                        "#実話 #アンデスの奇跡 #ウルグアイ空軍571便 #サバイバル #遭難 #クライシスファイル"),
        "tags": ["アンデスの奇跡", "ウルグアイ空軍571便", "アンデス", "飛行機事故", "遭難", "雪山", "サバイバル", "ナンド・パラード",
                 "ロベルト・カネッサ", "生存者", "72日間", "実話", "クライシスファイル"]}
