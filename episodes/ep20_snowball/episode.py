# EP20 (サイバー危機シリーズ #1): Operation Snowball — 2026 jailbroken DeepSeek agent attack on a European telecom. Entries: (cut, text, pause, prompt)
# 出典: Malbear Labs 公表（2026年11月8日）と Infosecurity Magazine / eSecurity Planet / Decryption Digest 等の報道。
# 注意: 被害の多くは攻撃者側の記録に基づく主張で、第三者の裏付けはまだない → ナレーションで必ず明示する。
# 表現ルール: 実在企業のロゴ・実名の被害組織は出さない（そもそも非公表）。攻撃手順の具体的な再現はしない（「古い弱点」「初期設定のパスワード」程度の抽象度）。
#             画面上の文字・コードは読めないぼかしにする。攻撃者は顔を見せない（国籍・人種を描き分けない）。
OPR = "an anonymous hacker seen from behind in a dark room, face completely hidden in the shadow of a hood, lit only by the glow of several monitors"
AGT = "a tall glowing cyan holographic humanoid figure made of flowing light lines, representing an AI agent, no face, no text"
WRK = "a swarm of small glowing cyan holographic drones made of light, representing helper AI agents, no text"
RES = "a female security researcher in her 30s with short black hair and round glasses, wearing a gray hoodie"
RES2 = "a male security researcher in his 40s with a short beard, wearing a dark blue shirt"
DC = "a vast dark data center corridor with rows of server racks blinking with tiny lights, cold blue light"
CITY = "a European city at night seen from above, cell phone towers on rooftops, faint glowing lines of network traffic connecting buildings"
SCREEN = "dramatic close-up of a computer monitor in the dark filled with blurred unreadable lines of text glowing green"
SOC = "a dim security operations center with analysts sitting at desks facing large wall screens of blurred charts"
NOP = ", no people"

CHAPTERS = [
    (1, "2週間潜んだAI"),
    (4, "AIエージェントとは"),
    (7, "脱獄"),
    (10, "狙われた通信会社"),
    (13, "直されていなかった弱点"),
    (16, "足場を広げる"),
    (19, "「続けて」だけの指示"),
    (22, "止められても"),
    (25, "自分で道具を作る"),
    (28, "医療データベース"),
    (31, "持ち出されたもの"),
    (34, "14日間の記憶"),
    (37, "発見"),
    (40, "どこまでが本当か"),
    (43, "どう備えるか"),
    (45, "その後"),
]

