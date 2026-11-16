# EP18: José Salvador Alvarenga — 438 days adrift in the Pacific (2012-2014). Entries: (cut, text, pause, prompt)
# 服装ルール: アルバレンガ＝色あせた赤いTシャツ・黒い短パン・裸足（日焼け）、黒い巻き毛と口ひげ（日がたつほど髪とひげが伸びる）。
#             エセキエル＝白いTシャツ・青い短パン・細身の若者、短い黒髪。
# 表現ルール: 遺体・死の場面は直接描かない（空いた場所・海・夕日などで象徴的に）。血・傷は描かない。
ALV = ("Alvarenga, a 36-year-old Salvadoran fisherman with curly black hair and a thick black mustache, "
       "wearing a faded RED T-shirt and black shorts, barefoot, sun-tanned")
ALVL = ("Alvarenga, a Salvadoran fisherman with long wild curly black hair and a long tangled black beard, very thin and sunburned, "
        "wearing a torn faded RED T-shirt and black shorts, barefoot")
ALVF = "Alvarenga, a Salvadoran man in his late 30s with curly black hair and a black mustache"
EZE = "Ezequiel, a thin 22-year-old Mexican man with short black hair, wearing a WHITE T-shirt and BLUE shorts, barefoot"
BOAT = "a 7-meter open white fiberglass fishing skiff (panga) with a large white icebox in the middle and no roof"
BOATD = "a 7-meter open white fiberglass fishing skiff with a large white icebox and a broken outboard motor"
SEA = "the endless open Pacific Ocean, no land in sight"
TWO = ", only these two men in the boat, no other people"
ALONE = ", he is completely alone, no other people"
NOP = ", no people"

CHAPTERS = [
    (1, "438日間の漂流"),
    (4, "海辺の漁師"),
    (7, "出港"),
    (10, "嵐"),
    (13, "流される"),
    (16, "素手の漁"),
    (19, "雨水"),
    (22, "ゴミの中の食べ物"),
    (25, "通り過ぎる船"),
    (28, "相棒の異変"),
    (31, "ひとりきり"),
    (34, "月を数える"),
    (37, "1年が過ぎて"),
    (40, "島影"),
    (43, "なぜ生き延びたのか"),
    (45, "その後"),
]

