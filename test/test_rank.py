from test.rank import Rank

rank = Rank.E3
print(rank.value)
print(rank.value+1)

rank2 = Rank(rank.value + 1)
print(rank2)

promote_times = {}
promote_times[Rank.E3] = 23.0
promote_times[Rank.E4] = 24.0
promote_times[Rank.E5] = 25.0
promote_times[Rank.E6] = 26.0
promote_times[Rank.E7] = 27.0
print(promote_times)

e5_promote_time = promote_times[Rank.E7]
print(e5_promote_time)

print(promote_times[rank2.value + 1])

rank = Rank.E7 + 1
print(rank)
if rank in promote_times.keys():
    print(promote_times[rank])

rank = rank - 2
if rank in promote_times.keys():
    print(promote_times[rank])

