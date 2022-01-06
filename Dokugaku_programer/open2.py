# 日本語だとencodingを追加しないと文字化けする
st = open("st.txt","w",encoding="utf-8")
st.write("Pythonからこんにちは")
st.close()
