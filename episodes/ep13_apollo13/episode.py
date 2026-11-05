# EP13: Apollo 13 (April 1970), ~21 min. Entries: (cut, text, pause, prompt)
LOVELL = "a calm American astronaut commander in his forties with short dark hair and a steady gaze, wearing a white 1970 inflight coverall"
SWIG = "a young American astronaut in his late thirties with light brown hair and a sharp face, wearing a white 1970 inflight coverall"
HAISE = "a lean American astronaut in his mid thirties with short dark hair and a friendly face, wearing a white 1970 inflight coverall"
CREW = "three American astronauts of 1970 in white inflight coveralls"
KRANZ = "an American flight director of 1970 with a flat-top crew cut, wearing a white vest, intense eyes"
MCC = "a 1970 mission control room in Houston with rows of consoles, glowing green screens, controllers in white shirts and headsets"
CSM = "a white cone-shaped Apollo command module attached to a long silver cylindrical service module, flying in black space"
STACK = "a white cone-shaped Apollo command module and silver service module docked nose to nose with a gold-foil spider-legged lunar module, flying in black space"
CMIN = "the cramped interior of an Apollo command module with three couches, dense panels of switches and dials, small triangular windows"
LMIN = "the cramped interior of an Apollo lunar module with standing room only, metal panels, cables, two small triangular windows"
EARTH = "the blue and white Earth floating small in the black void of space"
MOON = "the grey cratered surface of the Moon seen up close from orbit"

CHAPTERS = [
    (1, "宇宙の闇"),
    (4, "13号の3人"),
    (7, "発射"),
    (10, "爆発"),
    (13, "月をあきらめる"),
    (16, "救命ボート"),
    (19, "月の裏側"),
    (23, "凍える船内"),
    (26, "二酸化炭素"),
    (30, "手動の噴射"),
    (34, "最後の準備"),
    (38, "帰還"),
    (42, "その後"),
]