LINES = [
    # ch1 438日間の漂流
    (1, '2014年1月。太平洋の真ん中に浮かぶ、マーシャル諸島。', 's', 'a tiny tropical atoll in the Marshall Islands seen from above, palm trees, turquoise lagoon, deep blue Pacific Ocean' + NOP),
    (1, '小さな島の浜辺に、1そうのボートが流れ着いた。', 'l', BOATD + ', battered and covered in barnacles, drifting toward a palm-lined beach' + NOP),
    (1, '乗っていたのは、髪もひげも伸び放題の、やせ細った男だった。', 'l', ALVL + ', sitting in a battered boat near a tropical beach' + ALONE),
    (1, '男の名は、ホセ・サルバドール・アルバレンガ。', 'l', 'portrait of ' + ALVL + ', staring with wild exhausted eyes' + ALONE),
    (2, '彼は、メキシコの海岸から漁に出たまま、太平洋を流され続けていた。', 's', 'a map-like view of the Pacific Ocean from Mexico to the Marshall Islands, a dotted line across the ocean, no readable text' + NOP),
    (2, 'その距離、およそ1万キロ。', 'l', SEA + ', a tiny boat in the vast ocean seen from high above' + NOP),
    (2, '漂流した日数は、438日。1年と2か月以上である。', 'l', BOATD + ' drifting under a huge starry sky' + NOP),
    (2, '食料も、水も、通信手段もない、屋根のない小さなボートで。', 'c', BOATD + ' baking under the blazing sun on a flat ocean' + NOP),
    (3, 'なぜ、彼は生き延びることができたのか。', 's', 'close-up of ' + ALVL + '\'s eyes, determined' + ALONE),
    (3, 'そして、一緒に海に出た、もう1人の若者は、どうなったのか。', 'l', 'an empty spot in the bow of a small open boat at sunset, a white T-shirt folded on the seat' + NOP),
    (3, 'これは、太平洋を漂流した漁師の、438日間の記録である。', 'c', 'a lonely small boat on the Pacific at dawn, golden light' + NOP),
    (3, 'この漂流は、のちに世界中で報道され、本にもなった。', 'l', 'newspapers from around the world spread on a table, no readable text' + NOP),

    # ch2 海辺の漁師
    (4, 'アルバレンガは、中米のエルサルバドルで生まれた。', 's', 'a small fishing village on the Pacific coast of El Salvador, palm trees, wooden boats on the beach' + NOP),
    (4, '海辺の村で育ち、若いころから漁師として働いてきた。', 'l', 'a young man pulling a fishing net on a beach in El Salvador at sunrise, alone'),
    (4, '2000年代のはじめ、彼はメキシコに渡り、南部の漁村で暮らし始めた。', 'l', 'the fishing village of Costa Azul in Chiapas, Mexico, colorful small houses, fishing skiffs pulled up on the sand' + NOP),
    (4, '村の人たちは、彼を「チラヤ」というあだ名で呼んでいたという。', 'l', ALV + ' laughing with other fishermen on a Mexican beach, friendly mood'),
    (4, 'エルサルバドルは、中米でいちばん小さな国。漁業は、海辺の人たちの大切な仕事だった。', 'l', 'a small fishing port in El Salvador with colorful boats and pelicans' + NOP),
    (5, 'アルバレンガは、腕のいい漁師だった。', 's', ALV + ' standing proudly in a fishing skiff holding a big fish' + ALONE),
    (5, '小さなボートで沖へ出て、サメやシイラを釣り上げる。', 'l', ALV + ' pulling a long fishing line from a small boat on the ocean' + ALONE),
    (5, 'ひとたび漁に出れば、一晩から2日ほど、海の上で過ごすのが普通だった。', 'l', BOAT + ' on the ocean at night under the stars, a lamp glowing' + NOP),
    (5, '海の怖さも、よく知っているつもりだった。', 'c', ALV + ' looking at a cloudy horizon from the beach, confident' + ALONE),
    (5, '家族とは遠く離れ、海と仕事だけの毎日だった。', 'l', ALV + ' sitting alone on the edge of a wooden pier at dusk, looking at the sea' + ALONE),
    (6, '2012年11月。アルバレンガは、いつものように漁に出る準備をしていた。', 's', ALV + ' loading ice and fishing gear into a skiff on the beach' + ALONE),
    (6, 'ところが、いつも組んでいた相棒が、急に来られなくなった。', 'l', 'an empty spot on a beach next to a fishing skiff, a pair of sandals left behind' + NOP),
    (6, '代わりに声をかけたのは、ほとんど話したこともない若者だった。', 'l', EZE + ', standing shyly on a Mexican beach next to a fishing skiff'),
    (6, '名前は、エセキエル・コルドバ。20代はじめで、沖での漁の経験は、ほとんどなかった。', 'c', 'portrait of ' + EZE + ', nervous smile, beach behind'),
    (6, 'それでもアルバレンガは、すぐ戻るのだから大丈夫だと考えた。', 'l', ALV + ' patting ' + EZE + ' on the shoulder, reassuring him' + TWO),

    # ch3 出港
    (7, '2012年11月17日。2人を乗せたボートは、メキシコ南部の海岸を出発した。', 's', BOAT + ' leaving a Mexican beach at dawn, two men aboard' + TWO),
    (7, 'ボートの長さは、およそ7メートル。屋根もない、小さな漁船である。', 'l', BOAT + ' seen from above on calm blue water' + NOP),
    (7, '積んでいたのは、燃料と、飲み水、釣り針、そして魚を冷やすための大きな氷の箱。', 'l', 'fuel cans, water jugs, fishing hooks, knives and a big white icebox inside a small open boat' + NOP),
    (7, '予定は、およそ30時間の漁。翌日には、村に戻るはずだった。', 'c', ALV + ' and ' + EZE + ' sitting in the boat, smiling, heading out to sea' + TWO),
    (7, '出発の朝、空は晴れていて、海もおだやかだった。', 'l', 'a calm sunny morning over the Pacific coast of Mexico, gentle waves' + NOP),
    (7, '誰も、これが438日にもおよぶ旅の始まりになるとは、思っていなかった。', 'c', BOAT + ' becoming small on the horizon as it heads out to sea' + NOP),
    (8, '沖に出ると、魚は、面白いほどよく釣れた。', 's', ALV + ' pulling a large mahi-mahi fish into the boat while ' + EZE + ' helps' + TWO),
    (8, '氷の箱は、みるみるうちに魚でいっぱいになっていった。', 'l', 'a big white icebox filled with fresh fish on ice inside a boat' + NOP),
    (8, 'エセキエルも、はじめての沖の漁に、目を輝かせていた。', 'l', 'close-up of ' + EZE + ' smiling with excitement on a boat'),
    (8, 'しかし、そのとき、空の向こうで、黒い雲が広がり始めていた。', 'c', 'dark storm clouds gathering on the horizon over the Pacific, a small boat in the foreground' + NOP),
    (8, '2人は、交代で釣り糸を引き、休むひまもなく働いた。', 'l', ALV + ' and ' + EZE + ' working fishing lines side by side in the boat' + TWO),
    (8, '夕方には、これまでで一番の大漁になりそうだと、アルバレンガは笑った。', 'l', 'close-up of ' + ALV + ' laughing on the boat at sunset' + ALONE),
    (9, 'このあたりの海では、この季節、強い北風が吹き荒れることがある。', 's', 'strong winds whipping the ocean surface into white caps' + NOP),
    (9, '経験のある漁師ほど、その怖さを知っていた。', 'l', 'close-up of ' + ALV + '\'s face watching the dark sky, serious' + ALONE),
    (9, 'アルバレンガは、急いで村に戻ろうとした。', 'c', ALV + ' steering the outboard motor hard toward the coast, waves rising' + TWO),
    (9, 'しかし、ボートは岸から、すでに100キロ近くも離れていた。', 'l', BOAT + ' far out at sea, no coast visible, dark clouds approaching' + TWO),

    # ch4 嵐
    (10, 'だが、嵐は、あっという間に2人のボートを飲みこんだ。', 's', BOAT + ' tossed by huge storm waves under a black sky, rain lashing' + TWO),
    (10, '高い波が、何度もボートを打ちつける。', 'l', 'a giant wave crashing over a small open boat in a violent storm' + NOP),
    (10, '2人は、必死で水をくみ出し続けた。', 'l', ALV + ' and ' + EZE + ' bailing water out of the boat with buckets in heavy rain' + TWO),
    (10, 'ボートを軽くするため、釣ったばかりの魚も、海に捨てた。その量は、およそ500キロ。', 'c', ALV + ' throwing fish overboard from the icebox in a storm' + TWO),
    (10, 'エセキエルは、恐怖で震えていた。', 'l', 'close-up of ' + EZE + ' gripping the side of the boat, terrified, rain on his face'),
    (10, 'アルバレンガは、ボートが転覆しないよう、波に向かって船首を保ち続けた。', 'l', ALV + ' steering the boat into a huge wave, determined' + TWO),
    (11, 'アルバレンガは、無線で、村の雇い主に助けを求めた。', 's', ALV + ' shouting into a handheld two-way radio in the rain' + TWO),
    (11, '「エンジンがだめだ。すぐに来てくれ！」', 'l', 'close-up of a wet handheld radio in a hand, rain drops' + NOP),
    (11, 'しかし、その直後、無線の電池が切れた。', 'l', 'close-up of a dead handheld radio, its screen dark, rain on it' + NOP),
    (11, 'GPSも、壊れて動かなくなっていた。', 'c', 'a broken GPS device with a dark screen on the wet floor of a boat' + NOP),
    (11, 'アルバレンガは、壊れた無線とGPSを、怒りにまかせて海に投げ捨てたという。', 'l', ALV + ' throwing a broken radio into the stormy sea in anger' + TWO),
    (12, 'エンジンは、とうとう止まった。', 's', 'close-up of a dead outboard motor on the back of a skiff, waves splashing' + NOP),
    (12, '嵐は、5日間も続いたという。', 'l', BOAT + ' in the storm at night, lightning in the distance' + TWO),
    (12, '村からは、捜索の船が出された。', 'l', 'a small search boat on a stormy sea, poor visibility, rain'),
    (12, 'しかし、視界が悪く、2日ほどで捜索は打ち切られてしまった。', 'c', 'a gray empty stormy sea with fog, no boats visible' + NOP),
    (12, '2人を待っていたのは、あまりにも長い漂流だった。', 'c', BOATD + ' alone on a gray ocean after the storm' + NOP),

    # ch5 流される
    (13, '嵐がおさまったとき、まわりには、何も見えなかった。', 's', BOATD + ' on a calm gray ocean after a storm, no land anywhere' + TWO),
    (13, '陸地も、ほかの船も。', 'l', SEA + ', calm and empty, a flat horizon' + NOP),
    (13, 'エンジンも、オールも、帆もない。ボートは、ただ海の流れに運ばれていくだけだった。', 'l', BOATD + ' drifting on a slow ocean current' + NOP),
    (13, '風と海流は、2人を、陸とは反対の方向、太平洋の沖へと押し流していた。', 'c', 'a wide view of the Pacific Ocean, a tiny boat being carried westward by the current' + NOP),
    (13, 'どこまで流されるのか、誰にもわからなかった。', 'l', 'a tiny boat on the curve of the vast ocean horizon' + NOP),
    (14, 'アルバレンガは、まず、残っているものを確かめた。', 's', ALV + ' checking the remaining gear in the boat with a serious face' + TWO),
    (14, '飲み水は、ほとんど残っていない。食べ物もない。', 'l', 'empty water jugs and an empty icebox inside a small open boat' + NOP),
    (14, '残っていたのは、ナイフと、バケツ、そして、魚を入れる氷の箱だった。', 'l', 'a knife, plastic buckets and a big white icebox in a small boat' + NOP),
    (14, 'アルバレンガは、ブイを海に投げ、ボートが流されすぎないようにした。', 'c', ALV + ' tying floats on a rope and throwing them into the sea as a makeshift sea anchor' + TWO),
    (14, 'エセキエルは、不安そうに、アルバレンガの顔を見た。', 'l', EZE + ' looking anxiously at ' + ALV + ' in the boat' + TWO),
    (14, '「大丈夫だ。きっと、誰かが見つけてくれる」アルバレンガは、そう言って励ました。', 'c', ALV + ' putting a hand on ' + EZE + '\'s shoulder, encouraging him' + TWO),
    (15, '昼は、焼けつくような日差し。', 's', 'a blazing tropical sun over a small open boat on a flat ocean' + NOP),
    (15, '屋根のないボートの上には、日差しをさえぎるものが何もない。', 'l', ALV + ' and ' + EZE + ' squinting under the blazing sun, sweating' + TWO),
    (15, '2人は、氷の箱の中に入って、日差しから身を守った。', 'l', EZE + ' curled up inside a big open white icebox in a boat, shading himself from the sun'),
    (15, '夜になると、今度は、寒さが2人を襲った。', 'c', BOATD + ' on the dark ocean at night, two men huddled together' + TWO),
    (15, '風の強い夜には、2人で身を寄せ合って、寒さに耐えた。', 'l', ALV + ' and ' + EZE + ' huddled together under the night sky, shivering' + TWO),

    # ch6 素手の漁
    (16, '釣り針も、釣り竿も、嵐で流されてしまっていた。', 's', 'close-up of an empty tackle box in a boat' + NOP),
    (16, 'アルバレンガは、ボートのふちから、海の中に、じっと手を入れた。', 's', ALV + ' leaning over the side of the boat with both arms in the water, waiting' + TWO),
    (16, '魚が近づいてきた瞬間、素手でつかみ上げる。', 'l', ALV + ' grabbing a fish from the water with his bare hands, splash' + TWO),
    (16, '漁師として長年きたえた腕が、命をつないだ。', 'l', 'close-up of strong sun-tanned hands holding a fish' + NOP),
    (16, 'はじめは何度も失敗したが、少しずつ、こつをつかんでいった。', 'l', ALV + ' with arms in the sea, a fish slipping away, splash' + TWO),
    (16, '魚をつかむ瞬間を待つあいだ、何時間も、海に手を入れたままのこともあった。', 'l', ALV + ' lying on the edge of the boat with one arm in the water for hours' + TWO),
    (17, 'つかまえた魚は、生のまま食べた。', 's', ALV + ' eating a piece of raw fish in the boat' + TWO),
    (17, 'エセキエルは、魚を細く切り、ボートのふちに並べて、日に干した。', 'l', EZE + ' laying thin strips of fish to dry on the edge of the boat in the sun'),
    (17, '干した魚は、保存食になった。', 'l', 'thin strips of fish drying in the sun on the edge of a boat' + NOP),
    (17, 'やがて2人は、海に浮かぶウミガメもつかまえるようになった。', 'c', ALV + ' pulling a sea turtle into the boat' + TWO),
    (17, 'カメの甲羅は、雨水をためる器にもなった。', 'l', 'an empty turtle shell used as a bowl, holding water inside a boat' + NOP),
    (18, '空を飛ぶ海鳥も、ボートに止まったところを、手でつかまえた。', 's', ALV + ' catching a seabird that landed on the edge of the boat' + TWO),
    (18, 'どれも、火を使わずに、そのまま食べるしかなかった。', 'l', 'a small open boat with no stove, raw fish strips and feathers on the floor' + NOP),
    (18, 'アルバレンガは、エセキエルに言い聞かせた。「食べなければ、生きて帰れない」', 'l', ALV + ' handing a piece of dried fish to ' + EZE + ', encouraging him' + TWO),
    (18, 'エセキエルは、顔をしかめながらも、少しずつ口に運んだ。', 'c', 'close-up of ' + EZE + ' grimacing while eating dried fish'),
    (18, '2人は、生きるために、食べられるものは何でも食べた。', 'c', 'a small open boat with dried fish strips hanging on a line' + NOP),

    # ch7 雨水
    (19, '何より苦しかったのは、のどの渇きだった。', 's', 'close-up of ' + ALV + '\'s cracked dry lips under the sun' + ALONE),
    (19, '海の水は、塩辛くて飲めない。飲めば、かえって体の水分を奪われてしまう。', 'l', 'a hand scooping seawater, sun glinting on the waves' + NOP),
    (19, '2人は、生きのびるために、自分の尿を飲んだ。', 'l', ALV + ' and ' + EZE + ' sitting weakly in the boat, exhausted, faces in shadow' + TWO),
    (19, 'ウミガメの血を飲んで、のどを潤したこともあったという。', 'c', 'a sea turtle shell lying on the floor of a boat, no blood visible' + NOP),
    (19, '太陽の熱と渇きで、頭がぼんやりしてくる。', 'l', ALV + ' squinting dizzily under the blazing sun' + TWO),
    (20, '漂流が始まって、およそ2週間。', 's', 'dark rain clouds approaching over the ocean' + NOP),
    (20, '空から、ついに雨が降ってきた。', 'l', 'heavy rain falling on a small open boat on the ocean' + NOP),
    (20, '2人は、顔を空に向け、口を大きく開けて、雨を飲んだ。', 'l', ALV + ' and ' + EZE + ' with faces turned up to the rain, mouths open, joyful' + TWO),
    (20, 'バケツや氷の箱に、できるだけ多くの雨水をためた。', 'c', 'rainwater collecting in plastic buckets and an icebox in a boat' + NOP),
    (20, 'それは、漂流が始まってから、いちばんうれしい出来事だった。', 'l', ALV + ' laughing in the rain, arms open' + TWO),
    (21, 'それからは、雨が降るたびに、水をためた。', 's', 'buckets of fresh water lined up in a boat under a cloudy sky' + NOP),
    (21, '雨が少ない時期には、1日にほんの少しずつ、大切に飲んだ。', 'l', ALV + ' carefully sipping a little water from a plastic bottle cap' + TWO),
    (21, '水があるかないか。それが、生と死を分けていた。', 'c', 'close-up of a half-full plastic bucket of rainwater in a boat' + NOP),
    (21, 'アルバレンガは、空の雲の形を見て、雨が来るかどうかを読むようになった。', 'l', ALV + ' studying tall clouds on the horizon' + TWO),

    # ch8 ゴミの中の食べ物
    (22, '太平洋には、陸から流れ出たゴミが、たくさん浮かんでいる。', 's', 'floating plastic trash and debris drifting on the open ocean' + NOP),
    (22, 'アルバレンガは、流れてくるゴミの中に、食べられるものがないか、目をこらした。', 'l', ALV + ' leaning out of the boat, reaching for floating debris' + TWO),
    (22, 'ビニール袋の中に、野菜のかけらが残っていたこともあった。', 'l', 'a plastic bag floating in the sea with some cabbage and carrots inside' + NOP),
    (22, '空のペットボトルは、水を入れる容器として拾い集めた。', 'c', 'a collection of empty plastic bottles inside a boat' + NOP),
    (22, 'それでも、何も見つからない日のほうが、はるかに多かった。', 'l', 'empty ocean with a single plastic bottle floating' + NOP),
    (23, '大きなゴミの下には、小魚が集まってくる。', 's', 'small fish gathering in the shade under floating debris in clear blue water' + NOP),
    (23, 'その小魚をねらって、さらに大きな魚がやってくる。', 'l', 'a larger fish chasing small fish near floating trash, underwater view' + NOP),
    (23, 'アルバレンガは、ゴミのまわりで、魚をつかまえた。', 'l', ALV + ' grabbing fish beside a floating piece of debris' + TWO),
    (23, '海に浮かぶゴミさえも、彼にとっては、命をつなぐ道具だった。', 'c', ALV + ' looking at floating plastic in the sea, thoughtful' + TWO),
    (23, 'ボートのまわりは、いつしか、小さな生き物たちの集まる場所になっていった。', 'l', 'fish, jellyfish and seabirds gathering around a drifting boat, underwater and above water view' + NOP),
    (24, 'ボートの上で、2人は、いろいろな話をした。', 's', ALV + ' and ' + EZE + ' sitting and talking in the boat at sunset' + TWO),
    (24, '家族のこと。故郷のこと。帰ったら、何を食べたいか。', 'l', 'a dreamlike vision of a family dinner table with tortillas and beans, warm light, faces indistinct'),
    (24, 'エセキエルは、母親のことを、よく口にしていたという。', 'l', 'close-up of ' + EZE + ' looking at the horizon, missing home'),
    (24, '話をすることが、2人の心を支えていた。', 'c', BOATD + ' at sunset, two small silhouettes in it' + TWO),
    (24, '時には、2人で、故郷の歌を口ずさむこともあった。', 'l', ALV + ' and ' + EZE + ' singing softly together in the boat at night under stars' + TWO),

    # ch9 通り過ぎる船
    (25, 'ある日、遠くに、大きな船の姿が見えた。', 's', 'a huge container ship on the distant horizon seen from a small boat' + NOP),
    (25, 'アルバレンガは、立ち上がって、両手を大きく振った。', 'l', ALV + ' standing up in the boat waving both arms wildly at a distant ship' + TWO),
    (25, '声がかれるまで、叫び続けた。', 'l', 'close-up of ' + ALV + ' shouting desperately' + ALONE),
    (25, 'しかし、船は、ボートに気づかないまま、遠ざかっていった。', 'c', 'a container ship sailing away on the horizon, a tiny boat behind it' + NOP),
    (25, 'アルバレンガは、ひざから崩れ落ちた。', 'l', ALV + ' falling to his knees in the boat, devastated' + TWO),
    (26, '漂流のあいだ、アルバレンガは、何度も船を見たという。', 's', 'container ships passing far away on the ocean, small and distant' + NOP),
    (26, 'しかし、広い海の上で、小さなボートは、ほとんど見えない。', 'l', 'a view from a ship\'s high bridge over a vast ocean, a tiny dot of a boat far away' + NOP),
    (26, '一度だけ、船の甲板に立つ人が、手を振り返したように見えたこともあった。', 'l', 'a container ship passing at a distance, a tiny figure on the deck'),
    (26, 'それでも、船は止まらなかった。', 'c', 'the stern of a large ship moving away, its wake spreading on the sea' + NOP),
    (26, '夜には、遠くを通る船の明かりも見えた。', 'l', 'lights of a distant ship on a dark night ocean' + NOP),
    (26, 'しかし、ボートには、明かりをともす道具もなかった。', 'c', BOATD + ' in total darkness on the night sea' + NOP),
    (27, '船が見えるたびに、希望がわき、そして、消えていく。', 's', ALV + ' sitting down slowly in the boat, watching a ship disappear' + TWO),
    (27, 'その繰り返しが、2人の心を、少しずつ削っていった。', 'l', BOATD + ' alone on the ocean at dusk' + NOP),
    (27, 'それでもアルバレンガは、「次の船は、きっと止まる」と、自分に言い聞かせた。', 'c', 'close-up of ' + ALV + '\'s determined eyes scanning the horizon' + ALONE),
    (27, 'それでも、エセキエルの顔からは、少しずつ笑顔が消えていった。', 'l', 'close-up of ' + EZE + ' staring blankly at the sea, losing hope'),

    # ch10 相棒の異変
    (28, '漂流が始まって、何か月かがたったころ。', 's', BOATD + ' drifting under a hazy sky' + TWO),
    (28, 'エセキエルの様子が、おかしくなり始めた。', 'l', EZE + ' lying weakly in the boat, pale and sick'),
    (28, '生の海鳥を食べたあと、ひどく体調をくずしたのだという。', 'l', EZE + ' clutching his stomach in pain in the boat'),
    (28, 'それ以来、エセキエルは、食べ物を口にしなくなった。', 'c', EZE + ' turning his face away from a piece of food offered by a hand'),
    (28, '体に合わない生の食べ物が、少しずつ、彼の体をむしばんでいた。', 'l', EZE + ' lying sick in the boat, sweating, eyes closed'),
    (29, 'アルバレンガは、何度も食べるように言った。', 's', ALV + ' holding out food to ' + EZE + ', pleading' + TWO),
    (29, 'しかし、エセキエルは、首を横に振るばかりだった。', 'l', 'close-up of ' + EZE + ' shaking his head weakly'),
    (29, '体は、日に日に、やせ細っていった。', 'l', EZE + ' lying very thin and weak in the shade of the icebox'),
    (29, '心も、少しずつ、生きる希望を失っていった。', 'c', 'close-up of ' + EZE + '\'s empty hopeless eyes looking at the sky'),
    (29, 'アルバレンガは、エセキエルの口元に、雨水を少しずつ運んだ。', 'l', ALV + ' gently giving water to ' + EZE + ' from a bottle cap' + TWO),
    (30, 'ある日、エセキエルは、アルバレンガにこう頼んだという。', 's', EZE + ' whispering to ' + ALV + ' in the boat' + TWO),
    (30, '「もし帰れたら、母に伝えてほしい」', 'l', 'close-up of two hands clasped together in a boat, soft light' + NOP),
    (30, 'アルバレンガは、その言葉を、しっかりと胸に刻んだ。', 'l', 'close-up of ' + ALV + '\'s face, tears in his eyes, nodding' + ALONE),
    (30, 'そして、その数日後。エセキエルは、静かに息を引き取った。', 'c', 'a quiet sunset over the empty ocean, golden light on calm water' + NOP),
    (30, '漂流が始まってから、およそ4か月がたっていたとされる。', 'c', 'a crescent moon over a calm dark ocean' + NOP),

    # ch11 ひとりきり
    (31, 'アルバレンガは、ひとりになった。', 's', ALVL + ' sitting alone in the boat, head in his hands' + ALONE),
    (31, '彼は、しばらくのあいだ、エセキエルが、まだそこにいるかのように話しかけ続けたという。', 'l', ALVL + ' talking softly toward the empty bow of the boat' + ALONE),
    (31, 'そして数日後、エセキエルを、静かに海へと送った。', 'l', 'a white T-shirt floating gently on calm ocean water at dawn, soft light' + NOP),
    (31, '広い海の上で、話し相手は、もう誰もいなかった。', 'c', BOATD + ' alone on the vast ocean seen from high above' + NOP),
    (31, '海の上の静けさが、これほど重く感じられたことはなかった。', 'l', 'a perfectly calm empty ocean at noon, oppressive silence' + NOP),
    (32, 'それから何日も、アルバレンガは、深い絶望の中にいた。', 's', ALVL + ' lying in the boat staring blankly at the sky' + ALONE),
    (32, '自分も、もう終わりにしてしまおうか。そう考えたこともあったという。', 'l', 'close-up of ' + ALVL + '\'s hollow eyes, despair' + ALONE),
    (32, 'しかし、彼を思いとどまらせたのは、神への信仰と、家族の存在だった。', 'l', 'a small wooden cross made of two sticks tied with string inside a boat, soft light' + NOP),
    (32, 'そして、エセキエルとの約束。彼の母親に、言葉を伝えなければならない。', 'c', ALVL + ' sitting up, gripping the edge of the boat, determined' + ALONE),
    (32, '4日間、彼は、ほとんど何もせずに、ただ空を見ていたという。', 'l', ALVL + ' lying motionless in the boat under the open sky' + ALONE),
    (32, '母親に会うまでは、死ねない。彼は、そう心に決めた。', 'l', 'close-up of ' + ALVL + '\'s face at dawn, a new determination in his eyes' + ALONE),
    (33, 'アルバレンガは、ふたたび、海に手を入れ始めた。', 's', ALVL + ' reaching into the sea to catch fish' + ALONE),
    (33, '魚をつかまえ、鳥をつかまえ、雨水をためる。', 'l', ALVL + ' collecting rainwater in buckets' + ALONE),
    (33, '1日1日を、ただ生きる。それだけを考えるようにした。', 'c', BOATD + ' on the ocean at sunrise' + NOP),
    (33, '生きて帰る。それが、エセキエルとの約束を果たす、ただ1つの道だった。', 'l', 'close-up of ' + ALVL + '\'s hands tightening a rope, determined' + ALONE),

    # ch12 月を数える
    (34, '時計も、カレンダーもない。', 's', 'the empty floor of a small boat with scattered gear, no clock' + NOP),
    (34, 'アルバレンガは、夜空の月を見て、時の流れを数えることにした。', 'l', ALVL + ' looking up at a full moon over the ocean at night' + ALONE),
    (34, '月が満ちて、欠けて、また満ちる。それで、およそ1か月。', 'l', 'phases of the moon over a dark ocean, a crescent moon and stars' + NOP),
    (34, '満月が来るたびに、彼は、ひと月が過ぎたことを確かめた。', 'c', 'a bright full moon reflected on the calm ocean' + NOP),
    (34, '満月の数が増えるたびに、家族との距離が、遠くなっていくようにも感じた。', 'l', ALVL + ' looking at the moon with a sad face' + ALONE),
    (34, '数を忘れないよう、彼は、ボートのふちに、ナイフで小さな印を刻んだ。', 'l', 'close-up of small notches carved into the edge of a fiberglass boat with a knife' + NOP),
    (35, 'ひとりきりの長い時間、アルバレンガは、空想の中で過ごすことが多くなった。', 's', ALVL + ' lying in the boat daydreaming, looking at clouds' + ALONE),
    (35, '故郷の村を歩く自分。好きな料理を食べる自分。', 'l', 'a dreamlike vision of a sunny village street in El Salvador with food stalls, soft focus' + NOP),
    (35, '空想の中では、彼は、どこにでも行くことができた。', 'l', 'a dreamlike vision of a man walking on a beach toward a village, golden light, soft focus'),
    (35, 'それが、正気を保つための、彼なりの方法だった。', 'c', 'close-up of ' + ALVL + '\'s calm face with eyes closed' + ALONE),
    (35, '空想の中で、彼は、たくさんの料理を味わい、家族と語り合った。', 'l', 'a dreamlike vision of a warm family meal with laughter, soft focus, faces indistinct'),
    (36, '海は、ときに、思いがけない仲間も連れてきた。', 's', 'a school of fish swimming under a small boat in clear blue water' + NOP),
    (36, 'ボートのまわりには、魚の群れが、ずっとついてきた。', 'l', 'fish and small sharks swimming around the shadow of a drifting boat' + NOP),
    (36, '海鳥たちも、ボートに羽を休めにやってきた。', 'l', 'seabirds resting on the edge of a small drifting boat' + NOP),
    (36, '彼らは、食べ物であり、同時に、孤独をやわらげる存在でもあった。', 'c', ALVL + ' watching seabirds on the boat\'s edge with a faint smile' + ALONE),
    (36, '小さな魚が、何か月も同じボートの下で泳ぎ続けたこともあったという。', 'l', 'a small fish swimming under the shadow of a boat in clear water' + NOP),
    (36, 'ある時は、大きなサメが、ボートのまわりを何日も泳ぎ回ったこともあった。', 'l', 'a large shark fin circling near a small drifting boat' + NOP),

    # ch13 1年が過ぎて
    (37, '漂流が始まって、およそ1年。', 's', BOATD + ', now old and faded, drifting on a calm ocean' + NOP),
    (37, 'ボートは、メキシコから、はるか西へと流されていた。', 'l', 'a wide view of the western Pacific, a tiny boat in the middle' + NOP),
    (37, 'アルバレンガの髪とひげは、長く伸び放題になっていた。', 'l', 'close-up of ' + ALVL + ', long hair and beard blowing in the wind' + ALONE),
    (37, '体は、骨が浮き出るほど、やせ細っていた。', 'c', ALVL + ' sitting in the boat, ribs showing under the torn shirt' + ALONE),
    (37, '鏡もない海の上で、彼は、自分がどんな姿になっているのかもわからなかった。', 'l', ALVL + '\'s reflection wavering on the calm sea surface' + ALONE),
    (37, '太平洋のまんなか。いちばん近い陸地まで、何千キロも離れていた。', 'l', 'a satellite-like view of the vast blue Pacific with a tiny dot of a boat' + NOP),
    (38, 'それでも、彼の手は、魚をつかむことをやめなかった。', 's', ALVL + ' grabbing a fish from the sea with a quick motion' + ALONE),
    (38, '嵐が来れば、ボートにしがみつき、波をやり過ごした。', 'l', ALVL + ' clinging to the boat in a rough sea at night' + ALONE),
    (38, '日照りが続けば、氷の箱の中で、じっと体力を温存した。', 'l', ALVL + ' resting inside the icebox in the boat, shading from the sun' + ALONE),
    (38, '海で生きる方法を、彼は、体で覚えていった。', 'c', ALVL + ' standing in the boat, balancing calmly, looking at the sea' + ALONE),
    (38, 'ボートの底には、貝やフジツボがびっしりとついていた。', 'l', 'the underside of a drifting boat covered with barnacles, small fish around it, underwater view' + NOP),
    (38, 'それでも、心が折れそうになる日は、何度もあった。', 'l', ALVL + ' sitting slumped in the boat under a gray sky' + ALONE),
    (38, 'そんなとき彼は、家族の顔と、エセキエルとの約束を思い出したという。', 'c', 'close-up of ' + ALVL + ' closing his eyes, remembering, faint smile' + ALONE),
    (39, '満月を数えて、15回目。', 's', 'a full moon rising over the dark Pacific Ocean' + NOP),
    (39, '漂流は、すでに1年と2か月を超えていた。', 'l', BOATD + ' drifting under a pink morning sky' + NOP),
    (39, 'そのとき、海の色が、少し変わったことに、彼は気づいた。', 'c', 'the open ocean changing from deep blue to lighter turquoise, birds in the sky' + NOP),
    (39, '頭の上を飛ぶ鳥の数も、少しずつ増えていた。', 'l', 'many seabirds flying above a small boat in the sky' + NOP),
    (39, '陸地が近いのかもしれない。アルバレンガの胸に、かすかな希望がわいた。', 'c', 'close-up of ' + ALVL + '\'s eyes widening with hope' + ALONE),

    # ch14 島影
    (40, '2014年1月30日。', 's', 'dawn over the Pacific Ocean, a thin line of green on the horizon' + NOP),
    (40, '水平線の向こうに、緑色のものが見えた。ヤシの木だった。', 'l', 'palm trees on a tiny distant island seen from a small boat' + NOP),
    (40, 'マーシャル諸島の、エボン環礁と呼ばれる、小さな島々だった。', 'l', 'Ebon Atoll in the Marshall Islands seen from above, a ring of small green islets in a turquoise lagoon' + NOP),
    (40, 'アルバレンガは、ボートと海をつないでいたブイのロープを、ナイフで切った。', 'c', ALVL + ' cutting a rope with a knife at the edge of the boat, the island in the distance' + ALONE),
    (40, 'ここで島を逃せば、ボートは、また広い海へと流されてしまう。', 'l', 'a tiny island slipping past a drifting boat, ocean beyond' + NOP),
    (41, 'ボートは、波に乗って、島のほうへ近づいていく。', 's', BOATD + ' riding a wave toward a reef and a palm-lined beach' + NOP),
    (41, 'サンゴ礁の上で、ボートは大きく揺れた。', 'l', BOATD + ' tossed by breaking waves over a coral reef' + NOP),
    (41, 'アルバレンガは、海に飛びこみ、浜辺へと泳いだ。', 'l', ALVL + ' swimming through surf toward a white sand beach' + ALONE),
    (41, 'そして、砂の上に、はうようにしてたどり着いた。', 'c', ALVL + ' crawling onto a white sand beach under palm trees, exhausted' + ALONE),
    (41, 'サンゴで足を切らないよう、必死で波をかわした。', 'l', ALVL + ' struggling through waves over a coral reef' + ALONE),
    (41, 'ボートを捨てることは、大きな賭けだった。しかし、ほかに道はなかった。', 'l', ALVL + ' standing on the edge of the boat, ready to jump into the sea' + ALONE),
    (42, '1年以上ぶりに踏む陸地。しかし、足に力が入らず、立ち上がることもできなかった。', 's', ALVL + ' lying on the white sand clutching it with his hands, crying with relief' + ALONE),
    (42, 'しばらくして、島の住民の2人が、彼を見つけた。', 'l', 'two Marshallese islanders, a man and a woman, walking on a beach and stopping in surprise'),
    (42, '2人は驚きながらも、彼に食べ物と水を与え、助けを呼びに走った。', 'l', 'a Marshallese islander woman giving water to ' + ALVL + ' sitting on the beach'),
    (42, '漂流が始まってから、438日目のことだった。', 'c', 'a palm-lined beach at sunset on a tiny Pacific atoll, an old boat on the shore' + NOP),
    (42, 'その姿を見た住民は、言葉も通じない、この男が、どこから来たのか、すぐにはわからなかった。', 'l', 'two Marshallese islanders looking puzzled at ' + ALVL + ' on the beach'),
    (42, 'やがて、警察と看護師がかけつけ、アルバレンガは保護された。', 'l', 'a police officer and a nurse helping ' + ALVL + ' onto a stretcher on a beach'),

    # ch15 なぜ生き延びたのか
    (43, 'アルバレンガは、なぜ、438日もの漂流を生き延びることができたのか。', 's', BOATD + ' resting on a beach, weathered and empty' + NOP),
    (43, '1つ目は、漁師としての腕。素手で魚や鳥をつかまえる技術が、食べ物を絶やさなかった。', 'l', 'close-up of strong weathered hands holding a fish' + NOP),
    (43, '2つ目は、雨水をため、少しずつ飲むという、水の管理だった。', 'l', 'buckets of rainwater in a boat under a cloudy sky' + NOP),
    (43, 'そして3つ目は、心の強さ。空想や信仰、そして相棒との約束が、彼を支え続けた。', 'l', ALVL + ' looking at a sunrise over the sea, calm' + ALONE),
    (43, 'どれか1つが欠けても、438日を生き延びることはできなかっただろう。', 'c', BOATD + ' on a beach at golden hour' + NOP),
    (44, 'ただし、専門家の多くは、運も大きかったと指摘している。', 's', 'a wide view of ocean currents with clouds, a tiny boat in the middle' + NOP),
    (44, '海流が、ほんの少しずれていれば、ボートは、島のない海の真ん中を、流れ続けていたかもしれない。', 'l', 'a vast empty ocean with no islands, a tiny boat drifting' + NOP),
    (44, 'それでも、最後まで生きることをあきらめなかったからこそ、その運をつかむことができたのである。', 'c', 'a tiny atoll appearing in the vast Pacific at dawn' + NOP),
    (44, '実際、太平洋で漂流した人の多くは、陸にたどり着くことなく、行方がわからなくなっている。', 'l', 'a vast ocean at dusk with no boats, solemn mood' + NOP),

    # ch16 その後
    (45, '保護されたアルバレンガは、マーシャル諸島の病院で手当てを受けた。', 's', ALVL + ' sitting in a hospital bed in a hospital gown, a nurse beside him'),
    (45, '足はむくみ、貧血もひどかったが、命に別状はなかった。', 'l', ALVL + ' in a hospital bed eating a meal slowly, sunlight from the window'),
    (45, '世界中のメディアが、この奇跡の生還を伝えた。', 'l', 'reporters with cameras and microphones crowding outside a hospital, no readable text'),
    (45, 'あまりに信じがたい話に、本当なのかと疑う声も上がった。', 'l', 'people reading newspapers with skeptical faces, no readable text'),
    (45, 'しかし、海流の研究者たちは、メキシコ沖から流されたボートが、この島の近くにたどり着くことは十分にありえると結論づけた。', 'l', 'scientists looking at a large ocean current map on a computer screen, no readable text'),
    (45, '体の中には、生の肉を食べたことによる寄生虫もいると考えられた。', 'l', 'a doctor looking at a chart beside ' + ALVL + ' in a hospital bed'),
    (45, 'それでも11日間の入院のあと、彼は、故郷へ帰れるまでに回復した。', 'l', ALVL + ' walking slowly in a hospital corridor with a nurse'),
    (46, '2014年2月。アルバレンガは、故郷のエルサルバドルに帰った。', 's', ALVF + ', short-haired and clean-shaven now except his mustache, being hugged by his elderly parents at an airport'),
    (46, '家族と、何年ぶりかの再会を果たした。', 'l', ALVF + ' sitting with his family in a simple house in El Salvador, tears and smiles'),
    (46, 'そして彼は、メキシコを訪れ、エセキエルの母親に会った。', 'l', ALVF + ' meeting an elderly Mexican woman at her door, both emotional'),
    (46, '海の上で交わした約束を、果たすためだった。', 'l', 'close-up of two people holding hands, an elderly woman and a man, soft warm light'),
    (46, '帰国後のアルバレンガは、長いあいだ、海を怖がるようになったという。', 's', ALVF + ' standing far from the shore, looking at the sea with fear'),
    (46, '2016年には、彼の体験をまとめた本『438日』が出版され、世界中で話題になった。', 'l', 'a book on a wooden table next to a model of a small fishing boat, no readable text' + NOP),
    (46, '屋根のない小さなボートで、1万キロの海を越えた男。', 'l', BOATD + ' on a beach at sunset, palm trees' + NOP),
    (46, '彼を最後まで支えたのは、生きて帰るという、強い思いだった。', 'c', 'sunrise over the Pacific Ocean, a single seabird flying' + NOP),
    (46, 'アルバレンガは、のちのインタビューで、こう語っている。生きのびることができたのは、あきらめなかったからだと。', 'l', ALVF + ' speaking calmly in an interview in a bright room, no readable text'),
    (46, 'このチャンネルでは、実際に起きた極限のサバイバルを記録している。', 's', 'a dark archive room with shelves of case files, one file open under a single desk lamp'),
    (46, '次の記録を見逃さないよう、チャンネル登録をお願いしたい。', 'x', 'the case file closing, the desk lamp switching off, darkness'),
]