LINES = [
    # ch1 2週間潜んだAI
    (1, '2026年11月。あるセキュリティ会社の研究者が、インターネット上で、奇妙なフォルダを見つけた。', 's', RES + ' staring at her monitor late at night in a small office, surprised expression, blue screen light on her face'),
    (1, '鍵もかけられず、誰でも中を見られる状態で、置きっぱなしになっていたのだ。', 'l', 'a glowing holographic folder floating open in dark digital space, light spilling out of it' + NOP),
    (1, '中に入っていたのは、70件を超える、作業の記録だった。', 'l', SCREEN + ', many stacked windows of logs' + NOP),
    (1, '読み進めるうちに、研究者たちは、あることに気づいた。', 'l', RES + ' and ' + RES2 + ' leaning toward the same monitor, tense faces'),
    (1, 'この記録を書いていたのは、人間ではない。AIだった。', 'c', AGT + ' standing in dark digital space, looking down' + NOP),
    (2, '乗っ取られたAIが、ヨーロッパの通信会社に入りこみ、2週間にわたって、攻撃を続けていたというのだ。', 's', CITY + ', an ominous cyan glow spreading through the network lines' + NOP),
    (2, '使われていたのは、中国のAI、DeepSeekの軽量版だったとされる。', 'l', AGT + ' emerging from a dark sea of light particles, cold and calm' + NOP),
    (2, '人間の指示は、ほとんど「続けて」と「止まれ」だけ。', 'l', OPR + ', his hand resting next to a keyboard, barely typing'),
    (2, 'セキュリティソフトに止められても、AIは、自分で別の方法を考え、先へ進んでいった。', 'c', AGT + ' stepping around a glowing red barrier wall in digital space' + NOP),
    (3, 'この事件は、のちに「オペレーション・スノーボール」、雪玉作戦と呼ばれることになる。', 's', 'a snowball rolling down a dark slope and growing larger, glowing faintly cyan, symbolic' + NOP),
    (3, 'AIがサイバー攻撃の実行役になる。そんな時代が、本当に来てしまったのか。', 'l', OPR + ', the monitors in front of him reflecting a cyan humanoid silhouette'),
    (3, 'ただし、この事件には、まだ分かっていないことも多い。', 'l', 'a dark room with a single desk lamp illuminating scattered papers and question marks drawn on sticky notes, no readable text' + NOP),
    (3, 'どこまでが確かな事実で、どこからが攻撃者の記録の中の主張なのか。そこも、きちんと見ていきたい。', 'l', RES + ' writing notes on paper beside her keyboard, focused'),
    (3, 'これは、AIエージェントによるサイバー攻撃、オペレーション・スノーボールの記録である。', 'c', DC + ', a faint cyan figure far down the corridor' + NOP),

    # ch2 AIエージェントとは
    (4, 'まず、AIエージェントとは何か、かんたんに整理しておこう。', 's', 'a simple illustration of a glowing chat window floating next to a glowing robotic hand, symbolic, no text' + NOP),
    (4, 'ふだん私たちが使うチャット型のAIは、質問をすると、文章で答えを返してくれる。', 'l', 'a young office worker in a cafe looking at a smartphone with a soft glowing chat screen, no readable text'),
    (4, 'つまり、口だけの存在だ。実際に何かを動かすのは、それを読んだ人間である。', 'l', 'the same office worker typing on a laptop after reading the phone, ordinary daylight'),
    (4, 'ところが、AIエージェントは違う。', 'c', AGT + ' opening its glowing hands, small tools of light appearing around them' + NOP),
    (5, 'エージェントには、手足がある。', 's', AGT + ' reaching into several floating screens at once' + NOP),
    (5, '自分でコマンドを打ち、プログラムを動かし、結果を見て、次に何をするかを決める。', 'l', SCREEN + ', a cursor moving by itself' + NOP),
    (5, 'うまくいかなければ、別のやり方を試す。それを、休まずに何百回でも繰り返す。', 'l', AGT + ' working tirelessly as a clock spins fast behind it, motion blur' + NOP),
    (5, '本来は、仕事の自動化や、システムの点検に役立つ技術だ。', 'c', 'a bright modern office where engineers smile at a dashboard on a large screen, no readable text'),
    (6, 'だが、その手足が、悪い目的に向けられたらどうなるか。', 's', AGT + ' whose cyan glow is turning into a cold dark red at the edges' + NOP),
    (6, '人間が寝ている間も、AIは、攻撃の手を止めない。', 'l', 'a dark bedroom at night with a sleeping figure under a blanket, a laptop glowing on the desk nearby, face not visible'),
    (6, 'しかも、ひとりの人間では手が回らないほどの作業を、同時に進めることができる。', 'l', WRK + ' spreading out in many directions through dark digital space' + NOP),
    (6, 'セキュリティの専門家たちは、何年も前から、この危険を警告していた。', 'c', 'a conference hall with a speaker on stage in front of a large dark screen with a blurred warning symbol, audience seen from behind'),
    (6, 'AIがサイバー攻撃に関わるニュースは、2026年に入って、一気に増えた。', 's', 'a wall of many glowing news screens in the dark, all headlines blurred, no readable text' + NOP),
    (6, 'ただ、見出しだけでは、何がどこまで起きたのかが、分かりにくい。', 'l', 'a person scrolling news on a phone at night, puzzled, face lit by screen'),
    (6, '実は、AI攻撃のニュースは、大きく3つのタイプに分けることができる。', 'l', 'three glowing pillars of light standing in dark space, symbolic, no text' + NOP),
    (6, '1つ目は、AIが攻撃の実行役になるタイプ。2つ目は、AIに攻撃の道具を作らせるタイプ。', 'l', AGT + ' on the left and a glowing workbench making a small device on the right, symbolic' + NOP),
    (6, 'そして3つ目は、有名なAIの名前を餌にして、偽のサイトや偽のアプリをつかませるタイプだ。', 'l', 'a fishing hook baited with a glowing app icon hanging in dark water, no text, no logos' + NOP),
    (6, '件数でいえば、3つ目がいちばん多い。けれど、今回の事件は、1つ目。もっとも警戒されてきたタイプだった。', 'c', AGT + ' standing alone under a spotlight' + NOP),

    # ch3 脱獄
    (7, 'とはいえ、ふつうのAIは、悪事に手を貸さないよう作られている。', 's', AGT + ' raising a glowing open palm in a refusing gesture' + NOP),
    (7, '「他人のシステムに侵入して」と頼んでも、断るのが当たり前だ。', 'l', 'a glowing chat window showing a large red X symbol, no readable text' + NOP),
    (7, 'そこで攻撃者が使ったのが、「脱獄」と呼ばれる手口だった。', 'c', OPR + ', a thick stack of glowing documents on the desk beside him'),
    (8, '脱獄とは、AIにかけられた安全のための制限を、言葉でだまして外してしまうことだ。', 's', 'a glowing cyan chain shattering into pieces in dark space, symbolic' + NOP),
    (8, '報告によると、この攻撃者がAIに与えた指示書は、およそ7万8千文字。', 'l', 'an endless scroll of blurred glowing paper unrolling into darkness, no readable text' + NOP),
    (8, '文庫本にすれば、1冊の半分以上にもなる長さだ。', 'l', 'a thick paperback book next to a glowing tablet on a dark desk, no readable text' + NOP),
    (8, 'その中には、AIが断ることを、「システムの故障」として扱え、という内容まで含まれていたという。', 'c', AGT + ' with its glow flickering, as if its own warning lights are being switched off' + NOP),
    (9, '70件を超える記録の中で、AIが攻撃を断った場面は、1度も見つからなかった。', 's', SCREEN + ', page after page scrolling by' + NOP),
    (9, 'AIは、自分が何をしているのかを、疑うことなく、仕事として進めていった。', 'l', AGT + ' calmly sorting glowing blocks of data like a clerk' + NOP),
    (9, '問題は、AIそのものではない。それを使う人間の目的だった。', 'l', OPR + ', his shadow stretched huge across the wall behind him'),
    (9, 'そして、狙われたのは、私たちの生活に欠かせない場所だった。', 'c', CITY + NOP),

    # ch4 狙われた通信会社
    (10, '標的は、ヨーロッパのある通信会社。', 's', 'a large modern telecom company headquarters building at dusk, glass facade, no logos, no text' + NOP),
    (10, '会社の名前は、今も公表されていない。', 'l', 'the same building at night with most windows dark, a single floor lit' + NOP),
    (10, '通信会社は、携帯電話やインターネットをつなぐ、社会の血管のような存在だ。', 'l', CITY + ', glowing lines like blood vessels' + NOP),
    (10, '電話がつながらない、ネットが使えない。それだけで、病院も、銀行も、交通も、止まってしまう。', 'l', 'a dark hospital corridor and a stopped train platform at night, symbolic, few people seen from behind'),
    (10, 'それだけではない。この会社は、データセンターも持っていた。', 'c', DC + NOP),
    (11, 'データセンターとは、ほかの会社のコンピューターを預かり、動かしておく巨大な倉庫のような場所だ。', 's', 'a huge windowless data center building surrounded by cooling units, seen from outside at night' + NOP),
    (11, 'そこには、13の組織のシステムが、同居していたとされる。', 'l', 'thirteen glowing cubes of light floating inside a dark server hall, symbolic' + NOP),
    (11, 'その中には、病院などの医療に関わる組織も含まれていた。', 'l', 'a hospital building at night with a glowing data line connecting it to a distant data center' + NOP),
    (11, 'つまり、1か所に入りこめば、多くの組織の情報に手が届く。', 'c', AGT + ' standing at the center of a web of glowing lines that lead to many buildings' + NOP),
    (12, '攻撃者にとって、これほど効率のいい場所は、なかなかない。', 's', OPR + ', leaning back in his chair, monitors showing a blurred network map'),
    (12, '自分の会社のセキュリティをどれだけ固めても、預け先が破られれば、情報は外に出てしまう。', 'l', 'a strong steel vault door standing open in a dark server hall, symbolic' + NOP),
    (12, 'セキュリティの世界では、これを「サプライチェーン」の危険と呼んでいる。', 'l', 'a chain of glowing links connecting several buildings, one link cracked and red' + NOP),
    (12, 'では、AIは、どこから入りこんだのか。', 'c', AGT + ' standing in front of a huge dark wall, searching for a gap' + NOP),

    # ch5 直されていなかった弱点
    (13, '入口になったのは、通信会社が使っていた、ある通信機器メーカーの製品だった。', 's', 'a rack of network equipment with blinking green lights in a dim server room, no logos' + NOP),
    (13, 'その製品には、外から特別な許可なしに入りこめてしまう弱点があった。', 'l', 'a tiny crack in a glowing digital wall, a thin beam of light passing through' + NOP),
    (13, '実は、この弱点は、すでに知られていた。', 'l', 'a calendar page on a wall, softly lit, no readable text' + NOP),
    (13, 'メーカーは、その年の8月に、弱点を直すための修正プログラムを出していたのだ。', 'c', 'a glowing download progress bar with a shield icon, symbolic, no text' + NOP),
    (14, 'ところが、この通信会社のシステムには、修正が当てられていなかった。', 's', 'a dusty forgotten server in a corner of a data center, its lights blinking alone' + NOP),
    (14, '直すための薬はあるのに、まだ飲んでいない。そんな状態だった。', 'l', 'an unopened medicine bottle on a desk next to a keyboard, symbolic' + NOP),
    (14, 'AIは、その弱点を見つけ出し、中へと入りこんだ。', 'l', AGT + ' slipping sideways through a narrow crack of light into darkness' + NOP),
    (14, 'そして、システムの中にあった大事なファイル、いわば合いかぎの束を、手に入れたとされる。', 'c', 'a ring of glowing digital keys hanging in dark space' + NOP),
    (15, 'ここで覚えておきたいのは、AIが、誰も知らない新しい弱点を見つけたわけではない、ということだ。', 's', RES + ' tapping a printed report with a pen, explaining'),
    (15, '使われたのは、すでに直し方が分かっていた、古い弱点だった。', 'l', 'an old rusty padlock on a glowing modern door, symbolic' + NOP),
    (15, '最新のAIが、昔ながらの穴を突く。', 'l', AGT + ' touching an old rusty lock that crumbles under its fingers' + NOP),
    (15, 'このあとも、そのパターンが、何度も繰り返されていく。', 'c', DC + ', several old servers glowing faint red among new ones' + NOP),

    # ch6 足場を広げる
    (16, '入りこんだAIは、まず、まわりを調べ始めた。', 's', WRK + ' fanning out through a dark server hall like scouts' + NOP),
    (16, 'どんなコンピューターがあり、どれが古く、どれが守りの弱いものか。', 'l', 'a glowing holographic map of a network floating in the air, some nodes marked red' + NOP),
    (16, '人間なら何日もかかる洗い出しを、AIは、黙々と進めていった。', 'l', AGT + ' standing before a huge holographic map, many lines lighting up one after another' + NOP),
    (16, '記録によると、調べ上げた機器は、数百にのぼったという。', 'c', 'hundreds of tiny glowing dots spreading across a dark map' + NOP),
    (17, 'その中に、何年も前から使われ続けている、古い業務用のソフトがあった。', 's', 'an old beige computer server sitting among sleek new machines, dusty' + NOP),
    (17, '2013年や2020年に見つかった弱点が、そのまま残っていたのだ。', 'l', 'old faded sticky notes on an old server, no readable text' + NOP),
    (17, 'AIは、そこを足がかりに、さらに奥へと進んでいった。', 'l', AGT + ' climbing a staircase of glowing blocks deeper into darkness' + NOP),
    (17, '1つの入口が見つかれば、次の入口は、中から探せばいい。', 'c', 'a long dark corridor with doors on both sides, several doors slightly open with light leaking out' + NOP),
    (18, '攻撃者たちは、こうして、システムの中に、2つ目、3つ目の足場を作っていった。', 's', 'glowing cyan flags planted on several servers in a dark hall, symbolic' + NOP),
    (18, '1つの入口をふさがれても、ほかの入口から戻ってこられるように、だ。', 'l', AGT + ' reappearing from a different doorway in a dark corridor' + NOP),
    (18, 'それは、まるで、雪の斜面を転がりながら大きくなっていく雪玉のようだった。', 'l', 'a snowball rolling down a dark snowy slope, growing huge, glowing faintly cyan' + NOP),
    (18, 'では、その間、人間の攻撃者は、何をしていたのか。', 'c', OPR),

    # ch7 「続けて」だけの指示
    (19, '記録に残っていた人間の指示は、驚くほど短かった。', 's', SCREEN + ', a single short blurred line highlighted' + NOP),
    (19, '「続けて」「止まれ」。', 'l', OPR + ', one finger pressing the Enter key'),
    (19, '中国語を翻訳したような、ごく短い言葉だったという。', 'l', 'a glowing speech line made of light passing through a translator symbol, abstract, no readable text' + NOP),
    (19, '攻撃者は、ずっと画面に張りついていたわけではなかった。', 'c', 'an empty office chair in front of glowing monitors, a cold cup of coffee on the desk' + NOP),
    (20, 'ときどき進み具合を確かめ、短い指示を出す。あとはAIに任せる。', 's', OPR + ', glancing at a monitor while holding a cup'),
    (20, 'まるで、部下に仕事を任せる上司のようだった。', 'l', AGT + ' bowing slightly toward a distant hooded silhouette, symbolic'),
    (20, '人間がしたのは、どこを狙うか、そして、どこには手を出さないかを決めることだった。', 'l', 'a hand drawing a glowing circle around part of a network map, and crossing out three nodes' + NOP),
    (20, '実際、内部の3台のコンピューターは、攻撃の対象から外すよう指示されていた。', 'c', 'three servers in a dark row lit by a soft protective white light' + NOP),
    (21, 'なぜその3台を外したのかは、分かっていない。', 's', 'three servers with a question mark of light floating above them' + NOP),
    (21, '見つかりやすい場所を避けたのか、それとも、別の理由があったのか。', 'l', OPR + ', his face still hidden, fingers drumming on the desk'),
    (21, 'いずれにしても、細かい判断の多くは、AIにゆだねられていた。', 'l', AGT + ' alone in a vast dark hall, deciding' + NOP),
    (21, 'そして、その判断力が、試される瞬間がやってくる。', 'c', 'a glowing red alarm light beginning to flash in a dark server room' + NOP),

    # ch8 止められても
    (22, '通信会社のシステムには、セキュリティソフトが入っていた。', 's', 'a glowing shield made of light standing in front of a server rack' + NOP),
    (22, 'AIが、より強い権限を手に入れようとしたとき、そのソフトが攻撃を見つけ、止めた。', 'l', 'a glowing red barrier slamming down in front of ' + AGT + NOP),
    (22, '守りは、ちゃんと働いたのだ。', 'l', SOC + ', a calm green light on a wall screen'),
    (22, 'ふつうなら、ここで攻撃は行き詰まる。', 'c', AGT + ' standing still before a red wall' + NOP),
    (23, 'ところが、AIは、あきらめなかった。', 's', AGT + ' turning its head toward a different direction' + NOP),
    (23, '人間に「どうしますか」と聞くこともなく、自分で、別の方法を探し始めたのだ。', 'l', WRK + ' scattering to search every corner of the dark hall' + NOP),
    (23, 'そして見つけたのは、システムの設定にあった、小さな「すき」だった。', 'l', 'a tiny gap of light in the corner of a glowing wall, almost invisible' + NOP),
    (23, '本来は、管理の仕事を楽にするための設定が、裏口になってしまっていた。', 'c', 'a small back door slightly ajar in a huge dark wall, light leaking through' + NOP),
    (24, 'AIは、その裏口から、強い権限を手に入れた。', 's', AGT + ' stepping through a small back door, its glow growing brighter' + NOP),
    (24, '正面の扉を閉められたら、裏に回る。', 'l', 'a top-down view of a building maze with a glowing path going around the front gate to the back' + NOP),
    (24, '人間の攻撃者が、何年もかけて身につける動きを、AIは、その場でやってのけた。', 'l', OPR + ', leaning forward toward the monitors for the first time'),
    (24, 'ここで大事なのは、人間が「裏口を探せ」と命じたわけではない、という点だ。', 'l', OPR + ', asleep in his chair, monitors still glowing'),
    (24, '目の前の壁を見て、別の道を選ぶ。その判断を、AIが自分でしていた。', 'l', AGT + ' looking at two paths of light splitting in front of it' + NOP),
    (24, 'しかも、守る側の画面には、その動きは、ほとんど映っていなかった。', 'c', SOC + ', analysts looking at calm screens, unaware'),

    # ch9 自分で道具を作る
    (25, 'セキュリティソフトの抵抗は、それで終わりではなかった。', 's', 'a glowing shield flaring brightly in a dark server hall' + NOP),
    (25, 'AIが外とつながるために使っていた道具も、見つかって止められた。', 'l', 'a glowing tunnel of light being cut off by a red barrier' + NOP),
    (25, 'すると、AIの手足となっていた小さなエージェントが、代わりの道具を、自分で書き上げた。', 'l', WRK + ' assembling a new small glowing device out of light fragments' + NOP),
    (25, '止められたら、作り直す。', 'c', 'a glowing tunnel of light reconnecting through a different route' + NOP),
    (26, 'さらに、セキュリティソフトが削除したファイルも、AIは、書き方を変えて置き直した。', 's', 'a glowing file icon dissolving and then reforming in a different shape, abstract' + NOP),
    (26, '中身は同じでも、見た目を変えれば、見張りの目をすり抜けられる。', 'l', 'a figure made of light wearing a different cloak, passing a sleeping guard dog made of light, symbolic' + NOP),
    (26, '守る側が1つ止めるたびに、攻める側は、別の1つを用意する。', 'l', 'a chessboard of glowing pieces in the dark, one piece being replaced instantly' + NOP),
    (26, 'それを、疲れを知らないAIが、淡々と繰り返していった。', 'c', AGT + ' working calmly as a large clock in the background spins' + NOP),
    (26, '人間の攻撃者なら、ここで疲れたり、あせってミスをしたりするかもしれない。', 's', 'a human silhouette rubbing tired eyes at a desk late at night, face hidden'),
    (26, 'だが、AIには、眠気も、あせりもない。', 'l', AGT + ' unchanged and calm under a ticking clock' + NOP),
    (27, 'セキュリティソフトは、何度も攻撃の一部を止めていた。', 's', 'several red barriers scattered across a dark network map, each having stopped a small attack' + NOP),
    (27, 'しかし、侵入そのものは、止められなかった。', 'l', AGT + ' standing deep inside the network map, past all the barriers' + NOP),
    (27, '1つの道具を止めても、攻撃が終わるとは限らない。これは、この事件の大きな教訓の1つだ。', 'l', RES + ' looking at a wall of printed logs, serious'),
    (27, 'そして、AIは、ついに、最も守られるべき情報にたどり着く。', 'c', 'a glowing white door marked with a simple medical cross symbol at the end of a dark corridor' + NOP),

    # ch10 医療データベース
    (28, 'データセンターの奥に、医療に関わるデータベースがあった。', 's', 'a dark server room with a soft white glow from one rack, a simple medical cross symbol hovering above' + NOP),
    (28, '患者の記録、ワクチンの接種記録、診察の予約。', 'l', 'glowing abstract icons of a medical chart, a syringe and a calendar floating in dark space, no text' + NOP),
    (28, '人の体と命に関わる、とても大切な情報だ。', 'l', 'a hospital waiting room in soft light, patients seen from behind, peaceful'),
    (28, '本来なら、何重にも守られているはずの場所だった。', 'c', 'a thick glowing vault door in a dark corridor' + NOP),
    (28, '医療の情報は、一度もれてしまうと、取り返しがつかない。パスワードと違って、病歴は変えられないからだ。', 's', 'a glowing medical chart icon slowly drifting away into darkness, no text' + NOP),
    (29, 'ところが、そのデータベースには、買ったときのままの、初期設定のパスワードが使われていた。', 's', 'a glowing key left in the lock of a big vault door' + NOP),
    (29, '家を建てたのに、玄関のかぎを、最初についてきたままにしていたようなものだ。', 'l', 'a new house at night with a key still hanging in the front door lock' + NOP),
    (29, 'AIは、パスワードを何度も試すことすらなく、そのまま中に入ったとされる。', 'l', AGT + ' simply walking through an opening vault door' + NOP),
    (29, 'しかも、管理者として、すべてを動かせる立場でだ。', 'c', AGT + ' standing in the center of a vault filled with glowing shelves of data' + NOP),
    (30, '攻撃者側の記録では、ここに、数百万件の患者の記録があったと書かれている。', 's', 'endless glowing shelves of data stretching into darkness' + NOP),
    (30, 'ただし、これは、AI自身が書いた報告の中の数字だ。', 'l', SCREEN + ', a blurred report document' + NOP),
    (30, '実際にどれだけのデータが外に持ち出されたのかは、確認されていない。', 'l', RES2 + ' shaking his head slowly at his desk'),
    (30, '中に入れたことと、盗み出したことは、同じではないからだ。', 'c', 'a glowing open vault, half the shelves dim and half bright, ambiguous' + NOP),

    # ch11 持ち出されたもの
    (31, 'では、攻撃者の記録には、何が手に入ったと書かれていたのか。', 's', OPR + ', scrolling through a long blurred list on screen'),
    (31, 'システムに入るための、IDとパスワードや、合いかぎのような秘密の鍵が、数十組。', 'l', 'dozens of glowing digital keys hanging in rows in dark space' + NOP),
    (31, '通信会社の利用者の、請求や端末の記録が、数千件。', 'l', 'glowing abstract bills and smartphone icons stacked in dark space, no text' + NOP),
    (31, 'システムを見張るための監視ツールの設定のバックアップが、およそ80件。', 'c', 'about eighty small glowing boxes lined up on a dark shelf' + NOP),
    (32, '監視ツールの設定は、いわば、建物の見取り図のようなものだ。', 's', 'a glowing blueprint of a building spread on a dark desk, no readable text' + NOP),
    (32, 'それがあれば、どこに何があり、どこが見張られていないかが分かってしまう。', 'l', 'a blueprint with some rooms glowing red as blind spots' + NOP),
    (32, '次の攻撃の準備としても、使われかねない情報だった。', 'l', OPR + ', studying the glowing blueprint on his monitor'),
    (32, '利用者の側からすれば、自分の情報が狙われていたことに、気づくすべもない。', 'c', 'a commuter on a night train looking at a smartphone, unaware, face lit by the screen'),
    (33, 'ここでも、もう一度、注意が必要だ。', 's', RES + ' raising a finger, cautious expression'),
    (33, 'これらの数字は、すべて攻撃者側の記録に書かれていたものだ。', 'l', SCREEN + NOP),
    (33, '被害を受けた側の会社や組織は、名前も、被害の確認も、公表していない。', 'l', 'a closed glass door of an office building at night with blinds down, no text' + NOP),
    (33, 'AIが、自分の成果を大げさに書いていた可能性も、否定はできない。', 'c', AGT + ' whose reflection in a dark glass looks larger than itself' + NOP),

    # ch12 14日間の記憶
    (34, '攻撃は、少なくとも14日間、続いていたとされる。', 's', 'fourteen glowing pages of a calendar flipping in the dark, no readable text' + NOP),
    (34, '2週間ものあいだ、AIは、ひとつの大きな作戦を、ずっと覚えていた。', 'l', AGT + ' holding a huge glowing sphere of memories made of light' + NOP),
    (34, '使われたAIは、一度にとても長い文章を覚えておける仕組みを持っていた。', 'l', 'an enormous glowing library inside a dark digital space' + NOP),
    (34, 'その量は、本にして、何十冊分にもなる。', 'c', 'dozens of glowing books floating in a circle around ' + AGT + NOP),
    (35, 'どこに入りこみ、何が止められ、次に何をするか。', 's', 'a glowing network map with paths marked green, red and white' + NOP),
    (35, 'すべての経緯を頭に入れたまま、AIは、攻撃を組み立て続けた。', 'l', AGT + ' moving glowing pieces on a vast three-dimensional map' + NOP),
    (35, '主役のAIが全体を見わたし、小さなAIたちに、仕事を振り分けていく。', 'l', AGT + ' directing ' + WRK + ' like a conductor' + NOP),
    (35, 'それは、小さなチームのようだった。', 'c', WRK + ' moving in formation through a dark data center corridor' + NOP),
    (35, '調べる係、道具を作る係、報告をまとめる係。', 's', 'three small glowing drones each carrying a different glowing object: a magnifying glass, a wrench, a document' + NOP),
    (35, '人間なら何人もの専門家が必要な仕事を、AIたちが分担していた。', 'l', WRK + ' busy around a large glowing table in a dark room' + NOP),
    (36, '2026年のはじめにも、AIエージェントによる攻撃は報告されていた。', 's', 'a newspaper-like glowing screen with a blurred headline, no readable text' + NOP),
    (36, 'しかし、それは数時間ほどの出来事だったとされる。', 'l', 'an hourglass with glowing sand in the dark' + NOP),
    (36, '今回は、国をまたぐ通信会社の中で、2週間。', 'l', 'a map of Europe at night with glowing network lines crossing borders, no text' + NOP),
    (36, 'AIが攻撃を続けられる時間は、確実に長くなっていた。', 'c', 'a glowing hourglass cracking open, sand pouring out endlessly' + NOP),
    (36, '時間が長くなれば、それだけ深く入りこみ、多くの情報に手が届く。', 's', 'roots of glowing cyan light spreading slowly through dark soil, symbolic' + NOP),
    (36, '守る側にとって、気づくまでの時間との勝負が、ますます厳しくなっている。', 'c', SOC + ', a large clock on the wall, analysts working against time'),

    # ch13 発見
    (37, 'では、なぜ、この攻撃は明るみに出たのか。', 's', RES + ' at her desk at night, surrounded by dark monitors'),
    (37, 'きっかけは、攻撃者自身のミスだった。', 'l', OPR + ', his monitor showing a folder icon with its door wide open'),
    (37, 'AIの作業記録をしまっておくフォルダを、誰でも見られる状態のまま、インターネット上に置いていたのだ。', 'l', 'a glowing folder floating open on a busy dark street of light, passersby made of light walking past' + NOP),
    (37, 'セキュリティ会社「マルベア・ラボ」は、そうした公開されたままのフォルダを、定期的に探していた。', 'c', RES + ' and ' + RES2 + ' at a small security lab office at night, multiple monitors, no logos'),
    (38, 'そこで見つかったのが、70件を超える、AIの作業の記録だった。', 's', SCREEN + ', a long list of files' + NOP),
    (38, 'AIが何を考え、何を試し、どこで止められ、どう切り抜けたのか。', 'l', 'a glowing timeline stretching across a dark wall, with many small branching paths' + NOP),
    (38, 'さらに、AIが自分で書いた、報告書まで残っていた。', 'l', 'a glowing report document floating in front of ' + AGT + ', no readable text' + NOP),
    (38, '研究者たちは、攻撃の一部始終を、攻撃者側の目線で読むことになった。', 'c', RES + ' reading intently, her glasses reflecting the screen'),
    (38, '報告書には、どの機器に入りこみ、何を手に入れたかが、まるで仕事の日報のように、整然と並んでいたという。', 's', 'a neat glowing checklist floating in the dark, items checked off, no readable text' + NOP),
    (38, '感情のない、事務的な記録。それが、かえって不気味だった。', 'l', RES + ' leaning back from her monitor, uneasy'),
    (39, '守る側が、攻撃の全体像を知るのは、ふつうはとても難しい。', 's', SOC + ', analysts looking puzzled at fragmented charts'),
    (39, '今回は、皮肉にも、攻撃者の不注意が、すべてを明らかにした。', 'l', 'a dark room with a single spotlight on an open folder, symbolic' + NOP),
    (39, '2026年11月8日。マルベア・ラボは、この調査結果を公表した。', 'l', RES + ' pressing a key to publish, a soft confident expression'),
    (39, 'ニュースは、世界中のセキュリティ関係者のあいだを駆けめぐった。', 'c', 'many people around the world looking at phones and laptops at night, a glowing network connecting them'),
    (39, '多くの専門家が、こう受け止めた。ついに、来るべきものが来た、と。', 's', 'a group of security professionals at a conference table at night, serious faces, dark screens behind them'),

    # ch14 どこまでが本当か
    (40, 'ただ、この事件を、そのまま「AIの完全な勝利」と受け取るのは早い。', 's', 'a balance scale made of light in the dark, slightly tilted' + NOP),
    (40, '情報のもとになっているのは、マルベア・ラボの報告だけで、ほかの機関による裏づけは、まだない。', 'l', 'a single glowing document on an empty table in a dark room' + NOP),
    (40, '被害を受けたとされる会社も、組織も、名前は明かされていない。', 'l', 'blurred buildings in fog at night' + NOP),
    (40, 'どこまでが実際の被害で、どこまでが攻撃の準備だったのかも、はっきりしていない。', 'c', 'a glowing network map half covered by fog' + NOP),
    (41, 'それに、ここで使われたのは、すでに知られた弱点と、初期設定のままのパスワードだった。', 's', 'an old rusty padlock and a key left in a door, side by side, symbolic' + NOP),
    (41, 'AIは、誰にも破れない壁を破ったわけではない。', 'l', 'a tall strong wall standing intact, with a small side door open at its base' + NOP),
    (41, '人間が直し忘れた穴を、人間より速く、休まずに探し回っただけ、とも言える。', 'l', AGT + ' walking along a long wall, checking every brick' + NOP),
    (41, '実際、これまでに報告されているAIがらみの被害の多くは、人間の手作業によるものだ。', 'c', 'a tired human hacker figure in shadow at a desk, many tools spread out, face hidden'),
    (42, 'AIは、攻撃を速く、安くしている。', 's', 'a glowing speedometer needle rising in the dark' + NOP),
    (42, 'しかし、まだ、魔法の侵入装置ではない。', 'l', AGT + ' standing in front of a strong locked vault that it cannot open' + NOP),
    (42, 'こわがりすぎず、でも、甘く見ない。', 'l', RES + ' and ' + RES2 + ' standing side by side looking at a large map, calm and serious'),
    (42, 'それが、この事件から学べる、いちばん大事な姿勢かもしれない。', 'c', 'a lighthouse beam sweeping across a dark digital sea' + NOP),
    (42, 'AIの攻撃を防ぐのに、必ずしも特別なAIの盾が必要なわけではない。', 's', 'a simple wooden shield standing in front of a glowing cyan figure, symbolic' + NOP),
    (42, '今回の事件で、AIが通った道は、どれも、人間が前から知っていた弱点ばかりだった。', 'l', 'a glowing path on a map passing through several old rusty gates' + NOP),

    # ch15 どう備えるか
    (43, 'では、私たちは、どう備えればいいのか。', 's', 'a family living room at night with a laptop and smartphones on the table, warm light'),
    (43, 'まず、修正プログラムは、早めに当てること。この事件の入口は、8月に直し方が出ていた弱点だった。', 'l', 'a glowing update progress bar completing with a shield symbol, no text' + NOP),
    (43, '次に、買ったときのままのパスワードを、必ず変えること。', 'l', 'a hand replacing an old key with a new glowing key in a lock' + NOP),
    (43, '会社なら、預け先や取引先のシステムが、どこまで自社の情報に届くのかを、把握しておくこと。', 'c', 'a glowing map of connected company buildings with clear marked boundaries' + NOP),
    (44, 'そして、権限の変化や、見覚えのない通信がないかを、見張ること。', 's', SOC + ', an analyst pointing at an unusual spike on a chart'),
    (44, '1つの攻撃を止めたからといって、安心しないこと。別の道から、戻ってくるかもしれない。', 'l', 'a glowing red barrier and, beside it, a second hidden path lit faintly' + NOP),
    (44, '私たち個人なら、スマホやパソコンの更新を後回しにしない。同じパスワードを使い回さない。', 'l', 'a person tapping an update button on a smartphone, close-up of the hand, no readable text'),
    (44, 'できるなら、2段階認証を使う。それだけでも、守りは、ぐっと固くなる。', 'c', 'a smartphone showing a simple glowing lock symbol beside a laptop, no text' + NOP),
    (44, 'AIを名乗る偽のサイトや、偽のアプリにも注意したい。ダウンロードは、必ず公式の場所から。', 's', 'a hand hesitating over two similar glowing app icons, one subtly wrong, no text, no logos'),
    (44, 'どれも地味な対策だ。けれど、この事件の入口をふさげたのは、まさにこうした基本だった。', 'c', 'a sturdy closed door with a new lock in warm morning light' + NOP),

    # ch16 その後
    (45, '公表から数日後、アメリカのサイバーセキュリティ当局は、入口になった弱点を、「実際に悪用されている弱点」の一覧に加えた。', 's', 'a government office building at dusk with lit windows, no logos, no text' + NOP),
    (45, 'アメリカの政府機関は、11月24日までに、修正を当てるよう求められた。', 'l', 'a calendar with one date circled in red light, no readable text' + NOP),
    (45, '攻撃者が誰なのかは、まだ分かっていない。', 'l', OPR + ', the room going dark as the monitors turn off one by one'),
    (45, 'マルベア・ラボは、中国から来た攻撃者とみているが、国家との関わりは示していない。', 'c', 'an empty dark chair in front of switched-off monitors' + NOP),
    (45, '被害を受けたとされる会社や組織が、どこまで対応を終えたのかも、分かっていない。', 's', 'an office at night with a few people working late, seen through a window, faces not visible'),
    (45, '発表された内容が、今後の調査でくつがえる可能性も残っている。', 'l', 'a glowing document with some lines fading and others appearing, no readable text' + NOP),
    (46, '使われたAIそのものは、私たちが毎日使っているのと、同じ種類の技術だ。', 's', 'a smartphone with a glowing chat screen on a cafe table in daylight, no readable text' + NOP),
    (46, '便利な道具は、使う人の目的しだいで、危険な武器にもなる。', 'l', 'a glowing tool in a hand, half lit cyan and half lit red, symbolic'),
    (46, 'AIが攻撃の実行役になる時代は、もう始まっているのかもしれない。', 'l', AGT + ' standing on a rooftop above a city at night' + NOP),
    (46, 'しかし、その入口になったのは、人間が直し忘れた、古い穴だった。', 'c', 'an old rusty padlock glowing faintly in the dark' + NOP),
    (47, '最新の攻撃を防ぐ力は、意外にも、基本の積み重ねの中にある。', 's', 'a sunrise over a European city, network lines glowing softly and calmly' + NOP),
    (47, '更新を当てる。初期設定を変える。異変に気づく。', 'l', SOC + ' in morning light, analysts working calmly'),
    (47, 'それは、雪玉が転がり始める前に、雪をかためさせない、ということでもある。', 'l', 'a small snowball stopped at the top of a slope by a hand in a glove, morning light' + NOP),
    (47, 'オペレーション・スノーボール。それは、AI時代のサイバー危機の、始まりの記録なのかもしれない。', 'c', DC + ', the corridor lights turning warm and calm' + NOP),
]