LINES = [
    # ch1 宇宙の闇
    (1, '1970年4月。地球から、およそ32万キロメートル離れた宇宙。', 's', EARTH + ', seen from very far away, tiny, lonely, silent'),
    (1, 'そこを、3人の男を乗せた、小さな宇宙船が飛んでいた。', 'l', STACK + ', tiny against the vast darkness, the Earth far behind'),
    (1, '船内の温度は、冷蔵庫の中のように下がり、窓には霜がついていた。', 'l', LMIN + ', frost on the windows, three astronauts shivering in the dark, breath steaming'),
    (1, '電気も、水も、空気も、すべてが足りなかった。', 'l', 'close-up of a dark instrument panel with most lights switched off, a single dim gauge glowing, cold'),
    (1, 'それでも彼らは、生きて地球へ帰ろうとしていた。', 'c', CREW + ' looking out a small triangular window at the distant Earth, exhausted, determined'),
    (2, '一方、地球では、何百人もの人々が、眠らずに働き続けていた。', 'x', MCC + ', late at night, tense, crowded, cigarette smoke in the air'),
    (2, '机の上には、図面と計算用紙が、山のように積まれていた。', 'l', 'engineers of 1970 in white shirts bent over desks covered with blueprints and paper calculations, slide rules, no readable text'),
    (2, '誰もが、たった1つの答えを探していた。', 'l', 'close-up of tired engineers of 1970 arguing over a blueprint under fluorescent lights, no readable text'),
    (2, 'どうすれば、あの3人を、生きて連れ戻せるのか。', 'c', KRANZ + ' standing at a console in mission control, staring at the screens, absolute focus'),
    (3, 'アポロ13号。人類で3度目の、月面着陸を目指した宇宙船。', 's', 'a giant white Saturn V rocket standing on the launch pad at dawn in 1970, searchlights, steam'),
    (3, 'その旅は、月へ向かう途中で、突然、命がけの脱出劇へと変わった。', 'l', STACK + ', a sudden burst of white gas spraying from the service module, dramatic'),
    (3, '宇宙船の中で、何が起きたのか。そして、3人は、どうやって生き延びたのか。', 'l', CMIN + ', three astronauts staring at a panel full of red warning lights, shock'),
    (3, '人類の宇宙開発の歴史で、最も危険だった4日間の記録である。', 'c', 'a dark archive desk with a case file and an old photograph of a rocket clipped to it, single desk lamp, no readable text'),
    # ch2 13号の3人
    (4, '1969年7月。アポロ11号が、人類で初めて、月に降り立った。', 's', 'an astronaut in a white spacesuit standing on the grey lunar surface, the black sky and the Earth above, 1969, iconic'),
    (4, '世界中が、テレビの前で、その瞬間を見守った。', 'l', 'a family of 1969 gathered around a black and white television in a living room, amazed faces'),
    (4, 'そして、その年の11月には、12号も、月面着陸に成功した。', 'l', 'two astronauts in white spacesuits working on the lunar surface next to a gold lunar module, 1969'),
    (4, '月へ行くことは、もう、特別なことではない。多くの人が、そう感じ始めていた。', 'c', 'people of 1970 walking past a television shop window without stopping, bored, a rocket on the screen, no readable text'),
    (5, '次に月を目指すのは、アポロ13号。船長は、ジム・ラベルだった。', 's', 'portrait of ' + LOVELL + ', calm and experienced'),
    (5, 'ラベルは、すでに3回の宇宙飛行を経験した、ベテランの飛行士だった。', 'l', LOVELL + ' studying a flight manual at a desk in a training building, focused'),
    (5, '月を回る、アポロ8号にも乗った。しかし、月の上に降りたことは、まだなかった。', 'l', MOON + ', seen through a small spacecraft window, the curve of the Moon, longing'),
    (5, '今回こそ、その夢がかなうはずだった。', 'c', 'close-up of ' + LOVELL + ' looking up at the Moon in the night sky, hopeful'),
    (5, '家では、妻と4人の子どもたちが、父の帰りを待っていた。', 's', 'an American family of 1970, a wife and four children, waving goodbye in front of a house, warm'),
    (5, '月から戻ったら、たくさん話を聞かせてほしい。子どもたちは、そう言って父を送り出した。', 'c', 'close-up of a young child of 1970 hugging an astronaut father, warm light, emotional'),
    (6, '月着陸船の操縦を担当するのは、フレッド・ヘイズ。', 's', 'portrait of ' + HAISE + ', confident smile'),
    (6, 'そして、司令船の操縦士は、もともと、ケン・マッティングリーという男だった。', 'l', 'a young American astronaut of 1970 with short light hair in a white coverall, sitting in a simulator, focused'),
    (6, 'ところが、発射の数日前、思わぬ問題が起きる。', 'l', 'a doctor of 1970 in a white coat holding a clipboard with a serious face, a worried astronaut in front of him'),
    (6, '控えの飛行士の1人が風疹にかかり、マッティングリーにうつっているおそれが出たのだ。', 'l', 'a medical examination room of 1970, an astronaut sitting on a bed, a doctor checking him, tense'),
    (6, '彼は、風疹にかかったことがなかった。宇宙で発病すれば、命にかかわる。', 'l', 'close-up of a frustrated young astronaut clenching his fist, disappointment'),
    (6, '代わりに選ばれたのは、控えの飛行士、ジャック・スワイガートだった。', 's', 'portrait of ' + SWIG + ', serious, ready'),
    (6, '発射の、わずか3日前のことだった。', 'c', 'a wall calendar of April 1970 with a date circled in red, no readable text'),
    # ch3 発射
    (7, '1970年4月11日。アメリカ、フロリダ州のケネディ宇宙センター。', 's', 'a giant white Saturn V rocket on the launch pad in Florida, clear blue sky, 1970'),
    (7, '高さ110メートルの巨大なロケット、サターン5型が、発射の時を待っていた。', 'l', 'looking up at a towering white Saturn V rocket from the base of the launch pad, enormous scale'),
    (7, '3人の飛行士は、宇宙服に身を包み、ロケットの先端の司令船に乗り込んだ。', 'l', CREW + ' in white spacesuits and helmets walking toward the launch tower, waving'),
    (7, '午後1時13分。エンジンが火を噴き、ロケットは、ゆっくりと空へ昇っていった。', 'l', 'a Saturn V rocket lifting off with huge flames and smoke, crowds watching from far away, 1970'),
    (7, '打ち上げの途中、エンジンの1つが、予定より早く止まった。', 'l', 'the engine section of a rocket stage in flight, one engine nozzle going dark, ominous'),
    (7, 'しかし、ほかのエンジンが長く燃えて補い、宇宙船は無事、軌道に乗った。', 'c', 'a rocket stage glowing in space above the curve of the Earth, success'),
    (8, '13号は、地球を回ったあと、月へ向かう軌道に入った。', 's', STACK + ', leaving the Earth behind, heading into darkness'),
    (8, '宇宙船は、大きく2つに分かれていた。', 'l', STACK + ', seen from the side, clear shapes, documentary illustration'),
    (8, '3人が暮らす、円すい形の司令船「オデッセイ」。', 'l', 'a white cone-shaped Apollo command module floating in black space, close view'),
    (8, 'その後ろには、酸素や電気、エンジンを積んだ、機械船がつながっていた。', 'l', 'a long silver cylindrical Apollo service module with a large engine bell, floating in space, detailed'),
    (8, 'そして先端には、月に降りるための着陸船、「アクエリアス」が取り付けられていた。', 'c', 'a gold-foil spider-legged lunar module floating in black space, close view'),
    (9, '旅は、順調だった。船内では、3人が冗談を言い合うほどだった。', 's', CMIN + ', three astronauts floating and laughing in zero gravity, relaxed'),
    (9, '地球に向けて、テレビ中継も行われた。', 'l', SWIG + ' floating in a spacecraft holding a television camera, smiling, 1970'),
    (9, 'しかし、アメリカのテレビ局の多くは、その中継を放送しなかった。', 'l', 'a television studio of 1970 with an empty news desk, cameras turned away, no readable text'),
    (9, '月への旅は、もう、ニュースにならなかったのだ。', 'c', EARTH + ', silent, the spacecraft far away and unnoticed'),
    # ch4 爆発
    (10, '4月13日の夜。発射から、およそ56時間。', 's', STACK + ', drifting quietly in the darkness, calm before the storm'),
    (10, 'テレビ中継を終えた3人は、それぞれの作業に戻っていた。', 'l', CMIN + ', three astronauts putting away a camera and floating to their positions, quiet'),
    (10, '地上の管制室から、1つの指示が届いた。酸素タンクの中を、かき混ぜてほしい。', 'l', MCC + ', a controller speaking into a headset microphone, routine'),
    (10, 'いつも行っている、簡単な作業だった。スワイガートが、スイッチを入れた。', 'l', 'close-up of a finger flipping a toggle switch on a spacecraft control panel, ordinary moment'),
    (10, 'その直後、宇宙船に、ドンという大きな音と衝撃が走った。', 'x', STACK + ', a sudden violent burst from the side of the service module, debris flying, dramatic, not gory'),
    (11, '船内の警報が鳴り響き、計器の針が、一斉に揺れ始めた。', 's', CMIN + ', red warning lights flashing, needles swinging on gauges, chaos'),
    (11, 'スワイガートは、地上に向かって、こう伝えた。', 'l', 'close-up of ' + SWIG + ' pressing a microphone to his mouth, tense face'),
    (11, 'ヒューストン、問題が起きた。', 'c', 'close-up of a 1970 headset microphone in front of a tense astronaut face, red light, dramatic'),
    (11, '最初、地上の管制室は、何が起きたのか、わからなかった。', 's', MCC + ', controllers frozen, staring at their screens in confusion'),
    (11, '画面の数字は、次々とおかしな値を示していた。計器の故障だと考える者もいた。', 'l', 'close-up of a 1970 green monochrome console screen with columns of numbers, a controller squinting, no readable text'),
    (11, '電気を作る装置が、2つ止まっていた。そして、酸素の量が、みるみる減っていった。', 'c', 'close-up of an oxygen gauge needle dropping toward zero on a spacecraft panel, ominous'),
    (12, 'ラベルは、窓の外を見た。', 's', 'close-up of ' + LOVELL + ' pressing his face to a small triangular window, eyes widening'),
    (12, '宇宙船のまわりに、白い霧のようなものが、噴き出していた。', 'l', STACK + ', a white cloud of gas spraying into space from the service module, glittering in sunlight'),
    (12, 'それは、宇宙船の命綱ともいえる、酸素だった。', 'l', 'close-up of white gas venting into black space from a torn metal panel, sunlight, dramatic'),
    (12, 'ラベルは、こう伝えた。何かが、宇宙に噴き出している。', 'l', LOVELL + ' speaking into a microphone in a dark cockpit, grave face'),
    (12, 'この瞬間、3人の運命は、大きく変わった。', 'c', CREW + ' looking at each other in silence inside a spacecraft, fear in their eyes'),
    # ch5 月をあきらめる
    (13, '管制室の責任者は、フライトディレクターの、ジーン・クランツだった。', 's', 'portrait of ' + KRANZ + ', standing in mission control'),
    (13, 'クランツは、まず、全員にこう命じた。落ち着け。推測でものを言うな。', 'l', KRANZ + ' raising his hand to quiet a room full of controllers, commanding'),
    (13, '事実を1つずつ確かめ、何が起きているのかを、正確につかもうとした。', 'l', 'controllers of 1970 at consoles writing notes and talking into headsets, focused'),
    (13, 'わかってきたことは、最悪の内容だった。', 'c', 'close-up of a tired controller taking off his glasses and rubbing his eyes, bad news'),
    (14, '機械船にあった、2つの酸素タンク。その1つが、爆発していた。', 's', 'a cutaway illustration of a spacecraft service module with two round tanks, one burst open, documentary style, no readable text'),
    (14, 'そして、残ったもう1つのタンクからも、酸素が漏れ続けていた。', 'l', 'a round metal tank inside a spacecraft leaking white gas from a cracked pipe, close-up'),
    (14, '司令船の電気は、酸素を使って作られていた。酸素がなくなれば、電気も止まる。', 'l', 'a dark spacecraft control panel with lights going out one by one, ominous'),
    (14, '残された時間は、わずか、2時間ほどだった。', 'c', 'a large analog clock on the wall of a 1970 control room, the hands ticking, tense'),
    (15, 'クランツたちは、決断した。月への着陸は、中止する。', 's', KRANZ + ' standing up at his console and speaking firmly to the room, decisive'),
    (15, 'これからの目標は、ただ1つ。3人を、生きて地球に帰すことだ。', 'l', MCC + ', all controllers turning toward the flight director, determination'),
    (15, '宇宙船の中で、ラベルは、窓から月を見つめていた。', 'l', LOVELL + ' looking through a small window at the grey Moon, quiet sorrow'),
    (15, 'あと少しで、手が届くはずだった月。その夢は、ここで終わった。', 'c', MOON + ', large and close, out of reach, melancholy'),
    # ch6 救命ボート
    (16, '問題は、どうやって、生き延びるかだった。', 's', CMIN + ', the lights dimming, three astronauts working quickly in the dark'),
    (16, '司令船の電気は、地球に戻るときのために、残しておかなければならない。', 'l', 'close-up of hands switching off rows of switches on a spacecraft panel, careful'),
    (16, 'そこで目をつけたのが、月に降りるはずだった、着陸船アクエリアスだった。', 'l', 'a gold-foil spider-legged lunar module attached to the nose of a command module, floating in space, hope'),
    (16, '着陸船には、独自の電気と、酸素と、エンジンがあった。', 'l', LMIN + ', lights switching on, panels glowing, coming to life'),
    (16, '3人は、司令船の電気を落とし、着陸船へと移った。', 'c', CREW + ' floating one by one through a narrow tunnel from the command module into the lunar module'),
    (17, 'こうして、月着陸船は、宇宙の救命ボートになった。', 's', STACK + ', the lunar module glowing faintly, the command module dark, lifeboat'),
    (17, 'しかし、着陸船は、2人が、2日ほど過ごすためにつくられた乗り物だった。', 'l', LMIN + ', two narrow standing positions, very cramped, documentary illustration'),
    (17, 'そこに、3人が、4日間乗り続けなければならない。', 'l', CREW + ' squeezed into a tiny cramped lunar module cabin, shoulder to shoulder'),
    (17, '電気も、水も、酸素も、まったく足りなかった。', 'c', 'a chalkboard of 1970 covered with calculations of power, water and oxygen, an engineer staring at it, no readable text'),
    (18, '地上では、着陸船をつくった会社の技術者たちも集まり、計算をやり直した。', 's', 'engineers of 1970 crowded around a table covered with paper charts in a hangar, urgent'),
    (18, '使える電気を、1日ごとに細かく割り当てる。', 'l', 'close-up of a hand writing numbers on a paper chart with a pencil, slide rule beside it, no readable text'),
    (18, '使わない装置は、すべて止める。ヒーターも、コンピューターの多くも止める。', 'l', LMIN + ', panels going dark switch by switch, only a few lights left'),
    (18, '宇宙船は、ほとんど、眠ったような状態になった。', 'c', STACK + ', dark and silent, drifting in the void'),
    # ch7 月の裏側
    (19, 'もう1つの問題は、帰り道だった。', 's', EARTH + ' and the Moon in the same view, a long curved path between them, documentary illustration'),
    (19, '宇宙船は、月へ向かって、ものすごい速さで進んでいた。', 'l', STACK + ', speeding toward the Moon, motion blur of stars'),
    (19, 'その場で向きを変えて引き返すには、燃料も、エンジンも足りなかった。', 'l', 'a large engine bell of a spacecraft service module, dark and damaged, unusable'),
    (19, 'そこで選ばれたのは、月の周りを回り、その引力を使って、地球へ戻る道だった。', 'l', 'an illustrated diagram of a spacecraft path looping around the Moon and returning to the Earth, no readable text'),
    (19, 'ただし、そのためには、着陸船のエンジンを使って、進む道を細かく直す必要があった。', 'c', 'the descent engine of a gold lunar module firing a soft blue flame in space'),
    (20, '着陸船のエンジンが、短く火を噴いた。', 's', STACK + ', a small engine burn glowing beneath the lunar module, precise'),
    (20, '本来なら、司令船のコンピューターで計算するはずの噴射だった。', 'l', 'close-up of a dark command module computer keypad, switched off, frost'),
    (20, '地上の計算をもとに、3人は、慎重にエンジンを操作した。', 'l', CREW + ' gathered at the lunar module controls, reading numbers from a paper, focused'),
    (20, '宇宙船は、月を回って、地球へ戻る軌道に乗った。', 'l', STACK + ', approaching the Moon, the grey surface filling the view'),
    (20, 'やがて宇宙船は、月の裏側へと入っていった。', 'l', 'a spacecraft disappearing behind the edge of the Moon into darkness'),
    (20, '月の裏側にいる間は、地球との通信が、完全に途切れる。', 'c', MCC + ', controllers waiting in silence, static on the speakers, tense'),
    (21, '3人の目の前に、月の裏側の景色が、広がった。', 's', 'the far side of the Moon seen from close orbit, rugged craters, harsh sunlight, breathtaking'),
    (21, 'このとき彼らは、人類史上、地球から最も遠く離れた人間になった。', 'l', 'a tiny spacecraft above the far side of the Moon, the Earth tiny in the distance, epic scale'),
    (21, 'その距離は、およそ40万キロメートル。この記録は、今も破られていない。', 'l', EARTH + ', tiny and blue rising above the grey edge of the Moon, awe'),
    (21, 'ヘイズとスワイガートは、カメラを手に、窓の外を撮り続けた。', 'l', HAISE + ' and ' + SWIG + ' pressing a camera to a small window, the Moon outside'),
    (21, 'ラベルは、もう二度と、ここへ来ることはないだろうと思っていた。', 'c', 'close-up of ' + LOVELL + ' looking at the Moon through a window, bittersweet'),
    (22, '月の裏側を抜けたあと、もう1度、エンジンを噴かす必要があった。', 's', STACK + ' emerging from behind the Moon into sunlight'),
    (22, '帰り道を急ぐためだ。このままでは、地球に着くまで、時間がかかりすぎる。', 'l', 'close-up of a 1970 mission timer clock on a console, numbers counting, no readable text'),
    (22, '着陸船のエンジンが、およそ4分半、燃え続けた。', 'l', 'the descent engine of a gold lunar module firing a long bright flame in space, powerful'),
    (22, '地球に帰る時間が、およそ10時間、短くなった。', 'c', MCC + ', controllers nodding with relief, small smiles'),
    # ch8 凍える船内
    (23, 'しかし、本当の苦しみは、ここからだった。', 's', LMIN + ', dark, cold, three silhouettes in the dim light'),
    (23, '電気を節約するため、ヒーターは止められていた。', 'l', 'close-up of frost forming on a metal panel and a small spacecraft window, cold'),
    (23, '船内の温度は、どんどん下がり、やがて、3度ほどにまでなった。', 'l', CREW + ' shivering in the dark, wrapped in thin coveralls, breath steaming'),
    (23, '壁や窓には、水滴がつき、凍りついていった。', 'l', 'close-up of water droplets and ice crystals on the inside of a small triangular spacecraft window'),
    (23, '3人は、寒さで、ほとんど眠ることができなかった。', 'c', SWIG + ' curled up in a dark corner of a spacecraft, trying to sleep, shivering'),
    (24, '水も、足りなかった。', 's', 'close-up of a small water bag with a little water inside, floating in zero gravity'),
    (24, '着陸船の水は、装置を冷やすためにも使われていた。', 'l', 'a cutaway illustration of pipes and cooling equipment inside a spacecraft, documentary style, no readable text'),
    (24, '3人は、1日に、コップ1杯ほどの水しか飲まなかった。', 'l', HAISE + ' taking a tiny sip from a water bag, thirsty, tired'),
    (24, 'やがて、ヘイズは、体の具合が悪くなり、高い熱を出した。', 'l', 'close-up of ' + HAISE + ' sweating and shivering at the same time, fever, pale face'),
    (24, '寒さの中で、熱に震えながら、彼はそれでも、仕事を続けた。', 'c', HAISE + ' working at a dim control panel despite fever, determined'),
    (24, '地上では、医師たちも、3人の体の状態を、心配しながら見守っていた。', 's', 'flight surgeons of 1970 at a console in mission control looking at heart rate readouts, worried, no readable text'),
    (24, 'しかし、宇宙船にある薬は限られ、できることは、ほとんどなかった。', 'c', 'a small open medical kit floating in a dark spacecraft cabin, few items inside'),
    (25, '狭い船内で、3人の疲れは、限界に近づいていた。', 's', CREW + ' exhausted, unshaven, floating in a cramped dark cabin'),
    (25, '眠れない。食べられない。体が冷えきって、頭もうまく働かない。', 'l', 'close-up of ' + LOVELL + ' with tired red eyes, stubble, cold breath'),
    (25, '1つの小さなミスが、命取りになる。', 'l', 'close-up of a finger hovering over a spacecraft switch, hesitating, tension'),
    (25, 'それでも3人は、互いに声をかけ合い、決められた手順を、1つずつこなしていった。', 'c', CREW + ' helping each other in the cramped cabin, reading a checklist together, teamwork'),
    (25, 'ラベルは、船長として、2人の様子に、いつも気を配っていた。', 's', LOVELL + ' putting a hand on the shoulder of a tired crewmate in a dark cabin, leadership'),
    (25, '誰かが弱音を吐けば、別の誰かが、それを笑いに変えた。', 'c', CREW + ' sharing a tired smile in a cold dark cabin, small moment of humor'),
    # ch9 二酸化炭素
    (26, 'やがて、もう1つの危険が、静かに迫ってきた。', 's', LMIN + ', dim light, a faint haze in the air, ominous'),
    (26, '人が吐く息に含まれる、二酸化炭素だ。', 'l', 'close-up of an astronaut breathing out in cold air, breath visible, dark'),
    (26, '宇宙船の中では、特別な装置で、二酸化炭素を取り除いていた。', 'l', 'a round canister filter inside a spacecraft wall, close-up, documentary style'),
    (26, 'しかし、着陸船の装置は、2人分しか、想定されていなかった。', 'l', 'close-up of a gauge needle rising slowly into the red zone on a spacecraft panel'),
    (26, '3人で使い続けると、空気の中の二酸化炭素は、どんどん増えていく。', 'c', CREW + ' looking at a rising gauge with worried faces, sweat, headache'),
    (27, 'このままでは、3人は、自分たちの吐く息で、意識を失ってしまう。', 's', 'close-up of ' + SWIG + ' rubbing his forehead, dizzy, headache, dim light'),
    (27, '司令船には、予備のフィルターが、たくさん残っていた。', 'l', 'a stack of square filter cartridges stored inside a command module compartment'),
    (27, 'ところが、司令船のフィルターは四角く、着陸船の装置は丸かった。', 'l', 'a square filter cartridge held next to a round filter opening, close-up, mismatch'),
    (27, '形が合わず、そのままでは、使うことができなかった。', 'c', 'close-up of hands trying to fit a square cartridge into a round hole, frustration'),
    (28, '地上では、技術者たちが、机の上に、宇宙船にある物をすべて並べた。', 's', 'engineers of 1970 dumping a box of items onto a table: plastic bags, tape, cardboard, hoses, socks'),
    (28, 'ビニール袋、ガムテープ、ホース、ボール紙、そして靴下。', 'l', 'close-up of a table with plastic bags, a roll of gray duct tape, hoses and cardboard, 1970'),
    (28, 'これだけを使って、四角いフィルターを、丸い装置につなぐ方法を考えるのだ。', 'l', 'engineers of 1970 working with tape and plastic bags around a square cartridge, inventive, focused'),
    (28, '技術者たちは、何時間もかけて、その道具を作り上げた。', 'c', 'a strange makeshift contraption of plastic bags, cardboard and gray duct tape held up by a proud engineer'),
    (29, '作り方は、無線で、1つずつ、宇宙船に伝えられた。', 's', 'a controller of 1970 reading instructions into a headset microphone, careful'),
    (29, '袋を切り、テープを巻き、ホースをつなぐ。', 'l', 'close-up of an astronaut tearing gray duct tape in zero gravity, focused'),
    (29, '3人は、寒さでかじかむ手で、慎重に作業を進めた。', 'l', CREW + ' building a makeshift contraption of bags and tape inside a cramped cabin, teamwork'),
    (29, '完成した装置を取り付け、しばらくすると、計器の針が、ゆっくりと下がり始めた。', 'l', 'close-up of a gauge needle slowly falling back from the red zone, relief'),
    (29, '二酸化炭素の量が、減り始めたのだ。', 'c', MCC + ', controllers cheering quietly and patting each other on the back, relief'),
    (29, 'ビニール袋とガムテープが、3人の命をつないだ。', 's', 'close-up of a makeshift device of plastic bags, cardboard and gray duct tape attached to a spacecraft wall, triumphant'),
    (29, '限られた物しかない宇宙で、知恵と工夫が、危機を救ったのだ。', 'c', 'engineers of 1970 in mission control shaking hands and smiling, tired but proud'),
    # ch10 手動の噴射
    (30, 'しかし、問題は、まだ終わらなかった。', 's', STACK + ', drifting slightly off course, the Earth in the distance'),
    (30, '宇宙船の進む道が、少しずつ、ずれ始めていたのだ。', 'l', 'an illustrated diagram of a spacecraft path slowly drifting away from the correct line toward the Earth, no readable text'),
    (30, 'このままでは、地球の大気に、正しい角度で入ることができない。', 'l', EARTH + ', the thin glowing blue line of the atmosphere at the edge, close view'),
    (30, '角度が浅すぎれば、宇宙船は大気にはね返され、宇宙の闇へと飛んでいってしまう。', 'l', 'a small spacecraft skipping off the edge of the Earth atmosphere back into space, dramatic illustration'),
    (30, '深すぎれば、熱に耐えられず、燃えつきてしまう。', 'c', 'a spacecraft glowing with intense fire entering the atmosphere, dramatic, danger'),
    (31, '道を直すため、もう1度、エンジンを噴かすことになった。', 's', LMIN + ', three astronauts preparing for an engine burn, tense'),
    (31, 'しかし、電気を節約するため、向きを測るコンピューターは、止まっていた。', 'l', 'close-up of a dark spacecraft navigation computer display with no lights, switched off'),
    (31, '頼れるのは、窓から見える、地球だけだった。', 'l', EARTH + ', seen through a small triangular spacecraft window, a thin line of daylight and night across it'),
    (31, 'ラベルは、窓の十字の目印に、地球の昼と夜の境目を合わせ、手で宇宙船の向きを保った。', 'l', 'close-up of ' + LOVELL + ' gripping a hand controller, eyes fixed on a crosshair in the window'),
    (31, 'ヘイズが反対側の向きを担当し、スワイガートが時間を計った。', 'c', HAISE + ' and ' + SWIG + ' working beside the commander, one watching a stopwatch, teamwork'),
    (32, 'エンジン点火。', 's', 'the descent engine of a gold lunar module igniting with a bright flame in space'),
    (32, 'わずか14秒ほどの噴射。3人は、息を止めるようにして、その時間を耐えた。', 'l', CREW + ' braced in a shaking cabin, faces lit by a warning light, intense focus'),
    (32, 'エンジンが止まった。', 'l', 'a quiet moment inside a dark spacecraft cabin, the engine silent, held breath'),
    (32, '地上からの答えは、完ぺきだった。', 'c', MCC + ', controllers smiling and nodding, relief and pride'),
    (33, '3人の、手と目だけで行った操作だった。', 's', 'close-up of an astronaut hand resting on a hand controller, steady'),
    (33, 'コンピューターがなくても、人間の力で、宇宙船を正しい道に戻したのだ。', 'l', STACK + ', on the correct path toward the Earth, which grows larger ahead'),
    (33, '地球が、少しずつ、大きくなってきた。', 'c', EARTH + ', larger and brighter, seen from space, hope'),
    (33, 'しかし、地上の家族にとっては、眠れない夜が続いていた。', 's', 'an American wife of 1970 sitting alone by a window at night, holding a phone, worried'),
    (33, 'ラベルの妻は、テレビのニュースを見ながら、ひたすら夫の無事を祈っていた。', 'c', 'a woman of 1970 watching a television news broadcast in a dark living room, praying, no readable text'),
    # ch11 最後の準備
    (34, '最後に、もう1つ、大きな壁が残っていた。', 's', CMIN + ', completely dark and frozen, ice on the panels'),
    (34, '地球に帰るには、着陸船ではなく、司令船に乗らなければならない。', 'l', 'a white cone-shaped Apollo command module with a heat shield, documentary illustration'),
    (34, '大気に入る熱に耐えられるのは、司令船だけだったからだ。', 'l', 'close-up of the heat shield on the bottom of a cone-shaped capsule, scorched texture'),
    (34, 'しかし、司令船は、何日も電気を落としたまま、冷えきっていた。', 'l', CMIN + ', dark and cold, frost on the switches and windows'),
    (34, 'それを、少ない電気で、もう1度動かす。そんな手順は、どこにもなかった。', 'c', 'an engineer of 1970 staring at a blank sheet of paper on a desk, under pressure, no readable text'),
    (35, 'その手順を作ったのは、地上に残った、マッティングリーたちだった。', 's', 'a young American astronaut with short light hair in a white shirt sitting in a dark spacecraft simulator, focused'),
    (35, '宇宙へ行けなかった彼は、仲間を救うため、訓練用の装置に何時間もこもった。', 'l', 'a 1970 spacecraft simulator room at night, a single astronaut working inside, cables everywhere'),
    (35, 'どのスイッチを、どの順番で入れれば、電気が足りるのか。', 'l', 'close-up of a hand flipping switches in a simulator cockpit, testing, sweating'),
    (35, '何度も失敗し、何度もやり直した。', 'c', 'a tired young astronaut rubbing his face in a dim simulator, papers floating around, no readable text'),
    (36, 'ようやく完成した手順は、長い長い、作業のリストになった。', 's', 'a long stack of checklist papers held by a controller, no readable text'),
    (36, 'それを、スワイガートが、無線を聞きながら、すべて書き取った。', 'l', SWIG + ' writing down instructions on paper with a pencil in a cold dark cabin, focused'),
    (36, '書き取るだけで、何時間もかかった。', 'c', 'close-up of a hand writing with a pencil, papers full of notes floating in zero gravity, no readable text'),
    (37, '地球への突入の数時間前。まず、機械船を切り離した。', 's', 'a silver service module separating and drifting away from a command module in space'),
    (37, '遠ざかる機械船を見て、3人は、息をのんだ。', 'l', CREW + ' pressing their faces to small windows, shocked'),
    (37, '側面の板が1枚、まるごと吹き飛び、中がむき出しになっていた。', 'l', 'a silver cylindrical service module with one entire side panel blown away, exposed damaged interior, drifting in space'),
    (37, '自分たちが、どれほど危険な状態にあったのか。3人は、このとき初めて知った。', 'c', 'close-up of ' + LOVELL + ' staring out the window in silence, realization'),
    # ch12 帰還
    (38, 'そして、司令船が、目を覚ました。', 's', CMIN + ', lights flickering back on one by one, panels glowing, coming back to life'),
    (38, 'マッティングリーたちの手順は、見事に成功した。', 'l', MCC + ', controllers exhaling with relief, a young astronaut in a white shirt smiling'),
    (38, '3人は、司令船へ戻り、最後に、着陸船を切り離した。', 'l', 'a gold-foil lunar module separating and drifting away from a command module, the Earth behind'),
    (38, '4日間、彼らの命を守り続けた、アクエリアス。', 'l', 'a gold-foil lunar module drifting alone in space against the Earth, farewell'),
    (38, 'さよなら、アクエリアス。ありがとう。', 'c', 'close-up of ' + LOVELL + ' watching through a window as the lunar module drifts away, gratitude'),
    (39, '1970年4月17日。司令船は、地球の大気へと突入した。', 's', 'a cone-shaped capsule entering the Earth atmosphere surrounded by bright orange plasma, dramatic'),
    (39, '表面は、数千度の熱に包まれる。この間、地上との通信は、途切れる。', 'l', 'a capsule streaking through the sky as a glowing fireball, intense heat'),
    (39, 'いつもなら、通信が戻るまで、およそ4分。', 'l', MCC + ', controllers staring at a silent screen, waiting'),
    (39, 'しかし、4分がたっても、宇宙船からの声は、聞こえてこなかった。', 'l', 'close-up of a large analog clock in a 1970 control room, second hand moving, tension'),
    (39, '5分。そして、6分近く。管制室は、静まり返った。', 'c', MCC + ', complete silence, controllers frozen, some praying'),
    (40, 'そのとき、スピーカーから、声が聞こえた。', 'x', 'close-up of a 1970 control room speaker, a controller leaning toward it'),
    (40, 'スワイガートの声だった。', 'l', 'close-up of ' + SWIG + ' speaking into a microphone inside a capsule, exhausted but alive'),
    (40, '管制室に、大きな歓声が上がった。', 'l', MCC + ', controllers cheering, jumping and embracing, joy'),
    (40, '空には、3つの大きなパラシュートが、開いていた。', 'l', 'a cone-shaped capsule descending under three large orange and white parachutes in a blue sky'),
    (40, '司令船は、南太平洋の海へ、静かに着水した。', 'c', 'a cone-shaped capsule splashing down in a calm blue ocean, sunlight'),
    (41, '近くで待っていた船から、救助のヘリコプターが飛び立った。', 's', 'a 1970 navy helicopter flying over a calm ocean toward a floating capsule'),
    (41, '3人は、やせて、疲れきっていた。それでも、自分の足で、甲板に立った。', 'l', CREW + ' standing on the deck of a navy ship, thin and exhausted, waving, sailors cheering'),
    (41, '世界中の人々が、テレビの前で、その姿を見守っていた。', 'l', 'people of 1970 in many countries gathered around televisions, crying and cheering'),
    (41, '月への旅に興味を失っていた人々が、今度は、3人の帰りを祈っていたのだ。', 'c', 'a crowd of people of 1970 in a city square watching a big television screen, joyful, no readable text'),
    # ch13 その後
    (42, 'その後の調べで、事故の原因が明らかになった。', 's', 'investigators of 1970 examining a round metal tank in a laboratory, serious, no readable text'),
    (42, '酸素タンクの中の、電気の部品が、古い規格のまま残されていた。', 'l', 'a cutaway illustration of a metal tank with wires and a small switch inside, documentary style, no readable text'),
    (42, '発射前の地上での作業中、タンクの中が高い熱にさらされ、電線の覆いが傷ついていた。', 'l', 'close-up of damaged scorched wire insulation inside a metal tank, documentary'),
    (42, '宇宙で、そのタンクのスイッチを入れたとき、火花が出て、爆発につながったのだ。', 'l', 'a cutaway illustration of a spark inside a metal tank turning into an explosion, documentary style'),
    (42, '誰も気づかなかった小さな見落としが、重なっていた。', 'c', 'a dark archive desk with an inspection report and a magnifying glass, single lamp, no readable text'),
    (43, 'アポロ13号は、月に降りることはできなかった。', 's', MOON + ', silent and untouched, seen from far away'),
    (43, 'しかし、この出来事は、のちに「成功した失敗」と呼ばれるようになった。', 'l', 'three astronauts of 1970 in suits standing together at a ceremony, applause, dignified'),
    (43, '絶望的な状況から、全員が生きて帰ってきたからだ。', 'l', CREW + ' smiling together in front of an American flag, 1970, relief'),
    (43, '事故の教訓は、その後のアポロ計画に生かされ、宇宙船は改良された。', 'c', 'engineers of 1970 installing a new tank into a spacecraft service module in a clean room'),
    (44, 'ラベルは、その後、二度と宇宙へ行くことはなかった。', 's', 'an older ' + LOVELL.replace('in his forties', 'in his sixties') + ', looking up at the Moon in the night sky, peaceful'),
    (44, 'しかし、この体験を本にまとめ、それは映画にもなり、世界中で知られるようになった。', 'l', 'an older man of the 1990s signing books at a table, a long line of people, no readable text'),
    (44, 'マッティングリーは、のちにアポロ16号で、月へ向かった。', 'l', 'a spacecraft orbiting the Moon in 1972, an astronaut in the window, triumph'),
    (44, 'ヘイズは、その後も、宇宙開発の仕事を続けた。', 'c', 'an older engineer of the 1970s looking at a space shuttle on a runway, proud'),
    (45, '酸素の爆発、凍える寒さ、増え続ける二酸化炭素。', 's', STACK + ', drifting in darkness with the damaged side visible, the Earth far away'),
    (45, 'どれか1つでも乗り越えられなければ、3人は帰れなかった。', 'l', CREW + ' in a dark cold cabin, holding on, determination'),
    (45, '彼らを救ったのは、あきらめない心と、宇宙と地上をつないだ、何百人もの力だった。', 'l', MCC + ', crowded with people working together, warm light, unity'),
    (45, '限られた物で、限られた時間の中、人間は、ここまでできる。', 'c', 'the makeshift contraption of plastic bags, cardboard and gray duct tape displayed in a museum case, soft light'),
    (45, 'このチャンネルでは、実際に起きた極限のサバイバルを記録している。', 's', 'a dark archive room with shelves of case files, one file open under a single desk lamp'),
    (45, '次の記録を見逃さないよう、チャンネル登録をお願いしたい。', 'x', 'the case file closing, the desk lamp switching off, darkness'),
]

