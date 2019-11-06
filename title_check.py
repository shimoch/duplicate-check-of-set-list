# 任意のDJのセトリと、それ以外のDJのセトリに分ける
def divide_set_list(x):
	# 確認対象のDJのセトリ
	target = "set_list/" + x + ".txt"

	with open("dj.txt") as f:
		member_list = [member.strip() for member in f.readlines()]

	set_list = []

	for row in member_list:
		set_list.append("set_list/" + row + ".txt")

	# 確認対象以外のDJのセトリのリスト
	set_list.remove(target)

	return target, set_list


# 「任意のDJのセトリ」と、「それ以外のDJのセトリのリスト」を入力とし、「曲の重複結果」を出力
def check(one, others):
	with open(one) as f:
		one_song_list = [i.strip() for i in f.readlines()]
		one_set = set(one_song_list)

	path = one.replace("set_list/", "result/").replace(".txt", "._overlapping.txt")
	with open(path, mode='w') as f:
		pass
	L = []
	for row in others:
		with open(row) as f:
			row_song_list = [j.strip() for j in f.readlines()]
			row_set = set(row_song_list)
			intersection = one_set & row_set
			if len(intersection) >= 1:
				L = list(intersection)
				with open(path, mode='a') as f:
					for l in L:
						f.write(row.replace("set_list/", "").replace(".txt", "") + " と【" + l + "】が重複！")
						f.write("\n")
	if len(L) == 0:
		with open(path, mode='a') as f:
			f.write("重複なし！")
		return print(one.replace("set_list/", "").replace(".txt", "") + " はOK")
	else:
		return print(one.replace("set_list/", "").replace(".txt", "") + " は【重複あり】")


if __name__ == '__main__':

	with open("dj.txt") as f:
		member_list = [member.strip() for member in f.readlines()]
	for x in member_list:
		y, z = divide_set_list(x)
		check(y, z)