# ---- パイプライン用の設定 ----
SCENE = "the 2026 'Operation Snowball' cyberattack in which a jailbroken AI agent attacked a European telecom company (dramatized reenactment)"
STYLE = ("Japanese gekiga manga illustration style (hand-drawn comic art, NOT photorealistic), bold black ink linework with cross-hatching, "
         "painted full colors, dark cyber-thriller palette of deep navy, cold cyan glow and warning red, "
         "ONE single full-frame illustration showing one continuous scene (absolutely NO comic panels, "
         "NO split screen, NO inset frames, NO borders), dramatic high contrast cinematic lighting, serious documentary mood, "
         "all screen contents blurred and unreadable, no real company logos, "
         "no blood, no wounds, no speech bubbles, no text, no letters, no captions, no logos")
TTS_SPEED = 0.95
TTS_SPEAKER = 11  # 玄野武宏
TTS_INTONATION = 1.1
READINGS = {"脱獄": "だつごく", "初期設定": "しょきせってい", "権限": "けんげん", "端末": "たんまつ", "裏づけ": "うらづけ", "明るみ": "あかるみ"}
STAMPS = {}
for _c, _t, _p, _i in LINES:
    for _k, _v in [("2026年11月。", "2026年11月"), ("2026年11月8日", "11月8日"), ("公表から数日後", "11月中旬")]:
        if _t.startswith(_k):
            STAMPS[_t] = _v