# ---- 以下、パイプライン用の設定 ----
SCENE = "deep space between the Earth and the Moon / NASA mission control Houston, April 1970"
STYLE = ("Japanese gekiga manga illustration style (hand-drawn comic art, NOT photorealistic), bold black ink linework with cross-hatching, "
         "painted full colors, deep black space with harsh white sunlight, cold blue cabin light, "
         "accurate 1970 period details, ONE single full-frame illustration showing one continuous scene (absolutely NO comic panels, "
         "NO split screen, NO inset frames, NO borders), dramatic high contrast cinematic lighting, serious documentary mood, "
         "not gory, no speech bubbles, no text, no letters, no captions, no logos, no flags with text")
TTS_SPEED = 0.90

READINGS = {"ラベル": "ラベル", "司令船": "しれいせん", "機械船": "きかいせん", "着陸船": "ちゃくりくせん", "噴射": "ふんしゃ",
            "着水": "ちゃくすい", "甲板": "かんぱん"}
STAMPS = {}
for _c, _t, _p, _i in LINES:
    for _k, _v in [("1970年4月。", "1970年4月"), ("1969年7月。", "1969年7月"), ("1970年4月11日。", "1970年4月11日"),
                   ("4月13日の夜。", "1970年4月13日"), ("1970年4月17日。", "1970年4月17日")]:
        if _t.startswith(_k):
            STAMPS[_t] = _v
