# -*- coding: utf-8 -*-
# Streamlit app: 大喜利お題ルーレット by あすとらふぃーだ

import secrets
import html
import streamlit as st

X_URL = "https://x.com/Ascalaphidae"

st.set_page_config(
    page_title="大喜利お題ルーレット",
    layout="centered",
)

# =========================
# お題リスト
# =========================
ODAI_LIST = [
    "絶対に行きたくない動物園の特徴",
    "こんな給食はいやだ",
    "こんな先生は落ち着かない",
    "こんなカフェは入りづらい",
    "こんな温泉は安心できない",
    "こんな美容室はこわい",
    "こんな病院は不安になる",
    "こんなホテルは眠れない",
    "こんな遊園地はテンションが下がる",
    "こんな引っ越し業者は信用できない",
    "こんな探偵は頼りない",
    "こんなヒーローは困る",
    "こんな魔王はいやだ",
    "こんな宇宙人は地味すぎる",
    "こんな忍者は目立ちすぎる",
    "店員が思わず言ってしまった一言とは",
    "ヒーローが戦いの前に言ってはいけない一言とは",
    "初対面で言われたら困る一言とは",
    "占い師が急に自信をなくした理由とは",
    "校長先生の話の中に一つだけ変な一言がありました。何と言った？",
    "名探偵がまったく締まらなくなる一言とは",
    "プロポーズの場でそれはないだろ、何と言った？",
    "旅館の女将が言ってはいけない一言とは",
    "面接で言ったら終わる一言とは",
    "サンタが子どもに言ってはいけない一言とは",
    "運動会で見た、かなり変な光景",
    "コンビニで二度見したもの",
    "電車で見かけた、気になる人",
    "公園で起きていた謎の出来事",
    "結婚式で見てしまったもの",
    "無人島で一番いらないものが流れ着いた。何だった？",
    "宝箱を開けたら入っていた、がっかりするもの",
    "魔法学校の授業中に起きた、しょうもない事件",
    "宇宙船の中で一番どうでもいいトラブルとは",
    "やる気のない占い師の特徴",
    "優しすぎるラスボスの特徴",
    "気が弱すぎる不良の特徴",
    "せっかちな仙人の特徴",
    "小心者の海賊の特徴",
    "地味すぎるアイドルの特徴",
    "テンションが低すぎる実況者の特徴",
    "妙に現実的な魔法使いの特徴",
    "サービス精神が強すぎる泥棒の特徴",
    "ルールを守りすぎる怪盗の特徴",
    "盛大に失敗したサプライズの内容とは",
    "店名を変えたけど失敗した理由とは",
    "発明家の新作がまったく売れない理由とは",
    "伝説の剣が人気ない理由とは",
    "タイムマシンが全然使われない理由とは",
    "秘密基地なのに全然秘密じゃない理由とは",
    "無敵のロボがあっさり負けた理由とは",
    "そのダイエット法が流行らなかった理由とは",
    "未来の道具なのに不便な理由とは",
    "最強の呪文が不人気な理由とは",
    "そんなことある？と思った校則",
    "ちょっと変わったファミレスのルール",
    "見たことないタイプの注意書き",
    "そのアプリ、どんな機能があるの？",
    "新しくできた謎の部活とは",
    "最近できた変な資格とは",
    "あまりうれしくない新サービスとは",
    "いらないのに進化した家電とは",
    "その町だけにある変な風習とは",
    "誰が使うのか分からない便利グッズとは",
    "いや、そこだけ雑なんかい。何があった？",
    "急に夢が小さい。何を目指している？",
    "そこだけ正直すぎる。何と言った？",
    "がんばる方向を間違えている。何をした？",
    "無駄に気合いが入っている。何に？",
    "急に生活感が出た。何があった？",
    "変なこだわりだけ強い。どんな人？",
    "一番会いたくないサンタとは",
    "友達になりたくない妖精とは",
    "信用できない博士とは",
    "たぶん弱い勇者とは",
    "近所に住んでそうな魔王とは",
    "たまに見かける変な天使とは",
    "思ったより普通な宇宙人とは",
    "めんどうくさい神様とは",
    "ちょっと嫌な猫の妖怪とは",
    "クセが強い守護霊とは",
    "そんな映画のタイトルとは",
    "売れなさそうなゲームのタイトルとは",
    "絶対に泣けない小説のタイトルとは",
    "不安になる健康本のタイトルとは",
    "読みたくない恋愛漫画のタイトルとは",
    "子どもが見なくなる絵本のタイトルとは",
    "行きたくない旅行ツアーの名前とは",
    "人気が出なさそうなアイドルグループ名とは",
    "失敗しそうな新商品名とは",
    "あまり信用できないアプリ名とは",
    "誰も買わない商品のキャッチコピーとは",
    "その店の宣伝文句、何か変です。どんな文？",
    "ヒーロー募集の広告に書いてあったこととは",
    "魔王軍の求人広告に書いてありそうなこととは",
    "変な旅館の売り文句とは",
    "人気のないテーマパークの宣伝文とは",
    "その学校のパンフレット、何て書いてある？",
    "怪しい健康グッズの紹介文とは",
    "新作お菓子の失敗した宣伝文とは",
    "逆に不安になる安心アピールとは",
    "もしも鬼が会社員だったら",
    "もしも桃太郎がやる気ゼロだったら",
    "もしもドラゴンがペットショップにいたら",
    "もしも学校に魔王が転校してきたら",
    "もしもコンビニに侍がいたら",
    "もしも宇宙人が日本の田舎に来たら",
    "もしも天使にクレームを入れたら",
    "もしも神様がアルバイトを始めたら",
    "もしも幽霊がまじめすぎたら",
    "もしも忍者がSNSを本気でやっていたら",
    "すごそうで全然すごくないもの",
    "かわいそうだけどあまり同情できない話",
    "安心したのに安心できない理由",
    "お得そうで全然お得じゃないもの",
    "便利そうで不便なもの",
    "優しそうで怖い人",
    "強そうで弱いもの",
    "秘密っぽいのに全然秘密じゃないこと",
    "おしゃれそうでダサいもの",
    "本気っぽいのに中身が薄いもの",
    "朝から見たくないもの",
    "レジで起きたら困ること",
    "コンビニで一番いらない新サービスとは",
    "電話で聞きたくない一言とは",
    "家に帰ったら起きていた変なこと",
    "バイト初日に見たくないもの",
    "友達の家で困ること",
    "カラオケで起きたら嫌なこと",
    "エレベーターで気まずいこと",
    "宅配で来てほしくない人とは",
    "なんか様子のおかしい月曜日",
    "世界一どうでもいい能力とは",
    "神様のうっかりミスとは",
    "夢に出てきた変なルールとは",
    "未来でなぜか流行っているものとは",
    "異世界に行って最初に困ったこと",
    "この村、何かがおかしい。何が変？",
    "空から降ってきたら嫌なもの",
    "一番いらない奇跡とは",
    "妖精がやりがちな迷惑とは",
    "コメント欄がざわついた理由とは",
    "初見さんが来た瞬間に起きたこととは",
    "配信で一番見たくない表示とは",
    "ゲーム実況で言ってはいけない一言とは",
    "視聴者が困る参加型ルールとは",
    "そのゲーム、どんなバグがあるの？",
    "チュートリアルで心が折れる理由とは",
    "ラスボスより嫌な雑魚敵とは",
    "誰も喜ばないアプデ内容とは",
    "そのゲームの変な実績とは",
]

