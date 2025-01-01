# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# # CSS for custom styling
# st.markdown("""
#     <style>
#     body {
#         font-family: 'Hiragino Kaku Gothic Pro', 'メイリオ', sans-serif;
#         color: #002a7e;
#         background-color: #FFFFFF;
#     }
#     header {
#         background-color: #003ebb;
#         text-align: center;
#         padding: 20px;
#     }
#     .site-title {
#         font-size: 2.5rem;
#         color: white;
#     }
#     .nav {
#         display: flex;
#         justify-content: center;
#         margin-top: 20px;
#     }
#     .nav a {
#         margin: 0 15px;
#         color: white;
#         text-decoration: none;
#     }
#     .nav a:hover {
#         color: #fcee21;
#     }
#     .chart-wrapper {
#         display: flex;
#         justify-content: center;
#         align-items: center;
#         padding: 20px;
#     }
#     .email-link {
#         color: #007BFF;
#         text-decoration: none;
#         font-size: 1.2rem;
#     }
#     .email-link:hover {
#         color: #0056b3;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Header
# st.markdown("<header><h1 class='site-title'>Cist License Management</h1></header>", unsafe_allow_html=True)

# # Navigation
# st.markdown("""
# <nav class="nav">
#     <a href="#license">ライセンス</a>
#     <a href="#activity-log">アクティビティログ</a>
#     <a href="#budget">予算</a>
#     <a href="#account">アカウント管理</a>
# </nav>
# """, unsafe_allow_html=True)

# # License Section
# st.markdown("<h2 id='license'>ライセンス</h2>", unsafe_allow_html=True)
# st.write("登録されているライセンス一覧")
# license_data = pd.DataFrame({
#     "コード": ["L001", "L002", "L003"],
#     "ライセンス名": ["Word", "Excel", "PowerPoint"],
#     "管理者": ["山田太郎", "鈴木一郎", "佐藤花子"],
#     "期限日": ["2025-01-01", "2025-06-30", "2025-12-31"]
# })
# st.table(license_data)

# # Activity Log
# st.markdown("<h2 id='activity-log'>アクティビティログ</h2>", unsafe_allow_html=True)
# activity_logs = [
#     {"日付": "2023/10/06", "内容": "学生支援課がコード:11392のライセンス「B202教室_Word」を削除。"},
#     {"日付": "2021/12/15", "内容": "JSも少し書いてみた。"},
#     {"日付": "2020/09/27", "内容": "ああああああああああああああ"}
# ]
# for log in activity_logs:
#     st.markdown(f"- **{log['日付']}**: {log['内容']}")

# # Budget Section
# st.markdown("<h2 id='budget'>予算</h2>", unsafe_allow_html=True)
# fig, ax = plt.subplots()
# ax.pie([70, 30], labels=["使用済み", "残り予算"], colors=["#007bff", "#e0e0e0"], autopct='%1.1f%%')
# ax.legend(["使用済み: 70%", "残り予算: 30%"], loc="upper right")
# st.pyplot(fig)

# # Account Section
# st.markdown("<h2 id='account'>アカウント管理</h2>", unsafe_allow_html=True)
# st.write("不具合がありましたら以下のメールアドレスにご連絡ください。")
# st.markdown("""
# <p class="email-link"><a href="mailto:cistlicense@gmail.com"><i class="fas fa-envelope"></i> cistlicense@gmail.com</a></p>
# """, unsafe_allow_html=True)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Custom CSS for improved styling
st.markdown("""
    <style>
        body {
            font-family: 'Hiragino Kaku Gothic Pro', 'メイリオ', sans-serif;
            color: #002a7e;
            background-color: #f9f9f9;
        }
        header {
            background-color: #003ebb;
            padding: 20px;
            text-align: center;
            color: white;
            border-radius: 5px;
        }
        header h1 {
            margin: 0;
            font-size: 2.5rem;
        }
        .section {
            background-color: #ffffff;
            padding: 20px;
            margin: 20px 0;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .section h2 {
            color: #003ebb;
            font-size: 1.8rem;
            margin-bottom: 10px;
            border-bottom: 2px solid #e0e0e0;
            padding-bottom: 5px;
        }
        .table {
            margin-top: 10px;
            border-collapse: collapse;
            width: 100%;
        }
        .table th, .table td {
            border: 1px solid #e0e0e0;
            padding: 10px;
            text-align: left;
        }
        .table th {
            background-color: #f2f2f2;
            color: #003ebb;
        }
        .activity-log {
            list-style: none;
            padding-left: 0;
        }
        .activity-log li {
            margin-bottom: 15px;
        }
        .activity-log span.date {
            font-weight: bold;
            color: #0056b3;
        }
        .chart-wrapper {
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .email-link {
            color: #007BFF;
            text-decoration: none;
            font-size: 1.2rem;
            display: inline-block;
            margin-top: 10px;
        }
        .email-link:hover {
            color: #0056b3;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<header><h1>Cist License Management</h1></header>", unsafe_allow_html=True)

# License Section
st.markdown("<div class='section'><h2>ライセンス</h2>", unsafe_allow_html=True)
st.write("登録されているライセンス一覧")
license_data = pd.DataFrame({
    "コード": ["L001", "L002", "L003"],
    "ライセンス名": ["Word", "Excel", "PowerPoint"],
    "管理者": ["山田太郎", "鈴木一郎", "佐藤花子"],
    "期限日": ["2025-01-01", "2025-06-30", "2025-12-31"]
})
st.table(license_data)
st.markdown("</div>", unsafe_allow_html=True)

# Activity Log Section
st.markdown("<div class='section'><h2>アクティビティログ</h2>", unsafe_allow_html=True)
activity_logs = [
    {"日付": "2023/10/06", "内容": "学生支援課がコード:11392のライセンス「B202教室_Word」を削除。"},
    {"日付": "2021/12/15", "内容": "JSも少し書いてみた。"},
    {"日付": "2020/09/27", "内容": "ああああああああああああああ"}
]
st.markdown("<ul class='activity-log'>", unsafe_allow_html=True)
for log in activity_logs:
    st.markdown(f"<li><span class='date'>{log['日付']}</span>: {log['内容']}</li>", unsafe_allow_html=True)
st.markdown("</ul></div>", unsafe_allow_html=True)

# Budget Section
st.markdown("<div class='section'><h2>予算</h2>", unsafe_allow_html=True)
fig, ax = plt.subplots()
ax.pie([70, 30], labels=["使用済み", "残り予算"], colors=["#007bff", "#e0e0e0"], autopct='%1.1f%%', startangle=90)
ax.legend(["使用済み: 70%", "残り予算: 30%"], loc="upper right")
st.pyplot(fig)
st.markdown("</div>", unsafe_allow_html=True)

# Account Section
st.markdown("<div class='section'><h2>アカウント管理</h2>", unsafe_allow_html=True)
st.write("不具合がありましたら以下のメールアドレスにご連絡ください。")
st.markdown("""
<a class='email-link' href="mailto:cistlicense@gmail.com"><i class="fas fa-envelope"></i> cistlicense@gmail.com</a>
</div>
""", unsafe_allow_html=True)