# ---- パイプライン用の設定 ----
SCENE = "the 2012-2014 Pacific drift of fisherman José Salvador Alvarenga"
STYLE = ("Japanese gekiga manga illustration style (hand-drawn comic art, NOT photorealistic), bold black ink linework with cross-hatching, "
         "painted full colors, deep ocean blues and blazing sun tones, accurate 2010s small fishing boat details, "
         "ONE single full-frame illustration showing one continuous scene (absolutely NO comic panels, "
         "NO split screen, NO inset frames, NO borders), dramatic high contrast cinematic lighting, serious documentary mood, "
         "no blood, no wounds, no corpses, no speech bubbles, no text, no letters, no captions, no logos")
TTS_SPEED = 0.95
TTS_SPEAKER = 11  # 玄野武宏
TTS_INTONATION = 1.1
READINGS = {"尿": "にょう", "環礁": "かんしょう", "雇い主": "やといぬし", "息を引き取った": "いきをひきとった", "幻": "まぼろし", "正気": "しょうき"}
STAMPS = {}
for _c, _t, _p, _i in LINES:
    for _k, _v in [("2014年1月。", "2014年1月"), ("2012年11月。", "2012年11月"), ("2012年11月17日", "11月17日"),
                   ("漂流が始まって、およそ2週間", "2週間後"), ("漂流が始まって、何か月", "数か月後"),
                   ("漂流が始まって、およそ1年", "1年後"), ("2014年1月30日", "2014年1月30日")]:
        if _t.startswith(_k):
            STAMPS[_t] = _v