THUMB = {"image": 50, "big": "アポロ13号", "red": "生還", "top": "月へ向かう宇宙船で爆発", "sub": "酸素が尽きる…地球まで32万キロの脱出劇"}
SHORT = {"sel": [46, 48, 49, 50, 51, 52, 53, 56, 58],
         "stamp": {"46": "1970年4月13日"},
         "h1": "【実話】アポロ13号", "h2": "宇宙で酸素タンクが爆発", "e1": "残された時間は、わずか2時間――", "e2": "▶ 続きは本編で（固定コメント）",
         "title": "【実話】月へ向かう宇宙船で爆発…「ヒューストン、問題が起きた」アポロ13号 #shorts",
         "desc": "1970年、月へ向かうアポロ13号で酸素タンクが爆発した。地球から32万キロ、3人の飛行士に残された時間は――。\n#実話 #アポロ13号 #宇宙 #サバイバル #shorts"}
META = {"title": "【実話】アポロ13号…月へ向かう宇宙船で酸素タンクが爆発、地球まで32万キロから生還した3人の4日間",
        "description": ("アポロ13号（1970年）の実話。月面着陸を目指した宇宙船で、酸素タンクが爆発した。\n"
                        "「ヒューストン、問題が起きた」――電気も水も酸素も足りない中、3人の飛行士は月着陸船を救命ボートにして地球を目指した。"
                        "凍える船内、増え続ける二酸化炭素、手動でのエンジン噴射。宇宙と地上が力を合わせた4日間の脱出劇を、約20分で記録する。\n\n"
                        "▼チャプター\n{CHAPTERS}\n\n"
                        "※映像はすべて実話をもとにした再現イラストです。実在の人物の外見とは異なります。\n"
                        "※出来事の詳細には諸説あります。本動画は記録・資料をもとに構成しています。\n\n"
                        "▼前回：【実話】アンデスの奇跡…雪山に墜ちた45人、救助打ち切りから72日間を生き延びた若者たち\nhttps://youtu.be/YIfZoXJCMuA\n\n"
                        "▼参考資料\n・NASA「Report of Apollo 13 Review Board」(1970)\n・ジム・ラベル、ジェフリー・クルーガー『アポロ13』\n・NASA公開のミッション記録・交信記録\n\n"
                        "ナレーション：VOICEVOX:青山龍星\n\n"
                        "クライシス・ファイル〜極限サバイバル劇画〜\n実際に起きた極限のサバイバルを、劇画で記録するチャンネルです。\n"
                        "チャンネル登録：https://www.youtube.com/@CrisisFiles_Survival\n\n"
                        "#実話 #アポロ13号 #宇宙 #NASA #サバイバル #クライシスファイル"),
        "tags": ["アポロ13号", "アポロ13", "ヒューストン問題が起きた", "宇宙", "NASA", "宇宙事故", "ジム・ラベル", "月面着陸",
                 "サバイバル", "実話", "生還", "クライシスファイル"]}
