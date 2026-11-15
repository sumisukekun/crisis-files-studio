# EP17: Aron Ralston / Bluejohn Canyon (2003), ~20 min. Entries: (cut, text, pause, prompt)
# 服装ルール（全カット共通）: アーロン＝色あせた青いTシャツ、ベージュの半ズボン、茶色の登山靴、黒い小さなリュック。
# 表現ルール: 腕の切断は直接描かない（血・傷口・切断面は一切描写しない）。右腕は岩に隠れている／事後は白い布で包んだ状態。
ARON = ("Aron, a 27-year-old American man with short brown hair and light stubble, "
        "wearing a faded BLUE T-shirt, BEIGE hiking shorts, brown hiking boots and a small BLACK backpack")
ARONF = "Aron, a 27-year-old American man with short brown hair and light stubble"
ARONT = ARON + (", his right hand and forearm completely hidden behind a huge boulder wedged in the narrow canyon "
                "(his right arm disappears behind the rock), exhausted, dusty")
ARONW = ARON + ", gaunt, sunburned and exhausted, his right arm ending in a thick bundle of white cloth held against his chest, no blood"
SLOT = "a very narrow red sandstone slot canyon in the Utah desert, walls only about one meter apart, light from a thin strip of sky above"
STONE = "a huge round brown chockstone boulder wedged between the narrow red sandstone walls of a slot canyon"
DESERT = "the vast red-rock desert of southeastern Utah near Canyonlands National Park, mesas and dry washes under a blue sky"
NIGHT = "the inside of a narrow sandstone slot canyon at night, cold blue moonlight, stars in a thin strip of sky"
ALONE = " He is completely alone, no other people"
NOP = ", no people"

CHAPTERS = [
    (1, "岩に挟まれた右腕"),
    (4, "ひとりの冒険者"),
    (7, "ブルージョン・キャニオン"),
    (10, "落ちてきた岩"),
    (13, "誰も知らない"),
    (16, "岩を削る"),
    (19, "滑車"),
    (22, "水が尽きる"),
    (25, "壁に刻んだ名前"),
    (28, "ビデオの別れ"),
    (31, "幻の少年"),
    (34, "決断"),
    (37, "20メートルの崖"),
    (40, "ヘリコプター"),
    (43, "なぜ生き延びたのか"),
    (45, "その後"),
]