THUMB = {"image": 3, "big": "438日", "red": "漂流", "top": "屋根のない小舟で太平洋を", "sub": "1万キロ流された漁師の生還"}
SHORT = {"sel": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
         "stamp": {"1": "2014年1月"},
         "h1": "【実話】太平洋を438日漂流", "h2": "1万キロ流された漁師", "e1": "彼はなぜ生きていたのか――", "e2": "▶ 続きは本編で\n画面下の「関連動画」から見られます",
         "title": "【実話】屋根のない小舟で438日…1万キロ流されて島にたどり着いた漁師【2012年 アルバレンガ太平洋漂流】 #shorts",
         "desc": "2014年1月、マーシャル諸島の小さな島に、1そうのボートが流れ着いた。乗っていたのは、メキシコから438日間漂流した漁師だった――。\n#実話 #漂流 #サバイバル #太平洋 #438日 #shorts"}
META = {"title": "【実話】小舟で438日、太平洋を漂流…1万キロ流されて生還した漁師【2012年 アルバレンガ太平洋漂流】",
        "description": ("ホセ・サルバドール・アルバレンガ（2012〜2014年）の実話。メキシコ南部の海岸から30時間の漁に出た漁師と若い相棒。"
                        "嵐でエンジンも無線も失い、屋根のない7メートルのボートは太平洋の沖へ。"
                        "素手で魚や海鳥をつかまえ、雨水をためて生きのびた438日間、約1万キロの漂流を、約20分で記録する。\n\n"
                        "▼チャプター\n{CHAPTERS}\n\n"
                        "※映像はすべて実話をもとにした再現イラストです。実在の人物の外見とは異なります。\n"
                        "※出来事の詳細には諸説あります。本動画は当事者の証言・報道・資料をもとに構成しています。\n\n"
                        "▼前回：{PREV}\n\n"
                        "▼参考資料\n・Jonathan Franklin『438 Days』（2016年）\n・各種報道・インタビュー\n\n"
                        "ナレーション：VOICEVOX:玄野武宏\n\n"
                        "クライシス・ファイル〜極限サバイバル劇画〜\n実際に起きた極限のサバイバルを、劇画で記録するチャンネルです。\n"
                        "チャンネル登録：https://www.youtube.com/@CrisisFiles_Survival\n\n"
                        "#実話 #漂流 #サバイバル #太平洋 #438日 #アルバレンガ #クライシスファイル"),
        "tags": ["アルバレンガ", "438日", "漂流", "太平洋", "マーシャル諸島", "エボン環礁", "漁師", "遭難", "サバイバル", "実話", "生還", "クライシスファイル"]}
