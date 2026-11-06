# EP14: Shackleton / Endurance (1914-1916), ~21 min. Entries: (cut, text, pause, prompt)
SHACK = "a broad-shouldered British explorer in his forties with a strong jaw, short dark hair and intense eyes, wearing a 1915 wool sweater and heavy coat"
WORS = "a wiry New Zealand ship captain in his forties with a weathered face and sharp eyes, wearing a 1915 sea coat and cap"
CREAN = "a big strong Irish sailor in his late thirties with a broad friendly face, wearing a 1915 wool sweater and knitted cap"
WILD = "a calm small British explorer in his forties with a balding head and a steady gaze, wearing a 1915 heavy coat"
MEN = "bearded British polar explorers of 1915 in heavy wool clothing, knitted caps and fur mittens"
SHIP = "a three-masted wooden barquentine sailing ship of 1914 with black hull"
ICE = "a vast frozen white sea of pack ice under a low grey sky in Antarctica, endless"
CAMP = "a small camp of canvas tents and three wooden lifeboats on a flat ice floe in the frozen Weddell Sea"
BOAT = "a small open wooden lifeboat of 1916 with a makeshift canvas deck and a small sail"
ELEPH = "a barren rocky beach under black cliffs and glaciers on Elephant Island, Antarctica, stormy"

CHAPTERS = [
    (1, "氷の墓場"),
    (4, "南極横断の夢"),
    (7, "閉じ込められた船"),
    (10, "氷の上の冬"),
    (13, "船の最期"),
    (16, "氷上キャンプ"),
    (19, "三隻のボート"),
    (23, "エレファント島"),
    (26, "1300キロの海"),
    (30, "サウスジョージア"),
    (34, "山を越える"),
    (38, "仲間を迎えに"),
    (42, "その後"),
]

