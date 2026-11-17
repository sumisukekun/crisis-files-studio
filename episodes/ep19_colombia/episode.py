# EP19: 2023 Colombia Cessna crash — four Huitoto children survive 40 days in the Amazon. Entries: (cut, text, pause, prompt)
# 服装ルール（全カット共通）:
#   レスリー（13歳の姉）＝長い黒髪を後ろで結んだ先住民の少女、色あせたオレンジのTシャツ・黒いレギンス
#   ソレイニ（9歳の妹）＝肩までの黒髪、ピンクのTシャツ・青い短パン
#   ティエン（4歳の弟）＝短い黒髪、水色のTシャツ・灰色の短パン
#   クリスティン（11か月の赤ちゃん）＝白いロンパース
# 表現ルール: 遺体・死の場面・けがは一切描かない。墜落機は外観のみ。子どもは子どもらしく、痛々しすぎない描写に。
LES = "Lesly, a 13-year-old Indigenous Colombian girl with long black hair tied back, wearing a faded ORANGE T-shirt and black leggings"
SOL = "Soleiny, a 9-year-old Indigenous girl with shoulder-length black hair, wearing a PINK T-shirt and blue shorts"
TIE = "Tien, a 4-year-old Indigenous boy with short black hair, wearing a LIGHT BLUE T-shirt and gray shorts"
CRI = "Cristin, an 11-month-old baby girl in a white onesie"
KIDS = ("four Indigenous Colombian children: " + LES + " (carrying " + CRI + "), " + SOL + ", and " + TIE)
JUNGLE = "the dense Colombian Amazon rainforest, giant trees, hanging vines, deep green shadows, humid mist"
NIGHT = "the Amazon rainforest at night, total darkness, faint moonlight through the canopy, fireflies"
PLANE = "a small white single-engine Cessna 206 airplane"
WRECK = "the wreck of a small white single-engine airplane standing upright among dense jungle trees, its nose crushed into the vegetation, no people"
ONLYKIDS = ", only these four children, no adults, no other people"
NOP = ", no people"

CHAPTERS = [
    (1, "40日間の密林"),
    (4, "フイト族の子どもたち"),
    (7, "5月1日のフライト"),
    (10, "墜落"),
    (13, "母の言葉"),
    (16, "密林を歩く"),
    (19, "希望作戦"),
    (22, "残された手がかり"),
    (25, "空から届く祖母の声"),
    (28, "雨と飢え"),
    (31, "すれ違い"),
    (34, "犬のウィルソン"),
    (37, "40日目"),
    (40, "「おなかがすいた」"),
    (43, "なぜ生き延びたのか"),
    (45, "その後"),
]

