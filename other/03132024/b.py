# ques_num, peo_num = [int(x) for x in input().split()]
#
# peo_rank = []  # [0, 0] for _ in range(peo_num)
#
# for i in range(peo_num):
#     total_pass = 0
#     total_time = 0
#
#     for j in range(ques_num):
#         cnt, time, pass_ = [int(x) for x in input().split()]
#
#         if pass_ == 1:
#             total_pass += 1
#             total_time += time + 20 * (cnt - 1)
#
#     peo_rank.append([total_pass, total_time, i + 1])
#
# peo_rank.sort(key=lambda x: (-x[0], x[1]))
#
# new = []
# for idx, val in enumerate(peo_rank):
#     new.append([idx + 1, val[2], val[0], val[1]])
#
# new.sort(key=lambda x: x[1])
#
# for item in new:
#     print(item[0])
#     print(item[2])
#     print(item[3])
#
#
ques_num, peo_num = map(int, input().split())

peo_info = []  # pass_cnt,time,code

for i in range(peo_num):
    total_pass = 0
    total_time = 0

    for j in range(ques_num):
        submit_cnt, time, pass_ = map(int, input().split())

        if pass_ == 1:
            total_pass += 1
            total_time += time + 20 * (submit_cnt - 1)

    peo_info.append([total_pass, total_time, i + 1])

peo_info.sort(key=lambda x: (-x[0], x[1]))

rank_info = []  # ranking, code, pass_cnt, time
for rank, item in enumerate(peo_info):
    rank_info.append([rank + 1, item[2], item[0], item[1]])

rank_info.sort(key=lambda x: x[1])

for item in rank_info:
    print(item[0])
    print(item[2])
    print(item[3])
