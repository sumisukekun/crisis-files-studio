# EP16: Joe Simpson / Siula Grande (1985), ~20 min. Entries: (cut, text, pause, prompt)
# 服装ルール（全カット共通）: ジョー＝赤いジャケット＋紺のオーバーパンツ、サイモン＝青いジャケット＋黒いオーバーパンツ。
JOE = ("Joe, a 25-year-old British mountaineer with short dark-brown hair and a stubbly beard, "
       "wearing a RED 1980s mountaineering jacket, NAVY BLUE salopettes, a white helmet and crampons")
JOEI = JOE + ", his right leg broken and dragging, exhausted, face frostbitten"
SIMON = ("Simon, a 21-year-old British mountaineer with short blond hair, "
         "wearing a BLUE 1980s mountaineering jacket, BLACK salopettes, a yellow helmet and crampons")
RICHARD = "Richard, a young British man with glasses and a woolly hat, in casual brown trekking clothes (not a climber)"
PEAK = "Siula Grande, a steep 6,344-meter snow-and-ice peak in the Cordillera Huayhuash of the Peruvian Andes"
RIDGE = "a knife-edge snowy ridge with overhanging cornices high in the Peruvian Andes"
STORM = "a blizzard at dusk on a steep snow slope high in the Andes, spindrift blowing"
CREV = "the inside of a huge blue-ice crevasse in a glacier, dim blue light, icicles"
GLAC = "a vast crevassed glacier below Siula Grande under a harsh sun"
MOR = "a dry boulder-strewn moraine valley in the Peruvian Andes"
CAMP = "a small base camp with two 1980s tents beside a lake in the Peruvian Andes"
TWO = " Exactly two climbers only, no other people"
ALONE = " He is completely alone, no other people"

CHAPTERS = [
    (1, "切られたザイル"),
    (4, "誰も登ったことのない壁"),
    (8, "頂上"),
    (11, "ひざが砕けた"),
    (15, "90メートルのザイル"),
    (19, "宙づり"),
    (23, "ナイフ"),
    (26, "クレバスの底"),
    (30, "光の方へ"),
    (33, "氷河を這う"),
    (37, "声"),
    (41, "ベースキャンプ"),
    (44, "なぜ生き延びたのか"),
    (45, "その後"),
]