LINES = [
    # ch1 氷の墓場
    (1, '1915年11月。南極の海は、見渡すかぎり、真っ白な氷に覆われていた。', 's', ICE + ', silent, cold wind, no life'),
    (1, 'その氷の上に、28人の男たちが立っていた。', 'l', MEN + ' standing in a line on the pack ice, tiny against the vast white, silent'),
    (1, '彼らの目の前で、1隻の船が、ゆっくりと氷の下へ沈んでいった。', 'l', SHIP + ' crushed by ice, tilting, sinking slowly into a crack in the pack ice, dramatic'),
    (1, 'それは、彼らが乗ってきた、たった1つの帰りの手段だった。', 'l', 'the tip of a wooden mast disappearing into dark water between ice floes, solemn'),
    (1, '男たちの隊長は、静かにこう言った。船は、もうない。これから、家に帰る。', 'c', 'close-up of ' + SHACK + ' speaking calmly to his men on the ice, determined'),
    (2, '一番近い人のいる場所までは、およそ1000キロ以上。', 's', 'an illustrated old map of the Antarctic Peninsula and the Weddell Sea with a tiny marker in the ice, no readable text'),
    (2, '無線もない。助けを呼ぶ方法も、何1つなかった。', 'l', 'a pile of supplies, sledges and wooden crates on the ice, no radio, desolate'),
    (2, '冬になれば、気温はマイナス30度を下回る。', 'l', MEN + ' huddled in a blizzard on the ice, snow blowing sideways, freezing'),
    (2, 'それでも、この隊長は、1人も死なせないと決めていた。', 'c', SHACK + ' standing alone on a ridge of ice looking at the horizon, resolve'),
    (3, 'シャクルトン率いる、エンデュアランス号の探検隊。', 's', SHIP + ' sailing through icy seas in 1914, sails full, dramatic sky'),
    (3, '南極の氷に閉じ込められた28人は、およそ2年もの間、極寒の世界で生き続けた。', 'l', MEN + ' pulling a heavy wooden lifeboat across rough ice, exhausted, determined'),
    (3, '彼らは、どうやって生き延びたのか。', 'l', 'a tiny open lifeboat climbing a huge grey wave in the Southern Ocean, dramatic'),
    (3, '人類の探検の歴史で、最も壮絶な脱出劇の記録である。', 'c', 'a dark archive desk with a case file and an old photograph of a sailing ship in ice clipped to it, single desk lamp, no readable text'),
    # ch2 南極横断の夢
    (4, '20世紀のはじめ。世界の探検家たちは、地球の果てを目指して競い合っていた。', 's', 'explorers of the early 1900s in fur clothing standing beside sledges and dogs in polar snow, heroic'),
    (4, '1911年、ノルウェーのアムンセンが、人類で初めて、南極点にたどり着いた。', 'l', 'a small tent with a flag on a vast flat snowy plateau under a pale sky, 1911, no readable text'),
    (4, 'その後、イギリスのスコットの隊は、南極点からの帰り道で、全員が命を落とした。', 'l', 'a lonely snow cairn with a wooden cross on a vast white plain, solemn, wind'),
    (4, '南極は、それほど厳しい場所だった。', 'c', 'a fierce Antarctic blizzard sweeping across ice cliffs, white chaos'),
    (5, 'アーネスト・シャクルトン。アイルランド生まれのイギリスの探検家である。', 's', 'portrait of ' + SHACK + ', confident and charismatic'),
    (5, '彼は、以前の探検で、南極点まで、あと180キロほどの所までたどり着いていた。', 'l', SHACK + ' and three companions with sledges in a vast snowfield, turning back, 1909'),
    (5, 'しかし、仲間の命を守るため、そこで引き返すことを選んだ。', 'l', 'close-up of ' + SHACK + ' looking south over the snow, choosing to turn back, painful decision'),
    (5, '南極点は、もう先を越されてしまった。それなら、次の目標は何か。', 'c', SHACK + ' studying a large map on a wooden desk in a London office, 1914, no readable text'),
    (6, 'シャクルトンが選んだのは、南極大陸を、歩いて横断することだった。', 's', 'an illustrated map of Antarctica with a dotted line crossing the continent, old style, no readable text'),
    (6, '片方の海岸から南極点を通り、反対側の海岸まで、およそ3000キロ。', 'l', 'a huge empty white Antarctic plateau stretching to the horizon, epic'),
    (6, '誰も成しとげたことのない、壮大な計画だった。', 'l', 'men of 1914 loading wooden crates, sledges and dogs onto a sailing ship at a busy London dock'),
    (6, '集まったのは、船乗り、科学者、医師、写真家、大工など、28人の男たちだった。', 'l', MEN + ' posing together on the deck of a wooden ship, varied ages, proud'),
    (6, '船の名前は、エンデュアランス。「忍耐」という意味だった。', 'c', SHIP + ' leaving a harbor in 1914, crowds waving from the shore'),
    (6, '船には、70匹近くのそり犬も乗せられていた。', 's', 'sled dogs on the deck of a wooden sailing ship in 1914, men feeding them, lively'),
    (6, '隊員たちは、まさか、これから2年近くも帰れなくなるとは、思ってもいなかった。', 'c', MEN + ' smiling and waving from the rail of a wooden ship leaving port, innocent'),
    # ch3 閉じ込められた船
    (7, '1914年8月。ヨーロッパでは、第一次世界大戦が始まったばかりだった。', 's', 'soldiers of 1914 marching through a city street, crowds watching, early World War I'),
    (7, 'シャクルトンは、探検を中止して、国のために船を差し出すと申し出た。', 'l', SHACK + ' writing a telegram at a desk, serious, 1914, no readable text'),
    (7, 'しかし、海軍から返ってきた答えは、そのまま進め、というものだった。', 'l', 'a telegram paper held in a hand, a ship in the background, no readable text'),
    (7, 'エンデュアランス号は、南へ向かった。', 'c', SHIP + ' sailing south across a stormy grey ocean'),
    (8, '12月。南大西洋のサウスジョージア島。ここが、人が住む最後の場所だった。', 's', 'a whaling station of 1914 at the foot of snowy mountains on South Georgia island, wooden buildings, ships in the bay'),
    (8, '捕鯨基地の男たちは、今年は氷が多い、気をつけろと忠告した。', 'l', 'old whalers of 1914 in thick coats warning a ship captain on a wooden pier, serious'),
    (8, '12月5日。船は、南極の海、ウェッデル海へと出発した。', 'l', SHIP + ' leaving a mountainous bay, heading toward a horizon of white ice'),
    (8, 'すぐに、海は流れてくる氷でいっぱいになった。', 'c', SHIP + ' pushing slowly through a sea full of floating ice floes, careful'),
    (9, '船は、氷のすき間をぬうように、何週間もかけて南へ進んだ。', 's', SHIP + ' squeezing through narrow channels between ice floes, men watching from the mast'),
    (9, '目指す大陸の海岸は、もう目の前まで迫っていた。', 'l', 'a distant line of ice cliffs on the horizon beyond the pack ice, tantalizing'),
    (9, 'ところが1915年1月。強い風が氷を押し寄せ、船のまわりを、ぎっしりと固めてしまった。', 'l', SHIP + ' trapped tight in thick pack ice, no open water anywhere, ominous'),
    (9, '男たちは、のこぎりやつるはしで氷を割ろうとしたが、びくともしなかった。', 'l', MEN + ' cutting at thick ice with saws and picks beside a trapped ship, hopeless'),
    (9, 'エンデュアランス号は、海の上で、完全に動けなくなった。', 'c', SHIP + ' frozen in the middle of a vast white sea, tiny, alone'),
    # ch4 氷の上の冬
    (10, '南極の冬が来た。太陽は、何か月も昇らなくなる。', 's', SHIP + ' frozen in the ice under a dark sky with the aurora australis glowing above, beautiful and eerie'),
    (10, '船は、氷ごと、ゆっくりと海の上を流されていった。', 'l', 'an illustrated map with a long winding line drifting across the Weddell Sea, no readable text'),
    (10, 'シャクルトンは、男たちが希望を失わないよう、毎日の生活を大切にした。', 'l', SHACK + ' talking with crew members around a table in a warm wooden ship cabin, lamplight'),
    (10, '仕事の時間、食事の時間、そして楽しむ時間。', 'c', MEN + ' eating together at a long table inside a wooden ship, lamplight, warm, laughter'),
    (11, '男たちは、船の中で劇をしたり、歌を歌ったりして過ごした。', 's', MEN + ' singing and playing a banjo in a lamplit wooden ship cabin, joyful'),
    (11, '氷の上では、サッカーをして体を動かした。', 'l', MEN + ' playing football on the ice beside a frozen ship, laughing, 1915'),
    (11, '連れてきた犬たちの世話をし、氷の上で犬ぞりの練習をした。', 'l', 'sled dogs pulling a sledge across the ice beside a frozen ship, a man running beside them'),
    (11, '船長のフランク・ワースリーは、明るい性格で、皆を笑わせた。', 'c', 'portrait of ' + WORS + ', laughing'),
    (11, '写真家のフランク・ハーレーは、氷の中の船の姿を、何枚も写真に残した。', 's', 'a photographer of 1915 with a large wooden camera on a tripod on the ice, a frozen ship lit by flares at night'),
    (11, 'その写真は、のちに、この探検を世界に伝える貴重な記録となる。', 'c', 'an old glass plate photograph of a ship in ice resting on a wooden table, lamplight, no readable text'),
    (12, 'しかし、氷は、じわじわと船を締めつけていた。', 's', 'close-up of thick ice pressing against the wooden hull of a ship, cracks forming'),
    (12, '夜になると、船体がきしむ、不気味な音が響いた。', 'l', 'the dark interior of a wooden ship at night, beams bending, men lying awake listening'),
    (12, 'ワースリーは、のちにこう書いている。まるで、船が悲鳴を上げているようだった。', 'l', WORS + ' standing on the deck at night, listening to the ice, worried'),
    (12, 'シャクルトンは、すでに覚悟していた。この船は、もう助からないかもしれない。', 'c', 'close-up of ' + SHACK + ' looking at the ice from the deck, grim realization'),
    # ch5 船の最期
    (13, '1915年10月。南極に、春が来た。', 's', ICE + ', pale sunlight returning, pressure ridges everywhere'),
    (13, '氷が動き始め、巨大な力で、船を押しつぶし始めた。', 'l', 'massive slabs of ice rising up and crushing against the side of a wooden ship, dramatic'),
    (13, '船体に穴が開き、海水が流れ込んできた。', 'l', 'seawater pouring into the dark hold of a wooden ship, men pumping desperately'),
    (13, '男たちは、何日も休まず、水をくみ出し続けた。', 'l', MEN + ' working hand pumps on a tilted deck, exhausted, determined'),
    (13, 'しかし、もう限界だった。', 'c', SHIP + ' heavily tilted and crushed in the ice, masts leaning, broken'),
    (14, '10月27日。シャクルトンは、船を捨てると決めた。', 's', SHACK + ' standing on a tilted deck giving the order, solemn'),
    (14, '男たちは、食料、テント、道具、そして3隻の救命ボートを、氷の上へと運び出した。', 'l', MEN + ' unloading crates, tents and three wooden lifeboats onto the ice beside a crushed ship'),
    (14, '持ち物は、1人あたり、およそ1キロまでと決められた。', 'l', 'close-up of a man choosing between a few personal items on the ice, a book, a photograph, no readable text'),
    (14, 'シャクルトンは、金貨や聖書を、自ら氷の上に置いてみせた。', 'l', 'close-up of gold coins and a book lying on the snow, a gloved hand leaving them behind'),
    (14, '生き延びるのに必要でないものは、すべて置いていく。それが、彼の示した覚悟だった。', 'c', SHACK + ' walking away from a small pile of abandoned things on the ice, determined'),
    (15, '11月21日。エンデュアランス号は、氷の下へと沈んでいった。', 's', SHIP + ' sinking stern first between broken ice floes, dramatic, solemn'),
    (15, '男たちは、ただ黙って、それを見つめていた。', 'l', MEN + ' standing silently on the ice watching their ship disappear, grief'),
    (15, '28人は、海に浮かぶ氷の上に、取り残された。', 'c', CAMP + ', tiny in the vast white emptiness'),
    (15, '気温はマイナス20度を下回り、風が吹けば、さらに体感温度は下がる。', 's', MEN + ' bracing against a freezing wind on the ice, faces wrapped, breath frozen'),
    (15, 'シャクルトンは、まず、温かい飲み物をいれさせ、皆に配った。', 'l', SHACK + ' handing out steaming mugs to his men in the snow, caring'),
    (15, 'どんなときも、男たちの気持ちを支えることを、彼は何より大切にした。', 'c', MEN + ' holding warm mugs around a stove on the ice, small comfort'),
    # ch6 氷上キャンプ
    (16, '彼らが暮らしたのは、流れる氷の上に張ったテントだった。', 's', CAMP + ', smoke rising from a small stove, men moving around'),
    (16, '地面の下は、深い海。氷が割れれば、テントごと海に落ちてしまう。', 'l', 'a crack opening in the ice floe near the tents, dark water below, danger'),
    (16, 'ある夜、テントの真下の氷に、突然、割れ目が走った。', 'l', 'a crack splitting the ice under a tent at night, men scrambling out, chaos'),
    (16, '1人の男が寝袋ごと海に落ち、シャクルトンが、とっさに引き上げた。', 'c', SHACK + ' pulling a man in a sleeping bag out of dark water at night, dramatic rescue'),
    (17, '食料も、少しずつ減っていった。', 's', 'a few tins and a small pile of seal meat on the snow beside a camp stove, scarce'),
    (17, '男たちは、アザラシやペンギンを捕まえて、食べ物と燃料にした。', 'l', MEN + ' cooking seal meat over a blubber stove on the ice, smoky, cold'),
    (17, '連れてきた犬たちとも、やがて別れなければならなかった。', 'l', 'sled dogs lying in the snow beside a tent, a sad man kneeling beside them, solemn, not graphic'),
    (17, '男たちにとって、それは、とてもつらい決断だった。', 'c', 'a lonely man sitting in the snow at dusk, grief, wind'),
    (17, '一度、食料を運ぶため、ボートを引いて氷の上を歩いて進もうとした。', 's', MEN + ' hauling a heavy wooden lifeboat on a sledge across rough ice ridges, exhausting'),
    (17, 'しかし、氷はでこぼこで、1日に進めたのは、わずか1キロほどだった。', 'l', 'men collapsing beside a lifeboat on rough ice, exhausted, little progress'),
    (17, '結局、男たちは、氷が流れていくのを、待つしかなかった。', 'c', CAMP + ', men sitting and waiting, grey sky'),
    (18, 'シャクルトンは、男たちが仲間割れしないよう、いつも気を配っていた。', 's', SHACK + ' walking between tents and talking quietly with his men, attentive'),
    (18, '不満を言う者がいれば、自分のテントに入れ、そばで見守った。', 'l', 'inside a crowded canvas tent, ' + SHACK + ' sitting beside a grumbling man, calm leadership'),
    (18, '彼は、こう考えていた。氷よりも怖いのは、希望を失うことだ。', 'l', 'close-up of ' + SHACK + ' with a calm determined face, wind blowing snow'),
    (18, '氷は、北へ、北へと流されていった。', 'c', 'an illustrated map of the Weddell Sea with a drifting line moving north toward small islands, no readable text'),
    # ch7 三隻のボート
    (19, '1916年4月。足元の氷が、どんどん小さく割れ始めた。', 's', 'the ice floe breaking into smaller pieces around a camp, dark water spreading, danger'),
    (19, 'もう、氷の上にはいられない。', 'l', MEN + ' looking at the shrinking ice floe with alarm'),
    (19, '4月9日。シャクルトンは命じた。ボートを出せ。', 'l', SHACK + ' shouting orders on the ice, pointing at the open water'),
    (19, '28人は、3隻の小さなボートに分かれて乗り込んだ。', 'l', 'three small wooden lifeboats launched into dark water between ice floes, men rowing'),
    (19, '目指すのは、北にある、小さな島だった。', 'c', 'three small boats rowing through a sea full of floating ice under a grey sky'),
    (20, 'ボートの旅は、地獄のようだった。', 's', 'three small open boats tossed by grey waves among ice floes, freezing spray'),
    (20, '冷たい波しぶきが、服を凍らせた。', 'l', 'close-up of ice forming on the beards and clothes of men in an open boat, freezing'),
    (20, '夜は、氷の上や、ボートの中で眠った。眠れる者は、ほとんどいなかった。', 'l', MEN + ' huddled in an open boat at night, snow falling, sleepless, misery'),
    (20, 'のどの渇きに苦しみ、男たちは、凍った肉をかじって水分をとった。', 'l', 'close-up of a man chewing on a piece of frozen seal meat in a boat, thirsty, exhausted'),
    (20, '凍傷で、手や足の感覚を失う者もいた。', 'c', 'close-up of swollen frostbitten hands gripping an oar, not graphic'),
    (21, 'ボートを導いたのは、船長のワースリーだった。', 's', WORS + ' standing in a small boat holding a brass sextant toward the sky'),
    (21, '彼は、六分儀という道具で太陽の高さを測り、自分たちの位置を割り出した。', 'l', 'close-up of a brass sextant held up toward a pale sun through clouds, ocean spray'),
    (21, '揺れるボートの上で、雲の切れ間から一瞬見える太陽を、必死にとらえた。', 'l', WORS + ' braced in a rocking boat, eye to a sextant, waves crashing, focus'),
    (21, 'その計算が1つでも狂えば、28人は、海の上で迷ってしまう。', 'c', 'three tiny boats in a vast grey ocean, no land in sight, lonely'),
    (22, '7日目。前方に、黒い崖が見えた。', 's', 'black cliffs and glaciers of an island appearing through the mist ahead of small boats'),
    (22, 'エレファント島。南極の海に浮かぶ、岩と氷だけの島だった。', 'l', ELEPH + ', seen from the sea, three small boats approaching'),
    (22, '4月15日。男たちは、ついに島へたどり着いた。', 'l', MEN + ' dragging a lifeboat onto a rocky beach, exhausted, crawling'),
    (22, '陸の上に立つのは、およそ1年半ぶりのことだった。', 'l', 'a man kneeling and touching the rocks of a beach with his bare hands, emotional'),
    (22, '男たちは、石をつかみ、泣き、笑った。', 'c', MEN + ' laughing and weeping on a rocky beach, relief'),
    # ch8 エレファント島
    (23, 'しかし、この島に、助けは来ない。', 's', ELEPH + ', empty, no ships, no people, desolate'),
    (23, '島は、船の通り道から遠く離れていた。誰も、彼らがここにいることを知らない。', 'l', 'an illustrated map showing a tiny island far from shipping routes in the Southern Ocean, no readable text'),
    (23, '吹きつける風は強く、テントは、すぐに裂けてしまった。', 'l', 'a canvas tent ripped by a violent wind on a rocky beach, men grabbing it'),
    (23, '男たちは、ひっくり返した2隻のボートを屋根にして、小屋を作った。', 'c', 'two upturned wooden lifeboats resting on stone walls as a roof of a small hut on a rocky beach'),
    (23, '中は暗く、煙が充満し、すき間からは雪が吹き込んだ。', 's', 'the cramped dark interior of a hut made of upturned boats, smoky, men lying shoulder to shoulder'),
    (23, '凍傷で足を痛めた仲間もいて、医師たちは、限られた道具で手当てを続けた。', 'c', 'two doctors of 1916 tending to an injured man in a dark smoky hut, lamplight, not graphic'),
    (24, 'シャクルトンは、決断した。', 's', 'close-up of ' + SHACK + ' staring out at the stormy sea, decision'),
    (24, '残る1隻のボートで、助けを呼びに行く。', 'l', BOAT + ' on the beach, men preparing it, waves beyond'),
    (24, '目指すのは、あのサウスジョージア島の捕鯨基地。', 'l', 'an illustrated map with a long line across the Southern Ocean from a small island to a larger island, no readable text'),
    (24, 'その距離は、およそ1300キロ。世界で最も荒れる海を、小さなボートで渡るのだ。', 'c', 'enormous grey waves of the Southern Ocean under a stormy sky, terrifying'),
    (25, 'ボートの名前は、ジェームズ・ケアード号。長さは、わずか7メートルほどだった。', 's', BOAT + ', close view, small and fragile'),
    (25, '大工のマクニッシュが、木材やキャンバスで、ボートの上に覆いを作った。', 'l', 'a carpenter of 1916 fitting canvas and wood over an open boat on a beach, focused'),
    (25, '一緒に行くのは、ワースリー、クリーン、マクニッシュ、そしてほかの2人。', 'l', 'six bearded men of 1916 standing beside a small boat on a rocky beach, ready'),
    (25, '島に残る22人は、副隊長のフランク・ワイルドに任された。', 'l', 'portrait of ' + WILD + ', calm and trustworthy'),
    (25, '4月24日。ボートは、荒れた海へとこぎ出した。', 'c', BOAT + ' leaving a rocky beach into grey waves, men on shore waving'),
    # ch9 1300キロの海
    (26, 'それは、想像を超える航海だった。', 's', BOAT + ' climbing a towering grey wave, spray flying, tiny'),
    (26, '巨大な波が、何度もボートに襲いかかった。', 'l', 'a huge wave crashing over a small boat, water pouring in, chaos'),
    (26, '6人は、交代で水をくみ出し、ずぶぬれのまま眠った。', 'l', 'men inside the cramped dark space under a boat canvas, soaked, exhausted, bailing water'),
    (26, '寝袋は水を吸って重くなり、腐り始めた。', 'c', 'close-up of soaked reindeer-skin sleeping bags in the bottom of a boat, miserable'),
    (27, 'やがて、ボートに氷がつき始めた。', 's', BOAT + ' covered in thick ice, the sail and ropes frozen white'),
    (27, '氷の重みで、ボートが沈みそうになる。', 'l', BOAT + ' riding dangerously low in the water under the weight of ice'),
    (27, '男たちは、揺れるボートの上にはい上がり、氷を割って海に捨てた。', 'l', 'men crawling on an icy boat cover in a storm, chipping ice with axes, dangerous'),
    (27, '手がかじかみ、一歩間違えれば、海に落ちる。', 'c', 'close-up of a frozen hand gripping a rope over a raging sea, danger'),
    (28, 'ある夜、シャクルトンは、空に晴れ間が見えたと思った。', 's', SHACK + ' at the tiller of a small boat at night, looking at a white line in the sky'),
    (28, 'しかし、それは晴れ間ではなかった。巨大な波の、白い頭だった。', 'l', 'a gigantic wave with a white crest towering over a tiny boat at night, terrifying'),
    (28, 'シャクルトンは叫んだ。しっかりつかまれ。', 'l', 'close-up of ' + SHACK + ' shouting in the storm, water spraying'),
    (28, '大波が、ボートをのみこんだ。', 'l', 'a tiny boat engulfed by a massive wave, white water everywhere, dramatic'),
    (28, '男たちは、死にもの狂いで水をくみ出し、ボートは、なんとか浮かび続けた。', 'c', 'men bailing water frantically in a half-flooded small boat, survival'),
    (29, '頼れるのは、ワースリーの航海術だけだった。', 's', WORS + ' holding a sextant while another man holds him steady in a rocking boat'),
    (29, '16日間で、太陽が見えたのは、わずか4回ほどだった。', 'l', 'a pale sun barely visible through dark storm clouds over the ocean'),
    (29, '計算に使う表の本は、水にぬれて、ページがくっついていた。', 'l', 'close-up of a soaked navigation book with pages stuck together, a pencil, no readable text'),
    (29, 'もし島を見逃せば、その先は、果てしない大西洋が広がるだけだ。', 'l', 'an endless grey ocean with no land, a tiny boat in the middle, hopeless'),
    (29, '水も、ほとんど残っていなかった。', 'c', 'close-up of an almost empty water cask in a boat, a cracked lip, thirst'),
    # ch10 サウスジョージア
    (30, '出発から14日目。クリーンが叫んだ。陸だ。', 's', CREAN + ' pointing ahead from a small boat, shouting, joy'),
    (30, '霧の向こうに、雪をかぶった山々が見えた。サウスジョージア島だった。', 'l', 'snowy mountains of South Georgia appearing through mist beyond the waves'),
    (30, 'ワースリーの計算は、正しかったのだ。', 'l', 'close-up of ' + WORS + ' smiling with tears, relief'),
    (30, 'しかし、喜びは、すぐに恐怖に変わった。', 'c', 'dark clouds gathering over a rocky coast, ominous'),
    (31, '猛烈な嵐が、ボートを岩だらけの海岸へと押しやった。', 's', BOAT + ' driven toward jagged rocks and towering cliffs by a hurricane, terrifying'),
    (31, '目の前に、陸がある。それなのに、近づけば、岩にたたきつけられる。', 'l', 'huge waves smashing against black cliffs, a tiny boat nearby, desperate'),
    (31, '男たちは、丸一日以上、嵐と戦い続けた。', 'l', 'men fighting the tiller and sail of a small boat in a violent storm, exhausted'),
    (31, '5月10日。ボートは、ようやく小さな入り江に滑り込んだ。', 'c', BOAT + ' entering a small sheltered cove with a rocky beach, calmer water'),
    (32, '男たちは、浜辺に倒れ込んだ。', 's', 'six exhausted men collapsing on a rocky beach beside a small boat, relief'),
    (32, '近くには、小さな洞窟と、真水の小川があった。', 'l', 'a small cave in a rocky cliff and a stream of fresh water on a beach, men drinking'),
    (32, '男たちは、アホウドリのひなを捕まえ、何日ぶりかの温かい食事をとった。', 'l', 'men cooking around a small fire inside a rocky cave, warm light, relief'),
    (32, 'しかし、ここは、島の反対側だった。', 'c', 'an illustrated map of South Georgia island with a cove on one side and a whaling station on the other, mountains between, no readable text'),
    (33, '捕鯨基地は、島の反対側にあった。', 's', 'snowy jagged mountains and glaciers of South Georgia, impassable looking'),
    (33, 'ボートは、もう傷みがひどく、島を回って海を行くのは無理だった。', 'l', BOAT + ' lying damaged on the rocks, a broken rudder'),
    (33, '残された道は、ただ1つ。地図にない、雪と氷の山々を、歩いて越えることだった。', 'c', 'towering unmapped mountains of ice and snow under the moon, daunting'),
    # ch11 山を越える
    (34, '5月19日の夜明け前。シャクルトン、ワースリー、クリーンの3人が出発した。', 's', SHACK + ', ' + WORS + ' and ' + CREAN + ' setting off up a snowy slope under the moon'),
    (34, '登山の道具は、ほとんどなかった。', 'l', 'close-up of boots with screws driven into the soles for grip, a short rope and an adze, makeshift'),
    (34, '靴の底には、ボートから抜いたねじを打ち込み、すべり止めにした。', 'l', 'close-up of hands hammering screws into the sole of a worn leather boot'),
    (34, '持ち物は、ロープ1本と、手おの、そして3日分の食料だけだった。', 'c', 'three men walking in single file across a vast glacier at dawn, tiny'),
    (34, '地図には、島の内側は、何も描かれていなかった。誰も、そこを歩いたことがなかったのだ。', 'l', 'an old map of an island with a blank white interior, no readable text'),
    (35, '山を越えたと思うと、その先は、切り立った崖だった。', 's', 'three small figures at the top of a ridge looking down at a sheer drop, despair'),
    (35, '引き返し、また別の道を探す。何度も、それを繰り返した。', 'l', 'three men trudging back up a snowy slope, exhausted, determined'),
    (35, '日が暮れ、気温は、どんどん下がっていった。', 'l', 'a snowy mountain ridge at dusk, deep blue shadows, cold'),
    (35, 'このまま山の上で夜を越せば、3人とも凍え死んでしまう。', 'c', 'three men standing on a dark icy ridge, freezing wind, fear'),
    (36, 'シャクルトンは、思い切った方法を選んだ。', 's', 'close-up of ' + SHACK + ' looking down a long dark snow slope, decision'),
    (36, '3人はロープを丸めて座り、1つにつながって、急な斜面を一気に滑り降りた。', 'l', 'three men sliding down a steep snow slope together sitting on a coiled rope, speeding into darkness'),
    (36, '何百メートルもの斜面を、ものすごい速さで滑り落ちていく。', 'l', 'three tiny figures speeding down a vast moonlit snow slope, spray of snow, thrilling'),
    (36, '3人は、雪の上に止まると、思わず笑い出した。', 'c', 'three men lying in deep snow at the bottom of a slope laughing, relief'),
    (36, 'のちにシャクルトンは、こう書いている。あの山の上で、3人ではなく、4人で歩いていたような気がした。', 's', 'three men walking on a moonlit glacier, a faint fourth shadow beside them, mysterious, quiet'),
    (36, 'ワースリーとクリーンも、同じことを感じていたという。', 'c', 'close-up of ' + WORS + ' and ' + CREAN + ' looking at each other in silence, awe'),
    (37, '一晩中、歩き続けた。', 's', 'three men walking across a glacier under a full moon, exhausted'),
    (37, '朝の7時ごろ。遠くから、かすかな音が聞こえた。', 'l', 'three men stopping on a snowy ridge at dawn, listening'),
    (37, '捕鯨基地で、人々を呼ぶ汽笛の音だった。', 'l', 'a distant whaling station with chimneys in a bay far below, steam rising, dawn'),
    (37, '1年半ぶりに聞く、人間の世界の音だった。', 'l', 'close-up of ' + CREAN + ' with tears in his eyes, listening, emotional'),
    (37, '5月20日。3人は、ストロムネスの捕鯨基地へとたどり着いた。', 'c', 'three ragged bearded men walking into a whaling station of 1916, workers staring in shock'),
    # ch12 仲間を迎えに
    (38, '基地の責任者は、3人を見ても、誰なのかわからなかった。', 's', 'a whaling station manager of 1916 at the door of a wooden house, staring at three ragged men'),
    (38, 'シャクルトンは言った。わたしの名は、シャクルトンだ。', 'l', 'close-up of ' + SHACK + ' with a black beard and dirty face, speaking quietly'),
    (38, '男は、思わず涙を流したという。', 'l', 'close-up of a tough whaling station manager with tears in his eyes, emotional'),
    (38, 'その日のうちに、島の反対側に残った3人も、船で迎えに行った。', 'c', 'a small whaling boat entering a cove where three men wave from a rocky beach'),
    (39, 'しかし、まだ終わりではない。エレファント島には、22人が待っている。', 's', ELEPH + ', the hut of upturned boats, men looking out to sea'),
    (39, 'シャクルトンは、すぐに助けの船を出した。', 'l', 'a small steam ship of 1916 leaving a harbor into grey seas'),
    (39, 'しかし、海の氷に阻まれ、船は島に近づけなかった。', 'l', 'a small steam ship blocked by pack ice, turning back, frustration'),
    (39, '2回目も、3回目も、失敗に終わった。', 'c', 'close-up of ' + SHACK + ' on the deck of a ship staring at ice, anguish'),
    (40, 'その間、島の22人は、ワイルドのもとで待ち続けていた。', 's', MEN + ' inside a dark smoky hut made of upturned boats, waiting'),
    (40, 'ワイルドは、毎朝、皆にこう声をかけた。荷物をまとめろ。今日、ボスが来るかもしれない。', 'l', WILD + ' speaking cheerfully to the men inside the hut in the morning'),
    (40, '何か月たっても、彼は、その言葉を言い続けた。', 'l', 'men looking out at an empty grey sea from a rocky beach, hope fading'),
    (40, '食料は、残りわずかになっていた。', 'c', 'a small pile of penguin meat and limpets on a rock, scarce food'),
    (41, '1916年8月30日。4回目の挑戦。', 's', 'a small steam tug of 1916 sailing through ice floes toward an island'),
    (41, 'チリの小さな船、イエルチョ号が、エレファント島に近づいた。', 'l', 'a small steam tug approaching a rocky island through the mist'),
    (41, '島の男たちは、船を見つけ、叫び声を上げた。', 'l', MEN + ' running and waving on a rocky beach, shouting, joy'),
    (41, 'ボートの上から、シャクルトンが叫んだ。皆、無事か。', 'l', SHACK + ' standing in a small rowing boat, shouting toward the beach'),
    (41, '答えは、こうだった。全員、無事だ。', 'c', MEN + ' cheering and embracing on the beach as a boat arrives, tears of joy'),
    (41, 'シャクルトンは、その言葉を聞いて、しばらく何も言えなかったという。', 's', 'close-up of ' + SHACK + ' in a rowing boat, overcome with emotion, eyes closed'),
    (41, '4か月以上、彼らは、この島で待ち続けていたのだ。', 'c', 'men climbing into a rowing boat from a rocky beach, helped by sailors, joy'),
    # ch13 その後
    (42, '28人は、1人も欠けることなく、生きて帰ってきた。', 's', 'twenty-eight bearded men of 1916 standing together on the deck of a small ship, thin, smiling'),
    (42, '南極の氷に閉じ込められてから、およそ2年近くがたっていた。', 'l', 'a small ship sailing away from icy mountains into the sunset, peaceful'),
    (42, 'しかし、彼らが戻った世界は、まだ戦争の中にあった。', 'l', 'a city street of 1916 with soldiers and posters, war time, no readable text'),
    (42, '隊員の多くが、その後、戦場へと向かった。', 'c', 'men of 1916 in uniform boarding a train, solemn'),
    (42, '南極では生き延びた仲間の中にも、戦争で命を落とした者がいた。', 'c', 'a field of white crosses in France under a grey sky, solemn'),
    (43, 'シャクルトンの南極横断という夢は、かなわなかった。', 's', 'a vast empty Antarctic plateau under the sun, untouched'),
    (43, 'しかし、絶望的な状況から、全員を連れて帰った彼の決断は、今も語り継がれている。', 'l', SHACK + ' standing on a ship deck looking at the horizon, older, dignified'),
    (43, 'シャクルトンは、1922年、次の南極探検の途中、サウスジョージア島で亡くなった。', 'l', 'a simple granite grave in a small cemetery on South Georgia island, snowy mountains behind, peaceful'),
    (43, '彼は今も、島の捕鯨基地グリトビケンの近くに眠っている。', 'c', 'a lonely grave by a bay with old whaling station buildings in the distance, quiet'),
    (43, '墓の向きは、南を向いているという。彼が生涯をかけた、南極の方角だ。', 'c', 'a granite grave facing south toward snowy mountains under a clear sky, peaceful'),
    (44, '2022年。南極の海の底、深さおよそ3000メートルで、エンデュアランス号が見つかった。', 's', 'a deep sea robot light illuminating the wooden hull of a sunken ship on the dark sea floor'),
    (44, '船は、100年以上たっても、驚くほど、きれいな姿のまま残っていた。', 'l', 'the stern of a wooden ship on the sea floor covered in sea life, well preserved, eerie and beautiful'),
    (44, '船尾には、エンデュアランスの文字が、はっきりと残っていたという。', 'c', 'close-up of carved letters on the stern of a sunken wooden ship in the deep sea, lit by a beam, letters blurred'),
    (45, '氷に閉じ込められた船、沈んだ船、荒れ狂う海、そして地図にない山々。', 's', 'a montage-like single scene: a tiny boat in a vast stormy sea under a sky with the aurora, epic'),
    (45, 'そのどれか1つでも乗り越えられなければ、28人は帰れなかった。', 'l', MEN + ' walking in a line across the snow, determined'),
    (45, '彼らを救ったのは、最後まであきらめない心と、仲間を信じる力だった。', 'l', MEN + ' with arms around each other on a rocky beach, unity'),
    (45, '極限の中で、人は、ここまで強くなれる。', 'c', SHACK + ' looking out to sea from a rocky shore at sunrise, hope'),
    (45, 'このチャンネルでは、実際に起きた極限のサバイバルを記録している。', 's', 'a dark archive room with shelves of case files, one file open under a single desk lamp'),
    (45, '次の記録を見逃さないよう、チャンネル登録をお願いしたい。', 'x', 'the case file closing, the desk lamp switching off, darkness'),
]