LINES = [
    # ch1 岩に挟まれた右腕
    (1, '2003年4月。アメリカ、ユタ州の砂漠。', 's', DESERT + ', wide view, dramatic light' + NOP),
    (1, 'ブルージョン・キャニオンと呼ばれる、深く細い谷の底で、1人の男が、動けなくなっていた。', 'l', 'looking down from above into ' + SLOT + ', a tiny man far below,' + ALONE),
    (1, '男の名は、アーロン・ラルストン。27歳。', 'l', 'portrait of ' + ARON + ', confident face, red rock canyon behind,' + ALONE),
    (1, '彼の右腕は、落ちてきた巨大な岩に挟まれ、ぴくりとも動かなかった。', 'l', ARONT + ', pushing against the boulder with his left hand, shocked face,' + ALONE),
    (2, '岩の重さは、およそ360キロ。', 's', 'close-up of ' + STONE + ', heavy and immovable' + NOP),
    (2, '誰にも行き先を告げずに来た、たった1人の冒険だった。', 'l', ARONT + ', looking up at the thin strip of sky, realizing,' + ALONE),
    (2, '水は、わずか350ミリリットル。食べ物は、ブリトーが2つ。', 'l', 'a small plastic water bottle, two wrapped burritos and a cheap multi-tool on the sand floor of a slot canyon' + NOP),
    (2, '助けは来ない。自分で岩を動かすこともできない。', 'c', ARONT + ', head bowed against the canyon wall, despair,' + ALONE),
    (3, 'それから、127時間。', 's', 'a digital wristwatch on a dusty left wrist showing time, red sandstone background, no readable numbers'),
    (3, '5日以上にわたって、彼は、岩と向き合い続けた。', 'l', ARONT + ', in the slot canyon at dawn, staring at the boulder,' + ALONE),
    (3, 'そして6日目の朝。彼は、誰も想像しなかった方法で、岩から自由になった。', 'l', 'a beam of morning light falling into ' + SLOT + ', dust in the air, hope' + NOP),
    (3, '水も食べ物も尽き、体力も限界。誰が見ても、助かる見込みはなかった。', 'l', ARONT + ', gaunt and pale at night, headlamp glowing weakly,' + ALONE),
    (3, 'のちに映画『127時間』として世界中に知られることになる、実際の遭難事故の記録である。', 'c', STONE + ', a single beam of light on it, dramatic' + NOP),

    # ch2 ひとりの冒険者
    (4, 'アーロン・ラルストンは、1975年、アメリカのオハイオ州で生まれた。', 's', 'a 1980s American suburban house with a big tree, autumn' + NOP),
    (4, '子どものころに家族でコロラド州へ移り住み、ロッキー山脈の自然の中で育った。', 'l', 'a boy hiking with a backpack on a trail in the Colorado Rocky Mountains, pine forest, alone on the trail'),
    (4, '大学では機械工学を学び、卒業後は、エンジニアとして働いていた。', 'l', ARONF + ' in a white shirt working at a desk in a 1990s engineering office with a computer,' + ALONE),
    (4, 'しかし、彼の心は、いつも山にあった。', 'l', ARON + ' looking out of an office window at distant snowy mountains,' + ALONE),
    (4, '休みの日には、雪山に登り、谷を歩き、川を下った。', 'l', ARON + ' kayaking down a mountain river on a weekend,' + ALONE),
    (5, 'やがて彼は、会社をやめ、山の町アスペンに移り住んだ。', 's', 'the small mountain town of Aspen, Colorado, surrounded by snowy peaks' + NOP),
    (5, '登山店で働きながら、休みのたびに、山や谷へ出かけた。', 'l', ARON + ' working in an outdoor gear shop, holding climbing rope,' + ALONE),
    (5, '彼の目標は、コロラド州にある標高4200メートル級の山、59座すべてに、冬に、たった1人で登ることだった。', 'l', ARONF + ' in a winter jacket climbing a snowy Colorado peak alone, wind and snow,' + ALONE),
    (5, 'それは、まだ誰も成しとげたことのない挑戦だった。', 'l', 'a range of snowy 14,000-foot Colorado peaks at sunrise' + NOP),
    (6, 'アーロンは、1人で行動することを好んだ。', 's', ARON + ' hiking alone on a high ridge, small figure,' + ALONE),
    (5, '冬の雪山に1人で登るのは、危険と隣り合わせだ。雪崩に巻きこまれたこともあった。', 'l', 'a small avalanche sweeping down a snowy slope in the Colorado mountains, a tiny figure at the edge,' + ALONE),
    (5, 'それでも、アーロンは、挑戦をやめなかった。', 'l', ARON + ' tightening the straps of his backpack at the foot of a snowy mountain, determined,' + ALONE),
    (6, '体力にも、経験にも、自信があった。', 'l', ARON + ' standing on a summit with arms raised, confident,' + ALONE),
    (6, 'しかし、彼には1つ、悪いくせがあった。', 'l', 'close-up of ' + ARON + ' smiling, slightly reckless look,' + ALONE),
    (6, '出かけるとき、行き先を、誰にも伝えないことが多かったのだ。', 'c', 'a phone on a kitchen table next to car keys, nobody around, quiet morning' + NOP),

    # ch3 ブルージョン・キャニオン
    (7, '2003年4月25日、金曜日の夜。', 's', 'a pickup truck driving on a lonely desert highway in Utah at night, headlights' + NOP),
    (7, 'アーロンは、仕事を終えると、車でユタ州の砂漠へ向かった。', 'l', ARON + ' driving a pickup truck at night, one hand on the wheel,' + ALONE),
    (7, '目的地は、キャニオンランズ国立公園の近くにある、ブルージョン・キャニオン。', 'l', DESERT + ', deep canyons cutting through the rock, morning' + NOP),
    (7, '雨と風が、何万年もかけて岩を削ってできた、細い谷だった。', 'l', SLOT + ', beautiful curved walls, warm light' + NOP),
    (7, 'このあたりは、人の住む町から遠く離れ、携帯電話の電波も届かない場所だった。', 'l', DESERT + ', empty, no roads, no buildings' + NOP),
    (7, 'アーロンは、トラックの荷台で、ひと晩を過ごした。', 'l', 'a pickup truck parked alone in the desert at night under a sky full of stars' + NOP),
    (8, '翌朝、4月26日、土曜日。', 's', 'sunrise over the red desert of Utah, a pickup truck parked at a dirt trailhead' + NOP),
    (8, 'アーロンは、マウンテンバイクで、砂の道を、およそ24キロ走った。', 'l', ARON + ' riding a mountain bike on a sandy dirt road through the desert,' + ALONE),
    (8, '自転車を木につなぐと、そこから先は、歩いて谷を目指した。', 'l', ARON + ' locking a mountain bike to a juniper tree in the desert,' + ALONE),
    (8, '空は青く、風もおだやか。最高の天気だった。', 'l', ARON + ' walking across slickrock under a clear blue sky, smiling,' + ALONE),
    (9, 'ブルージョン・キャニオンの入り口は、地面にできた、細い割れ目のようだった。', 's', 'a narrow crack in the desert slickrock leading down into darkness, the entrance of a slot canyon' + NOP),
    (9, '中に入ると、両側の壁が、どんどん高くなっていく。', 'l', ARON + ' walking down into a deepening slot canyon, walls rising high on both sides,' + ALONE),
    (9, '谷の幅は、ところによって、人がやっと通れるほどしかない。', 'l', ARON + ' squeezing sideways through ' + SLOT + ',' + ALONE),
    (9, '日の光は、はるか上の、細い空のすき間からしか届かなかった。', 'l', 'looking up from the bottom of ' + SLOT + ', a thin bright strip of sky far above' + NOP),
    (9, 'アーロンは、この美しい谷を、心から楽しんでいた。', 'l', ARON + ' smiling, touching the smooth curved red wall of a slot canyon,' + ALONE),
    (9, '段差を飛び降り、岩をよじ登り、谷の奥へと進んでいった。', 'l', ARON + ' climbing down between boulders in ' + SLOT + ',' + ALONE),

    # ch4 落ちてきた岩
    (10, '午後3時ごろ。アーロンは、谷の中の、少し高い段差にさしかかった。', 's', ARON + ' facing a small drop in ' + SLOT + ', a boulder wedged between the walls ahead,' + ALONE),
    (10, '目の前には、両側の壁の間に、大きな岩がはさまっていた。', 'l', STONE + ', at chest height, a small drop below it' + NOP),
    (10, 'アーロンは、その岩に足をかけ、下へ降りようとした。', 'l', ARON + ' stepping onto the wedged boulder, climbing down,' + ALONE),
    (10, 'これまでにも、同じような岩は、何度も乗り越えてきた。何も心配はいらないはずだった。', 'l', 'close-up of ' + ARON + '\'s boot stepping onto a wedged boulder,' + ALONE),
    (10, 'そのときだった。岩が、ぐらりと動いた。', 'c', 'the huge boulder shifting and starting to roll inside the slot canyon, dust flying, motion blur' + NOP),
    (11, '岩は、アーロンといっしょに、下へ落ちてきた。', 's', ARON + ' falling down a short drop in the slot canyon as a huge boulder tumbles after him, dust,' + ALONE),
    (11, 'とっさに、彼は手を上げた。', 'l', ARON + ' raising his arms in shock as a boulder comes down, motion blur,' + ALONE),
    (11, '次の瞬間、岩は、彼の右手を、谷の壁に押しつけるようにして止まった。', 'l', ARONT + ', the boulder now jammed in place, dust settling,' + ALONE),
    (11, '右手と右腕は、岩と壁の間に、がっちりとはさまれてしまったのである。', 'l', ARONT + ', staring at the rock where his arm vanishes, frozen in shock,' + ALONE),
    (12, '激しい痛みが、全身を走った。', 's', 'close-up of ' + ARON + '\'s face screaming in pain, eyes shut,' + ALONE),
    (12, 'アーロンは、左手で岩を押した。', 'l', ARONT + ', pushing the boulder hard with his left hand,' + ALONE),
    (12, '体を引き、足をふんばり、何度も、何度も、引き抜こうとした。', 'l', ARONT + ', bracing his feet against the wall and pulling back with all his strength,' + ALONE),
    (12, 'しかし、360キロの岩は、びくともしなかった。', 'c', STONE + ', not moving at all, dust motes in the air' + NOP),
    (12, '360キロといえば、大人の男性5人分以上の重さである。', 'l', 'five large adult men standing in a row beside a huge boulder for size comparison, silhouettes'),

    # ch5 誰も知らない
    (13, 'アーロンは、深呼吸をして、自分に言い聞かせた。落ち着け。', 's', ARONT + ', eyes closed, taking a deep breath,' + ALONE),
    (13, 'まず、自分が持っているものを確かめた。', 'l', ARONT + ', emptying his small black backpack onto the sand with his left hand,' + ALONE),
    (13, '水が、350ミリリットル。ブリトーが2つ。', 'l', 'a small water bottle and two wrapped burritos on the sand in a slot canyon' + NOP),
    (13, 'ビデオカメラと、デジタルカメラ。ヘッドライトと、登山用のロープ。', 'l', 'a small 2003 camcorder, a compact digital camera, a headlamp and a coil of climbing rope laid out on sand' + NOP),
    (13, 'そして、懐中電灯のおまけについてきた、安物のマルチツール。刃の長さは、わずか5センチほどだった。', 'l', 'close-up of a cheap small folding multi-tool with a short dull blade on sand' + NOP),
    (14, 'アーロンは、考えた。誰かが、自分を探しに来てくれるだろうか。', 's', ARONT + ', looking up at the strip of sky, thinking,' + ALONE),
    (14, '答えは、すぐに出た。', 'l', 'close-up of ' + ARON + '\'s face, realization dawning,' + ALONE),
    (14, '行き先を、誰にも伝えていない。', 'l', 'an empty apartment in Aspen, Colorado, a calendar on the wall with nothing written on it, no readable text' + NOP),
    (14, '会社の同僚も、家族も、彼がユタ州の砂漠にいることを知らなかった。', 'l', 'a mother looking at a phone in a quiet Colorado kitchen, unaware, worried'),
    (14, 'しかも、ここは、ふだんほとんど人が通らない谷だった。', 'c', SLOT + ', empty and silent, long shadows' + NOP),
    (14, '大声で叫んでも、その声は、谷の壁に吸いこまれていった。', 'l', ARONT + ', shouting for help, voice echoing in the empty canyon,' + ALONE),
    (14, '返事は、どこからも返ってこなかった。', 'c', SLOT + ', silent, dust in a beam of light' + NOP),
    (15, '日が沈むと、谷の中は、急に冷えこんだ。', 's', NIGHT + ', ' + ARONT + ', shivering,' + ALONE),
    (15, '砂漠の夜は、昼と違って、驚くほど寒い。', 'l', ARONT + ', hugging himself with his left arm in the cold night,' + ALONE),
    (15, 'アーロンは、ロープを足に巻きつけ、少しでも体を温めようとした。', 'l', ARONT + ', wrapping climbing rope around his legs for warmth at night,' + ALONE),
    (15, '座ることも、横になることもできない。立ったまま、長い夜が過ぎていった。', 'l', ARONT + ', standing awake in the cold dark slot canyon, headlamp glowing,' + ALONE),
    (15, 'ヘッドライトの電池を節約するため、明かりは、ほとんど消したままだった。', 'l', NIGHT + ', total darkness except a faint glow,' + ALONE),
    (15, '真っ暗な谷の底で、聞こえるのは、自分の呼吸の音だけだった。', 'c', NIGHT + ', the faint outline of a man pinned by a boulder,' + ALONE),

    # ch6 岩を削る
    (16, '2日目。アーロンは、岩を削ることにした。', 's', ARONT + ', holding the small multi-tool in his left hand, determined,' + ALONE),
    (16, '小さなナイフで、岩を少しずつ削れば、腕を抜くすき間ができるかもしれない。', 'l', 'close-up of a small knife blade scraping the surface of a brown boulder, rock dust falling' + NOP),
    (16, '彼は、何時間も、何時間も、岩を削り続けた。', 'l', ARONT + ', chipping at the boulder with a small knife, sweating,' + ALONE),
    (16, 'しかし、削れたのは、ほんのわずか。岩は、ナイフよりも、はるかに硬かった。', 'l', 'a tiny pile of rock dust on the sand under the boulder' + NOP),
    (16, '岩をたたく、カツ、カツという音だけが、静かな谷に響き続けた。', 'l', ARONT + ', tapping the boulder with a small knife, dust in a beam of light,' + ALONE),
    (16, 'もし腕が抜けても、すぐに歩けるように、彼は、荷物をまとめておいた。', 'l', ARONT + ', packing gear neatly into his small black backpack with his left hand,' + ALONE),
    (17, 'それどころか、ナイフの刃が、どんどんすり減っていった。', 's', 'close-up of a dull, worn small knife blade in a dusty hand' + NOP),
    (17, '昼になると、細い空のすき間から、日の光が差しこんできた。', 'l', 'a narrow shaft of sunlight entering ' + SLOT + ', warm glow' + NOP),
    (17, '日の光が当たるのは、1日に、わずか15分ほど。', 'l', ARONT + ', turning his face up into a brief shaft of sunlight, eyes closed,' + ALONE),
    (17, 'そのわずかな時間を、アーロンは、何よりも楽しみにしていた。', 'l', 'close-up of ' + ARON + '\'s face in warm sunlight, a small smile,' + ALONE),
    (17, '日が当たらない時間、谷の底は、薄暗く、ひんやりとしていた。', 'l', SLOT + ', dim and cool, deep shadows' + NOP),
    (17, '空の青さと、日の光のありがたさを、彼は、このとき初めて知ったという。', 'c', 'looking up at a bright blue strip of sky between red canyon walls' + NOP),
    (18, '水は、少しずつ、少しずつ飲んだ。', 's', ARONT + ', taking a tiny sip from a small water bottle,' + ALONE),
    (18, '一度に飲んでしまえば、あとは何も残らない。', 'l', 'close-up of a water bottle with only a little water left in it' + NOP),
    (18, '彼は、エンジニアらしく、残りの量を計算し、飲む量を決めた。', 'l', ARONT + ', looking carefully at the water bottle, calculating,' + ALONE),
    (18, '持ってきたものを使い切ったとき、自分の命も尽きる。それが、わかっていた。', 'c', ARONT + ', staring at the water bottle in dim light, serious,' + ALONE),
    (18, 'もう1つの問題は、トイレだった。腕が抜けない以上、その場で済ませるしかない。', 'l', ARONT + ', looking away embarrassed in the dim canyon,' + ALONE),
    (18, '岩の前の、わずか1メートルほどの場所が、彼の世界のすべてになった。', 'l', 'top-down view of a tiny sandy space in front of a boulder in a narrow slot canyon, scattered gear' + NOP),

    # ch7 滑車
    (19, '3日目。アーロンは、別の方法を考えた。', 's', ARONT + ', looking up at the canyon walls above the boulder, thinking,' + ALONE),
    (19, '持ってきたロープを使って、岩を持ち上げる仕組みを作るのだ。', 'l', ARONT + ', uncoiling climbing rope with his left hand,' + ALONE),
    (19, '彼は、片手だけで、ロープを壁の上の岩に引っかけた。', 'l', ARONT + ', throwing a rope over a rock knob high on the canyon wall,' + ALONE),
    (19, 'そして、ロープを岩に巻きつけ、滑車のような仕組みを作った。', 'l', 'climbing rope rigged from the canyon wall around a wedged boulder like a simple pulley system' + NOP),
    (20, 'アーロンは、全身の力をこめて、ロープを引いた。', 's', ARONT + ', pulling the rope with his left hand and his whole body weight,' + ALONE),
    (20, 'ロープが、ぎしぎしと音を立てる。', 'l', 'close-up of a taut climbing rope straining around a rock edge' + NOP),
    (20, 'しかし、岩は、1ミリも動かなかった。', 'l', STONE + ', a rope wrapped around it, unmoved' + NOP),
    (20, '何度やっても、結果は同じだった。', 'c', ARONT + ', slumping against the wall, exhausted, rope slack,' + ALONE),
    (20, 'わずかに持ち上がったように見えても、手を離せば、岩はまた元の場所に戻ってしまう。', 'l', 'close-up of a rope slackening around a boulder that settles back into place' + NOP),
    (21, '夜になると、寒さと痛みで、ほとんど眠れなかった。', 's', NIGHT + ', ' + ARONT + ', eyes open, shivering,' + ALONE),
    (21, 'うとうとしては、寒さで目を覚ます。それを、ひと晩じゅう繰り返した。', 'l', ARONT + ', dozing standing up then jerking awake in the cold night,' + ALONE),
    (21, '頭の上を、ときどき、飛行機の音が通り過ぎていった。', 'l', 'a tiny airplane crossing the strip of night sky high above a slot canyon' + NOP),
    (21, 'しかし、谷の底にいる彼に、気づく人はいない。', 'l', 'looking down from the sky at the desert at night, a tiny dark crack of a canyon' + NOP),
    (21, 'アーロンは、自分の時計で、時間を確かめ続けた。', 'l', 'close-up of a digital wristwatch glowing on a dusty left wrist at night, no readable numbers' + NOP),
    (21, '時間の感覚を失わないこと。それが、正気を保つための方法だった。', 'c', ARONT + ', staring at his glowing watch in the dark,' + ALONE),
    (21, '朝が来るたびに、彼は、今日が何日目なのかを、声に出して確かめた。', 'l', ARONT + ', whispering to himself at dawn, counting on his fingers,' + ALONE),

    # ch8 水が尽きる
    (22, '4日目。', 's', ARONT + ', at dawn, gaunt and pale,' + ALONE),
    (22, 'アーロンは、はさまれた腕を、どうにかしなければならないと考え始めた。', 'l', ARONT + ', staring at the boulder with a grim face,' + ALONE),
    (22, '腕を岩から引き離す。それしか、生きて出る方法はないのかもしれない。', 'l', 'close-up of ' + ARON + '\'s eyes, a terrible thought forming,' + ALONE),
    (22, '彼は、腕のつけ根を、ひもできつく縛ってみた。', 'l', ARONT + ', tying a thin tube tightly around his upper right arm with his left hand and teeth,' + ALONE),
    (22, 'しかし、手元にある小さなナイフでは、骨までは、とても切れない。', 'c', 'close-up of the small dull multi-tool lying on a rock' + NOP),
    (23, 'その日、水が、とうとう尽きた。', 's', 'close-up of an empty plastic water bottle lying on the sand' + NOP),
    (23, '最後の一口を飲み終えたとき、アーロンは、しばらく空のボトルを見つめていた。', 'l', ARONT + ', holding an empty water bottle, staring at it,' + ALONE),
    (23, 'ブリトーも、もう残っていない。', 'l', 'an empty crumpled food wrapper on the sand' + NOP),
    (23, 'のどの渇きは、痛みよりも、つらかったという。', 'l', 'close-up of ' + ARON + '\'s cracked dry lips,' + ALONE),
    (23, '口の中は乾ききり、舌が、上あごにはりつくほどだった。', 'l', 'close-up of ' + ARON + '\'s parched mouth and cracked lips,' + ALONE),
    (23, 'アーロンは、空のボトルを見つめながら、冷たい水を飲む夢を、何度も見た。', 'l', 'a dreamlike vision of cold clear water pouring into a glass, soft light' + NOP),
    (24, '体から、水分が、どんどん失われていく。', 's', ARONT + ', sweating in the afternoon heat, dazed,' + ALONE),
    (24, '人は、水を飲まずに生きられるのは、わずか数日と言われている。', 'l', 'a desert sun blazing above a narrow slot canyon, heat haze' + NOP),
    (24, 'アーロンは、生きのびるために、自分の尿を飲んだ。', 'l', ARONT + ', holding a bottle with yellowish liquid, grimacing,' + ALONE),
    (24, 'それほどまでに、彼は追いつめられていたのである。', 'c', ARONT + ', head against the wall, eyes closed, exhausted,' + ALONE),
    (24, '体が水を失うと、血液はどろどろになり、頭は、ぼんやりしてくる。', 'l', 'close-up of ' + ARON + '\'s unfocused eyes, heat shimmer,' + ALONE),
    (24, 'アーロンの意識も、少しずつ、はっきりしなくなっていった。', 'l', ARONT + ', swaying, eyes half closed, dazed,' + ALONE),

    # ch9 壁に刻んだ名前
    (25, '5日目。', 's', ARONT + ', at dawn, very weak, sunken eyes,' + ALONE),
    (25, 'アーロンは、自分が、ここで死ぬのだと思った。', 'l', 'close-up of ' + ARON + '\'s gaunt face, quiet acceptance,' + ALONE),
    (25, '彼は、ナイフを手に取ると、目の前の岩の壁に、文字を刻み始めた。', 'l', ARONT + ', carving into the red sandstone wall with a small knife,' + ALONE),
    (25, '自分の名前。生まれた年と月。', 'l', 'close-up of a small knife carving letters into red sandstone, the letters blurred and unreadable' + NOP),
    (25, 'そして、「2003年4月」。自分が死ぬであろう日付だった。', 'c', 'carved letters on a red sandstone wall lit by a headlamp, blurred and unreadable' + NOP),
    (26, 'いつか、誰かがここで自分を見つけたとき、それが誰なのか、わかるように。', 's', ARONT + ', looking at the carving on the wall, calm and sad,' + ALONE),
    (26, '刻み終えると、アーロンは、壁にもたれて、目を閉じた。', 'l', ARONT + ', leaning against the canyon wall with eyes closed,' + ALONE),
    (26, '谷の中は、しんと静まり返っていた。', 'l', SLOT + ', silent, dust in a beam of light' + NOP),
    (26, 'そのとき彼が考えていたのは、家族や、友人たちの顔だった。', 'c', 'a warm memory of a family dinner table in Colorado, soft blurry light, faces indistinct'),
    (27, '一方そのころ、アーロンの勤め先の登山店では、同僚たちが首をかしげていた。', 's', 'two coworkers talking worriedly behind the counter of an outdoor gear shop in Aspen'),
    (27, '月曜日になっても、アーロンが出勤してこない。', 'l', 'an empty spot behind a shop counter, a work apron hanging unused' + NOP),
    (27, '連絡もつかない。同僚たちは、彼の母親に知らせた。', 'l', 'a woman on the phone in a Colorado kitchen, worried'),
    (27, '母親は、すぐに警察に届け出た。しかし、どこを探せばいいのか、誰にもわからなかった。', 'c', 'police officers looking at a large map of the western United States spread on a table, no readable text'),
    (27, '母親は、息子のメールを調べ、ユタ州の地名を手がかりに見つけ出した。', 'l', 'a worried mother looking at an old desktop computer screen at night, screen text blurred and unreadable'),
    (27, 'こうして、捜索の目は、少しずつ、ユタ州の砂漠へと向けられていった。', 'c', 'a map of Utah with red canyons, a hand pointing at the desert, no readable text'),

    # ch10 ビデオの別れ
    (28, 'アーロンは、ビデオカメラを取り出した。', 's', ARONT + ', holding a small 2003 camcorder with his left hand,' + ALONE),
    (28, 'そして、レンズを自分に向けて、話し始めた。', 'l', ARONT + ', pointing a camcorder at his own face, red recording light,' + ALONE),
    (28, '父へ。母へ。妹へ。', 'l', 'close-up of ' + ARON + '\'s face lit by the small camcorder screen glow, speaking softly,' + ALONE),
    (28, '家族ひとりひとりに向けて、感謝と、別れの言葉を、静かに残していった。', 'l', ARONT + ', speaking to a camcorder, tears in his eyes,' + ALONE),
    (28, 'その声は、かすれ、ときどき、言葉がとぎれた。', 'l', 'close-up of ' + ARON + '\'s dry lips speaking, dim light,' + ALONE),
    (29, '行き先を伝えなかったことを、彼は、何度も謝った。', 's', 'close-up of ' + ARON + '\'s eyes looking into a camera lens, regret,' + ALONE),
    (29, '自分の荷物を、誰に渡してほしいかも、話した。', 'l', ARONT + ', speaking to a camcorder in dim light,' + ALONE),
    (29, 'それは、残される人たちへの、最後の手紙のようなものだった。', 'l', 'a small camcorder resting on a rock ledge in a slot canyon, red light on' + NOP),
    (29, '録画を止めると、アーロンは、深いため息をついた。', 'c', ARONT + ', lowering the camcorder, exhaling, eyes closed,' + ALONE),
    (30, 'その夜は、これまでで、いちばん寒い夜だった。', 's', NIGHT + ', ' + ARONT + ', shivering violently,' + ALONE),
    (30, '意識が、少しずつ、遠のいていく。', 'l', ARONT + ', eyes half closed in the dark, blurry vision effect,' + ALONE),
    (30, 'アーロンは、もう朝は来ないかもしれないと思った。', 'l', 'stars in a thin strip of night sky above a canyon, very cold' + NOP),
    (30, 'それでも彼は、夜明けまで、時計の数字を見つめ続けた。', 'c', 'close-up of a glowing digital watch in total darkness, no readable numbers' + NOP),
    (30, '寒さで、体の震えが止まらない。歯が、ガチガチと鳴り続けた。', 'l', ARONT + ', teeth chattering, shaking with cold in the dark,' + ALONE),

    # ch11 幻の少年
    (31, 'そのとき、アーロンは、ある光景を見た。', 's', ARONT + ', eyes opening wide in the dark, a soft glow on his face,' + ALONE),
    (31, '小さな男の子が、こちらに向かって、走ってくる。', 'l', 'a dreamlike soft-focus vision of a small blond boy running across a sunny living room toward the viewer, glowing'),
    (31, 'アーロンは、その子を、片腕で抱き上げていた。', 'l', 'a dreamlike soft-focus vision of a man lifting a laughing little boy, warm golden light, faces soft, no injuries shown'),
    (31, 'その子は、まだ会ったことのない、自分の息子だと、彼は感じた。', 'l', 'a dreamlike glowing vision of a little boy smiling, soft light, warm colors'),
    (32, 'それは、幻だった。', 's', NIGHT + ', ' + ARONT + ', staring into darkness,' + ALONE),
    (32, 'しかし、アーロンの心の中で、何かが変わった。', 'l', 'close-up of ' + ARON + '\'s face, a new spark in his eyes,' + ALONE),
    (32, '自分には、まだ、生きる理由がある。', 'l', ARONT + ', clenching his left fist, determined,' + ALONE),
    (32, 'いつか、この子に会うために、生きて帰らなければならない。', 'l', 'a dreamlike soft vision of a small boy waving in warm golden light'),
    (32, 'ここで死ぬわけには、いかない。', 'c', ARONT + ', looking up at the first light of dawn above the canyon,' + ALONE),
    (33, '6日目の朝が来た。', 's', 'pale dawn light spreading into ' + SLOT + NOP),
    (33, 'はさまれた右手は、もう、まったく感覚がなかった。', 'l', ARONT + ', looking down at the boulder, grim,' + ALONE),
    (33, '何日も血が通わず、手は、すでに死んでいたのである。', 'l', 'close-up of ' + STONE + ' in cold dawn light' + NOP),
    (33, 'このままでは、毒が体中に回り、命にかかわる。', 'c', 'close-up of ' + ARON + '\'s pale sweating face,' + ALONE),
    (33, 'もう、迷っている時間はなかった。', 'c', ARONT + ', breathing hard, staring at the boulder,' + ALONE),

    # ch12 決断
    (34, 'アーロンは、怒りにまかせて、腕を思いきり引っ張った。', 's', ARONT + ', yanking his body back in fury,' + ALONE),
    (34, 'そのとき、彼は、あることに気づいた。', 'l', 'close-up of ' + ARON + '\'s face, sudden realization,' + ALONE),
    (34, '岩に固定された腕に、体の重みをかけて、てこのように力を加えれば、骨を折ることができる。', 'l', 'a simple diagram-like illustration of a lever and a fulcrum drawn in sand' + NOP),
    (34, 'ナイフで切れないなら、骨を折ればいい。', 'c', ARONT + ', bracing his body against the boulder, decision made,' + ALONE),
    (35, 'アーロンは、体を岩に押しつけ、全身の力をこめた。', 's', ARONT + ', throwing his body weight sideways against the boulder, teeth clenched,' + ALONE),
    (35, '鈍い音が、谷に響いた。', 'l', 'the narrow slot canyon walls, a cloud of dust trembling in a beam of light' + NOP),
    (35, 'そして、彼は、あの小さなナイフを手に取った。', 'l', 'close-up of a left hand gripping the small dull multi-tool, trembling' + NOP),
    (35, '飲み水用のチューブで、腕のつけ根をきつく縛り、血が出すぎないようにした。', 'l', ARONT + ', tightening a thin tube around his upper right arm with his teeth,' + ALONE),
    (36, 'それから、およそ1時間。', 's', 'a beam of morning light slowly moving across the red sandstone wall' + NOP),
    (36, '刃の短い、切れ味の悪いナイフで、彼は、自分の腕を、岩から切り離した。', 'l', 'close-up of ' + ARON + '\'s face, eyes squeezed shut, sweat pouring, enduring, only his face visible,' + ALONE),
    (36, '想像を絶する痛みだった。それでも、彼は、手を止めなかった。', 'l', 'close-up of ' + ARON + '\'s clenched jaw and tears, extreme determination, only his face,' + ALONE),
    (36, 'いちばん太い血管は、最後に残した。血を失いすぎないための、ぎりぎりの判断だった。', 'l', 'close-up of ' + ARON + '\'s face, intense concentration, sweat dripping, only his face,' + ALONE),
    (36, '2003年5月1日、木曜日の朝。アーロンは、ついに、岩から自由になった。', 'c', ARONW + ', stepping back from the boulder in the slot canyon, swaying,' + ALONE),

    # ch13 20メートルの崖
    (37, 'しかし、まだ、助かったわけではなかった。', 's', ARONW + ', standing in the slot canyon, breathing hard,' + ALONE),
    (37, '車までは、およそ13キロ。', 'l', DESERT + ', a long way, heat haze' + NOP),
    (37, 'しかも、谷を出るには、高さ20メートルの崖を、ロープで降りなければならなかった。', 'l', 'a sheer 20-meter red sandstone cliff drop at the end of a slot canyon' + NOP),
    (37, '片手で、しかも、大けがをした体で。', 'c', ARONW + ', looking down over the edge of a sheer cliff,' + ALONE),
    (37, 'アーロンは、谷の壁に刻んだ文字を、最後にもう一度見つめた。', 'l', ARONW + ', looking back at carved letters on the sandstone wall, blurred and unreadable,' + ALONE),
    (37, 'そして、背を向けて、歩き出した。', 'c', ARONW + ', walking away from the boulder down the slot canyon, back view,' + ALONE),
    (38, 'アーロンは、ロープを岩に固定すると、左手1本で、ゆっくりと崖を降り始めた。', 's', ARONW + ', rappelling down a sheer red cliff with one hand on the rope,' + ALONE),
    (38, '手がすべれば、まっさかさまに落ちる。', 'l', 'close-up of a single dusty left hand gripping a climbing rope tightly' + NOP),
    (38, '1メートル、また1メートル。', 'l', ARONW + ', halfway down a tall sandstone cliff on a rope, small figure,' + ALONE),
    (38, 'ついに、彼の足が、崖の下の地面に着いた。', 'c', ARONW + ', landing at the bottom of the cliff, knees buckling,' + ALONE),
    (38, 'ここまで、ロープとハーネスを持ってきていたことが、彼の命を救った。', 'l', 'close-up of a climbing harness and a rope through a belay device on a sandstone cliff' + NOP),
    (39, '崖の下には、雨水がたまった、小さな水たまりがあった。', 's', 'a small muddy rainwater pool at the bottom of a desert canyon' + NOP),
    (39, 'アーロンは、むさぼるように水を飲んだ。', 'l', ARONW + ', kneeling and drinking from a muddy pool,' + ALONE),
    (39, 'そして、焼けつくような日差しの中を、歩き始めた。', 'l', ARONW + ', walking along a wide sandy canyon floor under a scorching sun,' + ALONE),
    (39, '体は、すでに、多くの血を失っていた。一歩ごとに、足元がふらついた。', 'l', ARONW + ', staggering in the desert heat, blurry vision,' + ALONE),
    (39, '照りつける太陽の下、気温は、30度近くまで上がっていた。', 'l', 'a blazing sun over a red desert canyon, heat haze' + NOP),
    (39, 'それでも、アーロンは、止まらなかった。止まれば、2度と立ち上がれない気がした。', 'c', ARONW + ', staggering forward along a sandy canyon floor,' + ALONE),

    # ch14 ヘリコプター
    (40, '歩き始めて、数時間後。', 's', ARONW + ', walking in a wide red canyon, tiny figure,' + ALONE),
    (40, 'アーロンの目の前に、人影が見えた。', 'l', 'three distant hikers in a wide sandy canyon seen through heat haze'),
    (40, 'オランダから旅行に来ていた、3人の家族だった。', 'l', 'a Dutch family of three tourists (a father, a mother and a teenage son) hiking in a Utah canyon with backpacks and sun hats'),
    (40, 'アーロンは、声をふりしぼった。「助けてください。」', 'c', ARONW + ', calling out with a hoarse voice, raising his left hand, the family visible in the distance'),
    (40, '家族は、思わず立ち止まった。目の前に現れた男の姿に、言葉を失った。', 'l', 'a Dutch family of three tourists stopping in shock in a sandy canyon, wide eyes'),
    (40, 'アーロンは、落ち着いた声で、自分に何が起きたのかを説明したという。', 'c', ARONW + ', speaking calmly to a Dutch tourist father in a canyon'),
    (41, '家族は、アーロンに、水とクッキーを分けてくれた。', 's', 'a Dutch tourist father handing a water bottle to ' + ARONW + ' in a desert canyon, the mother and son nearby'),
    (41, 'そして、助けを呼ぶため、母親と息子が、先へと急いだ。', 'l', 'a woman and a teenage boy running ahead along a sandy canyon trail'),
    (41, 'そのころ、警察は、アーロンの車を手がかりに、ようやく捜索の範囲をしぼりこんでいた。', 'l', 'a police officer looking at an empty pickup truck parked at a remote desert trailhead'),
    (41, '空には、捜索のヘリコプターが飛んでいた。', 'l', 'a rescue helicopter flying low over the red canyons of Utah' + NOP),
    (41, 'アーロンと父親の2人は、ゆっくりと、谷の出口に向かって歩き続けた。', 'l', ARONW + ' walking slowly with a Dutch tourist father beside him in a wide canyon, helping him'),
    (42, 'ヘリコプターは、谷の広い場所に、2人の姿を見つけた。', 's', 'a helicopter hovering above a wide sandy canyon, two tiny figures (two men) waving below'),
    (42, 'ヘリが着陸すると、アーロンは、自分の足で歩いて、乗りこんだという。', 'l', ARONW + ', walking toward a landed helicopter in a cloud of dust, rotor spinning,' + ALONE),
    (42, 'ヘリコプターの中で、アーロンは、救助隊員に、自分の状態を落ち着いて説明したという。', 'l', ARONW + ', sitting inside a helicopter, talking calmly to a rescuer in uniform'),
    (42, '腕を切り離してから、およそ4時間後のことだった。', 'l', 'a rescue helicopter lifting off from a desert canyon, dust swirling' + NOP),
    (42, 'あの日、谷に入ってから、127時間が過ぎていた。', 'c', 'a helicopter flying away over the vast red desert at midday, small and distant' + NOP),

    # ch15 なぜ生き延びたのか
    (43, 'アーロンは、なぜ、生き延びることができたのか。', 's', 'a beam of light falling on ' + STONE + ', now empty, silent' + NOP),
    (43, '1つ目は、パニックにならず、自分の持ち物と、水の量を、冷静に計算したこと。', 'l', 'a water bottle, burritos and a multi-tool laid out neatly on sand, top view' + NOP),
    (43, '2つ目は、岩を削る、滑車を作る。思いつく方法を、ひとつずつ、あきらめずに試したこと。', 'l', 'climbing rope rigged around a boulder in a slot canyon, a small knife beside it' + NOP),
    (43, 'そして3つ目は、生きる理由を、最後まで見失わなかったことである。', 'l', 'a dreamlike soft vision of a small boy running in warm light'),
    (43, '彼は、のちに、こう語っている。あの岩は、自分を罰するために落ちてきたのではない。自分を変えるために、そこにあったのだと。', 'l', ARON + ', older, sitting calmly on a red rock in the desert at sunset,' + ALONE),
    (44, 'ただし、彼自身が、何度も語っている教訓がある。', 's', ARONF + ', older, speaking calmly in a bright room, his right arm in a long sleeve,' + ALONE),
    (44, 'それは、どこへ行くのか、必ず誰かに伝えておくこと。', 'l', 'a handwritten note on a kitchen table next to car keys, the writing blurred and unreadable' + NOP),
    (44, 'もし、行き先を伝えていれば、彼は、もっと早く見つけてもらえたかもしれない。', 'l', 'a search helicopter flying above canyons at dawn' + NOP),
    (44, 'たった一言の連絡が、命を救うこともあるのだ。', 'c', 'a phone glowing on a table with a short message being typed, text blurred and unreadable' + NOP),
    (44, 'そして、どんな状況でも、最後まで、生きる道を探し続けることだと。', 'l', ARONF + ', older, smiling gently in a bright room,' + ALONE),

    # ch16 その後
    (45, 'アーロンは、体重が18キロも減り、体の血液のおよそ4分の1を失っていた。', 's', ARONF + ', gaunt and pale, in a hospital gown, his right arm bandaged in white under the blanket, no blood, lying in a hospital bed, pale, eyes open,' + ALONE),
    (45, 'しかし、命は助かった。', 'l', ARONF + ', in a hospital bed, his mother holding his left hand, tears, soft light'),
    (45, '医師たちは、彼が生きていたこと自体が、奇跡だと驚いた。', 'l', 'doctors in a hospital corridor talking in surprise'),
    (45, 'その後、国立公園の職員たちが、岩の下から、彼の腕を取り出した。', 's', 'park rangers with ropes and a hydraulic jack working around a boulder in a slot canyon, no body parts visible'),
    (45, '岩を動かすのに、13人がかりで、機械を使っても、大変な作業だったという。', 'l', 'many rangers straining together with a winch to move a huge boulder in a slot canyon'),
    (45, '半年後、28歳の誕生日に、アーロンは、あの場所を再び訪れた。', 'l', ARONF + ', six months later, in a jacket, standing quietly before the boulder in the slot canyon, his right sleeve empty,' + ALONE),
    (46, '2004年、アーロンは、この体験を本にまとめた。', 's', 'a desk with a laptop and stacks of manuscript pages, a climbing rope coiled beside it, no readable text' + NOP),
    (46, '日本でも『奇跡の6日間』という題で出版され、2010年には、映画『127時間』として公開された。', 'l', 'people in a dark cinema watching a red desert canyon on a big screen, silhouettes, no readable text'),
    (46, '映画は、アカデミー賞の6部門にノミネートされ、世界中で話題になった。', 'l', 'a golden film award statuette silhouette on a dark stage with spotlights, no readable text' + NOP),
    (46, 'アーロンは、義手をつけて、ふたたび山に登り始めた。', 'l', ARONF + ', wearing a prosthetic right arm with an ice axe attachment, climbing a snowy Colorado peak,' + ALONE),
    (46, '講演会では、世界中の人々に、あの6日間の体験を語り続けている。', 'l', ARONF + ', older, speaking on a stage to a large audience, warm stage light, no readable text'),
    (46, '自分の失敗も、迷いも、すべて隠さずに話すその姿は、多くの人の心を動かした。', 'l', 'an audience listening intently in a dark hall, silhouettes, warm light'),
    (46, 'そして2005年、彼は、あの目標を達成した。', 'l', ARONF + ', with a prosthetic arm, standing on a snowy summit in winter, arms raised,' + ALONE),
    (46, 'コロラド州の59座すべてに、冬に、たった1人で登ったのである。それは、世界で初めての記録だった。', 'l', 'a panorama of snowy Colorado 14,000-foot peaks at sunrise' + NOP),
    (46, '2010年。アーロンに、男の子が生まれた。', 's', ARONF + ', holding a newborn baby in his left arm, smiling, soft warm light, his right arm out of frame'),
    (46, 'あの日、谷の底で見た幻の少年は、本当に、彼のもとへやって来たのである。', 'l', ARONF + ' playing with a small blond boy in a sunny park, lifting him up, laughing'),
    (46, 'すべてを失いかけた谷の底で、彼は、生きるための、たった1つの道を、自分の手で切り開いた。', 'c', 'sunlight pouring into an empty narrow red slot canyon, hope' + NOP),
    (46, 'このチャンネルでは、実際に起きた極限のサバイバルを記録している。', 's', 'a dark archive room with shelves of case files, one file open under a single desk lamp'),
    (46, '次の記録を見逃さないよう、チャンネル登録をお願いしたい。', 'x', 'the case file closing, the desk lamp switching off, darkness'),
]