LINES = [
    # ch1 切られたザイル
    (1, '1985年6月。南米ペルー、アンデス山脈の高峰、シウラ・グランデ。', 's', PEAK + ', dramatic clouds, wide view, no people'),
    (1, '標高6344メートルの雪山で、2人のイギリス人登山家が遭難した。', 'l', 'two tiny climbers on a vast steep snow face of ' + PEAK + ',' + TWO),
    (1, '1人の名は、ジョー・シンプソン。25歳。', 'l', 'portrait of ' + JOE + ', serious face, snowy mountains behind'),
    (1, 'もう1人は、サイモン・イェーツ。21歳。', 'l', 'portrait of ' + SIMON + ', determined face, snowy mountains behind'),
    (2, '下山の途中、ジョーは足の骨を折り、自分では歩けなくなった。', 's', JOEI + ', lying in the snow on a steep slope, in agony,' + ALONE),
    (2, '2人をつなぐのは、1本のロープ、ザイルだけ。', 'l', 'close-up of a climbing rope stretched tight across a snow slope in a storm, no people visible'),
    (2, 'そして、吹雪の夜。サイモンは、そのザイルを、自分の手で切った。', 'l', SIMON + ' sitting in a snow seat in a blizzard at night, holding a small pocket knife near a taut rope, anguished face,' + ALONE),
    (2, 'ジョーは、氷の裂け目、クレバスの暗闇へと落ちていった。', 'c', 'a dark blue-ice crevasse opening in a glacier at night, a frayed rope end falling into the darkness, no people visible'),
    (3, 'それでも、ジョーは生きていた。', 's', JOEI + ', lying on an ice ledge inside ' + CREV + ', opening his eyes,' + ALONE),
    (3, '折れた足のまま、食べ物も水もほとんどなく、氷河と岩の谷を、およそ8キロ。', 'l', JOEI + ', crawling across ' + GLAC + ', tiny figure,' + ALONE),
    (3, '彼は、3日間、這い続けて、ベースキャンプに戻ってきたのである。', 'l', JOEI + ', crawling over rocks in ' + MOR + ' at dusk,' + ALONE),
    (3, '仲間に命綱を切られた男は、なぜ、生きて帰ることができたのか。', 'l', 'close-up of the cut end of a rope swinging in the wind over a dark crevasse'),
    (3, 'これは、のちに「運命を分けたザイル」として世界中に知られることになる、実際の遭難事故の記録である。', 'c', 'an old climbing rope cut cleanly in the middle lying on snow, dramatic light, no people'),

    # ch2 誰も登ったことのない壁
    (4, 'ジョーとサイモンは、イギリスの若い登山家だった。', 's', JOE + ' and ' + SIMON + ' laughing together in a 1980s British pub before the expedition, climbing gear on the floor.' + TWO),
    (4, '2人が目指したのは、まだ誰も登ったことのない、シウラ・グランデの西壁。', 'l', 'the huge unclimbed west face of ' + PEAK + ', icy and steep, morning light, no people'),
    (4, '当時のペルー・アンデスには、まだ多くの未踏の壁が残されていた。', 'l', 'a panorama of icy Cordillera Huayhuash peaks at sunrise, no people'),
    (4, 'ジョーは、明るく、少し向こう見ずな性格だった。', 'l', JOE + ' grinning confidently with a coiled rope over his shoulder,' + ALONE),
    (4, 'サイモンは、冷静で、どんな状況でも落ち着いて判断できる男だった。', 'l', SIMON + ' calmly checking climbing gear, focused,' + ALONE),
    (4, '2人は、何度も一緒に山に登り、互いの命をザイルで預け合ってきた仲だった。', 'l', JOE + ' and ' + SIMON + ' roped together on an alpine ridge in the Alps, years earlier.' + TWO),
    (4, '若い登山家にとって、誰も登ったことのない壁を登ることは、何よりの夢だった。', 'l', JOE + ' looking up at a huge icy face with shining eyes,' + ALONE),
    (4, '高さ1300メートル以上、氷と雪がそそり立つ、巨大な壁だった。', 'l', 'a towering wall of ice and fluted snow on ' + PEAK + ', seen from below, no people'),
    (4, '壁の上部には、雪が氷のひだのように張りつき、その先には、雪庇の続く稜線がある。', 'l', 'close-up of fluted snow and overhanging cornices at the top of a huge ice face, no people'),
    (5, '2人は、ふもとの湖のそばに、ベースキャンプを作った。', 's', CAMP + ', ' + JOE + ' and ' + SIMON + ' pitching a tent, ' + RICHARD + ' helping'),
    (5, 'キャンプには、もう1人、リチャード・ホーキングというイギリス人がいた。', 'l', 'portrait of ' + RICHARD + ' sitting by a tent at ' + CAMP),
    (5, 'リチャードは登山家ではなく、旅の途中で知り合い、留守番を引き受けてくれた青年だった。', 'l', RICHARD + ' waving goodbye at ' + CAMP + ', two climbers walking away in the distance'),
    (5, 'ベースキャンプから山のふもとまでは、氷河と岩の谷を、歩いて何時間もかかる。', 'l', MOR + ' leading toward a glacier and a huge white peak, two climbers walking.' + TWO),
    (5, 'もし山で何かが起きても、リチャードには、助けに行く方法はなかった。', 'l', RICHARD + ' sitting alone outside a tent, looking at the distant mountain, worried,' + ALONE),
    (5, '2人は、必要最低限の道具だけを背負い、身軽な姿で壁に向かった。', 'c', JOE + ' and ' + SIMON + ' walking up a glacier toward the west face with small backpacks.' + TWO),
    (6, '登山のスタイルは、アルパインスタイル。', 's', JOE + ' and ' + SIMON + ' climbing a steep ice wall roped together, ice axes in the ice.' + TWO),
    (6, '固定ロープもキャンプも作らず、2人だけで、一気に登って一気に下りる。', 'l', JOE + ' leading up a steep ice gully, ' + SIMON + ' belaying below.' + TWO),
    (6, '速くて自由だが、何かあれば、助けを呼ぶ方法はない。', 'l', 'two tiny climbers on an enormous ice face with no one else for miles, lonely.' + TWO),
    (7, '2人は、ザイルで体をつなぎ、氷に斧を打ち込みながら、少しずつ登っていった。', 's', 'close-up of ice axes and crampons biting into blue ice, a rope trailing, gloved hands'),
    (7, '夜は、雪の斜面に穴を掘り、その中で眠った。', 'l', JOE + ' and ' + SIMON + ' inside a small snow cave at night, a tiny stove glowing.' + TWO),
    (7, '壁の上部は、粉のような雪が、垂直に近い角度で張りついていた。', 'l', 'steep powdery snow flutings on a near-vertical ice face, a climber digging through them,' + ALONE),
    (7, '足を置いた雪が崩れ、いつ落ちてもおかしくない。2人は、何時間もかけて、その雪をかき分けた。', 'l', JOE + ' and ' + SIMON + ' struggling up loose powder snow on a steep face, exhausted.' + TWO),
    (7, '3日目、壁を登りきった2人は、頂上へと続く稜線に出た。', 'c', JOE + ' and ' + SIMON + ' emerging onto ' + RIDGE + ', clouds below.' + TWO),
    (7, '振り返ると、自分たちが登ってきた壁が、足もとの雲の中へと消えていた。', 'l', 'looking down a vast ice face disappearing into clouds below, two climbers on the edge.' + TWO),

    # ch3 頂上
    (8, 'そして、ついに、シウラ・グランデの頂上に立った。', 's', JOE + ' and ' + SIMON + ' standing on the snowy summit of ' + PEAK + ', arms raised.' + TWO),
    (8, '西壁からの、世界で初めての登頂だった。', 'l', 'a sea of clouds and jagged Andes peaks seen from the summit of ' + PEAK + ', golden light, no people'),
    (8, 'しかし、山では、頂上は、ゴールではない。', 'l', 'the summit of ' + PEAK + ' with thickening clouds rolling in, ominous, no people'),
    (8, '生きて下りるまでが、登山である。', 'c', JOE + ' and ' + SIMON + ' turning away from the summit to start descending in fog.' + TWO),
    (9, '2人は、北側の稜線を下ることにした。', 's', JOE + ' and ' + SIMON + ' carefully descending ' + RIDGE + ' in mist.' + TWO),
    (9, '稜線には、雪がひさしのように張り出した、雪庇が続いていた。', 'l', 'huge overhanging snow cornices along a knife-edge ridge, clouds swirling, no people'),
    (9, '雲の中で、どこが地面で、どこが雪のひさしなのか、見分けがつかない。', 'l', 'a white-out on a snowy ridge, ground and sky indistinguishable, two faint figures.' + TWO),
    (9, '一歩まちがえれば、雪のひさしごと、何百メートルも下へ落ちていく。', 'l', 'a boot stepping near the crumbling edge of a snow cornice, a huge void below'),
    (10, 'そのとき、サイモンの足もとの雪庇が崩れ落ちた。', 's', SIMON + ' falling through a collapsing snow cornice, snow blocks tumbling,' + ALONE),
    (10, 'ザイルがぴんと張り、ジョーが踏ん張って、サイモンは何とか助かった。', 'l', JOE + ' bracing hard on the ridge holding a taut rope that disappears over the edge,' + ALONE),
    (10, 'その夜、2人は雪の穴で過ごした。食料も、燃料も、もう尽きていた。', 'c', JOE + ' and ' + SIMON + ' huddled silently in a dark snow hole, an empty stove beside them.' + TWO),
    (10, 'もし、あのとき雪庇の反対側に落ちていたら、2人とも、1000メートル以上下まで落ちていたかもしれない。', 'l', 'looking down a sheer 1000-meter drop from a corniced ridge into clouds, dizzying, no people'),

    # ch4 ひざが砕けた
    (11, '翌朝、2人は、さらに稜線を下っていった。', 's', JOE + ' walking ahead along a snowy ridge in the morning, ' + SIMON + ' following far behind.' + TWO),
    (11, '先を行くジョーが、小さな氷の崖を下りようとしたときだった。', 'l', JOE + ' lowering himself down a small ice cliff with an ice axe,' + ALONE),
    (11, '氷に打ち込んだ斧が、突然、外れた。', 'l', 'close-up of an ice axe ripping out of brittle ice, ice chips flying'),
    (12, 'ジョーは、崖の下へ落ち、右足から雪面にたたきつけられた。', 's', JOE + ' falling down a small ice cliff and landing hard on his right leg in the snow,' + ALONE),
    (12, '右足のすねの骨が、ひざの中へと突き上げられた。', 'l', JOE + ' clutching his right knee in the snow, face twisted in pain, no blood shown,' + ALONE),
    (12, '激しい痛みの中で、ジョーは、自分の足が二度と元に戻らないことを悟った。', 'l', 'close-up of ' + JOE + ' gasping in pain, eyes wide with fear,' + ALONE),
    (13, '標高およそ6000メートル。救助のヘリコプターも、助けに来る人もいない。', 's', 'a vast empty landscape of icy Andes peaks, a tiny red dot of a climber in the snow, no helicopters'),
    (13, 'ここで足を折ることは、死を意味していた。', 'l', JOEI + ', sitting alone in the snow staring at the endless slopes below,' + ALONE),
    (13, 'ジョーは、骨の折れた足を引きずり、何とか1人で進もうとした。', 'l', JOEI + ', trying to hop along the ridge using his ice axes, failing,' + ALONE),
    (13, 'しかし、数歩も進めず、雪の上に倒れこんだ。', 'l', JOEI + ', collapsing face-first into the snow on the ridge,' + ALONE),
    (13, 'ジョーは、サイモンが自分を置いていくだろうと考えた。', 'l', JOE + ' looking up at the ridge, despair on his face,' + ALONE),
    (13, '山の世界には、動けなくなった仲間を、置いていくしかない場面もある。', 'l', 'a lonely set of footprints leading away across a snow ridge in the wind, no people'),
    (13, '1人を助けようとして、2人とも死んでしまうことがあるからだ。', 'l', 'two tiny climbers on a dangerous snow slope above a huge drop, storm clouds.' + TWO),
    (14, '追いついたサイモンも、ジョーの足を見て、同じことを思った。', 's', SIMON + ' arriving and looking down at ' + JOEI + ' in the snow, shocked.' + TWO),
    (14, 'それでも、サイモンは、ジョーを連れて下りることを選んだ。', 'l', SIMON + ' kneeling beside ' + JOEI + ', checking the rope, determined.' + TWO),
    (14, '2人だけの、前例のない下山が始まった。', 'c', 'two climbers on a huge snow slope beginning to descend together, clouds gathering.' + TWO),

    # ch5 90メートルのザイル
    (15, 'サイモンは、2本のザイルを結び合わせ、およそ90メートルの1本にした。', 's', 'close-up of gloved hands tying two climbing ropes together with a knot in the snow'),
    (15, '雪の斜面に座るための穴を掘り、そこに腰を下ろして、体で踏ん張る。', 'l', SIMON + ' sitting in a bucket seat dug into a snow slope, bracing with his legs, belaying a rope,' + ALONE),
    (15, 'そして、ジョーを、ザイルで少しずつ下へ降ろしていく。', 'l', JOEI + ', sliding down a steep snow slope on his back at the end of a rope,' + ALONE),
    (16, 'ザイルの長さいっぱいまで降ろすと、ジョーは、片足で雪を踏み固めて止まる。', 's', JOEI + ', stopping on a snow slope, digging in with one good leg,' + ALONE),
    (16, '今度はサイモンが下りてきて、また新しい穴を掘る。', 'l', SIMON + ' climbing down a steep snow slope toward a distant figure in red.' + TWO),
    (16, 'ザイルの結び目を通すたびに、2人は、何度も危険な作業を繰り返した。', 'l', 'close-up of a rope knot passing through a belay plate in gloved hands, snow blowing'),
    (16, '結び目を通す間は、ザイルを手で押さえ続けなければならない。手がすべれば、ジョーは、そのまま斜面を落ちていく。', 'l', 'close-up of ' + SIMON + ' holding the rope with one hand while passing a knot, intense concentration,' + ALONE),
    (17, '動くたびに、折れた足が雪にぶつかり、ジョーは叫び声を上げた。', 's', 'close-up of ' + JOEI + ', screaming in pain as he slides down the snow,' + ALONE),
    (17, 'それでも、2人は、この方法で、何百メートルも下っていった。', 'l', 'a long steep snow face with a thin rope line and two tiny figures far apart.' + TWO),
    (17, '1回で降ろせるのは、およそ90メートル。それを、何十回も繰り返さなければならない。', 'l', 'a long snow face seen from above with a rope snaking down to a tiny figure in red, ' + SIMON + ' in a snow seat at the top.' + TWO),
    (17, 'サイモンの腕も、もう限界に近づいていた。', 'l', 'close-up of ' + SIMON + ' gritting his teeth, frost on his eyebrows, holding the rope,' + ALONE),
    (17, '天気は崩れ始め、雪が激しく吹きつけてきた。', 'l', STORM + ', two faint figures linked by a rope.' + TWO),
    (17, '風の音で、声はほとんど届かない。2人は、ザイルを引く合図だけで、お互いの様子を知った。', 'l', 'close-up of a rope being tugged twice as a signal, snow blowing, gloved hands'),
    (18, '日が沈み、あたりは暗くなっていった。', 's', 'the sun setting behind jagged Andes peaks, a storm rolling in, no people'),
    (18, '寒さで、手の感覚がなくなっていく。', 'l', 'close-up of frost-covered gloves gripping a rope in the dark, ice crystals'),
    (18, 'あと少し下れば、氷河にたどり着けるはずだった。', 'c', STORM + ' at night, the dark glacier far below.' + TWO),

    # ch6 宙づり
    (19, '吹雪の中、サイモンは、いつものようにジョーを降ろし始めた。', 's', SIMON + ' in a snow seat in a blizzard at night, feeding the rope out, unable to see below,' + ALONE),
    (19, 'しかし、その先には、2人とも知らなかった、切り立った氷の崖があった。', 'l', 'a sheer overhanging ice cliff hidden in the darkness below a snow slope, no people'),
    (19, 'ジョーの体は、崖のふちを越え、宙に投げ出された。', 'l', JOEI + ', sliding over the edge of an ice cliff into the dark, arms flailing,' + ALONE),
    (19, 'サイモンの手に、急にザイルが重くなった感覚が伝わった。', 'l', 'close-up of ' + SIMON + '\'s gloved hands suddenly jerked by the rope, snow seat, night,' + ALONE),
    (20, 'ジョーは、崖の途中で、宙づりになった。', 's', JOEI + ', hanging in mid-air on a rope beside an overhanging ice cliff in a storm at night,' + ALONE),
    (20, '足もとには、暗いクレバスが口を開けていた。', 'l', 'looking down from a hanging rope into a dark gaping crevasse below an ice cliff, night'),
    (20, '叫んでも、吹雪の音で、上のサイモンには届かない。', 'l', JOEI + ', hanging on the rope and shouting upward into the blizzard,' + ALONE),
    (20, 'ザイルは、体の重さでぴんと張り、ゆっくりと回転した。', 'l', JOEI + ', slowly spinning on a taut rope in the dark beside an ice cliff,' + ALONE),
    (20, '手を伸ばしても、氷の崖には届かない。', 'l', 'close-up of a gloved hand reaching toward an ice wall just out of reach in the dark'),
    (21, 'ジョーは、ザイルをよじ登ろうとした。', 's', JOEI + ', hanging on the rope, trying to climb it with a small loop of cord,' + ALONE),
    (21, 'しかし、凍った手では、ひもを結ぶことができない。', 'l', 'close-up of frozen frostbitten gloved hands fumbling with a thin cord on a rope'),
    (21, '登るための細いひもの1本を、暗闇に落としてしまった。', 'l', 'a thin cord loop falling away into the dark abyss below a hanging climber'),
    (22, '一方、上にいるサイモンも、限界だった。', 's', SIMON + ' in a crumbling snow seat at night, the rope pulling him down, straining,' + ALONE),
    (22, 'ジョーの重さに引っぱられ、座っていた雪の穴が、少しずつ崩れていく。', 'l', 'close-up of a snow bucket seat crumbling under a climber\'s boots, the rope taut'),
    (22, 'このままでは、2人とも、崖の下へ引きずり落とされる。', 'c', 'a taut rope disappearing over the dark edge, a climber sliding toward it in the snow, blizzard'),
    (22, 'サイモンには、下で何が起きているのか、まったく見えなかった。', 'l', SIMON + ' peering down into the black blizzard, seeing nothing, the rope vanishing into darkness,' + ALONE),
    (22, 'わかるのは、ザイルにかかる、ジョーの重さだけだった。', 'l', 'close-up of a taut rope cutting into the snow edge, pulled by an unseen weight, blizzard'),

    # ch7 ナイフ
    (23, 'どれだけの時間がたったのか。サイモンは、1時間半以上、そのまま耐え続けたという。', 's', SIMON + ' frozen in place in the blizzard holding the rope, snow piling on his shoulders,' + ALONE),
    (23, 'ザイルを引いても、ジョーは上がってこない。', 'l', SIMON + ' pulling on the taut rope with all his strength, nothing moves,' + ALONE),
    (23, 'そのとき、サイモンは、リュックの中のナイフのことを思い出した。', 'l', SIMON + ' reaching into his backpack with shaking hands in the dark,' + ALONE),
    (24, '切れば、自分は助かるかもしれない。だが、ジョーは死ぬかもしれない。', 's', 'close-up of ' + SIMON + '\'s face in the storm, torn by an impossible decision,' + ALONE),
    (24, '切らなければ、2人とも死ぬ。', 'l', 'a small pocket knife blade glinting near a taut climbing rope in a blizzard'),
    (24, '時間がたつほど、サイモンの指の感覚もなくなっていく。', 'l', 'close-up of ' + SIMON + '\'s frost-white gloves on the rope, trembling,' + ALONE),
    (24, 'サイモンは、ナイフの刃を、ザイルに当てた。', 'l', 'close-up of a knife blade pressing against a taut rope, gloved hand trembling'),
    (24, '一瞬、サイモンの手が止まった。', 'l', 'close-up of a trembling gloved hand holding a knife, frozen in hesitation, blizzard'),
    (25, 'ぴんと張っていたザイルは、一瞬で切れた。', 's', 'a taut rope snapping apart, frayed fibers exploding, darkness'),
    (25, '重さが、ふっと消えた。', 'l', SIMON + ' falling back into his snow seat as the rope goes slack, stunned,' + ALONE),
    (25, 'サイモンは、雪の中で、ただ震えていた。', 'c', SIMON + ' curled up alone in the snow in the blizzard, shaking, head down,' + ALONE),

    # ch8 クレバスの底
    (26, 'ジョーは、暗闇の中を落ちていった。', 's', JOEI + ', falling through the dark air beside an ice cliff, rope trailing,' + ALONE),
    (26, 'そして、氷河に開いたクレバスの中へと、吸い込まれた。', 'l', 'a figure in red falling into the dark mouth of a crevasse at night, snow spraying'),
    (26, '60メートル以上落ちたあと、ジョーの体は、氷の出っ張りの上で止まった。', 'l', JOEI + ', lying on a narrow ice ledge inside ' + CREV + ', motionless,' + ALONE),
    (27, '奇跡的に、彼はまだ生きていた。', 's', 'close-up of ' + JOE + ' opening his eyes on an ice ledge in the dark crevasse, breath steaming,' + ALONE),
    (27, '落ちていく途中で、体のあちこちを氷の壁にぶつけたが、雪がクッションになった。', 'l', 'a body-shaped hollow in soft snow on an ice ledge inside a crevasse, dim blue light'),
    (27, 'ザイルをたぐり寄せると、その先は、きれいに切られていた。', 'l', 'close-up of gloved hands holding the cleanly cut end of a climbing rope, inside a dark crevasse'),
    (27, 'ジョーは、サイモンがザイルを切ったことを知った。', 'l', JOEI + ', staring at the cut rope end in disbelief inside ' + CREV + ',' + ALONE),
    (27, 'ジョーは、サイモンを責めなかったという。', 'l', 'close-up of ' + JOE + ' in the dim crevasse, a tired, understanding look,' + ALONE),
    (27, 'あの状況では、それしか方法がなかったことを、誰よりも分かっていたからだ。', 'l', JOEI + ', sitting on the ice ledge holding the cut rope, quiet,' + ALONE),
    (27, 'だが、ここから、どうやって出ればいいのか。', 'l', 'looking around the dark blue walls of a deep crevasse, no way out, eerie'),
    (28, '一方、サイモンは、翌朝、ひとりで斜面を下りた。', 's', SIMON + ' climbing down alone past the ice cliff in grey morning light,' + ALONE),
    (28, '崖の下には、大きなクレバスが口を開けていた。', 'l', SIMON + ' standing at the edge of a huge crevasse, looking down into the darkness,' + ALONE),
    (28, 'サイモンは、何度もジョーの名前を呼んだ。だが、返事はなかった。', 'l', SIMON + ' shouting into the crevasse with cupped hands, no answer,' + ALONE),
    (29, 'ジョーは、もう死んだ。サイモンは、そう思った。', 's', 'close-up of ' + SIMON + ' with tears freezing on his face at the crevasse edge,' + ALONE),
    (29, 'あの高さから落ちて、助かるはずがない。', 'l', 'the sheer ice cliff and dark crevasse seen from below in grey light, no people'),
    (29, 'サイモンは、ひとりでベースキャンプへと向かった。', 'l', SIMON + ' walking alone down a vast glacier toward a distant valley, small figure,' + ALONE),
    (29, 'キャンプに戻ったサイモンは、リチャードに、ジョーが死んだことを伝えた。', 'l', SIMON + ' sitting by a tent at ' + CAMP + ', head in his hands, ' + RICHARD + ' beside him. Exactly two people'),
    (29, 'ザイルを切ったことは、言えなかった。', 'l', 'close-up of ' + SIMON + '\'s haunted face staring at nothing,' + ALONE),
    (29, 'サイモンは、ジョーの服を燃やし、山に別れを告げた。', 'l', SIMON + ' burning clothes in a small fire by a lake at dusk, grief,' + ALONE),
    (29, 'そのころ、クレバスの中で、ジョーは、まだ生きていた。', 'c', JOEI + ', sitting on an ice ledge in ' + CREV + ', a faint glow from above,' + ALONE),

    # ch9 光の方へ
    (30, 'クレバスの上の入り口は、はるか頭上にあった。', 's', 'looking up from deep inside ' + CREV + ' at a distant slit of grey sky, unreachable'),
    (30, '折れた足で、氷の壁を登ることはできない。', 'l', JOEI + ', looking up at the sheer ice walls of the crevasse, hopeless,' + ALONE),
    (30, 'ジョーは、ある決断をした。', 'l', 'close-up of ' + JOE + ' in the dim crevasse, his face hardening with resolve,' + ALONE),
    (31, '上ではなく、さらに下へ降りる。', 's', JOEI + ', lowering himself on the rope deeper into ' + CREV + ', darkness below,' + ALONE),
    (31, '暗闇の底に何があるのか、わからないまま、ザイルで下りていった。', 'l', JOEI + ', abseiling down into the dark depths of a blue-ice crevasse,' + ALONE),
    (31, 'たどり着いたのは、雪が積もった、クレバスの底だった。', 'l', JOEI + ', landing on a snowy floor deep inside ' + CREV + ',' + ALONE),
    (31, 'もし、底がなければ、ザイルの端から、さらに深い暗闇へ落ちていた。', 'l', 'a rope end dangling over a bottomless black void inside a crevasse'),
    (31, 'それは、命をかけた、賭けだった。', 'l', 'close-up of ' + JOE + ' holding his breath as he lowers himself into darkness,' + ALONE),
    (31, 'ジョーは、ザイルの端に結び目を作った。手がすべっても、すっぽ抜けないようにするためだった。', 'l', 'close-up of gloved hands tying a stopper knot in the end of a rope inside a crevasse'),
    (32, 'そのとき、遠くに、ひとすじの光が見えた。', 's', 'a beam of sunlight shining down through a gap in the ice far away inside a crevasse, magical'),
    (32, 'ジョーは、光に向かって、雪の斜面を這い上がった。', 'l', JOEI + ', crawling up a snow ramp inside the crevasse toward a beam of sunlight,' + ALONE),
    (32, 'そして、ついに、クレバスの外へと抜け出した。', 'c', JOEI + ', emerging from a hole in the glacier into bright sunlight, squinting,' + ALONE),
    (32, '何時間もかかって、ようやく、外の世界に戻ってきたのだ。', 'l', JOEI + ', lying on the glacier surface in sunlight, gasping, relieved,' + ALONE),

    # ch10 氷河を這う
    (33, '目の前には、どこまでも続く氷河が広がっていた。', 's', GLAC + ', endless, a tiny figure in red at the edge of a hole,' + ALONE),
    (33, 'ベースキャンプまでは、およそ8キロ。', 'l', 'a long glacier valley stretching into the distance, a far-off lake, no people'),
    (33, '片足で歩くことはできない。ジョーは、ひじとひざを使って、這うしかなかった。', 'l', JOEI + ', crawling on his elbows and one knee across the snow, dragging his broken leg,' + ALONE),
    (33, '1メートル進むだけで、全身から汗が吹き出し、息が切れた。', 'l', 'close-up of ' + JOEI + ', panting, sweat and frost on his face, crawling,' + ALONE),
    (33, 'それでも、ここに止まれば、待っているのは死だけだった。', 'l', JOEI + ', a tiny figure on an endless white glacier,' + ALONE),
    (34, '氷河には、雪にかくれたクレバスが、いくつも口を開けている。', 's', 'hidden crevasses under a thin crust of snow on a glacier, faint cracks, no people'),
    (34, 'ジョーは、雪の上に残ったサイモンの足あとを見つけた。', 'l', 'a line of boot prints in the snow on a glacier, ' + JOEI + ' crawling beside them,' + ALONE),
    (34, 'その足あとは、安全な道を教えてくれる、たった1つの手がかりだった。', 'l', 'close-up of boot prints in the snow leading away across the glacier, sunlight'),
    (34, 'しかし、午後になると、雪が降り始め、足あとは少しずつ消えていった。', 'l', 'falling snow slowly filling in boot prints on a glacier, grey light, no people'),
    (34, 'ジョーは、足あとが消える前に進もうと、必死に這い続けた。', 'l', JOEI + ', crawling desperately along fading boot prints in falling snow,' + ALONE),
    (35, 'ジョーは、自分に、時間を区切って目標を決めた。', 's', JOEI + ', checking his wristwatch while lying in the snow,' + ALONE),
    (35, '腕時計の針だけが、彼の味方だった。', 'l', 'close-up of a 1980s wristwatch on a frostbitten wrist, snow on it'),
    (35, 'あの岩まで、20分で行く。', 'l', JOEI + ', fixing his eyes on a distant rock on the glacier, determined,' + ALONE),
    (35, '着いたら、また次の目標を決める。それを、何度も、何度も繰り返した。', 'l', JOEI + ', crawling slowly across the glacier under the sun,' + ALONE),
    (35, '20分以内に着けば、自分をほめる。遅れれば、自分をしかりつける。', 'l', JOEI + ', lying beside a rock on the glacier, catching his breath,' + ALONE),
    (35, '大きすぎるゴールを、小さな目標に分けることで、彼は心が折れるのを防いだ。', 'l', JOEI + ', fixing his eyes on the next rock far ahead,' + ALONE),
    (36, '昼は、強い日差しが照りつけ、夜は、凍えるほど寒い。', 's', JOEI + ', lying curled up on the glacier at night under the stars, shivering,' + ALONE),
    (36, '頭の中では、ずっと、ある声が聞こえていたという。', 'l', 'close-up of ' + JOE + '\'s exhausted face in the snow, eyes half closed,' + ALONE),
    (36, '「動け。止まるな。」', 'c', JOEI + ', pushing himself up on his arms in the snow, gritting his teeth,' + ALONE),
    (36, 'その声は、冷静に、次にやるべきことだけを命じてきたという。', 'l', JOEI + ', lying in the snow at dawn, eyes opening, calm and focused,' + ALONE),
    (36, '朝が来ると、ジョーは、また這い始めた。', 'l', JOEI + ', crawling across the glacier in pink dawn light,' + ALONE),

    # ch11 声
    (37, '氷河を抜けると、今度は、大きな岩が転がる谷が待っていた。', 's', MOR + ', huge boulders, a tiny figure in red,' + ALONE),
    (37, 'ジョーは、岩の上を、少しずつ這い進んだ。', 'l', JOEI + ', crawling over sharp boulders in ' + MOR + ',' + ALONE),
    (37, '岩にぶつかるたびに、折れた足に激痛が走った。', 'l', 'close-up of ' + JOEI + ' crying out as his leg hits a boulder,' + ALONE),
    (37, 'ジョーは、テントの中にあった、銀色のマットのことを思い出した。', 'l', JOEI + ', resting against a boulder, remembering, eyes closed,' + ALONE),
    (37, 'ザイルの切れ端で、折れた足に、そのマットを巻きつけ、添え木の代わりにした。', 'l', JOEI + ', wrapping a foam mat around his broken leg with pieces of rope as a splint,' + ALONE),
    (38, 'のどは、からからに乾いていた。', 's', 'close-up of ' + JOE + '\'s cracked lips and sunburned face,' + ALONE),
    (38, '岩のすき間に、わずかな水たまりを見つけ、夢中で口をつけた。', 'l', JOEI + ', drinking from a tiny meltwater pool between rocks,' + ALONE),
    (38, '水の流れる音が聞こえると、ジョーは、何時間もかけて、その音の方へ這っていった。', 'l', JOEI + ', crawling toward a small trickling stream between boulders,' + ALONE),
    (38, '食べ物は、何もない。体は、どんどんやせ細っていった。', 'l', JOEI + ', lying exhausted between boulders, gaunt face,' + ALONE),
    (39, '3日目。ジョーの意識は、もうろうとしていた。', 's', JOEI + ', crawling with unfocused eyes through the moraine at dusk,' + ALONE),
    (39, '頭の中では、昔のポップソングが、何度も鳴り続けていたという。', 'l', JOEI + ', lying on rocks with a dazed half-smile, hallucinating, dreamy light,' + ALONE),
    (39, 'それでも、彼は、止まらなかった。', 'c', JOEI + ', dragging himself forward over rocks under a dark sky,' + ALONE),
    (39, 'もし、サイモンたちがキャンプを去っていたら。その考えが、何度も頭をよぎった。', 'l', JOEI + ', resting against a rock, staring toward the distant lake with fear,' + ALONE),
    (39, '間に合わなければ、ここまで来たことも、すべて無駄になる。', 'l', 'a distant lake and tiny tents seen from far up a rocky valley at dusk, no people'),
    (40, 'その夜、ジョーは、ベースキャンプのすぐ近くまでたどり着いた。', 's', 'a dark moraine at night near a lake, faint tents in the distance, a figure in red crawling,' + ALONE),
    (40, 'しかし、そこで、体は動かなくなった。', 'l', JOEI + ', collapsed face-down on the rocks at night, unable to move,' + ALONE),
    (40, 'ジョーは、残った力をふりしぼって、サイモンの名前を叫んだ。', 'c', JOEI + ', lifting his head and shouting into the night,' + ALONE),
    (40, 'キャンプの近くには、トイレ代わりに使っていた場所があった。そのにおいで、キャンプが近いと分かったという。', 'l', JOEI + ', lifting his head on the dark rocks, sensing the nearby camp,' + ALONE),

    # ch12 ベースキャンプ
    (41, 'そのころ、テントの中では、サイモンとリチャードが、帰りの準備をしていた。', 's', SIMON + ' and ' + RICHARD + ' packing bags inside a tent by candlelight at night. Exactly two people'),
    (41, '2人は、翌朝、キャンプを去るつもりだった。', 'l', CAMP + ' at night, a single candle glowing inside a tent, no people outside'),
    (41, 'サイモンは、もう二度とジョーに会えないと思っていた。', 'l', 'close-up of ' + SIMON + ' staring at the candle flame in the tent, grief,' + ALONE),
    (41, '夜の闇の中から、かすかな声が聞こえた。', 'l', SIMON + ' freezing in the tent, listening, a candle flickering,' + ALONE),
    (42, '最初、サイモンは、それを空耳だと思った。', 's', 'close-up of ' + SIMON + '\'s face in candlelight, doubtful, listening,' + ALONE),
    (42, 'しかし、声は、何度も聞こえてきた。', 'l', SIMON + ' and ' + RICHARD + ' rushing out of a tent with flashlights into the dark night. Exactly two people'),
    (42, '懐中電灯の光の先に、うずくまる人影があった。', 'l', 'a flashlight beam in the dark revealing ' + JOEI + ' lying on the rocks'),
    (43, 'ジョーだった。', 's', 'close-up of ' + JOE + '\'s gaunt bearded face in the flashlight beam, barely alive,' + ALONE),
    (43, 'サイモンは、死んだと思っていた仲間を、抱きかかえた。', 'l', SIMON + ' kneeling and holding ' + JOEI + ' in his arms on the rocks at night. Exactly two people'),
    (43, 'ザイルが切られてから、3日あまり。ジョーは、自力で帰ってきたのだ。', 'c', SIMON + ' and ' + RICHARD + ' carrying ' + JOEI + ' toward the tents by flashlight. Exactly three people'),

    # ch12b なぜ生き延びたのか
    (44, 'なぜ、ジョーは、生き延びることができたのか。', 's', 'a lonely glacier at dusk with a faint crawl track across the snow, no people'),
    (44, '1つ目は、クレバスの中で、上ではなく、下へ進んだことだ。', 'l', JOEI + ', lowering himself down into ' + CREV + ',' + ALONE),
    (44, '登れない壁を前にして、彼は、見えない底に賭けた。', 'l', 'a beam of light at the bottom of a deep crevasse, hope, no people'),
    (44, '2つ目は、目標を、20分ごとの小さな区切りに分けたことだ。', 'l', 'close-up of a wristwatch on a frostbitten wrist in the snow'),
    (44, 'あまりに遠いゴールは、人の心を折ってしまう。だから、目の前の1歩だけを考えた。', 'l', JOEI + ', crawling toward a nearby rock, focused,' + ALONE),
    (44, '3つ目は、サイモンの足あとを、道しるべにしたことだ。', 'l', 'boot prints across a crevassed glacier, a crawl track beside them, no people'),
    (44, '足あとが続いている場所は、少なくとも、人が通れた場所だった。', 'l', 'a safe line of boot prints weaving between crevasses on a glacier, aerial view'),
    (44, 'そして、サイモンが、キャンプにまだ残っていたこと。', 'l', CAMP + ' at night, one candle-lit tent, no people outside'),
    (44, 'あと半日遅ければ、キャンプには、誰もいなかった。', 'c', 'an empty campsite by a lake in the morning, only stones and ashes left, no people'),
    (44, 'いくつもの判断と、いくつもの偶然が重なって、ジョーの命は、つながったのである。', 'l', JOEI + ', looking up at a beam of light inside a crevasse, hope,' + ALONE),

    # ch13 その後
    (45, 'ジョーは、病院に運ばれた。', 's', JOE + ' lying in a 1980s hospital bed in Peru with his right leg in a cast, exhausted,' + ALONE),
    (45, '体重は、大きく減っていた。足の手術は、6回におよんだ。', 'l', 'close-up of a plaster cast on a leg in a hospital bed, medical charts, no gore'),
    (45, '医者からは、もう二度と山には登れないと言われた。', 'l', JOE + ' sitting in a hospital bed looking out the window at distant mountains, thoughtful,' + ALONE),
    (45, 'それでも、ジョーは、生きて帰れたことを、何よりも喜んだ。', 'l', JOE + ' smiling weakly in a hospital bed, sunlight on his face,' + ALONE),
    (46, '一方、サイモンは、ザイルを切ったことで、多くの人から責められた。', 's', SIMON + ' sitting alone in a dim 1980s room, newspapers on the table, no readable text,' + ALONE),
    (46, 'しかし、ジョー本人は、こう語り続けた。', 'l', JOE + ' in casual clothes speaking calmly, warm light,' + ALONE),
    (46, 'サイモンがザイルを切らなければ、2人とも死んでいた。自分も、同じことをしただろう、と。', 'l', JOE + ' and ' + SIMON + ' shaking hands firmly in sunlight, friends.' + TWO),
    (46, '1988年、ジョーは、この体験を本にまとめた。', 's', 'a desk with a typewriter and a stack of manuscript pages, a climbing rope coiled beside it, no readable text, no people'),
    (46, 'その本は、世界中で読まれ、のちに映画にもなった。', 'l', 'people in a dark cinema watching a mountain on a big screen, silhouettes, no readable text'),
    (46, 'それは、あの日のサイモンの判断が正しかったことを伝える本でもあった。', 'l', JOE + ' and ' + SIMON + ', older, walking together on a mountain trail, talking.' + TWO),
    (46, '日本でも『死のクレバス』という題で出版され、映画は『運命を分けたザイル』として公開された。', 'l', 'a bookshelf with a mountaineering book and a film poster of a snowy peak, no readable text, no people'),
    (46, '映画には、ジョーとサイモン本人も出演し、あの日のことを語っている。', 'l', JOE + ' and ' + SIMON + ', older, sitting separately in quiet interview rooms, thoughtful. Exactly two people'),
    (46, 'サイモンも、その後、世界各地の山に登り続けた。', 'l', SIMON + ', older, climbing a snowy ridge in sunlight,' + ALONE),
    (46, '医者の予想を覆し、ジョーは、ふたたび山に登るようになった。', 'l', JOE + ' climbing a snowy mountain again in sunlight, older, smiling,' + ALONE),
    (46, 'クレバスの底で、彼は、上ではなく、下へ進むことを選んだ。', 'l', JOEI + ', inside ' + CREV + ', lowering himself toward a beam of light,' + ALONE),
    (46, '小さな目標を決めて、ひとつずつ、たどり着く。', 'l', JOEI + ', crawling toward a rock on the glacier, determined,' + ALONE),
    (46, '切られたザイルの先から、彼は、自分の力で、生きる道をつないだのである。', 'c', 'the cut end of a climbing rope on the snow, sunlight breaking through clouds over Siula Grande, hope, no people'),
    (46, 'このチャンネルでは、実際に起きた極限のサバイバルを記録している。', 's', 'a dark archive room with shelves of case files, one file open under a single desk lamp'),
    (46, '次の記録を見逃さないよう、チャンネル登録をお願いしたい。', 'x', 'the case file closing, the desk lamp switching off, darkness'),
]