LINES = [
    # ch1 40日間の密林
    (1, '2023年6月9日。南米コロンビアの、アマゾンのジャングル。', 's', JUNGLE + ', seen from above, endless green canopy' + NOP),
    (1, '墜落の知らせから、すでに1か月以上がたっていた。多くの人が、生存はもう難しいと考え始めていた。', 'l', 'tired soldiers resting in a jungle camp, exhausted faces'),
    (1, '深い森の中で、捜索隊が、ついに4人の子どもたちを見つけた。', 'l', 'a search team of Colombian soldiers and Indigenous trackers stopping in surprise among giant jungle trees, children visible ahead between the leaves'),
    (1, '13歳の姉と、9歳の妹、4歳の弟、そして1歳になったばかりの赤ちゃん。', 'l', KIDS + ', sitting together on the jungle floor, thin and tired' + ONLYKIDS),
    (1, '4人は、小型飛行機の墜落事故から、40日間、大人のいない密林で生き延びていた。', 'c', JUNGLE + ', a beam of sunlight falling to the forest floor, hope' + NOP),
    (2, 'アマゾンには、ジャガーや毒ヘビ、毒を持つ虫が数えきれないほどいる。', 's', 'a jaguar watching from the shadows of the Amazon jungle, eyes glowing' + NOP),
    (2, '大人でさえ、迷えば数日で命を落とすといわれる場所だ。', 'l', JUNGLE + ', dark and endless, no paths' + NOP),
    (2, 'そこで、子どもだけで、40日。', 'l', 'close-up of ' + LES + ', holding ' + CRI + ', determined eyes, jungle behind' + ONLYKIDS),
    (2, 'コロンビアの大統領は、この生還を「奇跡」と呼んだ。', 'c', 'a crowd in a Colombian city watching news on a big screen, cheering, no readable text'),
    (2, '夜には、気温が下がり、激しい雨が、何時間も降り続く。', 'l', JUNGLE + ', at night in heavy rain' + NOP),
    (3, 'なぜ、子どもたちは、生き延びることができたのか。', 's', KIDS + ', walking in a line through the jungle, seen from behind' + ONLYKIDS),
    (3, 'そこには、13歳の姉の、驚くべき強さと、森で生きる人々の知恵があった。', 'l', 'close-up of ' + LES + '\'s face in green jungle light, calm and strong' + ONLYKIDS),
    (3, 'これは、2023年、コロンビアのアマゾンで起きた、小型機墜落事故と、4人の子どもたちの、40日間の記録である。', 'c', 'a misty Amazon river winding through the rainforest at dawn' + NOP),
    (3, 'その中には、1匹の犬の物語もあった。', 'l', 'a Belgian Malinois search dog standing in the misty jungle' + NOP),

    # ch2 フイト族の子どもたち
    (4, '子どもたちは、アマゾンに暮らす先住民、フイト族の家族だった。', 's', 'a small Indigenous Huitoto village of wooden houses with thatched roofs by a river in the Colombian Amazon' + NOP),
    (4, '村は、深い森と川に囲まれた場所にあった。', 'l', 'a wide river through dense rainforest, small wooden canoes on the bank' + NOP),
    (4, '道路はなく、町へ行くには、船か、小さな飛行機に乗るしかない。', 'l', PLANE + ' on a small grass airstrip next to the jungle' + NOP),
    (4, '子どもたちは、森とともに育った。', 'c', KIDS + ', playing near a river in a village, laughing' + ONLYKIDS),
    (4, '川で魚をとり、森で木の実を集め、畑でイモを育てる。それが、村の暮らしだった。', 'l', 'Indigenous villagers fishing from a canoe and harvesting cassava near a jungle village'),
    (4, 'フイト族は、昔からアマゾンの森とともに暮らしてきた人々である。', 'l', 'Indigenous Huitoto elders in a traditional round house (maloca) in the Amazon, warm firelight'),
    (5, 'いちばん上の姉は、レスリー。13歳。', 's', 'portrait of ' + LES + ', shy smile, village behind'),
    (5, '働く母親に代わって、小さい妹や弟の世話をすることが多かった。', 'l', LES + ' carrying ' + CRI + ' on her hip in a village, smiling'),
    (5, '小さな弟や妹にとって、レスリーは、もう1人の母親のような存在だった。', 'l', LES + ' braiding ' + SOL + '\'s hair on a village porch, ' + TIE + ' watching'),
    (5, 'その下に、9歳の妹ソレイニ。4歳の弟ティエン。', 'l', SOL + ' and ' + TIE + ' sitting together on a wooden porch, eating fruit'),
    (5, 'そして、まだ生まれて11か月の、赤ちゃんのクリスティンがいた。', 'c', CRI + ' sleeping in a hammock, soft warm light'),
    (5, 'きょうだい4人は、いつも一緒だった。', 'l', KIDS + ', walking together along a village path, smiling' + ONLYKIDS),
    (6, '子どもたちの祖母は、森の知恵を、たくさん教えてくれた。', 's', 'an elderly Indigenous Huitoto grandmother showing a fruit to ' + LES + ' in the jungle'),
    (6, '食べられる木の実。飲める水。危ない虫や植物。', 'l', 'close-up of wild fruits, seeds and leaves on a wooden table in a village' + NOP),
    (6, '森の中で迷わないための、ちょっとしたこつ。', 'l', 'an elderly Indigenous woman and ' + LES + ' walking on a jungle path, the grandmother pointing at a tree'),
    (6, 'その知恵が、のちに、子どもたちの命を救うことになる。', 'c', 'sunlight through the jungle canopy onto a narrow path' + NOP),
    (6, 'レスリーは、祖母の話を、熱心に聞いていたという。', 'l', 'an elderly Indigenous grandmother telling a story to ' + LES + ' by a fire at night'),

    # ch3 5月1日のフライト
    (7, '2023年5月1日。', 's', 'early morning mist over a small Amazon town with a grass airstrip' + NOP),
    (7, '子どもたちと母親は、小さな飛行機に乗りこんだ。', 'l', 'an Indigenous mother helping ' + LES + ' and ' + SOL + ' climb into ' + PLANE + ' on a grass airstrip, ' + TIE + ' holding her hand'),
    (7, '出発地は、アマゾンの奥地、アララクアラ。目的地は、およそ350キロ離れた町、サンホセ・デル・グアビアレだった。', 'l', 'a map-like view of the Colombian Amazon with two towns connected by a dotted line, no readable text' + NOP),
    (7, '母親は、家族で新しい場所に移り住もうとしていたとされる。', 'c', 'an Indigenous mother looking out of a small airplane window, hopeful, children beside her'),
    (7, '家族にとって、この飛行機は、新しい生活への入り口になるはずだった。', 'l', PLANE + ' waiting on a grass airstrip under a blue sky' + NOP),
    (8, '飛行機は、6人乗りのセスナ206型機。', 's', PLANE + ' on a grass runway, propeller turning' + NOP),
    (8, '乗っていたのは、パイロットと、先住民の村の指導者、母親、そして4人の子どもたち。合わせて7人だった。', 'l', 'the inside of a small airplane cabin, seats close together, a mother holding a baby, children looking out the window, a pilot in front'),
    (8, '飛行機は、朝、エンジンの音を響かせて、緑の森の上へ飛び立った。', 'l', PLANE + ' taking off over the green Amazon jungle in the morning' + NOP),
    (8, '窓の外には、どこまでも続く、ジャングルが広がっていた。', 'c', 'view from a small airplane window over the endless green Amazon canopy' + NOP),
    (8, '小さな飛行機は、アマゾンの村と町をつなぐ、大切な足だった。', 'l', PLANE + ' flying low over a river in the Amazon' + NOP),
    (9, 'レスリーは、ひざの上で、赤ちゃんのクリスティンを抱いていたかもしれない。', 's', LES + ' holding ' + CRI + ' on her lap inside a small airplane, looking out the window'),
    (9, '弟のティエンは、窓に顔を押しつけて、外を見ていた。', 'l', TIE + ' pressing his face to a small airplane window, curious'),
    (9, 'あと1時間ほどで、目的地に着くはずだった。', 'c', PLANE + ' flying over rivers and jungle, white clouds' + NOP),
    (9, '飛行機の中には、赤ちゃんのミルクや、食べ物の袋も積まれていた。', 'l', 'bags, a baby bottle and a sack of cassava flour in the back of a small airplane cabin' + NOP),

    # ch4 墜落
    (10, '飛び立って、しばらくしたころ。', 's', PLANE + ' flying over the jungle, dark smoke beginning to trail from the engine' + NOP),
    (10, 'パイロットが、無線で叫んだ。「エンジンが止まった。緊急事態だ」', 'l', 'close-up of a pilot\'s hand gripping a radio microphone in a small cockpit, warning lights on'),
    (10, 'それが、飛行機からの、最後の通信になった。', 'l', 'a radar screen in a control room with a small blip disappearing, no readable text' + NOP),
    (10, '飛行機は、レーダーから姿を消した。', 'c', 'an empty sky over the endless Amazon jungle' + NOP),
    (10, '機体は、大きく揺れながら、高度を下げていった。', 'l', PLANE + ' tilting and losing altitude over the jungle' + NOP),
    (11, '機体は、高い木々の中へと落ちていった。', 's', PLANE + ' descending into tall jungle trees, leaves flying, seen from a distance' + NOP),
    (11, '機首から、深い森に突っこむようにして、止まった。', 'l', WRECK),
    (11, '機体は、木々にうもれるようにして、まっすぐ立った状態で止まっていたという。', 'l', WRECK + ', vines around it, mist'),
    (11, 'その衝撃は、すさまじいものだった。', 'c', 'leaves and branches falling slowly in the jungle after a crash, dust in light beams' + NOP),
    (11, '墜落した場所は、近くに村も道もない、深い森のまん中だった。', 'l', JUNGLE + ', seen from above, no roads, no villages' + NOP),
    (12, 'しかし、後ろの座席にいた子どもたちは、生きていた。', 's', 'close-up of ' + LES + '\'s eyes opening, dazed, dim light inside a small wrecked cabin'),
    (12, 'レスリーは、残骸の中で、赤ちゃんの小さな足を見つけた。', 'l', LES + ' reaching into a tangle of seats and branches inside a wrecked cabin, a tiny baby foot visible'),
    (12, 'そして、必死でクリスティンを引っぱり出した。', 'l', LES + ' pulling ' + CRI + ' out of the small airplane wreck, the baby crying, no injuries shown'),
    (12, '妹のソレイニも、弟のティエンも、無事だった。', 'c', SOL + ' and ' + TIE + ' standing next to ' + LES + ' holding ' + CRI + ' near the airplane wreck in the jungle, scared' + ONLYKIDS),
    (12, '4人は、奇跡的に、大きなけがをしていなかったとされる。', 'l', 'close-up of ' + SOL + ' hugging ' + TIE + ', both scared but unhurt, jungle behind' + ONLYKIDS),

    # ch5 母の言葉
    (13, '母親は、墜落のあとも、しばらく生きていたとされる。', 's', 'soft green light falling on the jungle floor near the airplane wreck, quiet and solemn' + NOP),
    (13, 'レスリーは、のちに、母親が4日ほど生きていたと話している。', 'l', 'close-up of ' + LES + ' sitting quietly with eyes lowered, holding ' + CRI + ', jungle behind'),
    (13, '大けがをした母親は、子どもたちに、こう伝えたという。', 'l', 'a mother\'s hand gently holding a girl\'s hand in soft light, close-up, no injuries shown'),
    (13, '「ここを離れなさい。あなたたちは、生きなさい」', 'c', 'a beam of soft light shining through the jungle canopy, sacred mood' + NOP),
    (13, 'それが、母親から子どもたちへの、最後の言葉になった。', 'c', 'close-up of a small wild flower in the jungle, a drop of rain on it' + NOP),
    (14, 'パイロットと、村の指導者は、墜落のときに亡くなっていた。', 's', 'the jungle around the airplane wreck in misty morning light, silent, no people visible'),
    (14, '13歳のレスリーは、残された3人の、母親がわりになった。', 'l', LES + ' holding ' + CRI + ' and taking ' + TIE + '\'s hand, ' + SOL + ' beside her, standing in the jungle' + ONLYKIDS),
    (14, '涙をこらえ、妹や弟を集めた。', 'l', 'close-up of ' + LES + ' wiping her tears, then looking up with determination'),
    (14, 'そして、飛行機のそばを離れることを決めた。', 'c', KIDS + ', walking away from the airplane wreck into the jungle, seen from behind' + ONLYKIDS),
    (14, '赤ちゃんを抱き、弟の手を引く。13歳の少女には、あまりにも重い役目だった。', 'l', LES + ' carrying ' + CRI + ' on her back with a cloth sling, holding ' + TIE + '\'s hand' + ONLYKIDS),
    (15, '機内には、フアリーニャと呼ばれる、イモの粉が残っていた。', 's', 'a bag of coarse yellow cassava flour (fariña) on the ground in the jungle' + NOP),
    (15, 'アマゾンの人々が、ふだんから食べている保存食だ。', 'l', 'close-up of yellow cassava flour in a small hand' + NOP),
    (15, 'レスリーは、それを持てるだけ持って、歩き出した。', 'l', LES + ' carrying a small bag and ' + CRI + ', leading her siblings along a jungle path' + ONLYKIDS),
    (15, '4人だけの、長い旅が始まった。', 'c', 'four small children walking among giant tree roots in the Amazon, tiny compared to the trees' + ONLYKIDS),
    (15, '飛行機に積まれていた、ほかの荷物も、役に立った。', 'l', 'a small bag with clothes, a towel and scissors on the jungle floor' + NOP),
    (15, 'レスリーは、どちらへ行けばいいのか、迷いながらも、前へ進んだ。', 'l', LES + ' looking in different directions in the jungle, unsure, ' + CRI + ' in her arms' + ONLYKIDS),

    # ch6 密林を歩く
    (16, '密林の中は、昼間でも薄暗い。', 's', JUNGLE + ', dim even at midday, light filtering through leaves' + NOP),
    (16, '高い木の葉が、空をすっかりおおっているからだ。', 'l', 'looking straight up at a dense jungle canopy blocking the sky' + NOP),
    (16, '足元には、木の根や、倒れた木が、どこまでも続いていた。', 'l', 'tangled tree roots and fallen logs covering the jungle floor' + NOP),
    (16, 'レスリーは、赤ちゃんを抱いたまま、木の根を乗り越えた。', 'c', LES + ' climbing over a huge tree root while holding ' + CRI + ', ' + SOL + ' helping ' + TIE + ' behind her' + ONLYKIDS),
    (16, '遠くで鳴く鳥や、サルの声が、森に響いた。', 'l', 'colorful birds and a monkey in the jungle canopy' + NOP),
    (16, '4歳のティエンは、すぐに疲れて、歩けなくなった。', 'l', TIE + ' sitting down tired on a jungle root, ' + SOL + ' kneeling beside him' + ONLYKIDS),
    (16, 'そのたびに、姉たちが、手を引いた。', 'c', SOL + ' pulling ' + TIE + ' up by the hand on a jungle path' + ONLYKIDS),
    (17, 'のどが渇けば、小川の水を飲んだ。', 's', KIDS + ', drinking from a small clear jungle stream with cupped hands' + ONLYKIDS),
    (17, 'おなかがすけば、少しずつイモの粉を分け合った。', 'l', LES + ' sharing cassava flour into the hands of ' + SOL + ' and ' + TIE + ', sitting on a log' + ONLYKIDS),
    (17, '赤ちゃんには、粉を水でといて、飲ませたという。', 'l', LES + ' feeding ' + CRI + ' with a small cup, gently' + ONLYKIDS),
    (17, 'レスリーは、イモの粉を一度に食べず、何日ももつように、少しずつ分けたという。', 'l', LES + ' carefully dividing cassava flour into small portions on a leaf' + ONLYKIDS),
    (17, '5月のアマゾンは、木の実がたくさん実る季節でもあった。', 'c', 'a jungle tree full of ripe wild fruits, sunlight' + NOP),
    (17, '妹のソレイニも、姉を助けて、赤ちゃんの面倒を見た。', 'l', SOL + ' holding ' + CRI + ' while ' + LES + ' gathers fruit' + ONLYKIDS),
    (17, '小川の水は冷たく、子どもたちの足を何度も冷やした。', 'l', KIDS + ', crossing a small jungle stream barefoot' + ONLYKIDS),
    (18, '日が暮れると、森は真っ暗になる。', 's', NIGHT + NOP),
    (18, 'レスリーは、枝や葉っぱを集めて、小さな小屋を作った。', 'l', LES + ' building a small shelter of sticks and big leaves in the jungle at dusk' + ONLYKIDS),
    (18, '4人は、その中で体を寄せ合って眠った。', 'l', KIDS + ', sleeping huddled together inside a small leaf shelter at night' + ONLYKIDS),
    (18, '夜の森には、虫の声と、遠くの動物の鳴き声が響いていた。', 'c', NIGHT + ', glowing eyes of an animal far away' + NOP),
    (18, 'レスリーは、タオルや布を使って、赤ちゃんを寒さから守った。', 'l', LES + ' wrapping ' + CRI + ' in a towel at night in a leaf shelter' + ONLYKIDS),

    # ch7 希望作戦
    (19, 'そのころ、飛行機が消えたという知らせは、コロンビア中に広がっていた。', 's', 'Colombian television news in a home, a reporter in front of a jungle map, no readable text'),
    (19, '軍は、すぐに捜索を始めた。', 'l', 'Colombian army helicopters flying low over the Amazon jungle' + NOP),
    (19, '作戦の名前は、「オペラシオン・エスペランサ」。日本語で「希望作戦」である。', 'l', 'Colombian soldiers in camouflage gathering at a jungle camp with backpacks and dogs'),
    (19, '100人を超える兵士と、捜索犬が、密林に入った。', 'c', 'a line of Colombian soldiers with search dogs walking into dense jungle'),
    (19, 'ヘリコプターが、森の上を、何度も飛び回った。', 'l', 'military helicopters circling over the Amazon canopy' + NOP),
    (19, '墜落した飛行機の位置は、なかなかわからなかった。', 'l', 'soldiers looking at a GPS device and a map in the jungle, no readable text'),
    (20, '捜索には、先住民の人たちも加わった。', 's', 'Indigenous trackers with machetes walking with soldiers in the jungle'),
    (20, '森を知り尽くした彼らは、兵士には見えない、小さな手がかりを読みとることができた。', 'l', 'an Indigenous tracker kneeling and studying a broken twig on the jungle floor'),
    (20, 'ふだんは、決して仲がいいとはいえない、軍と先住民。', 'l', 'a soldier and an Indigenous tracker standing apart, cautious, in the jungle'),
    (20, 'しかし、子どもたちを救うという思いは、同じだった。', 'c', 'a soldier and an Indigenous tracker shaking hands in the jungle, determined'),
    (20, '先住民の捜索隊は、自分たちの村から、何日もかけて歩いてきた人も多かった。', 'l', 'Indigenous volunteers arriving at a jungle camp with backpacks and machetes'),
    (21, '墜落から、およそ2週間後。', 's', 'soldiers pushing through thick jungle vegetation' + NOP),
    (21, '捜索隊は、ついに機体を見つけた。', 'l', WRECK + ', soldiers discovering it from a distance among the trees'),
    (21, 'しかし、そこに、子どもたちの姿はなかった。', 'l', 'the empty jungle around the airplane wreck, a soldier looking around in surprise'),
    (21, '子どもたちは、生きて、どこかへ歩いていったのだ。', 'c', 'small footprints in the mud leading away into the jungle' + NOP),
    (21, '機体の中には、大人3人がいた。しかし、子どもたちの姿は、どこにもなかった。', 'l', 'soldiers standing quietly near the airplane wreck in the jungle, heads bowed, no bodies visible'),
    (21, '捜索の目的は、子どもたちを見つけることに変わった。', 'c', 'soldiers and Indigenous trackers spreading out into the jungle in a line'),

    # ch8 残された手がかり
    (22, '捜索犬が、森の中で、赤ちゃんのほ乳びんを見つけた。', 's', 'a search dog sniffing a small baby bottle lying among jungle leaves' + NOP),
    (22, 'さらに、食べかけの果物や、はさみ、髪をしばるゴムも見つかった。', 'l', 'a half-eaten fruit, small scissors and a hair tie on jungle leaves' + NOP),
    (22, '枝を組んで作った、小さな小屋も見つかった。', 'l', 'an abandoned small shelter of sticks and leaves in the jungle' + NOP),
    (22, '子どもたちが、たしかに生きている証拠だった。', 'c', 'a soldier holding a tiny child\'s shoe in the jungle, hopeful face'),
    (22, '小屋の中には、赤ちゃんのおむつも残されていた。', 'l', 'inside an abandoned leaf shelter, a folded baby diaper and leaves' + NOP),
    (22, '見つかった品物は、一つひとつ、子どもたちの足どりを示す地図になっていった。', 'l', 'a soldier marking small objects on a hand-drawn map in a jungle camp, no readable text'),
    (23, '泥の上には、小さな足あとも残っていた。', 's', 'small children\'s footprints in jungle mud' + NOP),
    (23, '捜索隊は、足あとを追った。', 'l', 'soldiers and Indigenous trackers following footprints through the jungle'),
    (23, 'しかし、雨が降るたびに、足あとは消えてしまう。', 'l', 'heavy rain washing away footprints in the jungle mud' + NOP),
    (23, '密林は、あまりにも広く、深かった。', 'c', JUNGLE + ', seen from above, a tiny helicopter over the endless canopy' + NOP),
    (23, '捜索隊は、ジャングルに縦横の線を引き、1メートルずつ、しらみつぶしに歩いた。', 'l', 'soldiers walking side by side in a long line through the jungle, searching carefully'),
    (23, '森の中で迷わないよう、捜索隊は、木に目印のテープを巻きながら進んだ。', 'l', 'bright tape tied around a jungle tree as a trail marker' + NOP),
    (24, '一度は、「子どもたちが見つかった」というニュースが流れた。', 's', 'people looking at their phones with hope, a news alert glowing, no readable text'),
    (24, 'しかし、それは誤りだった。', 'l', 'a person lowering their phone with disappointment, no readable text'),
    (24, '国中が、喜びから、再び不安へと突き落とされた。', 'l', 'a family watching television news anxiously at night, no readable text'),
    (24, 'それでも、捜索隊は、あきらめなかった。', 'c', 'soldiers and Indigenous trackers continuing into the jungle in the rain'),
    (24, '捜索の期間は、軍のこれまでの記録を大きく超えていった。', 'l', 'a jungle base camp with tents and helicopters, soldiers working day and night'),

    # ch9 空から届く祖母の声
    (25, '捜索隊は、ある方法を考えた。', 's', 'a Colombian air force helicopter with a large loudspeaker mounted on it' + NOP),
    (25, 'ヘリコプターから、大きなスピーカーで、子どもたちの祖母の声を流したのだ。', 'l', 'a helicopter flying low over the jungle canopy, sound waves drawn in the air' + NOP),
    (25, 'フイト族の言葉で、祖母は呼びかけた。「その場から動かないで。みんなが探しているよ」', 'l', 'an elderly Indigenous grandmother speaking into a microphone in a small room, tears in her eyes'),
    (25, 'その声は、森の上を、何度も、何度も響いた。', 'c', 'the jungle canopy with a helicopter far above, mist rising' + NOP),
    (25, '祖母の声は、子どもたちが知っている、なつかしい声だった。', 'l', 'close-up of an elderly Indigenous grandmother\'s gentle face, eyes full of hope'),
    (25, 'ヘリコプターの音は、森の中では、どこから聞こえるのかもわからないほど、反響していた。', 'l', 'sound echoing in a misty jungle, a helicopter shadow on the canopy' + NOP),
    (26, '空からは、1万枚のビラもまかれた。', 's', 'thousands of paper leaflets falling from a plane over the jungle, no readable text' + NOP),
    (26, 'スペイン語とフイト族の言葉で、生きのびるための方法が書かれていた。', 'l', 'a leaflet caught on a jungle leaf, the writing blurred and unreadable' + NOP),
    (26, '食べ物の入った箱や、水も、森の中に投下された。', 'l', 'small boxes with parachutes dropping into the jungle' + NOP),
    (26, '捜索隊は、木に笛をつるし、子どもたちが見つけて吹けるようにした。', 'c', 'a whistle hanging on a string from a jungle tree branch' + NOP),
    (26, 'ビラには、川の近くにいること、移動しないことなどが書かれていたという。', 'l', 'a child\'s hand picking up a leaflet from the jungle floor, writing blurred and unreadable'),
    (27, '子どもたちに、祖母の声は届いていたのだろうか。', 's', KIDS + ', looking up at the jungle canopy, listening' + ONLYKIDS),
    (27, 'のちにわかったことだが、子どもたちは、ヘリコプターの音や声を怖がり、隠れていたこともあったという。', 'l', KIDS + ', hiding under big leaves, frightened, a helicopter sound in the air' + ONLYKIDS),
    (27, 'まさか自分たちを助けに来ているとは、思わなかったのかもしれない。', 'c', 'close-up of ' + TIE + ' hiding behind ' + LES + ', scared eyes'),
    (27, '森の中では、知らない大人もまた、危険な存在かもしれなかったからだ。', 'c', 'shadowy figures of armed men far away in the jungle, blurred' + NOP),

    # ch10 雨と飢え
    (28, 'アマゾンは、雨の多い森だ。', 's', 'heavy tropical rain pouring through the Amazon jungle' + NOP),
    (28, '激しい雨が、毎日のように降り続いた。', 'l', KIDS + ', sheltering from heavy rain under huge leaves' + ONLYKIDS),
    (28, '子どもたちは、ずぶぬれになりながら、身を寄せ合った。', 'l', KIDS + ', soaked, huddled together under a leaf shelter' + ONLYKIDS),
    (28, '雨水は、飲み水にもなった。', 'c', LES + ' collecting rainwater in a big leaf for ' + TIE + ONLYKIDS),
    (28, '雨は、足あとを消し、捜索をさらに難しくした。', 'l', 'muddy jungle ground after heavy rain, footprints washed away' + NOP),
    (28, 'ぬれた服は乾かず、夜は寒さに震えた。', 'l', KIDS + ', shivering in wet clothes inside a leaf shelter at night' + ONLYKIDS),
    (29, 'イモの粉は、やがて、なくなった。', 's', 'an empty bag on the jungle floor' + NOP),
    (29, 'レスリーは、森の中で、食べられる木の実や、種を探した。', 'l', LES + ' picking wild fruits from a low jungle tree, ' + SOL + ' helping' + ONLYKIDS),
    (29, '祖母に教わった知識で、毒のある実と、食べられる実を見分けた。', 'l', 'close-up of ' + LES + '\'s hands sorting wild fruits and seeds on a leaf'),
    (29, 'それでも、子どもたちの体は、日に日にやせていった。', 'c', KIDS + ', very thin and tired, sitting on a log in the jungle' + ONLYKIDS),
    (29, '姉たちは、自分の分を減らしてでも、弟と赤ちゃんに食べさせたという。', 'l', LES + ' giving her fruit to ' + TIE + ', smiling softly, hungry herself' + ONLYKIDS),
    (29, 'レスリーは、大人でも見分けるのが難しい、森の実の種類を知っていた。', 'l', 'close-up of various wild jungle fruits and seeds on big leaves' + NOP),
    (30, '危険な生き物も、すぐそばにいた。', 's', 'a venomous snake coiled on a jungle branch' + NOP),
    (30, '夜になると、レスリーは、弟や妹を守るように、入り口のそばで眠ったという。', 'l', LES + ' lying at the entrance of a leaf shelter at night, protecting her siblings sleeping inside' + ONLYKIDS),
    (30, '赤ちゃんのクリスティンは、5月の終わりに、1歳の誕生日を迎えた。', 'l', LES + ' gently holding ' + CRI + ' in the jungle, a soft beam of light on them' + ONLYKIDS),
    (30, '誰にも祝われることのない、森の中の誕生日だった。', 'c', 'a small wild flower placed on a leaf in the jungle, soft light' + NOP),
    (30, 'ヘビや、毒のある虫に、子どもたちが襲われることは、なかった。', 'l', 'a small jungle frog on a leaf, peaceful, misty light' + NOP),

    # ch11 すれ違い
    (31, '捜索は、1か月を超えた。', 's', 'tired soldiers resting in a jungle camp at dusk'),
    (31, '捜索隊は、子どもたちのすぐ近くまで、何度も迫っていた。', 'l', 'soldiers walking through the jungle, and only a few trees away, children hiding behind leaves'),
    (31, 'ある時は、わずか数十メートルの距離まで近づいていたこともあったという。', 'l', 'a soldier\'s boot on a jungle path, a child\'s small sandal nearby in the leaves' + NOP),
    (31, 'しかし、深い森の中では、すぐ近くにいても、姿が見えない。', 'c', 'a wall of dense green jungle vegetation, impossible to see through' + NOP),
    (31, '捜索隊は、大声で子どもたちの名前を呼び続けた。', 'l', 'a soldier cupping his hands and shouting into the jungle'),
    (31, 'ジャングルの中で、子どもたちは、移動を続けていたとみられている。', 'l', KIDS + ', walking slowly in a different part of the jungle' + ONLYKIDS),
    (32, '捜索隊の中にも、疲れと、あきらめの空気が広がり始めた。', 's', 'exhausted soldiers sitting in the rain in the jungle, heads down'),
    (32, 'それでも、先住民の捜索隊は、森の精霊に祈りながら、探し続けた。', 'l', 'Indigenous searchers performing a quiet ritual with smoke in the jungle at night, faces lit by a small fire'),
    (32, '「子どもたちは、生きている」。彼らは、そう信じていた。', 'l', 'close-up of an Indigenous elder\'s determined face in the jungle'),
    (32, '捜索の範囲は、少しずつしぼりこまれていった。', 'c', 'a map on a table in a jungle camp with a circled area, no readable text' + NOP),
    (32, 'ある先住民の男性は、森の中で、儀式のための飲み物を口にし、子どもたちの居場所を感じとろうとしたという。', 'l', 'an Indigenous elder sitting cross-legged in the jungle at night, eyes closed, meditating by a small fire'),
    (33, '墜落から1か月。子どもたちは、まだ森の中にいた。', 's', KIDS + ', walking slowly through the jungle, weak' + ONLYKIDS),
    (33, 'レスリーは、弟や妹を励まし続けた。', 'l', LES + ' kneeling and talking softly to ' + TIE + ', encouraging him' + ONLYKIDS),
    (33, '自分が、あきらめるわけにはいかない。', 'c', 'close-up of ' + LES + '\'s tired but determined face' + ONLYKIDS),
    (33, '赤ちゃんも、弱っていた。泣く声も、だんだん小さくなっていった。', 'l', LES + ' holding ' + CRI + ' close, worried face' + ONLYKIDS),
    (33, 'それでも4人は、一緒にいることをやめなかった。', 'c', KIDS + ', sitting close together under a giant tree' + ONLYKIDS),

    # ch12 犬のウィルソン
    (34, '捜索隊には、1匹の犬がいた。', 's', 'a Belgian Malinois search dog with a vest standing in the jungle' + NOP),
    (34, '軍の特殊部隊の捜索犬、ウィルソン。ベルジアン・シェパードという種類の犬だった。', 'l', 'close-up of a Belgian Malinois search dog with alert ears in the jungle' + NOP),
    (34, 'ある日、ウィルソンは、捜索隊からはぐれて、森の奥へ姿を消した。', 'l', 'a Belgian Malinois dog running alone into the deep jungle' + NOP),
    (34, '捜索隊は、ウィルソンも探したが、見つけることはできなかった。', 'c', 'soldiers calling into the jungle, looking for a lost dog'),
    (34, 'ウィルソンは、子どもたちのにおいを追って、森の奥へ入っていったのかもしれない。', 'l', 'a Belgian Malinois dog sniffing the jungle floor, following a trail' + NOP),
    (35, 'のちに、子どもたちは、こう話したという。', 's', KIDS + ', sitting together in the jungle' + ONLYKIDS),
    (35, '森の中で、1匹の犬が、自分たちのそばにいたと。', 'l', 'a Belgian Malinois dog sitting near ' + KIDS + ' in the jungle, protective' + ONLYKIDS),
    (35, 'その犬が、ウィルソンだったのかどうかは、わかっていない。', 'l', 'a Belgian Malinois dog standing guard at night near a leaf shelter in the jungle' + NOP),
    (35, 'しかし、多くの人が、ウィルソンが子どもたちを見守っていたのだと信じている。', 'c', 'a Belgian Malinois dog looking back over its shoulder in a beam of jungle light' + NOP),
    (35, 'もしそうなら、ウィルソンは、子どもたちと一緒に、夜の森を過ごしたことになる。', 'l', 'a Belgian Malinois dog lying beside a leaf shelter at night, fireflies' + NOP),
    (36, 'ウィルソンのいた場所の近くで、捜索隊は、新しい足あとを見つけた。', 's', 'fresh small footprints and dog paw prints in jungle mud' + NOP),
    (36, '子どもたちは、近い。', 'l', 'soldiers and Indigenous trackers moving fast through the jungle, excited'),
    (36, '捜索隊の足どりは、自然と速くなっていった。', 'c', 'Indigenous trackers leading the way through dense jungle, focused'),
    (36, 'それは、子どもたちが、まだ動いている証拠だった。', 'l', 'fresh broken branches and footprints along a jungle path' + NOP),

    # ch13 40日目
    (37, '2023年6月9日。墜落から、40日目。', 's', JUNGLE + ', morning mist, sunbeams' + NOP),
    (37, '先住民の捜索隊が、森の中で、何かの気配に気づいた。', 'l', 'an Indigenous tracker stopping and listening intently in the jungle'),
    (37, '木々の間に、小さな人影が見えた。', 'l', 'between jungle trees, the small silhouettes of children in the distance' + NOP),
    (37, '墜落現場から、およそ5キロ離れた場所だった。', 'c', 'a small clearing in the dense jungle with a leaf shelter' + NOP),
    (37, '先住民の男たちは、静かに、ゆっくりと近づいた。', 'l', 'Indigenous trackers moving carefully between jungle trees, gentle expressions'),
    (37, 'レスリーは、近づいてくる人影に気づき、赤ちゃんを強く抱きしめた。', 'l', LES + ' clutching ' + CRI + ' tightly, looking toward approaching figures in the jungle' + ONLYKIDS),
    (38, 'そこにいたのは、4人の子どもたちだった。', 's', KIDS + ', in a small jungle clearing, very thin, looking up' + ONLYKIDS),
    (38, 'やせ細り、体じゅうに虫刺されのあとがあった。', 'l', 'close-up of ' + SOL + ' and ' + TIE + ', thin and tired, sitting on leaves' + ONLYKIDS),
    (38, 'それでも、4人とも、生きていた。', 'l', LES + ' holding ' + CRI + ' and looking at the rescuers with tired eyes' + ONLYKIDS),
    (38, '捜索隊の男は、思わず、子どもたちを抱きしめた。', 'c', 'an Indigenous tracker gently hugging ' + TIE + ' in the jungle, tears'),
    (38, '赤ちゃんのクリスティンも、姉の腕の中で、しっかりと生きていた。', 'l', 'close-up of ' + CRI + ' in ' + LES + '\'s arms, eyes open' + ONLYKIDS),
    (39, '知らせは、無線で、すぐに伝えられた。', 's', 'a soldier speaking into a radio in the jungle, excited face'),
    (39, '合言葉は、「ミラグロ」。スペイン語で「奇跡」という意味だった。', 'l', 'close-up of a radio in a soldier\'s hand in the jungle' + NOP),
    (39, '「ミラグロ、ミラグロ、ミラグロ、ミラグロ」。4回の「奇跡」は、4人全員が生きているという意味だった。', 'c', 'soldiers and Indigenous trackers cheering together in the jungle'),
    (39, '森の中で、兵士たちと先住民たちは、抱き合って喜んだ。', 'l', 'soldiers and Indigenous searchers hugging each other in the jungle, tears of joy'),

    # ch14 「おなかがすいた」
    (40, '見つかったとき、レスリーは、捜索隊にこう言ったという。', 's', LES + ' holding ' + CRI + ', speaking weakly to a kneeling rescuer'),
    (40, '「おなかがすいた」', 'l', 'close-up of ' + LES + '\'s thin face, tired eyes' + ONLYKIDS),
    (40, 'そして、弟は、こう言った。「お母さんは、死んじゃった」', 'l', 'close-up of ' + TIE + '\'s sad face, a rescuer\'s gentle hand on his shoulder'),
    (40, 'その言葉に、捜索隊の誰もが、言葉を失った。', 'c', 'rescuers standing silently around the children in the jungle, heads bowed'),
    (40, '4人は、手当てを受け、水や食べ物を少しずつ与えられた。', 'l', 'Indigenous trackers giving water to the four children in the jungle, gently'),
    (40, '母親の言葉を守り、4人は、生きて帰ってきたのだ。', 'c', KIDS + ', wrapped in blankets, in a beam of soft light in the jungle' + ONLYKIDS),
    (41, '子どもたちは、毛布にくるまれ、ヘリコプターでつり上げられた。', 's', 'a child wrapped in a blanket being lifted by a helicopter hoist above the jungle canopy'),
    (41, '密林には、ヘリコプターが着陸できる場所がなかったからだ。', 'l', 'a helicopter hovering above the dense jungle canopy with a rescue cable' + NOP),
    (41, '4人は、病院へと運ばれた。', 'l', 'a military helicopter flying over the Amazon toward a town' + NOP),
    (41, '赤ちゃんを抱いて、40日間、森を歩き続けた13歳の姉は、ようやく、子どもに戻ることができた。', 'c', LES + ' resting in a hospital bed, finally at peace, soft light'),
    (41, '待っていた人々から、大きな拍手がわき起こった。', 'l', 'soldiers and medical staff clapping at a jungle airstrip as a helicopter lands'),
    (42, '首都ボゴタの病院では、子どもたちの家族が待っていた。', 's', 'family members waiting anxiously in a hospital corridor in Bogotá'),
    (42, '祖父は、4人の顔を見て、涙を流した。', 'l', 'an elderly Indigenous man crying with relief in a hospital room'),
    (42, '大統領も病院を訪れ、子どもたちの生還を喜んだ。', 'c', 'officials visiting a hospital room with children in beds, soft light, faces not detailed'),
    (42, '子どもたちの写真は、世界中に配信され、多くの人が涙を流した。', 'c', 'people around the world reading news on phones and newspapers, emotional, no readable text'),

    # ch15 なぜ生き延びたのか
    (43, '子どもたちは、なぜ、40日間も生き延びることができたのか。', 's', 'a beam of sunlight in the deep Amazon jungle' + NOP),
    (43, '1つ目は、祖母から教わった、森の知恵。食べられる実を見分け、雨水を飲み、森の中で眠る方法を知っていた。', 'l', 'an elderly Indigenous grandmother teaching ' + LES + ' about jungle fruits'),
    (43, '2つ目は、13歳のレスリーの、強さと責任感。最後まで、妹や弟を見捨てなかった。', 'l', LES + ' holding ' + CRI + ' and leading her siblings through the jungle' + ONLYKIDS),
    (43, 'そして3つ目は、軍と先住民が力を合わせた、あきらめない捜索だった。', 'l', 'soldiers and Indigenous trackers walking together in the jungle'),
    (43, 'どれか1つでも欠けていれば、4人そろっての生還は、なかったかもしれない。', 'c', 'the Amazon jungle at golden hour, peaceful' + NOP),
    (44, '専門家は、もし子どもたちが森を知らない都会の子だったら、生き延びるのは難しかっただろうと話している。', 's', 'a dense jungle with no paths, dangerous' + NOP),
    (44, '森とともに生きてきた人々の知恵が、4つの命を守ったのである。', 'l', 'an Indigenous village by a river at sunset, peaceful' + NOP),
    (44, 'そして、母親が最後に残した言葉が、子どもたちを前へと進ませた。', 'c', 'a soft beam of light through the jungle canopy, sacred mood' + NOP),
    (44, '密林の中で、彼らは、決してばらばらにならなかった。', 'l', KIDS + ', holding hands in a line in the jungle' + ONLYKIDS),

    # ch16 その後
    (45, '子どもたちは、およそ1か月、病院で治療を受けた。', 's', KIDS + ', in a hospital room, drawing pictures with crayons, recovering' + ONLYKIDS),
    (45, 'はじめは、固い食べ物を食べることもできなかった。', 'l', 'a nurse helping ' + TIE + ' drink from a cup in a hospital bed'),
    (45, 'しかし、少しずつ元気を取り戻し、絵を描いたり、笑ったりするようになった。', 'l', SOL + ' smiling and drawing a picture of trees in a hospital room'),
    (45, '一方、行方がわからなくなった犬のウィルソンは、その後も見つからなかった。', 's', 'a Belgian Malinois dog standing alone in the misty jungle, seen from afar' + NOP),
    (45, '多くの兵士や先住民が、ウィルソンを探し続けたが、捜索は、やがて打ち切られた。', 'l', 'soldiers standing at the edge of the jungle at sunset, looking into the trees'),
    (45, 'ウィルソンを探す作戦は、その後も、しばらく続けられた。', 'l', 'soldiers with search dogs walking into the jungle looking for a lost dog'),
    (45, 'ボゴタの病院には、全国から、子どもたちへの手紙や贈り物が届いたという。', 'l', 'a pile of colorful letters and toys in a hospital room, no readable text' + NOP),
    (46, 'この出来事は、のちにドキュメンタリーにもなり、世界中で知られることになった。', 's', 'people in a dark room watching a documentary about the jungle on a screen, silhouettes, no readable text'),
    (46, 'アマゾンの森で、大人のいない40日間を生き抜いた、4人の子どもたち。', 'l', KIDS + ', standing together in a beam of jungle light, hopeful' + ONLYKIDS),
    (46, 'それは、森の知恵と、きょうだいの絆、そして、多くの人の願いが生んだ奇跡だった。', 'c', 'the Amazon rainforest at sunrise, mist and golden light' + NOP),
    (46, 'コロンビアの人々は、この出来事を、今も「奇跡」として語り継いでいる。', 'l', 'a mural of four children and a dog in a Colombian town, colorful, no readable text' + NOP),
    (46, 'このチャンネルでは、実際に起きた極限のサバイバルを記録している。', 's', 'a dark archive room with shelves of case files, one file open under a single desk lamp'),
    (46, '次の記録を見逃さないよう、チャンネル登録をお願いしたい。', 'x', 'the case file closing, the desk lamp switching off, darkness'),
]