# ---- パイプライン用の設定 ----
SCENE = "the 2003 Bluejohn Canyon accident of Aron Ralston in the Utah desert"
STYLE = ("Japanese gekiga manga illustration style (hand-drawn comic art, NOT photorealistic), bold black ink linework with cross-hatching, "
         "painted full colors, warm red and orange sandstone desert tones with deep shadows, accurate early-2000s outdoor gear details, "
         "ONE single full-frame illustration showing one continuous scene (absolutely NO comic panels, "
         "NO split screen, NO inset frames, NO borders), dramatic high contrast cinematic lighting, serious documentary mood, "
         "not gory, no blood, no wounds, no injuries shown, no body parts, no corpses, no speech bubbles, no text, no letters, no captions, no logos")
TTS_SPEED = 0.95
TTS_SPEAKER = 11  # 玄野武宏（ノーマル）— 11/15 ユーザー指定(B)。以後の回もこれ
TTS_INTONATION = 1.1
READINGS = {"尿": "にょう", "鈍い": "にぶい", "義手": "ぎしゅ", "幻": "まぼろし", "一口": "ひとくち"}
STAMPS = {}
for _c, _t, _p, _i in LINES:
    for _k, _v in [("2003年4月。", "2003年4月"), ("2003年4月25日", "4月25日（金）"), ("翌朝、4月26日", "4月26日（土）"),
                   ("2日目。", "2日目"), ("3日目。", "3日目"), ("4日目。", "4日目"), ("5日目。", "5日目"),
                   ("6日目の朝", "6日目"), ("2003年5月1日", "5月1日（木）")]:
        if _t.startswith(_k):
            STAMPS[_t] = _v