# ---- パイプライン用の設定 ----
SCENE = "the 1985 Siula Grande mountaineering accident in the Peruvian Andes"
STYLE = ("Japanese gekiga manga illustration style (hand-drawn comic art, NOT photorealistic), bold black ink linework with cross-hatching, "
         "painted full colors, cold white and icy blue mountain tones, accurate 1985 mountaineering gear details, "
         "ONE single full-frame illustration showing one continuous scene (absolutely NO comic panels, "
         "NO split screen, NO inset frames, NO borders), dramatic high contrast cinematic lighting, serious documentary mood, "
         "not gory, no blood, no corpses shown, no speech bubbles, no text, no letters, no captions, no logos")
TTS_SPEED = 0.86
READINGS = {"雪庇": "せっぴ", "稜線": "りょうせん", "斧": "おの", "覆し": "くつがえし", "空耳": "そらみみ"}
STAMPS = {}
for _c, _t, _p, _i in LINES:
    for _k, _v in [("1985年6月。", "1985年6月"), ("3日目。ジョー", "クレバスから3日目"), ("1988年", "1988年")]:
        if _t.startswith(_k):
            STAMPS[_t] = _v
THUMB = {"image": 7, "big": "切られたザイル", "red": "生還", "top": "折れた足で、クレバスの底から", "sub": "標高6344m…3日間這って戻った男"}
SHORT = {"sel": [1, 2, 5, 6, 7, 8, 9],
         "stamp": {"1": "1985年6月"},
         "h1": "【実話】標高6344mの雪山", "h2": "仲間がザイルを切った", "e1": "落ちた男の運命は――", "e2": "▶ 続きは本編で\n画面下の「関連動画」から見られます",
         "title": "【実話】仲間がザイルを切った…クレバスに落ちた男は生きていた【1985年 シウラ・グランデ遭難】 #shorts",
         "desc": "1985年、ペルー・アンデスの雪山で、足を折った登山家と、彼をザイルで降ろす仲間。吹雪の夜、ザイルは切られた――。\n#実話 #雪山 #遭難 #登山 #サバイバル #shorts"}