# ---- パイプライン用の設定 ----
SCENE = "the Shackleton Endurance expedition, Antarctica and the Southern Ocean, 1914-1916"
STYLE = ("Japanese gekiga manga illustration style (hand-drawn comic art, NOT photorealistic), bold black ink linework with cross-hatching, "
         "painted full colors, cold white and blue ice, grey stormy seas, warm lamplight in cabins and tents, "
         "accurate 1914-1916 period details, ONE single full-frame illustration showing one continuous scene (absolutely NO comic panels, "
         "NO split screen, NO inset frames, NO borders), dramatic high contrast cinematic lighting, serious documentary mood, "
         "not gory, no speech bubbles, no text, no letters, no captions, no logos")
TTS_SPEED = 0.88
READINGS = {"六分儀": "ろくぶんぎ", "入り江": "いりえ", "汽笛": "きてき", "船尾": "せんび", "手おの": "ておの"}
STAMPS = {}
for _c, _t, _p, _i in LINES:
    for _k, _v in [("1915年11月。", "1915年11月"), ("1914年8月。", "1914年8月"), ("1915年10月。", "1915年10月"),
                   ("1916年4月。", "1916年4月"), ("1916年8月30日。", "1916年8月30日"), ("2022年。", "2022年")]:
        if _t.startswith(_k):
            STAMPS[_t] = _v
