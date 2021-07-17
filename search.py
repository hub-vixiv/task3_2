import pandas as pd
import eel


def kimetsu_search(filename, word):
    # 検索対象取得
    df=pd.read_csv("./" + filename)
    source = list(df["name"])

    # 検索
    if word in source:
        print("yes")
        eel.show_result(f"『{word}』はあります")
    else:
        print("no")
        eel.show_result(f"『{word}』はありません")
        # 追加
        # リストに保存するか確認ダイアログ表示
        add_yesno = eel.ask_add_list()()
        if add_yesno == True:   #リストに保存する
            source.append(word)
            print(source)
            # ファイルに保存するか確認ダイアログ表示
            save_yesno = eel.ask_save()()
            if save_yesno == True:  #ファイルに保存する
                #保存するパスを要求ダイアログ表示
                save_path = eel.ask_save_path()()
                if save_path != None: #パスが空でなければ
                    # CSV書き込み
                    df=pd.DataFrame(source,columns=["name"])
                    df.to_csv(f"{save_path}/source.csv",encoding="utf_8-sig")