import random
from datetime import datetime

import streamlit as st


st.set_page_config(
    page_title="Bilimlar jangi",
    page_icon="🎓",
    layout="centered",
)

st.markdown(
    """
    <style>
    .stApp { background: #f4f7f2; }
    [data-testid="stHeader"] { background: rgba(244, 247, 242, 0.9); }
    .stButton > button {
        min-height: 2.8rem;
        border-radius: 8px;
        font-weight: 650;
        transition: transform 160ms ease, box-shadow 160ms ease;
    }
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(23, 61, 46, 0.12);
    }
    .correct-text {
        color: #167447;
        font-size: 1.2rem;
        font-weight: 700;
        text-align: center;
    }
    .wrong-text {
        color: #b43c36;
        font-size: 1.2rem;
        font-weight: 700;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

questions_mc = [
    {
        "q": "Ekologik huquqiy tartibga solishning asosiy maqsadi nima?",
        "options": [
            "A) Faqat sanoatni rivojlantirish",
            "B) Tabiatni muhofaza qilish va ekologik xavfsizlik",
            "C) Faqat sanoat zararlarini to'lash",
            "D) Atrof-muhitni o'zgartirish",
        ],
        "ans": "B",
    },
    {
        "q": "Inson huquqlarining xalqaro himoyasi qaysi tashkilot orqali amalga oshadi?",
        "options": ["A) BMT", "B) FIFA", "C) WHO", "D) UNESCO"],
        "ans": "A",
    },
    {
        "q": "Atrof-muhitni muhofaza qilishga qaysi biri bevosita tegishli emas?",
        "options": [
            "A) Monitoring",
            "B) Ekologik ekspertiza",
            "C) Iqtisodiy soliq imtiyozlari",
            "D) Qonunchilik",
        ],
        "ans": "C",
    },
    {
        "q": "Tabiatni muhofaza qilish qaysi huquq turiga kiradi?",
        "options": [
            "A) Fuqarolik huquqi",
            "B) Ekologik huquq",
            "C) Mehnat huquqi",
            "D) Intellektual huquq",
        ],
        "ans": "B",
    },
    {
        "q": "Inson huquqlari umumjahon deklaratsiyasi qachon qabul qilingan?",
        "options": ["A) 1945-yil", "B) 1948-yil", "C) 1950-yil", "D) 1960-yil"],
        "ans": "B",
    },
    {
        "q": "Ekologik monitoringning asosiy maqsadi nima?",
        "options": [
            "A) Tabiat holatini kuzatish",
            "B) Daraxtlarni kesish",
            "C) Suvni iste'mol qilish",
            "D) Havoni ifloslantirish",
        ],
        "ans": "A",
    },
    {
        "q": "Ombudsman kimlarning huquqlarini himoya qiladi?",
        "options": [
            "A) Faqat davlat organlarining",
            "B) Huquqlari buzilgan insonlarning",
            "C) Faqat tadbirkorlarning",
            "D) Faqat mansabdor shaxslarning",
        ],
        "ans": "B",
    },
    {
        "q": "Konstitutsiyaviy sudning asosiy vazifasi nima?",
        "options": [
            "A) Qonunlarning Konstitutsiyaga mosligini tekshirish",
            "B) Jinoyatchilarni hibsga olish",
            "C) Soliq yig'ish",
            "D) Saylov o'tkazish",
        ],
        "ans": "A",
    },
    {
        "q": "Atrof-muhitning ifloslanishi qaysi huquqqa bevosita tahdid soladi?",
        "options": [
            "A) Sog'liqni saqlash huquqiga",
            "B) Ta'lim olish huquqiga",
            "C) Erkin harakatlanish huquqiga",
            "D) Ishga joylashish huquqiga",
        ],
        "ans": "A",
    },
    {
        "q": "Ekologik ekspertiza nima?",
        "options": [
            "A) Faoliyatning atrof-muhitga ta'sirini baholash",
            "B) Daraxtlarni sanash",
            "C) Suvni filtrlash",
            "D) Hayvonlarni o'rganish",
        ],
        "ans": "A",
    },
]

matching_data = [
    {
        "l": "Ekologik monitoring",
        "r": "Atrof-muhit holatini kuzatish",
    },
    {
        "l": "Ombudsman",
        "r": "Inson huquqlarini himoya qiluvchi institut",
    },
    {
        "l": "Konstitutsiyaviy sud",
        "r": "Qonunlarning Konstitutsiyaga mosligini tekshiruvchi organ",
    },
    {
        "l": "BMT",
        "r": "Global xalqaro tashkilot",
    },
    {
        "l": "Ekologik ekspertiza",
        "r": "Faoliyatning atrof-muhitga ta'sirini oldindan baholash",
    },
]


def reset_quiz():
    for key in list(st.session_state.keys()):
        if key == "name_input" or key.startswith(("r_", "m_")):
            del st.session_state[key]

    st.session_state.update(
        {
            "step": "START",
            "name": "",
            "score": 0,
            "wrong": 0,
            "q_idx": 0,
            "start_t": None,
            "answered": False,
            "match_options": random.sample(
                [item["r"] for item in matching_data], len(matching_data)
            ),
        }
    )


if "step" not in st.session_state:
    reset_quiz()


if st.session_state.step == "START":
    st.title("🎓 Bilimlar jangi")
    st.subheader("Ekologiya va inson huquqlari")
    st.write("10 ta test savoli va 5 ta moslashtirish topshirig'i.")
    name = st.text_input("Ism-familiyangizni yozing:", key="name_input")

    if st.button("Testni boshlash 🚀", type="primary"):
        if name.strip():
            st.session_state.name = name.strip()
            st.session_state.start_t = datetime.now()
            st.session_state.step = "QUIZ"
            st.rerun()
        else:
            st.warning("Ism-familiyangizni kiriting.")

elif st.session_state.step == "QUIZ":
    idx = st.session_state.q_idx

    if idx < len(questions_mc):
        question = questions_mc[idx]
        st.progress(idx / len(questions_mc), text=f"1-bosqich · {idx + 1}/{len(questions_mc)}")
        st.markdown(f"### {question['q']}")

        if not st.session_state.answered:
            choice = st.radio(
                "Javob variantini tanlang:",
                question["options"],
                index=None,
                key=f"r_{idx}",
            )

            if st.button("Javobni tekshirish", type="primary"):
                if choice is None:
                    st.warning("Davom etishdan oldin javob variantini tanlang.")
                else:
                    is_correct = choice.startswith(question["ans"] + ")")
                    st.session_state.answered = True
                    if is_correct:
                        st.session_state.score += 1
                    else:
                        st.session_state.wrong += 1
                    st.rerun()
        else:
            selected_answer = st.session_state[f"r_{idx}"]
            if selected_answer.startswith(question["ans"] + ")"):
                st.markdown(
                    '<p class="correct-text">To\'g\'ri javob! 🎉</p>',
                    unsafe_allow_html=True,
                )
            else:
                correct_answer = next(
                    option
                    for option in question["options"]
                    if option.startswith(question["ans"] + ")")
                )
                st.markdown(
                    '<p class="wrong-text">Bu safar xato javob.</p>',
                    unsafe_allow_html=True,
                )
                st.info(f"To'g'ri javob: {correct_answer}")

            if st.button("Keyingi savol →", type="primary"):
                st.session_state.q_idx += 1
                st.session_state.answered = False
                st.rerun()
    else:
        st.session_state.step = "MATCH"
        st.rerun()

elif st.session_state.step == "MATCH":
    st.title("Ⅱ bosqich: Moslashtirish")
    st.write("Har bir tushunchaga mos ta'rifni tanlang.")

    for idx, item in enumerate(matching_data):
        st.selectbox(
            item["l"],
            ["Tanlang..."] + st.session_state.match_options,
            key=f"m_{idx}",
        )

    if st.button("Natijani ko'rish 🏁", type="primary"):
        selections = [
            st.session_state.get(f"m_{idx}", "Tanlang...")
            for idx in range(len(matching_data))
        ]
        if "Tanlang..." in selections:
            st.warning("Barcha tushunchalar uchun ta'rif tanlang.")
        else:
            match_score = sum(
                selection == item["r"]
                for selection, item in zip(selections, matching_data)
            )
            st.session_state.score += match_score
            st.session_state.wrong += len(matching_data) - match_score
            st.session_state.match_score = match_score
            st.session_state.step = "FINAL"
            st.rerun()

elif st.session_state.step == "FINAL":
    duration = datetime.now() - st.session_state.start_t
    total_questions = len(questions_mc) + len(matching_data)

    st.title("📊 Yakuniy natija")
    st.write(f"👤 **Ishtirokchi:** {st.session_state.name}")
    st.write(f"✅ **To'g'ri javoblar:** {st.session_state.score}/{total_questions}")
    st.write(f"❌ **Noto'g'ri javoblar:** {st.session_state.wrong}")
    st.write(f"🔗 **Moslashtirish natijasi:** {st.session_state.match_score}/{len(matching_data)}")
    st.write(f"⏱️ **Sarflangan vaqt:** {str(duration).split('.')[0]}")

    if st.session_state.score >= 12:
        st.success("A'lo natija! Mavzuni juda yaxshi bilasiz. 🎉")
        st.balloons()
    elif st.session_state.score >= 8:
        st.info("Yaxshi natija! Yana biroz mashq qiling. 👍")
    else:
        st.error("Mavzuni yana bir bor takrorlab ko'ring. 📚")

    if st.button("Qayta boshlash 🔄"):
        reset_quiz()
        st.rerun()