THUMB = {"image": 3, "big": "エンデュアランス", "red": "全員生還", "top": "南極の氷に閉じ込められた28人", "sub": "船は沈んだ…2年におよぶ極限の脱出劇"}
SHORT = {"sel": [1, 2, 3, 4, 5, 6, 7, 8, 9],
         "stamp": {"1": "1915年11月"},
         "h1": "【実話】エンデュアランス号", "h2": "南極に取り残された28人", "e1": "彼らが選んだ道は――", "e2": "▶ 続きは本編で（固定コメント）",
         "title": "【実話】南極の氷に船が沈んだ…取り残された28人 #shorts",
         "desc": "1915年、南極の氷に閉じ込められた探検船エンデュアランス号が沈んだ。助けを呼ぶ方法もない28人の運命は――。\n#実話 #南極 #サバイバル #シャクルトン #shorts"}
META = {"title": "【実話】南極の氷に閉じ込められた28人…船は沈み、小舟で1300キロ、シャクルトン探検隊が全員生還した2年間",
        "description": ("シャクルトンのエンデュアランス号探検隊（1914〜1916年）の実話。南極大陸横断を目指した船が、ウェッデル海の氷に閉じ込められた。\n"
                        "押しつぶされて沈む船、流れる氷の上のキャンプ、3隻のボートでの脱出、そして小さなボートで世界一荒れる海を1300キロ。"
                        "地図にない山を越え、仲間を救い出すまでの、およそ2年にわたる極限の記録を約20分で描く。\n\n"
                        "▼チャプター\n{CHAPTERS}\n\n"
                        "※映像はすべて実話をもとにした再現イラストです。実在の人物の外見とは異なります。\n"
                        "※出来事の詳細には諸説あります。本動画は記録・資料をもとに構成しています。\n\n"
                        "▼前回：【実話】アポロ13号…月へ向かう宇宙船で酸素タンクが爆発、地球まで32万キロから生還した3人の4日間\nhttps://youtu.be/FHrHTfYS4Wg\n\n"
                        "▼参考資料\n・アーネスト・シャクルトン『South』\n・アルフレッド・ランシング『エンデュアランス号漂流』\n・Endurance22（2022年の沈没船発見調査）報道\n\n"
                        "ナレーション：VOICEVOX:青山龍星\n\n"
                        "クライシス・ファイル〜極限サバイバル劇画〜\n実際に起きた極限のサバイバルを、劇画で記録するチャンネルです。\n"
                        "チャンネル登録：https://www.youtube.com/@CrisisFiles_Survival\n\n"
                        "#実話 #南極 #シャクルトン #エンデュアランス #サバイバル #クライシスファイル"),
        "tags": ["シャクルトン", "エンデュアランス号", "エンデュアランス", "南極", "南極探検", "遭難", "漂流", "サバイバル",
                 "実話", "全員生還", "冒険", "クライシスファイル"]}