META = {"title": "【実話】仲間にザイルを切られ、クレバスの底へ…折れた足で8キロを這って戻った男【1985年 シウラ・グランデ遭難】",
        "description": ("ジョー・シンプソン（1985年）の実話。ペルー・アンデス山脈の高峰シウラ・グランデ（6344m）で、"
                        "西壁の初登頂に成功した2人のイギリス人登山家。下山中に右足を骨折したジョーを、相棒のサイモン・イェーツはザイルで降ろし続けた。"
                        "吹雪の夜、宙づりになったジョーとともに引きずり落とされそうになったサイモンは、ザイルを切る。"
                        "クレバスに落ちたジョーが、折れた足で氷河と岩の谷を這い、ベースキャンプへ戻るまでを、約20分で記録する。\n\n"
                        "▼チャプター\n{CHAPTERS}\n\n"
                        "※映像はすべて実話をもとにした再現イラストです。実在の人物の外見とは異なります。\n"
                        "※出来事の詳細には諸説あります。本動画は当事者の証言・報道・資料をもとに構成しています。\n\n"
                        "▼前回：{PREV}\n\n"
                        "▼参考資料\n・Joe Simpson『Touching the Void』（1988年）／邦題『死のクレバス』\n"
                        "・ドキュメンタリー映画『運命を分けたザイル』（2003年）\n・各種報道・インタビュー\n\n"
                        "ナレーション：VOICEVOX:青山龍星\n\n"
                        "クライシス・ファイル〜極限サバイバル劇画〜\n実際に起きた極限のサバイバルを、劇画で記録するチャンネルです。\n"
                        "チャンネル登録：https://www.youtube.com/@CrisisFiles_Survival\n\n"
                        "#実話 #雪山 #遭難 #登山 #ジョーシンプソン #運命を分けたザイル #サバイバル #クライシスファイル"),
        "tags": ["ジョー・シンプソン", "サイモン・イェーツ", "シウラ・グランデ", "運命を分けたザイル", "死のクレバス", "クレバス",
                 "雪山", "遭難", "登山", "アンデス", "ペルー", "サバイバル", "実話", "生還", "クライシスファイル"]}