# ---- パイプライン用の設定 ----
SCENE = "the 2023 Colombian Amazon plane crash where four Indigenous children survived 40 days"
STYLE = ("Japanese gekiga manga illustration style (hand-drawn comic art, NOT photorealistic), bold black ink linework with cross-hatching, "
         "painted full colors, lush deep greens of the Amazon rainforest, humid misty light, "
         "ONE single full-frame illustration showing one continuous scene (absolutely NO comic panels, "
         "NO split screen, NO inset frames, NO borders), dramatic cinematic lighting, serious but gentle documentary mood, "
         "children drawn respectfully and age-appropriately, no blood, no wounds, no injuries, no corpses, no speech bubbles, no text, no letters, no captions, no logos")
TTS_SPEED = 0.95
TTS_SPEAKER = 11  # 玄野武宏
TTS_INTONATION = 1.1
READINGS = {"先住民": "せんじゅうみん", "精霊": "せいれい", "合言葉": "あいことば", "絆": "きずな", "姉": "あね", "虫刺され": "むしさされ"}
STAMPS = {}
for _c, _t, _p, _i in LINES:
    for _k, _v in [("2023年6月9日。南米", "2023年6月9日"), ("2023年5月1日", "5月1日"), ("墜落から、およそ2週間", "2週間後"),
                   ("捜索は、1か月を超えた", "1か月後"), ("2023年6月9日。墜落から", "40日目")]:
        if _t.startswith(_k):
            STAMPS[_t] = _v