# =========================
# セッション状態
# =========================
if "current_odai" not in st.session_state:
    st.session_state.current_odai = ""

if "has_drawn" not in st.session_state:
    st.session_state.has_drawn = False

if "manual_input" not in st.session_state:
    st.session_state.manual_input = ""

# =========================
# 関数
# =========================
def draw_random_odai():
    st.session_state.current_odai = secrets.choice(ODAI_LIST)
    st.session_state.has_drawn = True

def show_manual_odai():
    text = st.session_state.manual_input.strip()
    if text:
        st.session_state.current_odai = text
        st.session_state.has_drawn = True

# =========================
# CSS
# =========================
st.markdown(
    """
    <style>
    .byline {
        font-size: 0.95rem;
        opacity: 0.8;
        margin-top: -0.2rem;
        margin-bottom: 1rem;
    }

    .box-wrap {
        width: 100%;
        max-width: 360px;
        margin: 0 auto;
    }

    .odai-box {
        width: 100%;
        aspect-ratio: 1 / 2;
        border: 2px solid #d9d9d9;
        border-radius: 18px;
        background: #ffffff;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.06);
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 1.2rem;
        text-align: center;
        box-sizing: border-box;
    }

    .odai-text {
        font-size: 1.5rem;
        font-weight: 700;
        line-height: 1.6;
        word-break: break-word;
        color: #222222;
    }

    .placeholder-text {
        font-size: 1.05rem;
        color: #777777;
        line-height: 1.8;
    }

    @media (max-width: 640px) {
        .odai-text {
            font-size: 1.25rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================
# タイトル
# =========================
st.title("大喜利お題ルーレット")
st.markdown(
    f'<div class="byline">by <a href="{X_URL}" target="_blank" style="text-decoration:none;">あすとらふぃーだ</a></div>',
    unsafe_allow_html=True,
)

# =========================
# モード選択
# =========================
mode = st.radio(
    "入力方法",
    ["ランダム抽選", "手動入力"],
    horizontal=True,
)

if mode == "手動入力":
    st.text_input(
        "表示したいお題を入力",
        key="manual_input",
        placeholder="ここにお題を入力",
    )

# =========================
# お題ボックス
# =========================
current_text = st.session_state.current_odai.strip()

st.markdown('<div class="box-wrap">', unsafe_allow_html=True)

if current_text:
    safe_text = html.escape(current_text)
    st.markdown(
        f"""
        <div class="odai-box">
            <div class="odai-text">{safe_text}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <div class="odai-box">
            <div class="placeholder-text">ここにお題が表示されます</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div style='height: 0.8rem;'></div>", unsafe_allow_html=True)

# =========================
# ボタン
# =========================
left, center, right = st.columns([1, 6, 1])

with center:
    if mode == "ランダム抽選":
        if not st.session_state.has_drawn:
            if st.button("お題を引く", type="primary", use_container_width=True):
                draw_random_odai()
                st.rerun()
        else:
            if st.button("次のお題を引く", type="primary", use_container_width=True):
                draw_random_odai()
                st.rerun()
    else:
        if st.button("手動入力したお題を表示", type="primary", use_container_width=True):
            show_manual_odai()
            st.rerun()

# =========================
# 補足
# =========================
with st.expander("登録されているお題数"):
    st.write(f"{len(ODAI_LIST)} 個")