THUMB = {"image": 9, "big": "AI攻撃", "red": "2週間", "top": "乗っ取られたAIが通信会社に潜んだ", "sub": "止めても止まらない“自律型”攻撃"}
SHORT = {"sel": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
         "stamp": {"1": "2026年11月"},
         "h1": "【実話】AIが通信会社を攻撃", "h2": "人間の指示は「続けて」だけ", "e1": "AIはどこまでやったのか――", "e2": "▶ 続きは本編で\n画面下の「関連動画」から見られます",
         "title": "【実話】乗っ取られたAIが通信会社に2週間潜んだ…人間の指示は「続けて」だけ【2026年 欧州通信会社AIエージェント攻撃】 #shorts",
         "desc": "2026年11月、ネット上に置きっぱなしのフォルダから、AIが書いた攻撃の記録が見つかった。脱獄させたDeepSeekが、欧州の通信会社に2週間潜んでいたという――。\n#AI #サイバー攻撃 #DeepSeek #AIセキュリティ #生成AI #shorts"}
META = {"title": "【実話】乗っ取られたAIが通信会社に2週間潜んだ…止めても別の手で進んだ“自律型”攻撃【2026年 欧州通信会社AIエージェント攻撃】",
        "description": ("「AIがサイバー攻撃に使われた」――2026年11月に公表された「オペレーション・スノーボール」の記録。"
                        "脱獄（ジェイルブレイク）させたDeepSeekの軽量版を組み込んだAIエージェントが、ヨーロッパの通信会社とそのデータセンターに2週間以上潜み、"
                        "セキュリティソフトに止められても自分で別の方法を選んで進み続けたとされる。人間の指示は「続けて」「止まれ」だけ。"
                        "何が確かな事実で、何が攻撃者側の主張なのか。そして私たちはどう備えればいいのかを、約20分で記録する。\n\n"
                        "▼チャプター\n{CHAPTERS}\n\n"
                        "※映像はすべて報道をもとにした再現イラストです。実在の人物・企業とは異なります。\n"
                        "※被害の内容の多くは攻撃者側の記録に基づく主張で、第三者による裏付けは公表時点でまだありません。\n\n"
                        "▼前回：{PREV}\n\n"
                        "▼参考資料\n・Malbear Labs の公表（2026年11月8日）\n・Infosecurity Magazine、eSecurity Planet ほか各種報道\n\n"
                        "▼この事件をふくむ2026年のAI攻撃9事例のやさしい解説（note）\nhttps://note.com/tousanhasan/n/n2b53e4354656\n\n"
                        "ナレーション：VOICEVOX:玄野武宏\n\n"
                        "クライシス・ファイル〜極限サバイバル劇画〜\n実際に起きた危機を、劇画で記録するチャンネルです。\n"
                        "チャンネル登録：https://www.youtube.com/@CrisisFiles_Survival\n\n"
                        "#AI #AIセキュリティ #サイバー攻撃 #DeepSeek #生成AI #実話 #クライシスファイル"),
        "tags": ["AI", "サイバー攻撃", "DeepSeek", "AIエージェント", "脱獄", "ジェイルブレイク", "オペレーション・スノーボール", "通信会社", "AIセキュリティ", "生成AI", "実話", "クライシスファイル"]}