THUMB = {"image": 3, "big": "40日", "red": "生還", "top": "アマゾンに墜落、子ども4人だけで", "sub": "13歳の姉が守り抜いた命"}
SHORT = {"sel": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
         "stamp": {"1": "2023年6月9日"},
         "h1": "【実話】アマゾンで子ども4人", "h2": "大人のいない40日間", "e1": "13歳の姉がしたこと――", "e2": "▶ 続きは本編で\n画面下の「関連動画」から見られます",
         "title": "【実話】小型機がアマゾンに墜落…子ども4人だけで40日、密林を生き延びた【2023年 コロンビア小型機アマゾン墜落事故】 #shorts",
         "desc": "2023年、南米コロンビアのアマゾン。小型機の墜落から40日後、密林の中で4人の子どもたちが見つかった――。\n#実話 #アマゾン #40日 #サバイバル #コロンビア #shorts"}
META = {"title": "【実話】密林に墜落、13歳の姉は妹弟3人を守り抜いた…子ども4人だけの40日間【2023年 コロンビア小型機アマゾン墜落事故】",
        "description": ("2023年5月1日、南米コロンビアのアマゾン上空で、7人を乗せた小型機セスナ206が墜落した。"
                        "生き残ったのは、先住民フイト族の4人の子どもたち。13歳のレスリーは、11か月の赤ちゃんを抱き、9歳の妹、4歳の弟を連れて密林を歩き続けた。"
                        "軍と先住民による「希望作戦」、空から流された祖母の声、行方不明になった捜索犬ウィルソン――。"
                        "40日後の奇跡の発見までを、約20分で記録する。\n\n"
                        "▼チャプター\n{CHAPTERS}\n\n"
                        "※映像はすべて実話をもとにした再現イラストです。実在の人物の外見とは異なります。\n"
                        "※出来事の詳細には諸説あります。本動画は報道・資料をもとに構成しています。\n\n"
                        "▼前回：{PREV}\n\n"
                        "▼参考資料\n・各種報道（2023年5〜6月）\n\n"
                        "ナレーション：VOICEVOX:玄野武宏\n\n"
                        "クライシス・ファイル〜極限サバイバル劇画〜\n実際に起きた極限のサバイバルを、劇画で記録するチャンネルです。\n"
                        "チャンネル登録：https://www.youtube.com/@CrisisFiles_Survival\n\n"
                        "#実話 #アマゾン #40日 #サバイバル #コロンビア #墜落事故 #クライシスファイル"),
        "tags": ["コロンビア", "アマゾン", "墜落事故", "子ども", "40日", "レスリー", "ウィルソン", "希望作戦", "サバイバル", "実話", "生還", "クライシスファイル"]}