THUMB = {"image": 4, "big": "127時間", "red": "生還", "top": "岩に右腕を挟まれ、谷の底で", "sub": "水350ml…6日目に彼が選んだ方法"}
SHORT = {"sel": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
         "stamp": {"1": "2003年4月"},
         "h1": "【実話】岩に挟まれた127時間", "h2": "誰も助けに来ない谷の底", "e1": "6日目、彼が選んだのは――", "e2": "▶ 続きは本編で\n画面下の「関連動画」から見られます",
         "title": "【実話】360キロの岩に右腕を挟まれ…誰も助けに来ない谷の底で127時間【2003年 ブルージョン・キャニオン事故】 #shorts",
         "desc": "2003年、アメリカ・ユタ州の細い谷。落ちてきた岩に右腕を挟まれた男。行き先は誰にも告げていなかった――。\n#実話 #127時間 #遭難 #サバイバル #アーロンラルストン #shorts"}
META = {"title": "【実話】岩に右腕を挟まれ127時間…水も尽きた谷の底から、自力で生還した男【2003年 ブルージョン・キャニオン事故】",
        "description": ("アーロン・ラルストン（2003年）の実話。アメリカ・ユタ州の砂漠にある細い谷、ブルージョン・キャニオン。"
                        "1人で谷を下っていた27歳の登山家の右腕を、落ちてきた約360キロの岩がはさんだ。行き先は誰にも伝えていない。"
                        "水350ミリリットルとブリトー2つ、安物のマルチツール。127時間後、6日目の朝に彼が選んだ方法とは――。"
                        "映画『127時間』のもとになった遭難事故を、約20分で記録する。\n\n"
                        "▼チャプター\n{CHAPTERS}\n\n"
                        "※映像はすべて実話をもとにした再現イラストです。実在の人物の外見とは異なります。\n"
                        "※出来事の詳細には諸説あります。本動画は当事者の証言・報道・資料をもとに構成しています。\n\n"
                        "▼前回：{PREV}\n\n"
                        "▼参考資料\n・Aron Ralston『Between a Rock and a Hard Place』（2004年）／邦題『奇跡の6日間』\n"
                        "・映画『127時間』（2010年）\n・各種報道・インタビュー\n\n"
                        "ナレーション：VOICEVOX:玄野武宏\n\n"
                        "クライシス・ファイル〜極限サバイバル劇画〜\n実際に起きた極限のサバイバルを、劇画で記録するチャンネルです。\n"
                        "チャンネル登録：https://www.youtube.com/@CrisisFiles_Survival\n\n"
                        "#実話 #127時間 #遭難 #サバイバル #アーロンラルストン #ブルージョンキャニオン #クライシスファイル"),
        "tags": ["アーロン・ラルストン", "127時間", "ブルージョン・キャニオン", "奇跡の6日間", "ユタ州", "キャニオンランズ",
                 "岩に挟まれた", "腕", "遭難", "サバイバル", "実話", "生還", "クライシスファイル"]}
